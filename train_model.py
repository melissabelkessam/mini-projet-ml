def build_model():
    import pandas as pd
    from sklearn.linear_model import LinearRegression
    import joblib

    df = pd.read_csv('houses.csv') # 1. lire le tableau

    df = df[df['price'] > 0] # 2. supprimer les prix négatifs (nettoyage)

    X = df[['size', 'nb_rooms', 'garden']] # 3. les entrées (features)
    y = df['price'] # 4. ce qu'on veut prédire (la cible)
    model = LinearRegression()
    model.fit(X, y) # 6. entraîner : le modèle apprend le lien entre X et y
    joblib.dump(model, "regression.joblib") # 7. sauvegarder le modèle dans un fichier


build_model()
