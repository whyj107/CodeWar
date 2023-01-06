# Lottery Ticket
# https://www.codewars.com/kata/57f625992f4d53c24200070e/train/python

# 나의 풀이
def bingo(ticket, win):
    cnt = sum(chr(n) in s for s, n in ticket)
    return 'Loser!' if cnt < win else 'Winner!'

# 다른 사람의 풀이
def bingo1(ticket, win):
    return 'Winner!' if sum(chr(n) in s for s, n in ticket) >= win else 'Loser!'

print(bingo([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 2), 'Loser!')
print(bingo([['ABC', 65], ['HGR', 74], ['BYHT', 74]], 1), 'Winner!')
print(bingo([['HGTYRE', 74], ['BE', 66], ['JKTY', 74]], 3), 'Loser!')

