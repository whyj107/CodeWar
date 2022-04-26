# Kingdoms Ep1:Jousting
# https://www.codewars.com/kata/6138ee916cb50f00227648d9/train/python

# 나의 풀이
def joust(list_field, v_knight_left, v_knight_right):
    if v_knight_left == v_knight_right and v_knight_left == 0:
        return list_field
    length = len(list_field[0])
    l, r = 2, length-3
    while l < r:
        l += v_knight_left
        r -= v_knight_right
    return (f"{' '*(l-2)}$->{' '*(length-l-1)}",
            f"{' '*(r)}<-P{' '*(length-(r+3))}")

input1 = ("$->    ", "    <-P"), 1, 1
# print(joust(*input1) == (" $->   ", "   <-P "))

input2 = ("$->     ", "     <-P"), 1, 1
# print(joust(*input2) == ("  $->   ", "   <-P  "))

input3 = ("$->              ", "              <-P"), 1, 1
# print(joust(*input3) == ("      $->        ", "        <-P      "))

input1 = ("$->    ", "    <-P"), 3, 3
# print(joust(*input1) == ("   $-> ", " <-P   "))

input2 = ("$->     ", "     <-P"), 0, 2
# print(joust(*input2) == ("$->     ", " <-P    "))

input3 = ("$->              ", "              <-P"), 2, 3
print(joust(*input3) == ("      $->        ", "     <-P         "))

input1 = ("$->  ", "  <-P"), 3, 3
# print(joust(*input1) == ("$->  ", "  <-P"))

input2 = ("$->", "<-P"), 3, 3
# print(joust(*input2) == ("$->", "<-P"))

input3 = ("$-> ", " <-P"), 0, 0
print(joust(*input3) == ("$-> ", " <-P"))

input1 = ("$->    ", "    <-P"), 0, 0
print(joust(*input1) == ("$->    ", "    <-P"))