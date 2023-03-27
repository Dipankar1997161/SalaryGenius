# SalaryGenius

![app home page](https://user-images.githubusercontent.com/85514219/228042142-dd263a7a-d3d9-4d95-b90c-7ad99d2170ac.png)

The following is a web app which predicts the salary based on Country, Experience and Education Level

## Overview
The Web-app is used to predict the salary on a world scale based on the experience level, education and country. It also shows a quick analysis of the data and the Job Market Salary.

The following web app is solely for Software Developers. More option/ other Professions will be added soon as this is the basic version.

## Experiment
The dataset used for training is extracted from StackOverflow. Year 2020 and 2021 were taken and merged to provide a larger file for training.

Currently only 3 techniues - Linear Regression, DecisionTree, and RandomForest were used for training purpose. The comparision showed that RandomForest performs better.

![normal training](https://user-images.githubusercontent.com/85514219/228039660-1a82ed9d-1afe-4523-9a9a-ad1fe172bdac.png)

However, since both Decision Tre and Random Forest were close. I decided to perform GridSearch based training with a random max-depth. The results were as follows:

![gridsearch training](https://user-images.githubusercontent.com/85514219/228040116-7d50e812-c9ac-4f3f-bcc8-83e7f8c64af1.png)

With this, I finalized my model on Random Forest for further prediction. I will be using CatBoost and XGBoost soon to make the model more robust.

## WebApp and Deployment

I used Streamlit for this purpose and generate the necessary web app for my application. It's my first time creating a web-app so I will improvise the design and build more apps in the coming time.
Here is the link for the webapp: https://dipankar1997161-salarygenius-app-h1x50m.streamlit.app/

## Quick Snap of the Prediction
![app prediction](https://user-images.githubusercontent.com/85514219/228042916-ed51ef1d-0a1d-4b59-965e-6e30fce95e6e.png)


