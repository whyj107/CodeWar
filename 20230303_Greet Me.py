# Greet Me
# https://www.codewars.com/kata/535474308bb336c9980006f2/train/python

# 나의 풀이
def greet(name):
    return f'Hello {name.title()}!'

# 다른 사람의 풀이
def greet1(name):
    return f"Hello {name.capitalize()}!"

print(greet('riley'), 'Hello Riley!')
print(greet('molly'), "Hello Molly!")
print(greet('BILLY'), "Hello Billy!")