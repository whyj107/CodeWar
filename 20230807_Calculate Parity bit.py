# Calculate Parity bit!
# https://www.codewars.com/kata/5df261342964c80028345a0a/train/python

# 나의 풀이
def check_parity(parity, bin_str):
    cnt = bin_str.count('1')
    if parity == 'even':
        return 0 if cnt%2==0 else 1
    else:
        return 0 if cnt%2!=0 else 1

# 다른 사람의 풀이
def check_parity1(parity, bin_str):
    return [0, 1][bin_str.count("1") % 2 == (parity == "even")]

def check_parity2(parity, bin_str):
    return (parity == "odd") ^ (bin_str.count('1') & 1)