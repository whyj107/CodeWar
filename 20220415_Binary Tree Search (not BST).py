# Binary Tree Search (not BST)
# https://www.codewars.com/kata/5acc79efc6fde7838a0000a0/train/python

# 나의 풀이
from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, value: int, left: Optional[Node] = None, right: Optional[Node] = None):
        self.value = value
        self.left = left
        self.right = right


def search(n: int, root: Optional[Node]) -> bool:
    if root == None: return False

    if n == root.value:
        return True
    else:
        return search(n, root.left) or search(n, root.right)


print(search(666, None), False)

root = Node(666, Node(555), Node(444))
print(search(444, root), True)
print(search(555, root), True)
print(search(666, root), True)
print(search(777, root), False)


root = Node(42)
print(search(42, root), True)
print(search(43, root), False)


SIZE = 20
nodes = [Node(i) for i in range(20)]

for i in range(SIZE):
    idx_left, idx_right = 2 * i + 1, 2 * i + 2
    nodes[i].left = nodes[idx_left] if idx_left < SIZE else None
    nodes[i].right = nodes[idx_right] if idx_right < SIZE else None

for i in range(SIZE):
    print(search(i, nodes[0]), True)

print(search(SIZE, nodes[0]), False)