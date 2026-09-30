import joblib
from fastapi import FastAPI
import os
import numpy as np
from pydantic import BaseModel

if os.path.exists("Amazon_dataset_model_pipe.pkl"):
    # class stock_inputs(BaseModel):
    #   Open: float
    #  High: float
    # Low: float
    # Close: float
    # Volume: float

    stock_model = joblib.load("Amazon_dataset_model_pipe.pkl")
    # model = FastAPI()

    # @model.post("/Amazon Stock Price Predict")
    def prediction(Open: float, High: float, Low: float, Close: float, Volume: float):
        x = np.array(
            [[Open, High, Low, Close, Volume]])
        prediction = stock_model.predict(x)
        return {"predicted_close_tomorrow": float(prediction[0])}
    try:
        open_price = float(input("Enter the OPEN price: "))
        high_price = float(input("Enter the HIGH Price: "))
        low_price = float(input("Enter the LOW price: "))
        close_price = float(
            input("Enter the CLOSE Price of the Today's day: "))
        volume = float(input("Enter the VOLUME: "))

        prediction_result = prediction(
            open_price, high_price, low_price, close_price, volume)
        print(
            f"Tomorrow's Closing price is predicted to be {prediction_result}")
    except ValueError:
        print("Enter the valid numbers for the inputs")
else:
    print("File unavailable")
