# Cat years, Dog years
# https://www.codewars.com/kata/5a6663e9fd56cb5ab800008b/train/python

# 나의 풀이
def human_years_cat_years_dog_years(human_years):
    dog = (human_years-1)*5 + 15
    cat = (human_years-1)*4 + 15
    if human_years > 1:
        dog += 4
        cat += 5
    return [human_years, cat, dog]

# 다른 사람의 풀이
def human_years_cat_years_dog_years1(x):
    return [x, 24+(x-2)*4 if (x != 1) else 15, 24+(x-2)*5 if (x != 1) else 15]

print(human_years_cat_years_dog_years(1), [1, 15, 15])
print(human_years_cat_years_dog_years(2), [2, 24, 24])
print(human_years_cat_years_dog_years(10), [10, 56, 64])