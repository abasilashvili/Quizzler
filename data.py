import requests

data = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}

response = requests.get(url="https://opentdb.com/api.php", params=data)

question_data = response.json()['results']