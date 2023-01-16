import requests

url = 'http://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1021'

response = requests.get(url).json()

no1 = response.get('drwtNo1')
no2 = response.get('drwtNo2')
no3 = response.get('drwtNo3')
no4 = response.get('drwtNo4')
no5 = response.get('drwtNo5')
no6 = response.get('drwtNo6')
bonusno = response.get('bnusNo')

"""
for i in range(1, 7) :
    key = f'drwtNo{i}'
    print(response.get(key))
"""
nums = ''
for i in range(1, 7):
    key = f'drwtNo{i}'
    nums += f'{response.get(key)}'

bnusNo = response.get("bnusNo")

print(f'당첨번호는 {no1},{no2},{no3},{no4},{no5},{no6} 그리고 보너스 번호는 {bonusno} 입니다.')
