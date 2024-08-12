import requests

endpoint = 'http://localhost:8000/api/'


res = requests.post(endpoint, json={
    "title": "hello world", 'content': "this is content", 'price': 'abc'})
print(res.json())
