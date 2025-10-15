#  Blood Cell Segmentation Project

## Overview

This project implements a complete **pipeline for blood cell segmentation** using deep learning.  
It focuses on segmenting blood cells (such as **red blood cells, white blood cells, and platelets**) from microscopic images.

The pipeline includes:

- **Data ingestion** from a remote source (Google Drive)
- **Data validation**
- **Model training** using **YOLOv8** for instance segmentation
- **Flask-based web application** for real-time predictions

This project is built with **Python**, leveraging libraries like **Ultralytics YOLO**, **Flask**, and **OpenCV** for computer vision tasks.

---

## Key Features

- **Data Handling:** Downloads and extracts dataset from Google Drive  
- **Validation:** Ensures required files are present in the dataset  
- **Training:** Trains a YOLOv8 model for segmentation  
- **Inference:** Flask API that accepts base64-encoded images, performs segmentation, and returns the segmented output  

---

## Prerequisites

- Python **3.8+**
- **Git** (for cloning the repository)
- **Google Drive link** for dataset download (must be valid and public)
- **GPU with CUDA** (recommended for faster YOLO training)

---

## Installation

### 1. Clone the repository
```bash
git clone https://github.com/thphuc273/blood-cell-segmentation.git
cd blood-cell-segmentation
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```
---

## How to Run

### 1. Training the Model
Ensure your dataset URL in `data_ingestion.py` is valid and public, pointing to a YOLO-format dataset (images, labels, and `data.yaml`).
```bash
python -m cellSegmentation.pipeline.training_pipeline
```
---
This will:
- Download & extract dataset
- Validate structure
- Train YOLO model
- Save best model → artifacts/model_trainer/best.pt
- Logs are automatically generated.

### 2. Running the Prediction Server
Ensure trained weights exist at:
```
artifacts/model_trainer/best.pt
```
Then start the Flask app:
```
python application.py
```

## Technologies Used

| Category | Libraries |
|--------------|--------------|
| **Deep Learning** | Ultralytics YOLOv8, PyTorch |
| **Computer Vision** | OpenCV, Pillow |
| **Web Backend** | Flask, Flask-CORS |
| **Utilities** | gdown, PyYAML |
| **Logging & Config** | Python logging, YAML |