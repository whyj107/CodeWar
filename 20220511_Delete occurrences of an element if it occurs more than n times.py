# Delete occurrences of an element if it occurs more than n times
# https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python

# 나의 풀이
def delete_nth(order, max_e):
    result = []
    for o in order:
        if result.count(o) != max_e:
            result.append(o)
    return result

# 다른 사람의 풀이
def delete_nth1(order,max_e):
    return [o for i, o in enumerate(order) if order[:i].count(o)<max_e ] # yes!



print(delete_nth([20, 37, 20, 21], 1),
                 [20, 37, 21])
print(delete_nth([1, 1, 3, 3, 7, 2, 2, 2, 2], 3),
                 [1, 1, 3, 3, 7, 2, 2, 2])