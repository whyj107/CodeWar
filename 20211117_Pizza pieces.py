# Pizza pieces
# https://www.codewars.com/kata/5551dc71101b2cf599000023/train/python

# 나의 풀이
def max_pizza(cuts):
    return int(1+cuts*(cuts+1)/2) if cuts > -1 else -1

print(max_pizza(-2), -1)
print(max_pizza(0), 1)
print(max_pizza(3), 7)
print(max_pizza(4), 11)
print(max_pizza(5), 16)
print(max_pizza(6), 22)