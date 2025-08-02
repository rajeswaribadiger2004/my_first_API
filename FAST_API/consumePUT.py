import requests.json
payload=json.dumps({
    "age": 21, ",
    "sex": "F"
})
response = requests.put("http://127.0.0.1:8000/predict?age=21&sex=F", data=payload)
print(response.json())

