
import requests


endpoint = 'http://localhost:8000/api/products/'

data = {
    'title': 'new title',
    'price': 20.22
}
res = requests.get(endpoint, json=data)

print(res.json())
