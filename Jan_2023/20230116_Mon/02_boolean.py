# 23시 이후이고, 잠이 오는 경우
hour = 23
status = 'sleepy'
print(hour >= 22 and status == 'sleepy')  # true

# 23시가 되었으나, 잠이 오지 않는 경우
hour = 23
status = 'nice'
print(hour >= 22 and status == 'sleepy')  # false
