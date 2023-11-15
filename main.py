from sensor.exception import SensorException
import sys
from sensor.logger import logging
from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
from sensor.constant.env_variable import MONGO_DB_URL_KEY
from sensor.constant.database import DATABASE_NAME

if __name__ == '__main__':
    training_pipeline_config = TrainingPipelineConfig()
    data_ingestion_config = DataIngestionConfig(training_pipeline_config =training_pipeline_config)
    print(data_ingestion_config.__dict__)

