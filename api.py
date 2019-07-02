import requests
p=requests.get('https://reqres.in/api/users?page=2')
print(p.json())
