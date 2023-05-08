# Fibonacci's FizzBuzz
# https://www.codewars.com/kata/57bf599f102a39bb1e000ae5/train/python

# 나의 풀이
# 3으로 나눠지면 Fizz, 5로 나눠지면 Buzz, 15로 나눠지면 FizzBuzz
def fibs_fizz_buzz(n):
    result = []
    x, y = 0, 1
    for i in range(n):
        x, y = y, y+x
        if x%15 == 0:
            result.append('FizzBuzz')
        elif x%5 == 0:
            result.append('Buzz')
        elif x%3 == 0:
            result.append('Fizz')
        else:
            result.append(x)
    return result

# 다른 사람의 풀이
def fibs_fizz_buzz1(n):
    a, b, out = 0, 1, []

    for i in range(n):
        s = "Fizz" * (b % 3 == 0) + "Buzz" * (b % 5 == 0)
        out.append(s if s else b)
        a, b = b, a + b

    return out

tests = [
    (2, [1, 1]),
    (5, [1, 1, 2, 'Fizz', 'Buzz']),
    (7, [1, 1, 2, 'Fizz', 'Buzz', 8, 13]),
    (10, [1, 1, 2, 'Fizz', 'Buzz', 8, 13, 'Fizz', 34, 'Buzz']),
    (15, [1, 1, 2, 'Fizz', 'Buzz', 8, 13, 'Fizz', 34, 'Buzz', 89, 'Fizz', 233, 377, 'Buzz']),
    (20, [1,1,2,"Fizz","Buzz",8,13,"Fizz",34,"Buzz",89,"Fizz",233,377,"Buzz","Fizz",1597,2584,4181,"FizzBuzz"]),
    (1, [1]),
    (40, [1,1,2,"Fizz","Buzz",8,13,"Fizz",34,"Buzz",89,"Fizz",233,377,"Buzz","Fizz",1597,2584,4181,"FizzBuzz",10946,17711,28657,"Fizz","Buzz",121393,196418,"Fizz",514229,"Buzz",1346269,"Fizz",3524578,5702887,"Buzz","Fizz",24157817,39088169,63245986,"FizzBuzz"]),
]

for args, expected in tests:
    print(fibs_fizz_buzz(args), expected)