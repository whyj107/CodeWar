# Circular List
# https://www.codewars.com/kata/5b2e60742ae7543f9d00005d/train/python

# 나의 풀이
class CircularList():
    def __init__(self, *args):
        self.a = args
        self.idx = -1
        if len(self.a) == 0: raise

    def next(self):
        self.idx += 1
        if self.idx == len(self.a):
            self.idx = 0
        return self.a[self.idx]

    def prev(self):
        self.idx -= 1
        if self.idx < 0:
            self.idx = len(self.a) - 1
        return self.a[self.idx]

# 다른 사람의 풀이
class CircularList1:
    def __init__(self, *args):
        if not args:
            raise TypeError
        self.xs = args
        self.i = None

    def next(self):
        self.i = 0 if self.i is None else (self.i + 1) % len(self.xs)
        return self.xs[self.i]

    def prev(self):
        self.i = -1 if self.i is None else (self.i - 1) % len(self.xs)
        return self.xs[self.i]

list = CircularList("one", "two", "three")
print(list.next(), "one")
print(list.next(), "two")
print(list.next(), "three")
print(list.next(), "one")
print(list.prev(), "three")
print(list.prev(), "two")
print(list.prev(), "one")
print(list.prev(), "three")

list1 = CircularList(1, 2, 3, 4, 5)
print(list1.prev(), 5)
print(list1.prev(), 4)
print(list1.next(), 5)
print(list1.next(), 1)
print(list1.prev(), 5)
print(list1.prev(), 4)
print(list1.prev(), 3)
print(list1.prev(), 2)
