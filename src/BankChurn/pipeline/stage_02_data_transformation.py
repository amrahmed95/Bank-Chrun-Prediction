from src.BankChurn.components.data_transformation import DataTransformationClass
from src.BankChurn.config.configuration import ConfigurationManager
from src.BankChurn import logger
import pandas as pd

STAGE_NAME = "Data transformation stage"


class DataTransformationTrainingPipeline:
    def __init__(self) -> None:
        self.config_manager = ConfigurationManager()
        self.logger = logger
    
    def main(self) -> None:
        try:
            DATA_PATH = 'artifacts/data_preprocessed/preprocessed_data.pkl'
            config = ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformationClass(data_path=DATA_PATH, config=data_transformation_config)
            data_transformation.transform_data()
        except Exception as e:
            raise e
