import requests

url = "http://localhost:8080/api/v1/file"
headers = {"Girder-Token": "your_api_token"}
with open("data.csv", "rb") as file:
    response = requests.post(url, headers=headers, files={"file": file})
print(response.json())
