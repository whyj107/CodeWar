# Drone Fly-By
# https://www.codewars.com/kata/58356a94f8358058f30004b5/train/python

# 나의 풀이
def fly_by(lamps, drone):
    return 'o' * min(len(lamps), len(drone)) + 'x' * (len(lamps)-len(drone))

# 다른 사람의 풀이
def fly_by1(lamps, drone):
    return lamps.replace('x', 'o', drone.count('=') + 1)

print(fly_by('xxxxxx', '====T') == 'ooooox')
print(fly_by('xxxxxxxxx', '==T') == 'oooxxxxxx')
print(fly_by('xxxxxxxxxxxxxxx', '=========T') == 'ooooooooooxxxxx')
