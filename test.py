import requests

data = {
    "features": [5.1, 3.5, 1.4, 0.2]
}

response = requests.post("http://localhost:5000/predict", json=data)
print(response.json())
