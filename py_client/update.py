import requests

endpoint = 'http://localhost:8000/api/products/1/update/'

data = {
    'title': 'hello world my old friend',
    'price': 1299.22

}

res = requests.put(endpoint, json=data)
print(res.json())
