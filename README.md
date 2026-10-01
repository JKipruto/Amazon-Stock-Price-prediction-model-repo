Amazon Stock Price Prediction

A machine learning regression project that predicts the next trading day’s Amazon (AMZN) closing price using historical stock-market data.

The project focuses on building a complete machine learning workflow, from data exploration and preprocessing to model comparison, hyperparameter tuning, model persistence, and real-world inference.

Project status: 🟡 Machine Learning pipeline completed. FastAPI deployment/API integration is the next step.



Project Objective

The goal of this project is to develop a regression model capable of predicting Amazon’s next-day closing price using information from the current trading day.

The project also demonstrates how a machine learning model can be taken beyond experimentation and prepared for integration into an application through model serialization and an API.


Tools & Technologies

Technology	Purpose
Python--->Main programming language
Pandas--->Data manipulation and analysis
NumPy--->Numerical computing
Matplotlib--->Data visualization
Seaborn--->Statistical visualization and EDA
Scikit-learn--->Preprocessing, models, tuning, evaluation and pipelines
Joblib--->Model serialization
Jupyter Notebook--->Experimentation and EDA
VS Code--->Development environment
Git & GitHub--->Version control
FastAPI(Planned)--->REST API deployment


Dataset

The dataset contains historical Amazon stock-market information, including:

* Date
* Open
* High
* Low
* Close
* Volume
* Adjusted Close

The dataset used for the main training and evaluation process contains data up to 18 September 2026.

The target variable is the following trading day’s closing price.

Target Engineering

The current day’s Close price is shifted to create the prediction target for the next trading day.

This allows the model to learn the relationship:

Today’s market information → Tomorrow’s closing price



Exploratory Data Analysis

Before training the models, I performed Exploratory Data Analysis to understand the structure and characteristics of the dataset.

The analysis included:

* Checking for missing/null values
* Inspecting data types
* Descriptive statistics
* Feature distributions
* Correlation analysis
* Feature-target relationships
* Visualization of stock-price trends
* Investigation of multicollinearity between price features

Matplotlib and Seaborn were used extensively for visualization.

One observation from the analysis was the strong relationship between Open, High, and Low, which is expected because these variables describe different prices from the same trading session.


Data Preprocessing

Time-Series Train/Test Split

Because stock-market data is time-dependent, I avoided using a random train_test_split.

Instead, the dataset was divided chronologically:

* 80% Training data
* 20% Testing data

This helps preserve the temporal order of the observations and reduces the risk of using future observations to train the model.

Feature Scaling

StandardScaler from Scikit-learn was used to standardize the numerical features.

The scaler was fitted using the training data and then applied to the test data to avoid data leakage.


 Machine Learning Models

I experimented with multiple regression algorithms, including:

* Linear Regression
* Ridge Regression
* Lasso Regression
* Decision Tree Regressor
* K-Nearest Neighbors Regressor
* Support Vector Regression (SVR)
* Random Forest Regressor
* Bagging Regressor
* Voting Regressor
* Other regression/ensemble approaches

Rather than assuming that a more complex model would automatically perform better, I compared multiple approaches and evaluated their performance on the same problem.


 Hyperparameter Tuning

I used Scikit-learn’s:

* GridSearchCV
* RandomizedSearchCV

to search for suitable hyperparameter configurations for the different models.

This allowed the models to be compared using tuned configurations rather than relying solely on their default parameters.



Model Evaluation

The models were evaluated using:

MAE

Mean Absolute Error

Measures the average absolute difference between the predicted and actual values.

MSE

Mean Squared Error

Penalizes larger prediction errors more heavily.

R² Score

Measures how much of the variation in the target variable is explained by the model.

I also compared the models against a naive baseline to determine whether the machine learning models provided useful predictive performance beyond a simple baseline approach.


 
 Model Selection

After evaluating the different models, Ridge Regression achieved the lowest error among the models tested on the evaluation data.

Ridge was particularly interesting because the dataset contains strongly correlated price-related features. Its L2 regularization can help manage the effects of multicollinearity while retaining the available features.



ML Pipeline

The selected model and preprocessing steps were combined into a Scikit-learn Pipeline.

The workflow is approximately:

Historical Stock Data
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Time-Based Train/Test Split
        ↓
StandardScaler
        ↓
Model Training
        ↓
Hyperparameter Tuning
        ↓
Model Evaluation
        ↓
Ridge Regression
        ↓
Scikit-learn Pipeline
        ↓
Joblib Serialization
        ↓
New Data
        ↓
Prediction


Model Persistence

The trained pipeline is serialized using Joblib.

This allows the trained model and preprocessing workflow to be loaded later without retraining the model.

Example workflow:

import joblib
model = joblib.load("model.pkl")
prediction = model.predict(new_data)


Current Prediction Interface

Before implementing the API, I created a terminal-based inference workflow.

The user can provide current-day stock information, and the trained model generates a prediction for the following day’s closing price.

I also tested the inference workflow using Amazon stock data from 23 September 2026 to predict the closing price for 24 September 2026.

This provided an additional check using newer data outside the original training dataset.


FastAPI Deployment

The next stage of the project is to expose the trained model through a REST API using FastAPI.

The planned workflow is:

Client/Application
       ↓
FastAPI POST Request
       ↓
Input Validation
       ↓
Saved ML Pipeline
       ↓
Ridge Model
       ↓
Prediction
       ↓
JSON Response

A future API request could look conceptually like:

{
    "open": 123.45,
    "high": 125.20,
    "low": 122.80,
    "volume": 50000000
}

and return a prediction such as:

{
    "predicted_close": 124.75
}



The exact structure may change as the FastAPI component is added.

Key Machine Learning Concepts I Practiced

Through this project, I worked with:

* Regression
* Time-series data splitting
* Feature engineering
* Exploratory Data Analysis
* Correlation analysis
* Multicollinearity
* Feature scaling
* Data leakage prevention
* Model selection
* Ensemble learning
* Hyperparameter tuning
* Cross-validation
* Grid Search
* Randomized Search
* MAE, MSE and R²
* Baseline comparison
* Scikit-learn Pipelines
* Model serialization
* Model inference
* REST API deployment

Limitations

Stock-price prediction is inherently difficult because market prices are influenced by many factors that are not represented in this dataset.

This project should therefore be viewed primarily as a machine learning engineering and experimentation project, rather than a system capable of reliably forecasting future market prices.

The current model primarily uses historical price and volume information and does not incorporate factors such as:

* News sentiment
* Macroeconomic indicators
* Market-wide movements
* Company financial statements
* Economic events
* Order-book information
* Intraday market data

These could be explored in future versions.



Future Improvements

Planned improvements include:
* Build the FastAPI REST API
* Add request validation using Pydantic
* Add API documentation/testing
* Containerize the application with Docker
* Add automated testing
* Improve feature engineering
* Experiment with additional time-series features
* Compare against dedicated time-series approaches
* Add model monitoring
* Deploy the API to a cloud platform
* Create a simple frontend for interacting with the model


What I Learned

This project helped me move beyond simply training individual machine learning models and understand a more complete ML workflow.

In particular, I gained practical experience in EDA, time-series data splitting, preprocessing, model comparison, hyperparameter optimization, evaluation, pipeline creation, model serialization, and inference.

The next step is to turn the trained model into an accessible machine learning service through FastAPI.


Software Engineering Student | Machine Learning & AI Enthusiast

This project was built as part of my journey into Machine Learning Engineering.
