# Remove All The Marked Elements of a List
# https://www.codewars.com/kata/563089b9b7be03472d00002b/train/python

# 나의 풀이
class List:
    def remove_(self, integer_list, values_list):
        return [i for i in integer_list if not i in values_list]

# 다른 사람의 풀이
class List1(object):
    def remove_(self, integer_list, values_list):
        blacklist = set(values_list)
        return [val for val in integer_list if val not in blacklist]


l = List()

integer_list = [1, 1, 2, 3, 1, 2, 3,4]
values_list = [1, 3]
print(l.remove_(integer_list, values_list), [2, 2, 4])

integer_list = [1, 1, 2, 3, 1, 2, 3, 4, 4, 3, 5, 6, 7, 2, 8]
values_list = [1, 3, 4, 2]
print(l.remove_(integer_list, values_list), [5, 6, 7,8])

integer_list = [8, 2, 7, 2, 3, 4, 6, 5, 4, 4, 1, 2, 3]
values_list = [2, 4, 3]
print(l.remove_(integer_list, values_list), [8, 7, 6, 5, 1])
