import pytest
import requests

def test_flask_detail():
    url = "http://127.0.0.1:5000/"

    response = requests.get(url)
    print(response.text)
    assert response.status_code ==200

def test_flask_save():
    url = "http://127.0.0.1:5000/"
    data = {"title": "This is pytest 1", "Creator": "Claudia" }

    response = requests.post(url, data=data)
    assert response.status_code == 200