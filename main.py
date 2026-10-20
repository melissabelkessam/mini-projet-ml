from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

model = joblib.load("regression.joblib")


class HouseFeatures(BaseModel):
    size: float
    nb_rooms: float
    garden: float


@app.get("/predict")
def predict_get():
    return {"y_pred": 2}


@app.post("/predict")
def predict_post(features: HouseFeatures):
    X = pd.DataFrame([[features.size, features.nb_rooms, features.garden]],
                     columns=["size", "nb_rooms", "garden"])
    prediction = model.predict(X)
    return {"y_pred": float(prediction[0])}
