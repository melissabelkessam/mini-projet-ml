import streamlit as st
import pandas as pd
import joblib

model = joblib.load("regression.joblib")

st.title("Prédiction du prix d'une maison")

size = st.number_input("Taille de la maison (m²)", min_value=0.0, value=100.0)
nb_rooms = st.number_input("Nombre de chambres", min_value=0, value=2, step=1)
garden = st.number_input("Jardin (0 = non, 1 = oui)", min_value=0, max_value=1, value=0, step=1)

X = pd.DataFrame([[size, nb_rooms, garden]], columns=["size", "nb_rooms", "garden"])
prediction = model.predict(X)
st.write("Prix estimé de la maison :", round(prediction[0], 2), "€")
