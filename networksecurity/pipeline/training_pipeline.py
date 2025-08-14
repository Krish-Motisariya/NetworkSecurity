import os
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer

from networksecurity.entity.config_entity import (
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrainerConfig
)

from networksecurity.entity.artifact_entity import (
    DataIngestionArtifact,
    DataValidationArtifact,
    DataTransformationArtifact,
    ModelTrainerArtifact
)

class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()

    def start_data_ingestion(self):
        try:
            data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("Start Data Ingestion")
            data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
            dataingestionartifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"data ingestion completed and artifact : {dataingestionartifact}")
            return dataingestionartifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def start_data_validation(self,data_ingestion_artifact: DataIngestionArtifact):
        try:
            datavalidationconfig = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact, data_validation_config=datavalidationconfig)
            logging.info("Initiate the data validation component")
            datavalidationartifact = data_validation.initiate_data_validation()
            return datavalidationartifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def start_data_transformation(self, data_validation_artifact: DataValidationArtifact):
        try:
            datatransformationconfig = DataTransformationConfig(training_pipeline_config=self.training_pipeline_config)
            data_transformation = DataTransformation(data_validation_artifact=data_validation_artifact, data_transformation_config=datatransformationconfig)
            logging.info("Initiate the Data transformation component")
            datatransformationartifact = data_transformation.initiate_data_transformation()
            return datatransformationartifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def start_model_trainer(self, data_transformation_artifact: DataTransformationArtifact) -> ModelTrainerArtifact:
        try:
            modeltrainerconfig = ModelTrainerConfig(training_pipeline_config=self.training_pipeline_config)
            model_trainer = ModelTrainer(data_transformation_artifact=data_transformation_artifact, model_trainer_config=modeltrainerconfig)
            logging.info("Model trainer component initiated")
            modeltrainerartifact = model_trainer.initiate_model_trainer()
            return modeltrainerartifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def run_pipeline(self):
        try:
            data_ingestion_artifcat = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifcat)
            data_transformation_artifcat = self.start_data_transformation(data_validation_artifact=data_validation_artifact)
            model_trainer_artifact = self.start_model_trainer(data_transformation_artifact=data_transformation_artifcat)
            return model_trainer_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)