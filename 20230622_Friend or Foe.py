# Friend or Foe?
# https://www.codewars.com/kata/55b42574ff091733d900002f/train/python

# 나의 풀이
def friend(x):
    return [_ for _ in x if len(_)==4]

print(friend(["Ryan", "Kieran", "Mark", ]), ["Ryan", "Mark"])
print(friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]), ["Ryan"])
print(friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]), ["Jimm", "Cari", "aret"])