import requests
import pytest

def test_statuscode():
    response = requests.get('https://petstore.swagger.io/v2/pet/findByStatus')
    assert response.status_code == 200

def test_piece_of_body():
    response = requests.get('https://api.hh.ru/metro/1')
    assert response.json()['name'] == 'Москва'

def test_body_starship():
    responce = requests.get('https://swapi.dev/api/starships/2')
    assert responce.json()['name'] == 'CR90 corvette'

@pytest.mark.parametrize("key, value, id", [('name','CR90 corvette',2),
('name','Star Destroyer',3),
('name','Sentinel-class landing craft',5)])

def test_body_several(key,value,id):
    response = requests.get(f'https://swapi.dev/api/starships/{id}')
    assert response.json()[key] == value 
