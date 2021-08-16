# Strings: swap vowels' case
# https://www.codewars.com/kata/5803c0c6ab6c20a06f000026/train/python

# 나의 풀이
def swap_vowel_case(st):
    return st.translate(st.maketrans('aeiouAEIOU', 'AEIOUaeiou'))

# 다른 사람의 풀이
def swap_vowel_case1(st):
    return "".join(x.swapcase() if x in "aeiouAEIOU" else x for x in st)

print(swap_vowel_case(" "), " ")
print(swap_vowel_case("C Is AlIvE!"), "C is alive!")
print(swap_vowel_case("to"), "tO")
print(swap_vowel_case("The"), "ThE")
