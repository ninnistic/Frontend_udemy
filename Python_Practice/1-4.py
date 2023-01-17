# Clear

# 1부터 999까지 출력하기
result = 0
for n in range(1, 1000):
    if n % 2 == 0 or n % 7 == 0:
        result += n
print(result)
