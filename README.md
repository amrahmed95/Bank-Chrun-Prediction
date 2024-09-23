## Bank Churn Prediction.

This project utilizes data analysis and machine learning techniques to predict customer churn in banking. By cleaning and extracting relevant features from historical data, it identifies patterns indicative of customer attrition. Through the development and testing of predictive models, banks gain valuable insights to proactively address customer retention, ensuring long-term satisfaction and loyalty


#### Business Problem

In the world of banking, one of the biggest challenges is keeping customers happy and staying with the bank. It's way cheaper to retain existing customers than to acquire new ones. But sometimes, customers decide to leave, and banks want to know why. That's where this project comes in. We're using smart computer methods to figure out when customers might leave.

We start by looking at all the data the bank has collected over time. Then, we clean it up and identify the most important parts. We use data cleaning to ensure the information is accurate and ready for analysis. After that, we employ clever techniques like feature engineering to extract the most useful bits of data. This helps us uncover patterns and trends that might predict if a customer will leave or not.

Once we've got everything prepared, we're building machine learning models using simple but effective methods to predict which customers might leave the bank. But we're not stopping there. We're also testing these models with separate data to ensure their efficiency. By doing all this, we hope to provide banks with the tools they need to keep their customers happy and loyal for the long haul.


## Overview
This project aims to predict customer churn for a banking service using a machine learning model. The pipeline includes data ingestion, preprocessing, transformation, model training, evaluation, and deployment through a Flask web application and a Streamlit app that allows users to interactively make predictions based on customer data.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Using Docker](#using-docker)
- [Project Pipeline](#project-pipeline)
- [Usage](#usage)
- [Results](#results)



## Technologies Used
- Python
- Flask
- Pandas
- NumPy
- scikit-learn
- MLflow (for logging)
- Joblib (for model saving and loading)

## Getting Started
1. Clone the repository:
   ```bash
   git clone https://github.com/amrahmed85/bank-churn-prediction.git
   cd bank-churn-prediction

2. Install the required packages:
     ```bash
    pip install -r requirements.txt

3. Run the app:
    ```bash
    python app.py

## Using Docker
To run the application in a Docker container, follow these steps:

1. Build the Docker image: 
    ```bash
    docker build -t bank-churn-prediction .

2. Run the Docker container:
    ```bash
    docker run -p 5000:5000 bank-churn-prediction

3. Accessing the Application - Navigate to the following URL in your web browser:
[http://localhost:5000/](http://localhost:5000/)


## Project Pipeline
The project consists of the following stages:

1. **Data Ingestion**: Downloads and extracts the dataset.
    
2. **Data Preprocessing and Validation**: Validates and preprocesses the data.
   
3. **Data Transformation**: Transforms the data for modeling.
  
4. **Model Training**: Trains a machine learning model.
     
5. **Model Evaluation**: Evaluates the model performance.
     
6. **Prediction**: Makes predictions using the trained model.
   
## Usage
To train the model, navigate to the `/train` endpoint::
    [http://localhost:5000/](http://localhost:5000/)



To make predictions, fill out the form on the home page and submit:

Navigate to the / endpoint:
[http://localhost:5000/](http://localhost:5000/)

## Results:
After making predictions, the results will be displayed indicating whether the customer is likely to leave the bank or not.


