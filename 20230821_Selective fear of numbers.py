# Selective fear of numbers
# https://www.codewars.com/kata/55b1fd84a24ad00b32000075/train/python

# 나의 풀이
def am_I_afraid(day,num):
    dic = {"Monday":num==12, "Tuesday":num>95,
          "Wednesday":num==34, "Thursday":num==0,
          "Friday":num%2==0, "Saturday":num==56, "Sunday":abs(num)==666}
    return dic[day]

sample_test_cases = [
#     day       num  expected
    ('Monday',   13,  False),
    ('Sunday', -666,  True),
    ('Tuesday',   2,  False),
    ('Tuesday', 965,  True),
    ('Friday',    2,  True),
]

for day, num, expected in sample_test_cases:
    print(am_I_afraid(day, num), expected)