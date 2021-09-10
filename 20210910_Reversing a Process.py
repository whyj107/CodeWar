# Reversing a Process
# https://www.codewars.com/kata/5dad6e5264e25a001918a1fc/train/python

# 풀이
def decode(r):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    n = int(''.join([i for i in r if i.isdigit()]))
    r = r.replace(str(n), '')
    result = ''.join(alpha[a] for i in r for a in range(26) if alpha[a*n%26] == i)
    return "Impossible to decode" if len(result) != len(r) else result

def testing_decode(s, exp):
    actual = decode(s)
    print(actual == exp)

testing_decode("1273409kuqhkoynvvknsdwljantzkpnmfgf", "uogbucwnddunktsjfanzlurnyxmx")
testing_decode("761328qockcouoqmoayqwmkkic", "Impossible to decode")
testing_decode("1544749cdcizljymhdmvvypyjamowl", "mfmwhbpoudfujjozopaugcb")
testing_decode("1122305vvkhrrcsyfkvejxjfvafzwpsdqgp", "rrsxppowmjsrclfljrajtybwviqb")