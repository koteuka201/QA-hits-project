import requests

BASE_URL='http://127.0.0.1:5000/'

def get_page(path=''):
    return requests.get(f"{BASE_URL}{path}")

def post_form(data, path=''):
    return requests.post(f"{BASE_URL}{path}", data = data)