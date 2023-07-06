# Minimum Perimeter of a Rectangle
# https://www.codewars.com/kata/5826f54cc60c7e5266000baf/train/python

# 나의 풀이
def minimum_perimeter(area):
    result = 5*(10**10)
    for i in range(1, int(area**0.5)+1):
        if area%i==0:
            result = min(result, (i+(area//i))*2)
    return result
