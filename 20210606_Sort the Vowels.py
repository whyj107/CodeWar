# Sort the Vowels!
# https://www.codewars.com/kata/59e49b2afc3c494d5d00002a/train/python

# 나의 풀이
def sort_vowels(s):
    result = []
    try:
        for i in s:
            if i.lower() in 'aeiou':
                result.append('|'+ i)
            else:
                result.append(i + '|')
    except:
        pass
    return '\n'.join(result)

# 다른 사람의 풀이
def sort_vowels1(s):
    return "" if not isinstance(s, str) else "\n".join("|" + x if x in "aeiouAEIOU" else x + "|" for x in s)

def sort_vowels2(s):
    try:
        return '\n'.join('|' + i  if i.lower() in 'aioue' else i + '|' for i in s)
    except:
        return ''

print(sort_vowels('Codewars') == 'C|\n|o\nd|\n|e\nw|\n|a\nr|\ns|')
print(sort_vowels('Rnd Te5T') == 'R|\nn|\nd|\n |\nT|\n|e\n5|\nT|')
print(sort_vowels(1337) == '')
print(sort_vowels(None) == '')