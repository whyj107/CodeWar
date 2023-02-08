# Hamming Distance
# https://www.codewars.com/kata/5410c0e6a0e736cf5b000e69/train/python

# 나의 풀이
def hamming(a, b):
    return sum(i!=j for i, j in zip(a, b))

print(hamming("hello world","hello tokyo"),4);
print(hamming("a man a plan a canal","a man a plan sobanal"),3);
print(hamming("hamming and cheese","Hamming and Cheese"),2);
print(hamming("espresso","Expresso"),2);
print(hamming("old father, old artificer","of my soul the uncreated "),24);