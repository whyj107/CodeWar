# Hello, Name or World!
# https://www.codewars.com/kata/57e3f79c9cb119374600046b/train/python

# 나의 풀이
def hello(name=None):
    return f"Hello, {str.title(name)}!" if name else "Hello, World!"

# 다른 사람의 풀이
def hello1(name=''):
    return f"Hello, {name.title() or 'World'}!"

tests = (
    ("John", "Hello, John!"),
    ("aLIce", "Hello, Alice!"),
    ("", "Hello, World!"),
)

for inp, exp in tests:
    print(hello(inp), exp)

print(hello(), "Hello, World!")