# File Path Operations
# https://www.codewars.com/kata/5844e0890d3bedc5c5000e54/solutions/python

# 나의 풀이
class FileMaster():
    def __init__(self, filepath):
        self.path = filepath.split('/')
        self.file = self.path[-1].split('.')
    def extension(self):
        return self.file[-1]
    def filename(self):
        return self.file[0]
    def dirpath(self):
        return '/'.join(self.path[:-1])+'/'

# 다른 사람의 풀이
class FileMaster1():
    def __init__(self, filepath):
        lk = filepath.rfind('.')
        ls = filepath.rfind('/')
        self.ext = filepath[lk + 1:]
        self.file = filepath[ls + 1:lk]
        self.path = filepath[:ls + 1]

    def extension(self):
        return self.ext

    def filename(self):
        return self.file

    def dirpath(self):
        return self.path