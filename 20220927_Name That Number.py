# Name That Number!
# https://www.codewars.com/kata/579ba41ce298a73aaa000255/train/python

# 나의 풀이 : 노가다....
def name_that_number(x):
    n = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
         5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine",
         10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
         15: "fifteen", 18: "eighteen"}
    a, b = divmod(x, 10)
    if a in [8, 5, 4, 3, 2]:
        return {8: "eighty", 5: "fifty", 4: "forty", 3: "thirty", 2: "twenty"}[a] + (" "+n[b] if b != 0 else "")
    else:
        if not x in n.keys():
            if a == 1:
                return n[b]+"teen"
            else:
                return n[a] + "ty" + (" " + n[b] if b != 0 else "")
        else:
            return n[x]

# 다른 사람의 풀이
numbers = [
    'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
    'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'
]
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
def name_that_number1(x):
    if x < 20:
        return numbers[x]
    a, b = divmod(x - 20, 10)
    if b:
        return '{} {}'.format(tens[a], numbers[b])
    return tens[a]

print(name_that_number(0), 'zero')
print(name_that_number(4), 'four')
print(name_that_number(9), 'nine')
print(name_that_number(23), 'twenty three')
print(name_that_number(17), 'seventeen')
print(name_that_number(67), 'sixty seven')
