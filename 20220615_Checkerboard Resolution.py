# Checkerboard Resolution
# https://www.codewars.com/kata/60576b180aef19001bce494d/train/python

# 풀이
def count_checkerboard(w, h, r):
    nW, rW = divmod(w, r)
    nH, rH = divmod(h, r)

    rect = nW * nH // 2 * r ** 2
    rStrip = (nH + nW % 2) // 2 * r * rW
    bStrip = (nW + nH % 2) // 2 * r * rH
    corner = (nH ^ nW) % 2 * rH * rW

    return rect + rStrip + bStrip + corner

def count_checkerboard1(w, h, r):
    rw = w // r // 2 * r + min(w % (2 * r), r)
    rh = h // r // 2 * r + min(h % (2 * r), r)
    return rw * (h - rh) + rh * (w - rw)

print(count_checkerboard(11, 6, 1) == 33)
print(count_checkerboard(11, 6, 2) == 32)
print(count_checkerboard(11, 6, 5) == 31)
print(count_checkerboard(9, 5, 2) == 22)
print(count_checkerboard(9, 5, 4) == 21)
print(count_checkerboard(9, 5, 8) == 5)
print(count_checkerboard(123456, 7654321, 333) == 472485924597)
print(count_checkerboard(10 ** 10, 10, 20) == 5 * 10 ** 10)
print(count_checkerboard(10 ** 10, 11, 21) == 54999999978)
print(count_checkerboard(8 ** 5, 7 ** 9, 124) == 661153496464)
print(count_checkerboard(0, 123, 1) == 0)
print(count_checkerboard(445, 998, 101010) == 0)
print(count_checkerboard(0, 0, 1) == 0)
""""""
