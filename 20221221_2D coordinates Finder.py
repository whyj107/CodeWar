# 2D Coordinates Finder!
# https://www.codewars.com/kata/639ac3ded3fb14000ed38f31/train/python

# 나의 풀이
def find_coords(plane):
    result = {}
    plane = plane.split('\n')
    l = len(plane) - 1
    j = 0
    for i in range(l, -1, -1):
        if ((l-i) % 2) != 0: j -= 1
        start = 0 if ((l-i)%2) != 0 else 1
        tmp = j
        for _ in range(start, len(plane[i]), 2):
            if plane[i][_] != ' ':
                result[plane[i][_]] = (l-i, tmp)
            tmp += 1
    return [v for k, v in sorted(result.items())]

# 다른 사람의 풀이
def find_coords1(plane):
    res = []
    for y, line in enumerate(plane.split("\n")[::-1]):
        for x, elem in enumerate(line):
            if elem.isdigit():
                res.append([int(elem), y, (x-y)//2])
    return [(y, x) for _, y, x in sorted(res)]

print(find_coords("\n".join([ "  / / / /", " / / / / ", "/0/1/2/  "])), [(0, 0), (0, 1), (0, 2)])

print(find_coords("\n".join(["  /2/ / /", " /1/ / / ", "/0/ / /  "])), [(0, 0), (1, 0), (2, 0)])

print(find_coords("\n".join(["  /1/ / /", " / / / / ", "/ /0/ /  "])), [(0, 1), (2, 0)])

print(find_coords("\n".join([" 1/ / / /", "0/ / / /3", "/ / / /2 "])), [(1, -1), (2, -1), (0, 3), (1, 3)])