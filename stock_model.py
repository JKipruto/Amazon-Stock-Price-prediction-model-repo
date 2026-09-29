import joblib
from fastapi import FastAPI
import os
import numpy as np
from pydantic import BaseModel

if os.path.exists("Amazon_dataset_model_pipe.pkl"):
    class stock_inputs(BaseModel):
        Open: float
        High: float
        Low: float
        Close: float
        Volume: float

    stock_model = joblib.load("Amazon_dataset_model_pipe.pkl")
    model = FastAPI()

    @model.post("/Amazon Stock Price Predict")
    def prediction(data: stock_inputs):
        x = np.array(
            [[data.Open, data.High, data.Low, data.Close, data.Volume]])
        prediction = stock_model.predict(x)
        return {"predicted_close_tomorrow": float(prediction[0])}
else:
    print("File unavailable")
