
print(range(4))  # range(0, 4)

# 담겨있는 숫자를 확인하기 위하여 리스트로 형변환(실제 활용시에는 형변환이 필요가 없다)

print(list(range(4)))
print(type(range(4)))  # class = 'range'


print(list(range(1, 5)))  # [1,2,3,4]

print(list(range(0, 10, 2)))  # [0, 2, 4, 6, 8]

print(list(range(0, 10, 3)))  # [0, 3, 6, 9]
