# Scaling Squared Strings
# https://www.codewars.com/kata/56ed20a2c4e5d69155000301/train/python

# 나의 풀이
def scale(strng, k, n):
    if strng == "": return ""
    t = []
    for i in strng.split('\n'):
        tmp = ""
        for j in i:
            tmp += j*k
        for _ in range(n):
            t.append(tmp)
    return '\n'.join(t)

#  다른 사람의 풀이
def scale1(strng, k, n):
    words = strng.split()
    words_h = ("".join(char * k for char in word) for word in words)
    return "\n".join("\n".join(word for _ in range(n)) for word in words_h)

def testing(actual, expected):
    print(actual, expected)

a = "abcd\nefgh\nijkl\nmnop"
r = "aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp"
# testing(scale(a, 2, 3), r)
# testing(scale("", 5, 5), "")
# testing(scale("Kj\nSH", 1, 2), "Kj\nKj\nSH\nSH")
print(scale("YVjosW\nHGhKGZ\nLHNMLm\nJtcWCj\ngVtjyk\nOJBkOK", 2, 2))