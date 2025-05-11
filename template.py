import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

project_name = "cellSegmentation"

list_of_files = [
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/constant/application.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "research/trials.ipynb",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir, filename = os.path.split(filepath)
    
    if file_dir != "":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Creating dir: {file_dir} for the {filename}")
    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, "w"):
            pass
        logging.info(f"Creating empty file: {filename}")
    else:
        logging.info(f"{filename} already created")
