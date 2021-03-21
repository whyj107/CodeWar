# Transportation on vacation
# https://www.codewars.com/kata/568d0dd208ee69389d000016/train/python

# 나의 풀이
def rental_car_cost(d):
    answer = d * 40
    if d >= 7:
        answer -= 50
    elif d >= 3:
        answer -= 20
    return answer

# 다른 사람의 풀이
def rental_car_cost1(d):
  return d * 40 - (d > 2) * 20 - (d > 6) * 30

print(rental_car_cost(1), 40)
print(rental_car_cost(4), 140)
print(rental_car_cost(7), 230)
print(rental_car_cost(8), 270)
