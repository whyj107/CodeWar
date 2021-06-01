# Turn String Input into Hash
# https://www.codewars.com/kata/52180ce6f626d55cf8000071/train/python

# 나의 풀이
def str_to_hash(st):
    return {i.split('=')[0]: int(i.split('=')[1]) for i in st.split(', ')} if st != '' else {}

# 다른 사람의 풀이
from re import findall
def str_to_hash1(st):
    return {i:int(j)for i, j in findall(r'(\w+)=(\d+)',st)}

print(str_to_hash("a=1, b=2, c=3, d=4"), { 'a': 1, 'b': 2, 'c': 3, 'd': 4})
print(str_to_hash(""), {})