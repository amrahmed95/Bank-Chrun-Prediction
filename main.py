from src.BankChurn import logger
from src.BankChurn.pipeline.stage_00_data_ingestion import DataIngestionTrainingPipeline

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