# Help the bookseller!
# https://www.codewars.com/kata/54dc6f5a224c26032800005c/train/python

# 나의 풀이
def stock_list(listOfArt, listOfCat):
    if listOfArt == []: return ''
    books = {i: [] for i in listOfCat}
    for l in listOfArt:
        try:
            books[l.split(' ')[0][0]].append(int(l.split(' ')[1]))
        except:
            continue
    return ' - '.join([f'({k} : {sum(v)})' for k, v in books.items()])

b = ["ABAR 200", "CDXE 500", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B"]
print(stock_list(b, c), "(A : 200) - (B : 1140)")
