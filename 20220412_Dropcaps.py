# Dropcaps
# https://www.codewars.com/kata/559e5b717dd758a3eb00005a/train/python

# 나의 풀이
def drop_cap(str_):
    tmp = ''
    result = ''
    for s in str_:
        if s != ' ':
            tmp += s
        else:
            result += (tmp.capitalize() if len(tmp)>2 else tmp) + s
            tmp = ''
    return result + (tmp.capitalize() if len(tmp)>2 else tmp)

# 다른 사람의 풀이
def drop_cap1(str_):
    return ' '.join( w.capitalize() if len(w) > 2 else w for w in str_.split(' ') )

print(drop_cap('Apple Banana'), "Apple Banana")
print(drop_cap('Apple'), "Apple")
print(drop_cap(''), "")