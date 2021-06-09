# Returning Strings
# https://www.codewars.com/kata/55a70521798b14d4750000a4/train/python

# 나의 풀이
def greet(name):
    return f"Hello, {name} how are you doing today?"

# 다른 사람의 풀이
def greet1(name):
    return "Hello, {} how are you doing today?".format(name)

def greet2(name):
    return "Hello, %s how are you doing today?" % name

def greet3(name):
    return "Hello, " + name + " how are you doing today?"

def greet4(name):
    return "Hello, {name} how are you doing today?".format(name = name)

print(greet('Ryan'), "Hello, Ryan how are you doing today?")
print(greet('Shingles'), "Hello, Shingles how are you doing today?")