import requests

base = 'http://localhost:8000'

endpoint = input('digite endpoint ')

result = requests.get(f'{base}/{endpoint}')


result = result.json()

print(">>>", result['message'])


