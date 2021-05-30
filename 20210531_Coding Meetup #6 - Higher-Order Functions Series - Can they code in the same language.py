# Coding Meetup #6 - Higher-Order Functions Series - Can they code in the same language?
# https://www.codewars.com/kata/58287977ef8d4451f90001a0/train/python

# 나의 풀이
def is_same_language(lst):
    return len(set(i["language"] for i in lst)) == 1

list1 = [
    {'firstName': 'Daniel', 'lastName': 'J.', 'country': 'Aruba', 'continent': 'Americas', 'age': 42,
     'language': 'JavaScript'},
    {'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 22,
     'language': 'JavaScript'},
    {'firstName': 'Hanna', 'lastName': 'L.', 'country': 'Hungary', 'continent': 'Europe', 'age': 65,
     'language': 'JavaScript'},
]

list2 = [
    {'firstName': 'Mariami', 'lastName': 'G.', 'country': 'Georgia', 'continent': 'Europe', 'age': 29,
     'language': 'Python'},
    {'firstName': 'Mia', 'lastName': 'H.', 'country': 'Germany', 'continent': 'Europe', 'age': 39,
     'language': 'Ruby'},
    {'firstName': 'Maria', 'lastName': 'I.', 'country': 'Greece', 'continent': 'Europe', 'age': 32,
     'language': 'C'},
]

print(is_same_language(list1), True)
print(is_same_language(list2), False)