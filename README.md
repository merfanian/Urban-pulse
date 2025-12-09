# Urban-pulse
Urban Pulse: Modeling Crime, Mobility, Weather, and Events in Chicago

Urban Pulse is a data-driven project exploring how urban activity patterns—crime, weather, mobility, and public events—interact across Chicago neighborhoods. Using multi-year public datasets and a combination of machine learning, clustering, NLP, and time-series analysis, the project uncovers how environmental and behavioral factors shape public safety.

🔍 Project Overview

This project integrates four major Chicago datasets:

Crime Data (2.7M+ incidents, 2014–2024)

Divvy Mobility Data (bike trip logs with timestamps and geolocation)

Weather Data (daily meteorological observations, 2023–2025)

Event Permits (public activity and event schedules across the city)

The analysis spans:

Exploratory data analysis and correlation studies

Neighborhood-level clustering and safety categorization

Weather–crime and mobility–crime relationships

Text analysis on CTA station and park reviews

Crime forecasting using ARIMA/SARIMAX

Machine learning models for predicting daily crime levels


📊 Key Features & Findings
1. Exploratory Data Analysis

Crime patterns vary sharply by neighborhood and season.

Crime drops significantly on event days, likely due to increased security.

Weather drives large behavioral shifts: warm and dry days increase mobility and crime exposure.

Divvy mobility rises in warm months and aligns with certain outdoor crime patterns.

2. Neighborhood Crime Clustering

Using PCA + K-means, neighborhoods are grouped into:

Safe

Moderate-risk

High-risk

These clusters reveal distinct crime compositions and geographic segments of the city.

3. NLP for Public Safety Perception

TF-IDF + Logistic Regression is used to analyze reviews of:

CTA stations

Chicago parks

A “concern score” is computed for robbery, assault, battery, etc., reflecting perceived safety from public reviews.

4. Machine Learning Models

We evaluate several models for predicting daily crime counts:

Linear Regression

Ridge / Lasso

Random Forest

XGBoost

Gradient Boosting

Best Model:
Gradient Boosting achieves R² ≈ 0.91, showing strong predictive performance.

Historical crime is the strongest signal, while events and weather provide additional value.

5. Time-Series Forecasting (ARIMA & SARIMAX)

We test whether Divvy mobility improves crime forecasting:

Citywide:
Divvy mobility does not improve predictions; SARIMAX performs worse than ARIMA.

By Crime Type:
Mobility improves forecasting for outdoor crimes like:

Criminal Damage

Assault

but not for crimes like Theft or Battery.

Neighborhood-Level:
Mobility helps only in neighborhoods with high Divvy activity.