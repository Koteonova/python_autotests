import requests
import pytest 


def test_statuscode():
    response = requests.get('https://petstore.swagger.io/v2/pet/600')
    assert response.status_code == 200


def test_body():
    response = requests.get('https://petstore.swagger.io/v2/pet/600')
    assert response.json()['name'] == 'test'  