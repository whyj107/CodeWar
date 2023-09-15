# Party People
# https://www.codewars.com/kata/65013fc50038a68939098dcf/train/python

# 풀이
def party_people(lst):
    lst = sorted(lst)
    while lst and lst[-1]>len(lst): lst.pop()
    return len(lst)

print(party_people([4, 5, 4, 1]), 1)
print(party_people([10, 12, 15, 15, 5]), 0)
print(party_people([2, 1, 2, 0]), 4)
print(party_people([0, 0, 0, 0]), 4)
print(party_people([5, 5, 5, 5]), 0)
print(party_people([5, 5, 5, 5, 5]), 5)
print(party_people([1, 5, 3, 5, 0]), 5)
print(party_people([13, 8, 11, 15, 13, 3, 12, 13, 6, 3]), 0)
print(party_people([11, 3, 4, 3, 11, 4, 0, 1, 1, 3]), 8)
print(party_people([15, 3, 8, 0, 2, 12, 13, 7, 6]), 3)
print(party_people([3, 11, 15, 5, 3, 4, 10, 8, 14, 6, 13, 1]), 6)
print(party_people([7, 14, 14, 0, 7, 3, 2, 2]), 4)
print(party_people([2, 6, 7, 4, 6, 10, 4, 3, 6, 2, 0]), 11)
print(party_people([0, 2, 3, 5, 6, 6, 6, 7, 11, 12, 13, 14, 16, 19, 20]), 8)