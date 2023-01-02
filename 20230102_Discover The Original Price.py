# Discover The Original Price
# https://www.codewars.com/kata/552564a82142d701f5001228/train/python

# 나의 풀이
# dp = x * (1 - sp/100)
def discover_original_price(discounted_price, sale_percentage):
    return round(discounted_price * 100 / (100-sale_percentage), 2)

print(discover_original_price(75, 25), 100)
print(discover_original_price(25, 75), 100)
print(discover_original_price(75.75, 25), 101)
print(discover_original_price(373.85, 11.2), 421)
print(discover_original_price(458.2, 17.13), 552.91)