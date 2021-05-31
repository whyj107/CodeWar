# Calculate BMI
# https://www.codewars.com/kata/57a429e253ba3381850000fb/train/python

# 나의 풀이
def bmi(weight, height):
    bmi = weight/(height**2)
    return "Underweight" if bmi <= 18.5 else ("Normal" if bmi <= 25 else ("Overweight" if bmi <= 30 else "Obese"))

# 다른 사람의 풀이
def bmi1(weight, height):
    b = weight / height ** 2
    return ['Underweight', 'Normal', 'Overweight', 'Obese'][(b > 30) + (b > 25) + (b > 18.5)]

print(bmi(50, 1.80), "Underweight")
print(bmi(80, 1.80), "Normal")
print(bmi(90, 1.80), "Overweight")
print(bmi(110, 1.80), "Obese")
print(bmi(50, 1.50), "Normal")