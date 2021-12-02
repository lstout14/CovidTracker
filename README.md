# Covid Tracker
## Capstone Project for DSCI 591

## Concept

This intent of this project is provide a unique interpretation of COVID-19 data. All too often, the only representations of the data are simple graphs of a feature vs time as can be found in many sources, such as the CDC. As a counter to that, a web app will be designed to generate interesting displays of various features with a simple and accessible interface.

## Data
So far, the data from OWID (https://github.com/owid/covid-19-data/tree/master/public/data) has been incorporated. This master set contains data from several reliable sources, such as JHU and the European CDC. The data are fairly clean, but the data is slightly inaccessible in its initial state. Preprocessing steps were required to make the data accessible and useful, as opposed to a massive conglomeration of all possible data with many aggregate features. While this could be helpful for general analysis, the form of the data muddles the clarity and usability of the data for the purpose of this project. To this end, many features had to be removed or adjusted. The "interesting features" alluded to previously refer to the information past the generic ones like population, number of cases, or number of deaths. A few unique facets for example are the countries' ratings on the extreme poverty index, the number of hospital beds available, and the presence of handwashing facilities.

## Web App
The final goal for this project is to develop a shareable web app that can be run to show a pleasant presentation of the data and all of its features. This implementaiton will be done using Plotly's Dash. This engine will be used to develop a production-grade app similar to what can be developed with PowerBI or Tableau, but with an entirely Python backend. The web pages planned are so far categorized by the following: home page, continent, country, and vaccinations.

## Assumptions
The data are limited by the reporting. There is no way of validating the reported data, especially for the early days of the pandemic when testing was limited and COVID-19 was spreading undetected or untested. This means that the data are inaccurate in many regions for substantial periods of time. However, as there is no way to interpolate the missing data accurately, the data will be assumed correct after a certain period of time. Therefore, data prior to an unspecified cutoff date will be ignored.

## Stretch Goals
Developing machine learning models to predict number of cases and number of deaths are higher level goals to be attempted if time permits. This will incur a new page on the app for predictions. This will be done using a split version of the provided data being processed in a linear model using sklearn.
