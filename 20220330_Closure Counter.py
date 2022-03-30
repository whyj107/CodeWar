# Closure Counter
# https://www.codewars.com/kata/60edafd71dad1800563cf933/train/python

# python에서 nonlocal이라는 것을 처음 보았음
# 함수 안의 함수도...

# 풀이
def counter():
    num = 0
    def f():
        nonlocal num
        num += 1
        return num
    return f

def counter1():
    def inner_counter(state=[0]):
        state[0] += 1
        return state[0]
    return inner_counter

print(type(counter).__name__, 'function')
print(counter(), 1)

counter_function = counter()
print(counter_function(), 1)
print(counter_function(), 2)

counter_one = counter()
counter_two = counter()
print(counter_one(), 1)
print(counter_one(), 2)
print(counter_two(), 1)
print(counter_two(), 2)