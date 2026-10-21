
#On importe les outils : Streamlit (la page web), pandas (les tableaux) et joblib (pour charger le modèle).
import streamlit as st
import pandas as pd
import joblib

#On recharge le modèle entraîné à l’étape d’avant. C’est l’inverse de joblib.dump.
model = joblib.load("regression.joblib")

st.title("Prédiction du prix d'une maison")

#Ces trois lignes créent 3 champs de saisie.
size = st.number_input("Taille de la maison (m²)", min_value=0.0, value=100.0)
nb_rooms = st.number_input("Nombre de chambres", min_value=0, value=2, step=1)
garden = st.number_input("Jardin (0 = non, 1 = oui)", min_value=0, max_value=1, value=0, step=1)

#On met les 3 valeurs dans un tableau d’une seule ligne, avec les mêmes noms de colonnes et le même ordre que dans train_model.py. Le modèle a appris avec ce format, il faut le lui redonner exactement pareil.
X = pd.DataFrame([[size, nb_rooms, garden]], columns=["size", "nb_rooms", "garden"])
prediction = model.predict(X)
st.write("Prix estimé de la maison :", round(prediction[0], 2), "€")
