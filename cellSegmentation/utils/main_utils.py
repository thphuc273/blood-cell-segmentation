import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import yaml
import base64

from cellSegmentation.exception import AppException
from cellSegmentation.logger import logging

def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yml_file:
            logging.info("Read yaml file successfully")
            return yaml.safe_load(yml_file)
    except Exception as e:
        raise AppException(e, sys)

def write_yaml_file(file_path: str, content: object, replace: bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, "w") as file:
            yaml.dump(content, file)
            logging.info("Write yaml file successfully")
    except Exception as e:
        raise AppException(e, sys)
        

def decodeImage(img_str, file_name):
    img_data = base64.b64decode(img_str)
    with open("./data/" + file_name, "wb") as f:
        f.write(img_data)
        f.close()
        
def encodeImageIntoBase64(croppedImgPath):
    with open(croppedImgPath, "rb") as f:
        return base64.b64encode(f.read())