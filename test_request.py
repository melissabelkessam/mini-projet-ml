import requests

# Test GET
response = requests.get("http://127.0.0.1:8000/predict")
print("GET:", response.status_code, response.json())

# Test POST
data = {"size": 100, "nb_rooms": 3, "garden": 1}
response = requests.post("http://127.0.0.1:8000/predict", json=data)
print("POST:", response.status_code, response.json())