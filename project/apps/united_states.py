import plotly.graph_objects as go
import plotly.io as pio
import plotly as plt
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from app import app
from datetime import datetime
import chess.pgn
from apps import match, graphs
import numpy as np

from collections import Counter
import plotly.express as px

import pandas as pd

new_template = pio.templates['plotly_white']
new_template['layout']['scene']['xaxis']['gridcolor'] = '#222222'
new_template['layout']['scene']['yaxis']['gridcolor'] = '#222222'

#This wholeass section is for data processing
#******************************************************************************************************************
# preparing various dataframes for visualisation
    
games = {}
limit = 1000 # for testing
with open('./apps/data/lichess_db_standard_rated_2013-01.pgn', 'r') as pgn_file:
    game = chess.pgn.read_game(pgn_file)
    L = 0
    while game != None:
        match1 = match.Match(game)
        idx = match1.game_id
        games[idx] = match1
        game = chess.pgn.read_game(pgn_file)
        L += 1
        if L == limit: break
            
for game in games.values():
    game.fill_tracker()
data = pd.concat([i.get_dataframe() for i in games.values()])

def to_uci(square):
        square = int(square)
        letter = chr(ord('a') + ((square)%8)) 
        number = square//8+1
        return f"{letter}{number}"
    

captures_df = (data.explode('captures').groupby(['piece','captures'])['game_id'].nunique()).to_frame().reset_index().sort_values('game_id', ascending=False).assign(piece_type = lambda df: df['piece'].str.split('-').str.get(0))
captures_df['captured_piece_type'] = captures_df['captures'].apply(lambda x: x[0])
new_df = captures_df[['piece_type', 'captured_piece_type']].drop_duplicates()

new_df['capture_count'] = new_df.apply(lambda x: sum(captures_df[(captures_df['piece_type'] == x['piece_type']) & (captures_df['captured_piece_type'] == x['captured_piece_type'])]['game_id']), axis=1)
new_df['color'] = new_df['piece_type'].apply(lambda x: 'white' if ord(x) >= 9812 or ord(x) <= 9817 else 'black')
    
#Page header
#******************************************************************************************************************

layout = html.Div([
    dbc.Container([
        dbc.Row([
        dbc.Col(html.H1(children='Chess gang'), className="mb-2")
        ]),
        dbc.Row([
            dbc.Col(html.H6(children='Visualising trends across the board'), className="mb-4")]),

#******************************************************************************************************************
        
#Block headers
#******************************************************************************************************************        
    dbc.Row([
        dbc.Col(dbc.Card(html.H3(children='Checkmates by Piece, constrained by ELO',
                                 className="text-center text-white bg-dark"), body=True, color="dark")
        , className="mt-4 mb-4")
    ]),
        
    dbc.Row([
        dbc.Col(dcc.Graph(id='captures_by_piece'), width=12)
    ]),
    dcc.RangeSlider(
        id='my-range-slider',
        min=100,
        max=2900,
        step=100,
        marks={
        100: '100',
        500: '500',
        900: '900',
        1300: '1300',
        1700: '1700',
        2100: '2100',
        2500: '2500',
        2900: '2900'
        },
        value=[1300, 1700]
        ),

    dbc.Row([
        dbc.Col(dbc.Card(html.H3(children='Overall piece capture rates, normalized by piece type count',
                                 className="text-center text-light bg-dark"), body=True, color="dark")
        , className="mb-4")
        ]),

    dbc.Row([
        dbc.Col(html.H5(children='Pieces are normalized by piece count. For example, the number for pawns was divided by 8, while rooks were divided by two.', className="text-center"),
                className="mt-4"),
    ]),

    dcc.Graph(id='pieces_captured'),

]) # container


]) # overall

# page callbacks
@app.callback([Output('pieces_captured', 'figure'),
               Output('captures_by_piece', 'figure')],
              [Input('my-range-slider', 'value')])

def update_graph(slider_range):
    elo_min, elo_max = slider_range
    
    #Pieces captured
    fig = graphs.pieces_captured(new_df)
    
    #Mating pieces
    fig2 = go.Figure()
    fig2 = px.histogram(data_frame=graphs.checkmates(data, elo_min, elo_max), x='Checkmate', labels={"Checkmate": "Mating Piece"})
    fig2.update_layout(paper_bgcolor = 'rgba(0,0,0,0)', plot_bgcolor = 'rgba(0,0,0,0)', template = new_template, margin = dict(t=0), xaxis={'categoryorder' : 'array', 'categoryarray':['Queen', 'Rook', 'Pawn', 'Knight','Bishop']})
    
    return fig, fig2
