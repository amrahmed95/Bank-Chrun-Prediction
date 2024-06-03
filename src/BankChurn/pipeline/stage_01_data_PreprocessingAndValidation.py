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
            data_validation_config = self.config_manager.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            preprocessed_data = data_validation.preprocess()
            self._save_preprocessed_data(preprocessed_data)
            validation_status = data_validation.validate_all_columns(preprocessed_data)
            self.logger.info(f"Validation status: {validation_status}")
        except Exception as e:
            self.logger.error(f"Error occurred: {e}")
            raise

    def _save_preprocessed_data(self, data: pd.DataFrame) -> None:
        data.to_pickle('../artifacts/data_preprocessed/1_preprocessed_df.pkl')