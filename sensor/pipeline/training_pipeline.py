from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig

class TrainPipeline:
    def __init__(self):
        training_pipeline_config = training_pipeline_config()
        self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=training_pipeline_config)
        self.training_pipeline_config  = training_pipeline_config
     