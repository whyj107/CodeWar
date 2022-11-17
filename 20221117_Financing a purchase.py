# Financing a purchase
# https://www.codewars.com/kata/59c68ea2aeb2843e18000109/train/python

# 나의 풀이
def amort(rate, bal, term, num_payments):
    rate = rate/(100*12)
    d = 1-(1+rate)**(-term)
    n = rate * bal
    c = n / d

    for i in range(num_payments):
        n = rate * bal
        princ = c - n
        bal -= princ
        c = n + princ
    return f'num_payment {num_payments} c {round(c)} princ {round(princ)} int {round(n)} balance {round(bal)}'

# 다른 사람의 풀이
def amort1(rate, bal, term, num_payments):
    r = rate / (100 * 12)
    n = r * bal
    d = 1 - (1 + r) ** (-term)
    c = n / d
    for i in range(num_payments):
        int_ = r * bal
        princ = c - int_
        bal -= princ
    return "num_payment %d c %.0f princ %.0f int %.0f balance %.0f" % (num_payments, c, princ, int_, bal)


print(amort(6, 100000, 360, 1),
      "\nnum_payment 1 c 600 princ 100 int 500 balance 99900")
print(amort(6, 100000, 360, 12),
      "\nnum_payment 12 c 600 princ 105 int 494 balance 98772")

"""
print(amort(7.4, 10215, 24, 20),
      "num_payment 20 c 459 princ 445 int 14 balance 1809")
print(amort(7.9, 107090, 48, 41),
      "num_payment 41 c 2609 princ 2476 int 133 balance 17794")
print(amort(6.8, 105097, 36, 4),
      "num_payment 4 c 3235 princ 2685 int 550 balance 94447")
print(amort(3.8, 48603, 24, 10),
      "num_payment 10 c 2106 princ 2009 int 98 balance 28799")
print(amort(1.9, 182840, 48, 18),
      "num_payment 18 c 3959 princ 3769 int 189 balance 115897")
print(amort(1.9, 19121, 48, 2),
      "num_payment 2 c 414 princ 384 int 30 balance 18353")
print(amort(2.2, 112630, 60, 11),
      "num_payment 11 c 1984 princ 1810 int 174 balance 92897")
print(amort(5.6, 133555, 60, 53),
      "num_payment 53 c 2557 princ 2464 int 93 balance 17571")
print(amort(9.8, 67932, 60, 34),
      "num_payment 34 c 1437 princ 1153 int 283 balance 33532")
print(amort(3.7, 64760, 36, 24),
      "num_payment 24 c 1903 princ 1829 int 75 balance 22389")
"""