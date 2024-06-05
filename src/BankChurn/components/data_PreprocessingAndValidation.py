import os
import pandas as pd
import pickle
from src.BankChurn import logger
from src.BankChurn.config.configuration import DataValidationConfig
from sklearn.preprocessing import LabelEncoder

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        #self.data_path = data_path
        self.config = config
        logger.info('Initialized DataValidation Class')
        

    def load_data(self):
        logger.info('Loading data from {}'.format(self.config.unzip_data_dir))
        self.df = pd.read_csv(self.config.unzip_data_dir)
        logger.info(f"Loaded data from {self.config.unzip_data_dir}")
        logger.info('Loaded data with shape {}'.format(self.df.shape))
        return self.df

    def preprocess(self):
        """ Preprocess the dataframe """
        self.load_data()

        # Drop unnecessary columns
        columns_to_drop = ['RowNumber', 'CustomerId', 'Surname']
        for col in columns_to_drop:
            if col in self.df.columns:
                self.df = self.df.drop(columns=[col])
                logger.info(f"Dropped column {col}")

        # Convert columns to integer type
        for col in ['EstimatedSalary', 'Balance']:
            if col in self.df.columns:
                self.df[col] = self.df[col].astype(int, errors='ignore')
                logger.info(f"Converted column {col} to integer type")

        # Encode categorical columns using LabelEncoder
        le = LabelEncoder()
        categorical_cols = ['Geography', 'Gender']
        for col in categorical_cols:
            if col in self.df.columns:
                self.df[col] = le.fit_transform(self.df[col])
                logger.info(f"Encoded categorical column {col}")

        # Drop additional column
        if 'HasCrCard' in self.df.columns:
            self.df = self.df.drop('HasCrCard', axis=1)
            logger.info("Dropped column HasCrCard")

        # Export preprocessed data
        validated_data_path = os.path.join('artifacts/data_preprocessed', 'preprocessed_data.pkl')
        os.makedirs(os.path.dirname(validated_data_path), exist_ok=True)
        self.df.to_pickle(validated_data_path , protocol=pickle.HIGHEST_PROTOCOL)
        logger.info(f"Exported preprocessed data to {validated_data_path}")

        return self.df

    def validate_columns(self, preprocessed_data: pd.DataFrame) -> bool:
        try:
            validation_status = True
            all_cols = list(preprocessed_data.columns)
            all_schema = self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    logger.error(f"Column {col} not found in schema")
                else:
                    schema_data_type = self.config.all_schema[col]
                    data_data_type = preprocessed_data[col].dtype

                    if schema_data_type != data_data_type:
                        validation_status = False
                        logger.error(f"Data type mismatch for column {col}: schema type {schema_data_type}, data type {data_data_type}")
                        
            
            with open(self.config.STATUS_FILE, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status
        except Exception as e:
            logger.exception(f"Error in validating columns: {e}")
            raise e
        
    
    def validate_data(self):
        preprocessed_data = self.preprocess()
        validation_status = self.validate_columns(preprocessed_data)
        logger.info(f"Validation status: {validation_status}")
        return validation_status