# print할 때, x와 y의 값을 다르게 출력하려면? x = 20, y = 10
x, y = 10, 20

# 방법1. tmp에 넣어서 바꾸기 (임시 변수에 넣어서 바꿈)
tmp = x
x = y
y = tmp

print(x, y)


# 방법2. Pythonic
x, y = 10, 20

y, x = x, y
print(x, y)  # 20, 10
