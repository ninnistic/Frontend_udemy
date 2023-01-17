# Clear

# 신규과목인 'algorithm'을 시험보았더니 90점을 받았다. 성적 딕셔너리에 이를 추가하여라.
# python 과목의 점수가 80점이 아닌 85점으로 정정되었다. 주어진 성적 딕셔너리를 수정하여라.
# 김해피의 전체 과목 평균 점수를 출력하라.

score = {
    'python': 80,
    'django': 89,
    'web': 83
}
score['algorithm'] = 90
score['python'] = 85

avg = 0
for value in score.values():
    avg += value/len(score)

print(avg)
