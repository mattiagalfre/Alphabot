import requests

url = 'http://192.168.1.141:5000'
payload = {'username': 'Anthony', 'password': '123456'}

response = requests.post(url, data=payload)
print(response.url)