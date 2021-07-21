# Cost of my ride
# https://www.codewars.com/kata/586430a5b3a675296a000395/train/python

# 나의 풀이
def insurance(age, size, num_of_days):
    result = 0
    if not num_of_days < 0:
        if age < 25:
            result += 10
        result += {"economy": 0, "medium": 10, "full-size": 15}.get(size, 15)
        result += 50
    return result * num_of_days

# 다른 사람의 풀이
sc={'economy':0,'medium':10,'full-size':15}
def insurance1(a,s,n):
    return (50+(a<25)*10+sc.get(s,15))*max(0,n)

print(insurance(18, "medium", 7), 490)
print(insurance(30, "full-size", 30), 1950)
print(insurance(21, "economy", -10), 0)
print(insurance(42, "my custom car", 7), 455)