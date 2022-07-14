import requests

response = requests.get("http://www.google.com")
response.raise_for_status()

data = response.json()
print(data)