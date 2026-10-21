import sys
import requests

URL = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8000"

response = requests.get(f"{URL}/predict")
print("GET:", response.status_code, response.json())

data = {"size": 100, "nb_rooms": 3, "garden": 1}
response = requests.post(f"{URL}/predict", json=data)
print("POST:", response.status_code, response.json())