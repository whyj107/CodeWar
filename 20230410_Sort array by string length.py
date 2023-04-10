# Sort array by string length
# https://www.codewars.com/kata/57ea5b0b75ae11d1e800006c/train/python

# 나의 풀이
def sort_by_length(arr):
    return sorted(arr, key=len)


tests = [
    [["i", "to", "beg", "life"], ["beg", "life", "i", "to"]],
    [["", "pizza", "brains", "moderately"], ["", "moderately", "brains", "pizza"]],
    [["short", "longer", "longest"], ["longer", "longest", "short"]],
    [["a", "of", "dog", "food"], ["dog", "food", "a", "of"]],
    [["", "bees", "eloquent", "dictionary"], ["", "dictionary", "eloquent", "bees"]],
    [["a short sentence", "a longer sentence", "the longest sentence"],
     ["a longer sentence", "the longest sentence", "a short sentence"]],
]

for exp, inp in tests:
    print(sort_by_length(inp), exp)