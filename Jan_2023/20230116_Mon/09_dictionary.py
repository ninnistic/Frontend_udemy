
dict_a = {}
print(type(dict_a))  # class 'dict'

dict_b = dict()
print(type(dict_b))  # class 'dict'

dict_a = {'a': 'apple', 'b': 'banana', 'list': [1, 2, 3]}
print(dict_a['list'])  # [1, 2, 3]

dict_b = dict(a='apple', b='banana', list=[1, 2, 3])
print(dict_b)

# key로 숫자를 지정하려면? Integer가 된다던데...왜 안돼에에엑

dict_c = {1: 'apple', 2: 'banana'}
print(dict_c)
# 이렇게 하면 해결 가능??

# (1='apple', b='banana', 이렇게는 안된다 )
