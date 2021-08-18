# Sort and Star
# https://www.codewars.com/kata/57cfdf34902f6ba3d300001e/train/python

# 나의 풀이
def two_sort(array):
    return '***'.join(sorted(array)[0])

# 다른 사람의 풀이
def two_sort1(lst):
    return '***'.join(min(lst))

print(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]), 'b***i***t***c***o***i***n' )
print(two_sort(["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]), 'a***r***e')
print(two_sort(["lets", "talk", "about", "javascript", "the", "best", "language"]), 'a***b***o***u***t')
print(two_sort(["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"]), 'c***o***d***e')
print(two_sort(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]), 'L***e***t***s')