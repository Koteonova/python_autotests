import requests
#1_создание_питомца
response = requests.post("https://petstore.swagger.io/v2/pet", json={
  "id": 600,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response.text)
print(response.status_code)

#2_смена_имени

response1 = requests.put("https://petstore.swagger.io/v2/pet",json={
  "id": 600,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "test",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
})
print(response1.text)
print(response1.status_code)

#3_нахождение_по_id
id_pet=600
response2 = requests.get("https://petstore.swagger.io/v2/pet/600",headers= {'HH-User-Agent':'PostmanRuntime/7.29.2'}, 
params={'petId': id_pet})
print(response2.text)
print(response2.status_code)