from src.BankChurn.config.configuration import ConfigurationManager
from src.BankChurn import logger
from src.BankChurn.components.model_evaluation import ModelEvaluation


STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self) -> None:
        self.config_manager = ConfigurationManager()
        self.logger = logger
        
    def main(self):
        try:
            config = ConfigurationManager()
            model_evaluation_config = config.get_model_evaluation_config()
            model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
            model_evaluation_config.log_into_mlflow()
        except Exception as e:
            raise e
