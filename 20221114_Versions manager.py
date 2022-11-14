# Versions manager
# https://www.codewars.com/kata/5bc7bb444be9774f100000c3/train/python

# 나의 풀이 : rollback의 오류 발생시키는 부분에서 자꾸 오류가 발생했다.
# 아직 왜 이런지 잘 모르겠다.
class VersionManager1:
    preV = ''

    def __init__(self, version="0.0.1"):
        if version == '': version = "0.0.1"
        self.v = ['0', '0', '0']
        for idx, v in enumerate(version.split('.')[:3]):
            if not v.isnumeric():
                raise Exception('Error occured while parsing version!')
            if idx < 3:
                self.v[idx] = v

    def release(self):
        return '.'.join(self.v)

    def major(self):
        VersionManager.preV = '.'.join(self.v)
        self.v = [str(int(self.v[0])+1), '0', '0']
        return VersionManager('.'.join(self.v))

    def minor(self):
        VersionManager.preV = '.'.join(self.v)
        self.v = [self.v[0], str(int(self.v[1])+1), '0']
        return VersionManager('.'.join(self.v))

    def patch(self):
        VersionManager.preV = '.'.join(self.v)
        self.v = [self.v[0], self.v[1], str(int(self.v[2])+1)]
        return VersionManager('.'.join(self.v))

    def rollback(self):
        if VersionManager.preV == '':
            raise Exception('Cannot rollback!')
        self.v = VersionManager.preV
        return VersionManager(self.v)

# 다른 사람의 풀이
class VersionManager:

    def __init__(self, version=None):
        if not version: version = '0.0.1'
        self.__memory = []
        try:
            arr = [*map(int, version.split('.')[:3])] + [0, 0, 0]
        except:
            raise Exception("Error occured while parsing version!")
        del arr[3:]
        self.__version = arr if any(arr) else [0, 0, 1]

    def release(self):
        return '.'.join(map(str, self.__version))

    def rollback(self):
        if not self.__memory: raise Exception("Cannot rollback!")
        self.__version = self.__memory.pop()
        return self

    def __update(self, i):
        self.__memory.append([*self.__version])
        self.__version[i] += 1
        self.__version[i + 1:] = [0] * (len(self.__version) - 1 - i)
        return self

    def major(self): return self.__update(0)

    def minor(self): return self.__update(1)

    def patch(self): return self.__update(2)


print(VersionManager().release(), "0.0.1")
print(VersionManager("").release(), "0.0.1")
print(VersionManager("1.2.3").release(), "1.2.3")
print(VersionManager("1.2.3.4").release(), "1.2.3")
print(VersionManager("1.2.3.d").release(), "1.2.3")
print(VersionManager("1").release(), "1.0.0")
print(VersionManager("1.1").release(), "1.1.0")

print(VersionManager().major().release(), "1.0.0")
print(VersionManager("1.2.3").major().release(), "2.0.0")
print(VersionManager("1.2.3").major().major().release(), "3.0.0")

print(VersionManager().minor().release(), "0.1.0")
print(VersionManager("1.2.3").minor().release(), "1.3.0")
print(VersionManager("1").minor().release(), "1.1.0")
print(VersionManager("4").minor().minor().release(), "4.2.0")

print(VersionManager().patch().release(), "0.0.2")
print(VersionManager("1.2.3").patch().release(), "1.2.4")
print(VersionManager("4").patch().patch().release(), "4.0.2")

print(VersionManager().major().rollback().release(), "0.0.1")
print(VersionManager().minor().rollback().release(), "0.0.1")
print(VersionManager().patch().rollback().release(), "0.0.1")
print(VersionManager().major().patch().rollback().release(), "1.0.0")
print(VersionManager().major().patch().rollback().major().rollback().release(), "1.0.0")

m = VersionManager("1.2.3")
m.major()
m.minor()
print(m.release(), "2.1.0")

print(VersionManager().rollback())