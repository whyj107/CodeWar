# Last Survivor
# https://www.codewars.com/kata/609eee71109f860006c377d1/train/python

# 나의 풀이
def last_survivor(letters, coords):
    letters = [l for l in letters]
    for c in coords:
        del letters[c]
    return ''.join(letters)

# 다른 사람의 풀이
def last_survivor1(letters, coords):
    l=[x for x in letters]
    [l.pop(x) for x in coords]
    return l[0]

def last_survivor2(letters, coords):
    for i in range(len(coords)):
        letters = letters[:coords[i]] + letters[coords[i] + 1:]
    return letters

print(last_survivor('abc', [1, 1]), 'a')
print(last_survivor('kbc', [0, 1]), 'b')
print(last_survivor('zbk', [2, 1]), 'z')
print(last_survivor('c', []), 'c')
print(last_survivor('foiflxtpicahhkqjswjuyhmypkrdbwnmwbrrvdycqespfvdviucjoyvskltqaqirtjqulprjjoaiagobpftywabqjdmiofpsr', [8, 59, 52, 93, 21, 40, 88, 85, 59, 10, 82, 18, 74, 59, 51, 47, 75, 49, 23, 56, 1, 33, 39, 33, 34, 44, 25, 0, 51, 25, 36, 32, 57, 10, 57, 12, 51, 55, 24, 55, 31, 49, 6, 15, 10, 48, 27, 29, 38, 30, 35, 42, 23, 32, 9, 39, 39, 36, 8, 29, 2, 33, 14, 3, 13, 25, 9, 25, 18, 10, 1, 2, 20, 8, 2, 11, 5, 7, 0, 10, 10, 8, 12, 3, 5, 1, 7, 7, 5, 1, 4, 0, 4, 0, 0, 1]), 'd')