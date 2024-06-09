from src.BankChurn.config.configuration import ConfigurationManager
from src.BankChurn import logger
from src.BankChurn.components.model_trainer import ModelTrainer


STAGE_NAME = "Model Trainer stage"

class ModelTrainerTrainingPipeline:
    def __init__(self) -> None:
        self.config_manager = ConfigurationManager()
        self.logger = logger
        
    def main(self):
        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer_config = ModelTrainer(config=model_trainer_config)
            model_trainer_config.Initialize_model_trainer()
        except Exception as e:
            raise e
