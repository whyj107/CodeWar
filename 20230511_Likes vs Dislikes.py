# Likes Vs Dislikes
# https://www.codewars.com/kata/62ad72443809a4006998218a/train/python

# 나의 풀이
def like_or_dislike(lst):
    result = Nothing
    for l in lst:
        if l == result:
            result = Nothing
        else:
            result = l
    return result

# 다른 사람의 풀이
def like_or_dislike2(lst):
	state = 'Nothing'
	for i in lst:
		state = 'Nothing' if i == state else i
	return state

print(like_or_dislike([Dislike]), Dislike, repr([Dislike]))
print(like_or_dislike([Like, Like]), Nothing, repr([Like, Like]))
print(like_or_dislike([Dislike, Dislike]), Nothing, repr([Dislike, Dislike]))
print(like_or_dislike([Like, Like, Like]), Like, repr([Like, Like, Like]))
print(like_or_dislike([Like, Dislike]), Dislike, repr([Like, Dislike]))
print(like_or_dislike([Dislike, Like]), Like, repr([Dislike, Like]))
print(like_or_dislike([Like, Dislike, Dislike]), Nothing, repr([Like, Dislike, Dislike]))
print(like_or_dislike([Dislike, Like, Dislike]), Dislike, repr([Dislike, Like, Dislike]))
print(like_or_dislike([Like, Like, Dislike, Like, Like, Like, Like, Dislike]), Dislike,
                   repr([Like, Like, Dislike, Like, Like, Like, Like, Dislike]))
print(like_or_dislike([]), Nothing, repr([]))