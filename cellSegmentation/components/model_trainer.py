import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException
from cellSegmentation.entity.artifacts_entity import ModelTrainerArtifact
from cellSegmentation.entity.config_entity import ModelTrainerConfig
from cellSegmentation.utils.main_utils import read_yaml_file

class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig):
        self.model_trainer_config = model_trainer_config
    def initiate_model_trainer(self)->ModelTrainerArtifact:
        logging.info("Enter initiate model trainer in Model Trainer")
        try:
            current_dir = os.getcwd()
            logging.info("Unzipping data")
            os.system("unzip data.zip")
            os.system("rm data.zip")
            data_yaml_path = os.path.join(current_dir, "data/data.yaml")
            
            os.system(f"yolo task=segment mode=train model={self.model_trainer_config.weight_name} data={data_yaml_path} epochs = {self.model_trainer_config.epochs} imgsz = 640 save = true") 
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            os.system(f"cp runs/segment/train/weights/best.pt {self.model_trainer_config.model_trainer_dir}")
            os.system("rm -rf yolov9c-seg.pt")
            os.system("rm -rf train")
            os.system("rm -rf validation")
            os.system("rm -rf test")
            os.system("rm -rf data.yaml")
            os.system("rm -rf runs")
            
            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="artifacts/model_trainer/best.pt"
            )
            
            logging.info("Exited model trainer in Model Trainer")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")
            
            return model_trainer_artifact
        except Exception as e:
            raise AppException(e, sys)
