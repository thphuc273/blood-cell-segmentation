import os
import sys

from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException
from cellSegmentation.components.data_ingestion import DataIngestion

from cellSegmentation.entity.config_entity import DataIngestionConfig
from cellSegmentation.entity.artifacts_entity import DataIngestionArtifact


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
    
    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            logging.info("Start data ingestion in Train Pipeline")
            logging.info("Getting data from url")
            
            data_ingestion = DataIngestion(
                data_ingestion_config=self.data_ingestion_config
            )
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            
            logging.info("Exited data ingestion in Train Pipeline")
            logging.info("Got data from url")
            
            return data_ingestion_artifact
        except Exception as e:
            raise AppException(e, sys)
    def run_pipeline(self) -> None:
        try:
            data_pipeline_artifact = self.start_data_ingestion()
        except Exception as e:
            raise AppException(e, sys)
        
        
    
    
        
