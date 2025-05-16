import os
import sys

from dataclasses import dataclass
from datetime import datetime
from cellSegmentation.constant.training_pipeline import *

ARTIFACTS_DIR: str = "artifacts"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_DOWNLOAD_URL = "https://drive.google.com/file/d/17UiTadFbST80QZHmjMfYP6vWg7cMbGnW/view?usp=sharing"

DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_STATUS_FILE: str = "status.txt"
DATA_VALIDATION_ALL_REQUIRED_FILE = ["train", "validation", "test", "data.yaml"]

MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov9c-seg.pt"
MODEL_TRAINER_EPOCHS: int = 40
MODEL_TRAINER_BATCH_SIZE: int = 16

@dataclass
class TrainingPipelineConfig:
    artifacts_dir: str = ARTIFACTS_DIR
    
training_pipeline_config:TrainingPipelineConfig = TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir, DATA_INGESTION_DIR_NAME
    )
    
    feature_store_file_path: str = os.path.join(
        data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR
    )
    data_download_url: str = DATA_DOWNLOAD_URL
    
@dataclass
class DataValidationConfig:
    data_validation_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir, DATA_INGESTION_DIR_NAME
    )
    
    valid_status_file_dir = os.path.join(data_validation_dir, DATA_VALIDATION_STATUS_FILE)
    
    required_file_list = DATA_VALIDATION_ALL_REQUIRED_FILE
    
@dataclass
class ModelTrainerConfig:
    model_trainer_dir: str = os.path.join(
        training_pipeline_config.artifacts_dir, MODEL_TRAINER_DIR_NAME
    )
    
    weight_name = MODEL_TRAINER_PRETRAINED_WEIGHT_NAME
    
    epochs = MODEL_TRAINER_EPOCHS
    
    batch_size = MODEL_TRAINER_BATCH_SIZE
    
    