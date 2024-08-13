import requests

endpoint = 'http://localhost:8000/api/products/11231223123122113122/'


res = requests.get(endpoint)
print(res.json())
