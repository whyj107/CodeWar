# [Code Golf] An Interesting Ritual
# https://www.codewars.com/kata/63d6dba199b0cc0ff46b5d8a/train/python

# 문제가 뭔말이지 모르겠음
ritual=1 .__eq__
ritual=lambda n:n<2
ritual=2 .__gt__
# 답을 보니까 2보다 작은지 큰지에 관한 것이였음
# 하지만 코드 길이에 대한 제한이 있기 때문에
# lambda나 매직 메소드로 사용해야 되는 문제

# 비교 매직 메소드 관련 문제
# __lt__ : x < y
# __le__ : x <= y
# __gt__ : x > y
# __ge__ : x >= y
# __eq__ : x == y
# __ne__ : x != y

print(ritual(1) == 1, True)
print(ritual(2) == 0, True)