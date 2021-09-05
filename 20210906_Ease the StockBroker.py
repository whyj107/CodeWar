# Ease the StockBroker
# https://www.codewars.com/kata/54de3257f565801d96001200/train/python

# 나의 풀이
def balance_statement(lst):
    buy, sell = 0, 0
    err = []
    for l in lst.split(', '):
        if l == '': break
        tmp = l.split(' ')
        try:
            a = int(tmp[1])
            if '.' in tmp[2]:
                b = float(tmp[2])
            else:
                raise
            if tmp[-1] == 'B':
                buy += (a*b)
            elif tmp[-1] == 'S':
                sell += (a*b)
            else:
                raise
        except:
            err.append(' '.join(tmp) + ' ;')
    return f'Buy: {round(buy)} Sell: {round(sell)}' + (f'; Badly formed {len(err)}: ' + ''.join(err) if len(err) > 0 else '')

# 다른 사람의 풀이
import re
def balance_statement1(lst):
    bad_formed, prices = [], {'B':0, 'S':0}
    for order in filter(None, lst.split(', ')):
        if not re.match('\S+ \d+ \d*\.\d+ (B|S)', order):
            bad_formed.append(order + ' ;')
        else:
            _, quantity, price, status = order.split()
            prices[status] += int(quantity) * float(price)
    ret = "Buy: %.0f Sell: %.0f" % (prices['B'], prices['S'])
    if bad_formed:
        ret += "; Badly formed %d: %s" % (len(bad_formed), ''.join(bad_formed))
    return ret

"""
print(
    balance_statement("ZNGA 1300 2.66 B, "
                      "CLH15.NYM 50 56.32 B, "
                      "OWW 1000 11.623 B, "
                      "OGG 20 580.1 B") ==
    "Buy: 29499 Sell: 0")
print(
    balance_statement("GOOG 90 160.45 B, "
                      "JPMC 67 12.8 S, "
                      "MYSPACE 24.0 210 B, "
                      "CITI 50 450 B, "
                      "CSCO 100 55.5 S") ==
    "Buy: 14440 Sell: 6408; Badly formed 2: MYSPACE 24.0 210 B ;CITI 50 450 B ;")

print(balance_statement("GOOG 113 23.912 P, CSCO 138 87.774 C") ==
      'Buy: 0 Sell: 0; Badly formed 2: GOOG 113 23.912 P ;CSCO 138 87.774 C ;')

print(balance_statement("") == 'Buy: 0 Sell: 0')
"""

print(balance_statement("GOOG 300 542.0 B, AAPL 50 145.0 B, CSCO 250.0 29 B, GOOG 200 580.0 S"),
      '\nBuy: 169850 Sell: 116000; Badly formed 1: CSCO 250.0 29 B ;')