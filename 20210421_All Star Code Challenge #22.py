# All Star Code Challenge #22
# https://www.codewars.com/kata/5865cff66b5699883f0001aa/train/python

# 나의 풀이
def to_time(seconds):
    return f"{seconds//3600} hour(s) and {seconds//60%60} minute(s)"

# 다른 사람의 풀이
def to_time1(seconds):
    return '{} hour(s) and {} minute(s)'.format(*divmod(seconds // 60, 60))

print(to_time(3600), '1 hour(s) and 0 minute(s)')
print(to_time(3601), '1 hour(s) and 0 minute(s)')
print(to_time(3500), '0 hour(s) and 58 minute(s)')
print(to_time(323500), '89 hour(s) and 51 minute(s)')
print(to_time(0), '0 hour(s) and 0 minute(s)')