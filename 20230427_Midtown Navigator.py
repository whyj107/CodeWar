# Midtown Navigator
# https://www.codewars.com/kata/59665001dc23af735700092b/train/python

# 나의 풀이
import re
def midtown_nav(start, end):
    start = start.split('and')
    end = end.split('and')
    b1_n = int(re.sub(r'[^0-9]', '', start[-1])) - int(re.sub(r'[^0-9]', '', end[-1]))
    b1_w = 'north' if b1_n < 0 else 'south'

    b2_n = int(re.sub(r'[^0-9]', '', start[0])) - int(re.sub(r'[^0-9]', '', end[0]))
    b2_w = 'west' if b2_n <= 0 else 'east'

    return f'Walk {abs(b1_n)} blocks {b1_w}, and {abs(b2_n)} blocks {b2_w}'

# 다른 사람의 풀이
def midtown_nav1(*start_end):
    sAv, sSt, eAv, eSt = map(int, re.findall(r'\d+',' '.join(start_end)))
    nV, nH = abs(eSt-sSt), abs(eAv-sAv)
    V,  H  = 'south' if sSt>eSt else 'north', 'east' if sAv>eAv else 'west'
    return f"Walk { nV } blocks { V }, and { nH } blocks { H }"


fixed_cases = (
    ("8th Ave and W 38th St", "7th Ave and W 36th St",
     "Walk 2 blocks south, and 1 blocks east"),

    ("5th Ave and W 46th St", "7th Ave and E 58th St",
     "Walk 12 blocks north, and 2 blocks west")
)

for start, end, expected in fixed_cases:
    print(midtown_nav(start, end), expected)
