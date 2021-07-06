# The Wide-Mouthed frog!
# https://www.codewars.com/kata/57ec8bd8f670e9a47a000f89/train/python

# 나의 풀이
def mouth_size(animal):
    return "small" if animal.lower() == "alligator" else "wide"

# 다른 사람의 풀이
def mouth_size1(animal):
    mouth = {'alligator':'small'}
    return mouth.get(animal.lower(), 'wide')

print(mouth_size("toucan"),"wide")
print(mouth_size("ant bear"),"wide")
print(mouth_size("alligator"),"small")