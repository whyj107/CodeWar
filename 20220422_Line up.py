# Line up
# https://www.codewars.com/kata/625d02d7a071210017c8f0c3/train/python

# 나의 풀이
def line_up(hints):
    result = {}
    start = set([i.split()[0] for i in hints]+[i.split()[2] for i in hints])
    for h in hints:
        h = h.split()
        if "left" in h:
            result[h[2]] = h[0]
            if h[0] in start:
                start.remove(h[0])
        elif "right" in h:
            result[h[0]] = h[2]
            if h[2] in start:
                start.remove(h[2])
    start = list(start)[0]
    r = [start]
    while start in result.keys():
        start = result[start]
        r.append(start)
    return r

# 다른 사람의 풀이
def line_up1(hints):
    graph = dict( (a,b) if side=='right' else (b,a) for a,_,b,_,_,side in map(str.split,hints))
    start = (set(graph) - set(graph.values())).pop()
    queue = []
    while start:
        queue.append(start)
        start = graph.get(start)
    return queue

def line_up2(hints: list) -> list:
    d = dict((h[0], h[2]) if h[5] == 'right' else (h[2], h[0]) for h in map(str.split, hints))
    res = list(d.keys() - d.values())
    while res[-1] in d: res.append(d[res[-1]])
    return res

print(line_up(["white has black on his left",
               "red has green on his right",
               "black has green on his left"]),
      ['red', 'green', 'black', 'white'])

print(line_up(["green has pink on his left",
               "green has white on his right",
               "black has red on his right",
               "red has blue on his right",
               "black has white on his left"]),
      ['pink', 'green', 'white', 'black', 'red', 'blue'])

print(line_up(["d has c on his left",
               "c has b on his left",
               "b has a on his left"]),
      ["a", "b", "c", "d"])

print(line_up(["d has c on his right",
               "c has b on his right",
               "b has a on his right"]),
      ['d', 'c', 'b', 'a'])

print(line_up(["red has green on his right",
               "green has red on his left"]),
      ['red', 'green'])