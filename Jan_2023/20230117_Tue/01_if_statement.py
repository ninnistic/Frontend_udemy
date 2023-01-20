num = int(input())

if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")

# Better way!(Truthy/Falsy값 이용 )
if num % 2:
    print("홀수입니다")
else:
    print("짝수입니다.")

# 조건 표현식
result = "홀수입니다" if num % 2 else "짝수입니다"
print(result)
