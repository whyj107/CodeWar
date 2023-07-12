# Working with Dictionaries
# https://www.codewars.com/kata/5639302a802494696d000077/train/python

# 나의 풀이
from preloaded import A001055 # to remember you the name of the database

def inf_database(range_, str_, val):
    tmp = []
    if str_ == "equals to":
        tmp = [i for i in range(range_[0], range_[1]+1) if A001055[i] == val]
    elif str_ == "higher than":
        tmp = [i for i in range(range_[0], range_[1]+1) if A001055[i] > val]
    elif str_ == "lower than":
        tmp = [i for i in range(range_[0], range_[1]+1) if A001055[i] < val]
    elif str_ == "higher and equals to":
        tmp = [i for i in range(range_[0], range_[1]+1) if A001055[i] >= val]
    elif str_ == "lower and equals to":
        tmp = [i for i in range(range_[0], range_[1]+1) if A001055[i] <= val]
    else:
        return 'wrong constraint'
    return (len(tmp), tmp)

# 다른 사람의 풀이
import operator
def inf_database1(range_, str_, val):
    ops = {"higher than": operator.gt, "lower than": operator.lt, "equals to": operator.eq,
           "higher and equals to": operator.ge, "lower and equals to": operator.le}
    if str_ not in ops:
        return "wrong constraint"

    result = [i for i in range(range_[0], range_[-1] + 1) if ops[str_](A001055[i], val)]
    return (len(result), result)