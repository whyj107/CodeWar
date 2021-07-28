# Parts of a list
# https://www.codewars.com/kata/56f3a1e899b386da78000732/train/python

# 나의 풀이
def partlist(arr):
    return [(' '.join(arr[:i]), ' '.join(arr[i:])) for i in range(1, len(arr))]

# 다른 사람의 풀이
def partlist1(arr):
    new_arr = []
    for x in range(1,len(arr)):
        y = ' '.join(arr[:x])
        z = ' '.join(arr[x:])
        new_arr.append((y,z))
    return new_arr

def testing(actual, expected):
    print(actual, expected)

testing(partlist(["I", "wish", "I", "hadn't", "come"]),
        [("I", "wish I hadn't come"), ("I wish", "I hadn't come"), ("I wish I", "hadn't come"),
         ("I wish I hadn't", "come")])
testing(partlist(["cdIw", "tzIy", "xDu", "rThG"]),
        [("cdIw", "tzIy xDu rThG"), ("cdIw tzIy", "xDu rThG"), ("cdIw tzIy xDu", "rThG")])
testing(partlist(["vJQ", "anj", "mQDq", "sOZ"]),
        [("vJQ", "anj mQDq sOZ"), ("vJQ anj", "mQDq sOZ"), ("vJQ anj mQDq", "sOZ")])