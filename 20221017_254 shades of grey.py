# 254 shades of grey
# https://www.codewars.com/kata/54d22119beeaaaf663000024/train/python

# 나의 풀이
def shades_of_grey(n):
    if n > 254: n = 254
    return ['#{:02x}{:02x}{:02x}'.format(i, i, i) for i in range(1, n+1, 1)]

# 다른 사람의 풀이
def shades_of_grey1(n):
    return ['#{0:02x}{0:02x}{0:02x}'.format(i+1) for i in range(min(254, n))]

print(shades_of_grey(-2), [])
print(shades_of_grey(-1), [])
print(shades_of_grey(0), [])
print(shades_of_grey(1), ["#010101"])
print(shades_of_grey(2), ["#010101", "#020202"])
print(shades_of_grey(3), ["#010101", "#020202", "#030303"])
print(shades_of_grey(4), ["#010101", "#020202", "#030303", "#040404"])
print(shades_of_grey(5),
      ["#010101", "#020202", "#030303", "#040404", "#050505"])
print(shades_of_grey(6),
      ["#010101", "#020202", "#030303", "#040404", "#050505", "#060606"])
print(shades_of_grey(7),
      ["#010101", "#020202", "#030303", "#040404", "#050505", "#060606", "#070707"])
print(shades_of_grey(8),
      ["#010101", "#020202", "#030303", "#040404", "#050505", "#060606", "#070707", "#080808"])
print(shades_of_grey(9),
      ["#010101", "#020202", "#030303", "#040404", "#050505", "#060606", "#070707", "#080808", "#090909"])
print(shades_of_grey(10),
      ["#010101", "#020202", "#030303", "#040404", "#050505", "#060606", "#070707", "#080808", "#090909", "#0a0a0a"])