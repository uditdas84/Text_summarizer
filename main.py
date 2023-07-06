from textsummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textsummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} starteed <<<<")
    data_inngestion = DataIngestionTrainingPipeline()
    data_inngestion.main()
    logger.info(f">>>> stage {STAGE_NAME} complted <<<<")

except Exception as e:
    logger.exception(e)
    raise e 