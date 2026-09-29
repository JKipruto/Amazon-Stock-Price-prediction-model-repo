import joblib
from fastapi import FastAPI
import os

if os.path.exists("Amazon_dataset_model_pipe.pkl"):
    print("File available")
