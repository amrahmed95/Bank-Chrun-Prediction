import os
from src.BankChurn import logger
from src.BankChurn.pipeline.stage_00_data_ingestion import DataIngestionTrainingPipeline
from src.BankChurn.pipeline.stage_01_data_PreprocessingAndValidation import DataPreprocessAndValidationTrainingPipeline
from src.BankChurn.pipeline.stage_02_data_transformation import DataTransformationTrainingPipeline
from src.BankChurn.pipeline.stage_03_model_trainer import ModelTrainerTrainingPipeline
from src.BankChurn.pipeline.stage_04_model_evaluation import ModelEvaluationTrainingPipeline


#logger.info("Welcome to our Custom logging")


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nx======================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Preprocess and Validation stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj = DataPreprocessAndValidationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nx======================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data transformation stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nx======================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Trainer stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nx======================x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Evaluation stage"
try:
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj = ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nx======================x")
except Exception as e:
    logger.exception(e)
    raise e

