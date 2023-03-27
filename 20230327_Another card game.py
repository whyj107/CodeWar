# Another card game
# https://www.codewars.com/kata/633874ed198a4c00286aa39d/train/python

# 나의 풀이
def solution(frank, sam, tom):
    count = 0
    for i in range(4):
        for j in range(4):
            if frank[j] > sam[i] and frank[j] > tom[i]:
                count += 1
                frank[j] = 0
                break
    return count >= 2

print(solution([2, 5, 8, 11], [1, 4, 7, 10], [0, 3, 6, 9]), True)
print(solution([1, 2, 3, 4], [5, 6, 7, 8], [0, 9, 10, 11]), False)