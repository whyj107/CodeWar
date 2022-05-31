# The Deaf Rats of Hamelin
# https://www.codewars.com/kata/598106cb34e205e074000031/train/python

# 나의 풀이
def count_deaf_rats(town):
    rat_cnt, p_idx, rat = 0, False, ''
    for t in town:
        if t == 'P':
            p_idx = True
        elif t == '~' or t == 'O':
            rat += t

        if len(rat) == 2:
            if p_idx and rat == '~O':
                rat_cnt += 1
            elif (not p_idx) and rat == 'O~':
                rat_cnt += 1
            rat = ''
    return rat_cnt

# 다른 사람의 풀이
def count_deaf_rats(town):
    return town.replace(' ', '')[::2].count('O')

print(count_deaf_rats("~O~O~O~O P"), 0)
print(count_deaf_rats("P O~ O~ ~O O~"), 1)
print(count_deaf_rats("~O~O~O~OP~O~OO~"), 2)
print(count_deaf_rats("PO~O~O~O~O~O~O~O~O~O~O~O~O~O~O~O~O~O~O~O~O~O~ O~O~O~O~ O~O~O~O~O~O~O~O~O~O~~O~OO~O~O~O~"), 2)