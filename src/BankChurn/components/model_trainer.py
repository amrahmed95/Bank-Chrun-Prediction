import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from src.BankChurn import logger
from src.BankChurn import evaluate_models

from src.BankChurn.config.configuration import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        logger.info("Initialize Model Training and Evaluation")
        self.config = config      
     
    
    def Initialize_model_trainer(self):
        config = self.config
        logger.info("Loading data")
        data = pd.read_pickle(self.config.train_data_path)
        
        logger.info("Start Splitting input data")
        df = data.copy()
        x_resampled = df.drop(columns=['Exited'])
        y_resampled = df['Exited']
        x_train, x_test, y_train, y_test = train_test_split(x_resampled, y_resampled, test_size=0.2, random_state=42)
        
        logger.info("Start Modelling and Evaluating")
        
        models={
            "logistic_regression": LogisticRegression(),
            "svc": SVC(),
            "random_forest": RandomForestClassifier(),
        }
        
        params = {
            "logistic_regression": {},
            "svc": {},
            "random_forest": {
                'n_estimators' : [int(x) for x in np.linspace(start = 10, stop = 80, num = 10)],
                'max_features' : ['sqrt', 'log2', None],
                'max_depth' : [None, 10, 20, 30],
                'min_samples_split' : [2, 5, 10],
                'min_samples_leaf' : [1, 2, 4],
                'bootstrap' : [True, False]
            }
        }

        model_report: dict = evaluate_models(
                X_train=x_train, y_train=y_train, X_test=x_test, y_test=y_test,
                models=models, param=params
            )
        #best_model_score = max(model_report.values())
        best_model_score = max(model_report.values(), key=lambda x: x['test_model_accuracy'])
        best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
        best_model = models[best_model_name]

        if best_model_score['test_model_accuracy'] < 0.6:
            raise Exception("No best model Found")
        
        logger.info(f"Best found model on both training and testing dataset")

        joblib.dump(best_model, os.path.join(self.config.root_dir, self.config.model_name))
        

   
   