# 사용자가 입력한 각 자릿수를 더해 출력하는 코드를 작성하라.

s = input('숫자를 입력해주세요 : ')
l = list(map(int, s))
print(sum(l))

# == print(sum(map(int,s)))


# solution 2
acc = 0
for idx in range(len(s)):
    acc = acc + int(s[idx])
print(acc)
