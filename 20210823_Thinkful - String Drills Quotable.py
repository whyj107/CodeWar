# Thinkful - String Drills: Quotable
# https://www.codewars.com/kata/5859c82bd41fc6207900007a/train/python

# 나의 풀이
def quotable(name, quote):
    return f'{name} said: "{quote}"'

# 다른 사람의 풀이
def quotable1(name, quote):
    return '{} said: "{}"'.format(name, quote)

print(quotable('Grae', 'Practice makes perfect') == 'Grae said: "Practice makes perfect"')
print(quotable('Dan', 'Get back to work, Grae'), 'Dan said: "Get back to work, Grae"')
print(quotable('Alex', 'Python is great fun'), 'Alex said: "Python is great fun"')
print(quotable('Bethany', 'Yes, way more fun than R'), 'Bethany said: "Yes, way more fun than R"')
print(quotable('Darrell', 'What the heck is this thing?'), 'Darrell said: "What the heck is this thing?"')