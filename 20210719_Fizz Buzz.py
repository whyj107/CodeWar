# Fizz Buzz
# https://www.codewars.com/kata/5300901726d12b80e8000498/train/python

# 나의 풀이
def fizzbuzz(n):
    return ['FizzBuzz' if i%3==0 and i%5==0 else('Fizz' if i%3==0 else('Buzz' if i%5==0 else i)) for i in range(1, n+1)]

# 다른 사람의 풀이
def fizzbuzz1(n):
    return ['Fizz'*(not i%3) + 'Buzz'*(not i%5) or i for i in range(1, n+1)]

expected = [1,2,'Fizz',4,'Buzz','Fizz',7,8,'Fizz','Buzz']
print(fizzbuzz(10) == expected)