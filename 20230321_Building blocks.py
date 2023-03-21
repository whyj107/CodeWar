# Building blocks
# https://www.codewars.com/kata/55b75fcf67e558d3750000a3/train/python

# 나의 풀이
class Block:
    def __init__(self, ary):
        self.w = ary[0]
        self.l = ary[1]
        self.h = ary[2]

    def get_width(self): return self.w

    def get_length(self): return self.l

    def get_height(self): return self.h

    def get_volume(self): return self.w * self.l * self.h

    def get_surface_area(self):
        return 2 *(self.w*self.l + self.w*self.h + self.l*self.h)


block1 = Block([2, 2, 2])
print(block1.get_width(), 2)
print(block1.get_length(), 2)
print(block1.get_height(), 2)
print(block1.get_volume(), 8)
print(block1.get_surface_area(), 24)