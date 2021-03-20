# 문제
# Messi is a soccer player with goals in three leagues:
#
# LaLiga
# Copa del Rey
# Champions
# Complete the function to return his total number of goals in all three leagues.
#
# Note: the input will always be valid.
#
# For example:
# 5, 10, 2 --> 17

# 입력 == 출력
# Test.assert_equals(goals(0, 0, 0), 0)
# Test.assert_equals(goals(5, 10, 2), 17)

# My Code
def goals(laLiga, copaDelRey, championsLeague):
    return laLiga+copaDelRey+championsLeague

def goals1(*a):
    return sum(a)

if __name__=='__main__':
    print(goals(0, 0, 0))
    print(goals(5, 10, 2))