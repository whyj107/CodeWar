# Thinkful - Logic Drills: Traffic light
# https://www.codewars.com/kata/58649884a1659ed6cb000072/train/python

# 나의 풀이
def update_light(current):
    return {'green': 'yellow', 'yellow': 'red', 'red': 'green'}.get(current)

# 다른 사람의 풀이
def update_light1(current):
    return {"green": "yellow", "yellow": "red", "red": "green"}[current]

def update_light2(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"
    else:
        return "This is not a traffic light color."

print(update_light('green'), 'yellow')
print(update_light('yellow'), 'red')
print(update_light('red'), 'green')