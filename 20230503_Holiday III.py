# Holiday III - Fire on the boat
# https://www.codewars.com/kata/57e8fba2f11c647abc000944/train/python

# 나의 풀이
def fire_fight(s):
    return s.replace("Fire", "~~")


tests = [
    # [input, expected]
    [
        "Boat Rudder Mast Boat Hull Water Fire Boat Deck Hull Fire Propeller Deck Fire Deck Boat Mast",
        "Boat Rudder Mast Boat Hull Water ~~ Boat Deck Hull ~~ Propeller Deck ~~ Deck Boat Mast"
    ],
    [
        "Mast Deck Engine Water Fire",
        "Mast Deck Engine Water ~~"
    ],
    [
        "Fire Deck Engine Sail Deck Fire Fire Fire Rudder Fire Boat Fire Fire Captain",
        "~~ Deck Engine Sail Deck ~~ ~~ ~~ Rudder ~~ Boat ~~ ~~ Captain"
    ],
]

for inp, exp in tests:
    print(fire_fight(inp), exp)