# 문제
# Task
# Given three integers a ,b ,c, return the largest number obtained
# after inserting the following operators and brackets: +, *, ()
# In other words , try every combination of a,b,c with [*+()] , and return the Maximum Obtained

# 입력 == 출력
# Test.it("Small values")
# Test.assert_equals(expression_matter(2, 1, 2), 6)
# Test.assert_equals(expression_matter(2, 1, 1), 4)
# Test.assert_equals(expression_matter(1, 1, 1), 3)
# Test.assert_equals(expression_matter(1, 2, 3), 9)
# Test.assert_equals(expression_matter(1, 3, 1), 5)
# Test.assert_equals(expression_matter(2, 2, 2), 8)
#
# Test.it("Medium values")
# Test.assert_equals(expression_matter(5, 1, 3), 20)
# Test.assert_equals(expression_matter(3, 5, 7), 105)
# Test.assert_equals(expression_matter(5, 6, 1), 35)
# Test.assert_equals(expression_matter(1, 6, 1), 8)
# Test.assert_equals(expression_matter(2, 6, 1), 14)
# Test.assert_equals(expression_matter(6, 7, 1), 48)
#
# Test.it("Mixed values")
# Test.assert_equals(expression_matter(2, 10, 3), 60)
# Test.assert_equals(expression_matter(1, 8, 3), 27)
# Test.assert_equals(expression_matter(9, 7, 2), 126)
# Test.assert_equals(expression_matter(1, 1, 10), 20)
# Test.assert_equals(expression_matter(9, 1, 1), 18)
# Test.assert_equals(expression_matter(10, 5, 6), 300)
# Test.assert_equals(expression_matter(1, 10, 1), 12)

# My Code
def expression_matter(a, b, c):
    if a == 1 and c == 1:
        return a + b + c
    elif a == 1:
        return max((a + b) * c, a + b * c)
    elif b == 1:
        return max((a + b) * c, a * (b + c))
    elif c == 1:
        return max(a * b + c, a * (b + c))
    else:
        return a * b * c

# Warriors Code
def expression_matter_(a, b, c):
    return max(a * b * c, a + b + c, (a + b) * c, a * (b + c))

if __name__=='__main__':
    answer = expression_matter(2, 10, 3)
    print(answer)
    answer = expression_matter(2, 10, 1)
    print(answer)