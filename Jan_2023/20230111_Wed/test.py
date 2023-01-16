# import requests
# url = 'http://api.agify.io/?name=jiyoung'
# print(requests.get(url).json())

# 실행하는 방법?

import requests

url = 'http://api.agify.io/?name=jiyoung'

response = requests.get(url).json()

name = response.get('name')
age = response.get('age')

print(f'{name}의 나이는 {age}살 입니다.')
