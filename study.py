import requests

url_hh='https://api.hh.ru/suggests/skill_set'
skill = 'Тестирование пользовательского интерфейса'
response = requests.get(url_hh, headers= {'HH-User-Agent':'PostmanRuntime/7.29.2'}, 
params={'text': skill})
print(response.text)