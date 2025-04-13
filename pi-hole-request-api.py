import requests

url = "https://192.168.15.2/api/auth"
payload = {"password": "CI3ZjCva"}

response = requests.request("POST", url, json=payload, verify=False)

response =  response.json()
""" print(response) """

sid = response["session"]["sid"]
print(sid)

