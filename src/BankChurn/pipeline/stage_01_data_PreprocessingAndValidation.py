from src.BankChurn.components.data_PreprocessingAndValidation import DataValidation
from src.BankChurn.config.configuration import ConfigurationManager
from src.BankChurn import logger, logging
import pandas as pd


STAGE_NAME = "Data Preprocess and Validation stage"

class DataPreprocessAndValidationTrainingPipeline:
    def __init__(self) -> None:
        self.config_manager = ConfigurationManager()
        self.logger = logger
    
    def main(self) -> None:
        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(data_validation_config)
            validation_status = data_validation.validate_data()
            print(f"Validation status: {validation_status}")
        except Exception as e:
            logger.error(f"Error occurred: {e}")
            raise e
