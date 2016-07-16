import requests

URL = 'http://localhost:8000/api/v1/members/'

headers = {'X-AUTH-TOKEN': 'myStatticAp1t0k3n'}

response = requests.get(URL,headers=headers)
import pudb; pu.db
print(response)
print(response.text)
