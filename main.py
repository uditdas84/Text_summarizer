from textsummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textsummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textsummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textsummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} starteed <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {STAGE_NAME} complted <<<<")

except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} starteed <<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>> stage {STAGE_NAME} complted <<<<")

except Exception as e:
    logger.exception(e)
    raise e 

STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} starteed <<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>> stage {STAGE_NAME} complted <<<<")

except Exception as e:
    logger.exception(e)
    raise e 