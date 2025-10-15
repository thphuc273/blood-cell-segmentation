import os
import sys
import subprocess
import glob
import shutil
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cellSegmentation.pipeline.training_pipeline import TrainPipeline
from cellSegmentation.utils.main_utils import decodeImage, encodeImageIntoBase64
from cellSegmentation.constant.application import APP_HOST, APP_PORT
from cellSegmentation.logger import logging
from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS, cross_origin
 

application = Flask(__name__)
app = application
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = os.path.join("data", "inputImage.jpg") 
        
@app.route("/")    
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST", "GET"])
@cross_origin()
def predictRoute():
    try:
        img = request.json['image']
        decodeImage(img, clientApp.filename)

        segment_path = "runs/segment"
        if os.path.exists(segment_path):
            for dir_name in os.listdir(segment_path):
                if dir_name.startswith("predict"):
                    dir_path = os.path.join(segment_path, dir_name)
                    shutil.rmtree(dir_path)
                    logging.info(f"Deleted old predict directory: {dir_path}")
        
        model_path = "artifacts/model_trainer/best.pt"
        predict_cmd = [
            "yolo",
            "task=segment",
            "mode=predict",
            f"model={model_path}",
            "conf=0.25",
            f"source={clientApp.filename}",
            "save=true"
        ]
        os.makedirs(segment_path, exist_ok=True)
        subprocess.run(predict_cmd, capture_output=True, text=True, check=True)
        
        output_images = glob.glob("runs/segment/predict/*.jpg")
        if not output_images:
            return Response("No output image found after prediction")
            
        output_image_path = output_images[0]

        opencodebase64 = encodeImageIntoBase64(output_image_path)
        res = {"image": opencodebase64.decode("utf-8")}

        subprocess.run(["rm", "-rf", "runs/segment/predict/"])
        
        return jsonify(res)

    except ValueError as val:
        print("ValueError:", val)
        return jsonify({"error": "Invalid value in request"}), 400
    except KeyError:
        return jsonify({"error": "Missing 'image' key in request"}), 400
    except Exception as e:
        print("Exception:", e)
        return jsonify({"error": "Internal server error"}), 500

# if __name__== "__main__":
#     clientApp = ClientApp()
#     app.run(host=APP_HOST, port=APP_PORT)