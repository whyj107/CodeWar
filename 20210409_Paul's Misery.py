# Paul's Misery
# https://www.codewars.com/kata/57ee31c5e77282c24d000024/train/python

# 나의 풀이
def paul(x):
    dic = {"kata": 5, "Petes kata": 10, "eating": 1, "life": 0}
    sum_ = sum(dic[i] for i in x)
    if sum_ < 40:
        return 'Super happy!'
    elif sum_ < 70:
        return 'Happy!'
    elif sum_ < 100:
        return 'Sad!'
    else:
        return 'Miserable!'

# 다른 사람의 풀이
def paul1(x):
    points = {'life': 0, 'eating': 1, 'kata': 5, 'Petes kata': 10}
    misery = sum(map(points.get, x))
    return ['Miserable!', 'Sad!', 'Happy!', 'Super happy!']\
            [(misery<40)+(misery<70)+(misery<100)]

points = {'kata': 5, 'Petes kata': 10, 'life': 0, 'eating': 1}
def paul2(x):
    score = sum(map(points.get, x))
    return (
        'Super happy!' if score < 40 else
        'Happy!' if score < 70 else
        'Sad!' if score < 100 else
        'Miserable!'
    )

print(paul(['life', 'eating', 'life']), 'Super happy!')
print(paul(['life', 'Petes kata', 'Petes kata', 'Petes kata', 'eating']), 'Super happy!')
print(paul(['Petes kata', 'Petes kata', 'eating', 'Petes kata', 'Petes kata', 'eating']), 'Happy!')
