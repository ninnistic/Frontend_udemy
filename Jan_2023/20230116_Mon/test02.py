# 백준 2475번

a = input().split()
acc = 0

for i in range(5):
    # 각 숫자를 제곱하도록 하기
    num = int(a[i])
    # 제곱한 수들의 합 구하기
    acc += int(a[i])**2
    # 제곱한 숫자들을 10으로 나누고 난 나머지 구하기
print(acc % 10)
