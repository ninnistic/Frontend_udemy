i = [5, 4, 1, 1, 2, 2, 3]  # list
s = set(i)  # set은 중복 없애고 순서 정렬
print(s)

s2 = set((4, 2, 6))
print(s2)

print(s - s2)  # 차집합
print(s & s2)  # 교집합 and
print(s | s2)  # 합집합 or
