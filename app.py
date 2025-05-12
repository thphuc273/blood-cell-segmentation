import os
import sys
 
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cellSegmentation.logger import logging
from cellSegmentation.pipeline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()

print("Training done")