import os
import sys
import shutil
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException
from cellSegmentation.entity.artifacts_entity import DataIngestionArtifact, DataValidationArtifact
from cellSegmentation.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(
        self,
        data_ingestion_artifacts: DataIngestionArtifact,
        data_validation_config: DataValidationConfig
    ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifacts
            self.data_validation_config = data_validation_config
            
        except Exception as e:
            raise AppException(e, sys)
    
    def validate_all_files_exist(self)->bool:
        try:
            validation_status = None
            
            all_files = os.listdir(self.data_ingestion_artifact.feature_store_path)
            all_files = [f for f in all_files if f not in ['data.yaml', '.gitkeep']]
            for file in all_files:
                if file not in self.data_validation_config.required_file_list:
                    validation_status = True
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok=True)
                    with open(self.data_validation_config.valid_status_file_dir, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
            return validation_status
   
        except Exception as e:
            raise AppException(e, sys)      
    def initiate_data_validation(self)-> DataValidationArtifact:
        logging.info("Entered initiate data validation method")
        try: 
            status = self.validate_all_files_exist()
            data_validation_artifact = DataValidationArtifact(
                validation_status = status)  
            logging.info("Exited data validation")
            logging.info(f"Data validation artifacts: {data_validation_artifact}")
            
            if status:
                shutil.copy(self.data_ingestion_artifact.data_zip_file_path, os.getcwd())
            return data_validation_artifact
        except Exception as e:
            raise AppException(e, sys)    
