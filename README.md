# Mini-projet : modèle de Machine Learning dans un service web

Modèle de régression linéaire qui prédit le prix d'une maison à partir de :
- `size` : taille en m²
- `nb_rooms` : nombre de chambres
- `garden` : jardin (0 = non, 1 = oui)

## Fichiers

| Fichier | Rôle |
|---|---|
| `houses.csv` | Données d'entraînement |
| `train_model.py` | Nettoie les données (prix négatifs supprimés) et entraîne le modèle → `regression.joblib` |
| `model_app.py` | Application Streamlit |
| `main.py` | API FastAPI (GET et POST sur `/predict`) |
| `test_request.py` | Test de l'API avec `requests` |
| `Dockerfile` | Image Docker de l'API |
| `requirements.txt` | Dépendances Python |

## 1. Entraîner le modèle

```bash
pip install -r requirements.txt
python train_model.py
```

## 2. Streamlit

```bash
pip install streamlit
streamlit run model_app.py
```

## 3. API FastAPI (Niveau 0)

```bash
uvicorn main:app --reload
```

- GET : http://127.0.0.1:8000/predict → `{"y_pred": 2}`
- POST : http://127.0.0.1:8000/predict avec le JSON `{"size": 100, "nb_rooms": 3, "garden": 1}`
- Documentation interactive : http://127.0.0.1:8000/docs

```bash
python test_request.py
```

## 4. Sur la machine distante (Niveau 0.5)

```bash
uvicorn main:app --host 0.0.0.0 --port 8213
```

## 5. Docker (Niveaux 1 et 2)

```bash
docker build -t house-api .
docker run -d -p 8213:8213 house-api
```

Puis : http://<IP>:8213/docs
