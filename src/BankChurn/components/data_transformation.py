import os
import pandas as pd
import numpy as np
from src.BankChurn import logger
import pickle
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from src.BankChurn.config.configuration import DataTransformationConfig

class DataTransformationClass:
    def __init__(self, data_path, config: DataTransformationConfig):
        self.data_path = data_path
        self.config = config
        logger.info('Initialized DataTransformationClass')

    def load_data(self):
        logger.info('Loading data from {}'.format(self.data_path))
        df = pd.read_pickle(self.data_path)
        logger.info('Loaded data with shape {}'.format(df.shape))
        return df

    def preprocess_data(self, df):
        numbCol = ['EstimatedSalary', 'Balance', 'CreditScore', 'Age']
        df[numbCol] = StandardScaler().fit_transform(df[numbCol])
        logger.info('Preprocessed data')
        return df

    def resample_data(self, df):
        x1 = df.drop(columns=['Exited'])
        y1 = df['Exited']
        over = SMOTE(sampling_strategy=1)
        x1_resampled, y1_resampled = over.fit_resample(x1, y1)
        logger.info('Oversampled data')
        return x1_resampled, y1_resampled

    def split_data(self, df_resampled):
        train, test = train_test_split(df_resampled, test_size=0.2, random_state=0)
        logger.info('Split data into train and test with shapes {} and {}'.format(train.shape, test.shape))
        return train, test

    def save_data(self, train, test):
        os.makedirs('artifacts/data_transformation', exist_ok=True)
        train.to_pickle(os.path.join(self.config.root_dir, "train.pkl"),protocol=pickle.HIGHEST_PROTOCOL)
        test.to_pickle(os.path.join(self.config.root_dir, "test.pkl"),protocol=pickle.HIGHEST_PROTOCOL)
        
    def transform_data(self):
        df = self.load_data()
        preprocessed_data = self.preprocess_data(df)
        resampled_data_x, resampled_data_y = self.resample_data(preprocessed_data)
        train, test = self.split_data(resampled_data_x)
        self.save_data(train, test)