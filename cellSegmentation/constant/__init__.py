
ARTIFACTS_DIR: str = "artifacts"

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""

DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_DOWNLOAD_URL = "https://drive.google.com/file/d/1wTEKZrV5z8MO4RUKfZgwUaVVK1YPkBth/view?usp=sharing"


"""
Data Validation related constant start with DATA_VALIDATION VAR NAME

"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_STATUS_FILE: str = "status.txt"
DATA_VALIDATION_ALL_REQUIRED_FILE = ["train", "validation", "test", "data.yaml"]

"""
Data Validation related constant start with MODEL_TRAINER VAR NAME

"""
MODEL_TRAINER_DIR_NAME: str = "model_trainer"
MODEL_TRAINER_PRETRAINED_WEIGHT_NAME: str = "yolov9c-seg.pt"
MODEL_TRAINER_EPOCHS: int = 40
MODEL_TRAINER_BATCH_SIZE: int = 16