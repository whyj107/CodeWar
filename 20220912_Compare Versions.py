# Compare Versions
# https://www.codewars.com/kata/53b138b3b987275b46000115/train/python

# 나의 풀이
def compare_versions(version1, version2):
    version1 = list(map(int, version1.split('.')))
    version2 = list(map(int, version2.split('.')))
    for idx, v in enumerate(version1):
        if idx >= len(version2):
            break
        if v < version2[idx]:
            return False
    return True if len(version1) >= len(version2) else False

# 다른 사람의 풀이
def compare_versions1(ver1,ver2):
    return [int(i) for i in ver1.split(".")] >= [int(i) for i in ver2.split(".")]

def dotest(v1, v2, expected):
    print(compare_versions(v1, v2), expected)


for v1, v2, expected in (
        ("11", "10", True),
        ("11", "11", True),
        ("10.4.6", "10.4", True),
        ("10.4", "10.4.8", False),
        ("10.4", "11", False),
        ("10.4", "10.10", False),
        ("10.4.9", "10.5", False),
):
    dotest(v1, v2, expected)
