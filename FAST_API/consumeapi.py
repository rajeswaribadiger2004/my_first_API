import requests
age=15
sex="F"
response=requests.get(f"http://127.0.0.1:8000/predict?age=21&sex=F")
output=response.json()
print(output)