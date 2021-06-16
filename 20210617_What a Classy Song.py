# What a "Classy" Song
# https://www.codewars.com/kata/6089c7992df556001253ba7d/train/python

# 나의 풀이
class Song():
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.many = []

    def how_many(self, arr):
        tmp = set([a.lower() for a in arr]) - set(self.many)
        self.many += tmp
        return len(tmp)

# 다른 사람의 풀이
class Song1:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self._seen = set()

    def how_many(self, people):
        tmp = set(map(str.lower, people))
        res = len(tmp - self._seen)
        self._seen.update(tmp)
        return res


mount_moose = Song('Mount Moose', 'The Snazzy Moose')
print(mount_moose.title, 'Mount Moose')
print(mount_moose.artist, 'The Snazzy Moose')
print(mount_moose.how_many(['John', 'Fred', 'Bob', 'Carl', 'RyAn']), 5)
print(mount_moose.how_many(['JoHn', 'Luke', 'AmAndA']), 2)
print(mount_moose.how_many(['Amanda', 'CalEb', 'CarL', 'Furgus']), 2)
print(mount_moose.how_many(['JOHN', 'FRED', 'BOB', 'CARL', 'RYAN', 'KATE']), 1)
