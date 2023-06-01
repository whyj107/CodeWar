# Make acronym
# https://www.codewars.com/kata/57a60bad72292d3e93000a5a/train/python

# 나의 풀이
def to_acronym(inp):
    return ''.join(_[0].upper() for _ in inp.split())

# 다른 사람의 풀이
def to_acronym1(input):
  # only call upper() once
  return ''.join(word[0] for word in input.split()).upper()

tests = (
    ("Code Wars", "CW"),
    ("Water Closet", "WC"),
    ("Portable Network Graphics", "PNG"),
    ("PHP: Hypertext Preprocessor", "PHP"),
    ("hyper text markup language", "HTML"),
)

for t in tests:
    inp, exp = t
    print(to_acronym(inp), exp)
