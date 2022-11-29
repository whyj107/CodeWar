# Finding Arrows in a String
# https://www.codewars.com/kata/63744cbed39ec3376c84ff4a/train/python

# 다른 사람의 풀이 : 봐도 이해가 잘 안되는구만
import re  # regex is good, let's use it
def arrow_search1(string: str) -> int:
    return sum(  # calculate sum of scores for each arrow
        # using the below method:
        len(arrow)  # size of the arrow
        * ((">" in arrow) - ("<" in arrow))  # multiplied by +1/-1 based on direction
        * (2 if "=" in arrow else 1)  # multiplied by 2 if it has a tail of "="

        for arrow in re.findall(  # for each arrow found
            """                             # using the below regex:
            <?-+>?                          #   arrow with "-" tail
               |                            #         or
            <?=*>?                          #   arrow with "=" tail
            """, string, re.VERBOSE)  # in the input string
    )

# 이 방법이 이해하기 쉽다
def arrow_search(s: str) -> int:
    return sum(points(m[0]) for m in re.finditer(r'<?(?:-+|=*)>?', s))
def points(s:str):
    sign = len(s) and (s[-1]=='>') - (s[0]=='<')
    coef = 1 + ('=' in s)
    return len(s) * coef * sign

print(arrow_search('>.'), 1)
print(arrow_search('<--..'), -3)
print(arrow_search('><=><--'), -2)
print(arrow_search('>===>->'), 11)
print(arrow_search('......'), 0)
print(arrow_search('<-->'), 0)