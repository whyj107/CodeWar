# Multiply Word in String
# https://www.codewars.com/kata/5ace2d9f307eb29430000092/train/python

# 나의 풀이
def modify_multiply(st, loc, num):
    return '-'.join([st.split()[loc]]*num)

# 다른 사람의 풀이
modify_multiply1=lambda s,l,n:"-".join([s.split()[l]]*n)

print(modify_multiply("This is a string", 3,5), "string-string-string-string-string", "The string is incorrect")
print(modify_multiply("Creativity is the process of having original ideas that have value. It is a process; it's not random.", 8, 10), "that-that-that-that-that-that-that-that-that-that")
print(modify_multiply("Self-control means wanting to be effective at some random point in the infinite radiations of my spiritual existence", 1, 1), "means")
print(modify_multiply("Is sloppiness in code caused by ignorance or apathy? I don't know and I don't care.", 6, 8), "ignorance-ignorance-ignorance-ignorance-ignorance-ignorance-ignorance-ignorance")
print(modify_multiply("Everything happening around me is very random. I am enjoying the phase, as the journey is far more enjoyable than the destination.", 2, 5), "around-around-around-around-around")