import requests

url = "http://127.0.0.1:5000/signal_stop"

requests.post(url, json={"id": 2})
