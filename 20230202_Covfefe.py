# Covfefe
# https://www.codewars.com/kata/592fd8f752ee71ac7e00008a/train/python

# 나의 풀이
def covfefe(s):
    c = "covfefe"
    return s.replace("coverage", c) if "coverage" in s else f'{s} {c}'

print(covfefe("coverage"),"covfefe")
print(covfefe("coverage coverage"),"covfefe covfefe")
print(covfefe("nothing"),"nothing covfefe")
print(covfefe("double space "),"double space  covfefe")
print(covfefe("covfefe"),"covfefe covfefe")
