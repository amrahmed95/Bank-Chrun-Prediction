import os
import pandas as pd
from src.BankChurn import logger
from sklearn.preprocessing import LabelEncoder
from src.BankChurn.config.configuration import DataValidationConfig

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        self.df = pd.read_csv(self.config.unzip_data_dir)
        
    def load_data(self):
        self.df = pd.read_csv(self.config.unzip_data_dir)

    def preprocess(self):
        """ Preprocess the dataframe """      

        # Drop unnecessary columns
        columns_to_drop = ['RowNumber', 'CustomerId', 'Surname']
        for col in columns_to_drop:
            if col in self.df.columns:
                self.df = self.df.drop(columns=[col])

        # Convert columns to integer type
        for col in ['EstimatedSalary', 'Balance']:
            if col in self.df.columns:
                self.df[col] = self.df[col].astype(int, errors='ignore')

        # Encode categorical columns using LabelEncoder
        le = LabelEncoder()
        categorical_cols = ['Geography', 'Gender']
        for col in categorical_cols:
            if col in self.df.columns:
                self.df[col] = le.fit_transform(self.df[col])

        # Drop additional column
        if 'HasCrCard' in self.df.columns:
            self.df = self.df.drop('HasCrCard', axis=1)
            
    
        return self.df
    

    def validate_all_columns(self, preprocessed_data: pd.DataFrame) -> bool:
        try:
            validation_status = True
            all_cols = list(preprocessed_data.columns)
            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                    return validation_status
                else:
                    schema_data_type = self.config.all_schema[col]
                    data_data_type = preprocessed_data[col].dtype

                    if schema_data_type != data_data_type:
                        validation_status = False
                        with open(self.config.STATUS_FILE, 'w') as f:
                            f.write(f"Validation status: {validation_status}")
                        return validation_status

            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status
        except Exception as e:
            raise e

