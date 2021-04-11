# Well of Ideas - Harder Version
# https://www.codewars.com/kata/57f22b0f1b5432ff09001cab/train/python

# 나의 풀이
def well(arr):
    cnt = 0
    for a in arr:
        for i in a:
            if str(i).upper() == "GOOD": cnt += 1
    return 'Fail!' if cnt == 0 else ('Publish!' if cnt < 3 else 'I smell a series!')

# 다른 사람의 풀이
def well1(arr):
    good_ideas = str(arr).lower().count('good')
    return 'I smell a series!' if (good_ideas > 2) else 'Fail!' if not(good_ideas) else 'Publish!'

print(well([['bad', 'bAd', 'bad'], ['bad', 'bAd', 'bad'], ['bad', 'bAd', 'bad']]), 'Fail!')
print(well([['gOOd', 'bad', 'BAD', 'bad', 'bad'], ['bad', 'bAd', 'bad'], ['GOOD', 'bad', 'bad', 'bAd']]), 'Publish!')
print(well([['gOOd', 'bAd', 'BAD', 'bad', 'bad', 'GOOD'], ['bad'], ['gOOd', 'BAD']]), 'I smell a series!')
