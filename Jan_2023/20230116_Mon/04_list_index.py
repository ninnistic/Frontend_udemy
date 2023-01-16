boxes = ['A', 'B', ['apple', 'banana', 'cherry']]

print(len(boxes))  # 3
print(boxes[2])  # ['apple', 'banana', 'cherry']
print(boxes[2][-1])  # cherry
print(boxes[-1][1][0])
# b  -> ['apple', 'banana', 'cherry'] -> banana -> banana's [0] = b
