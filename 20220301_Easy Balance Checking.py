# Easy Balance Checking
# 6kyu
# https://www.codewars.com/kata/59d727d40e8c9dd2dd00009f/train/python

# 나의 풀이
import re
def balance(book):
    result = []
    ob, te, cnt = 0, 0, 0
    book = book.replace("\r\n", "\n").split("\n")
    for idx, i in enumerate(book):
        if idx == 0:
            ob = float(re.search(r'\d*(\.?\d*)', i).group(0))
            result.append(f'Original Balance: {ob:.2f}')
        else:
            tmp = re.findall(r'[0-9a-zA-Z.]+', i)
            ob -= float(tmp[2])
            result.append(f'{tmp[0]} {tmp[1]} {float(tmp[2]):.2f} Balance {ob:.2f}')
            te += float(tmp[2])
            cnt += 1
    result.append(f'Total expense  {te:.2f}')
    result.append(f'Average expense  {te/cnt:.2f}')
    return '\r\n'.join(result)

# 다른 사람의 풀이
PATTERN = re.compile(r'([\d.]+)[^\w\n]*([a-zA-Z]+)[^\w\n]*([\d.]+)')
def balance1(book):
    balance, lst, (b, s) = 0, [], book.split('\n', 1)
    iBal = balance = float(next(re.finditer(r'[\d.]+', b)).group())

    lst.append("Original Balance: {:.2f}".format(balance))
    for num, item, amount in PATTERN.findall(s):
        amount = float(amount)
        balance -= amount
        lst.append("{} {} {:.2f} Balance {:.2f}".format(num, item, amount, balance))

    lst.append(
        "Total expense  {:.2f}\r\nAverage expense  {:.2f}".format(iBal - balance, (iBal - balance) / (len(lst) - 1)))
    return '\r\n'.join(lst)

b1 = "1000.00!=\n" \
     "125 Market !=:125.45\n" \
     "126 Hardware =34.95\n" \
     "127 Video! 7.45\n" \
     "128 Book :14.32\n" \
     "129 Gasoline ::16.10"

b1sol = "Original Balance: 1000.00\r\n" \
        "125 Market 125.45 Balance 874.55\r\n" \
        "126 Hardware 34.95 Balance 839.60\r\n" \
        "127 Video 7.45 Balance 832.15\r\n" \
        "128 Book 14.32 Balance 817.83\r\n" \
        "129 Gasoline 16.10 Balance 801.73\r\n" \
        "Total expense  198.27\r\n" \
        "Average expense  39.65"

print(balance(b1) == b1sol)

b2 = "1233.00\n" \
   "125 Hardware;! 24.8?;\n" \
   "123 Flowers 93.5\n" \
   "127 Meat 120.90\n" \
   "120 Picture 34.00\n" \
   "124 Gasoline 11.00\n" \
   "123 Photos;! 71.4?;\n" \
   "122 Picture 93.5\n" \
   "132 Tyres;! 19.00,?;\n" \
   "129 Stamps 13.6\n" \
   "129 Fruits{} 17.6\n" \
   "129 Market;! 128.00?;\n" \
   "121 Gasoline;! 13.6?;"

b2sol = "Original Balance: 1233.00\r\n" \
        "125 Hardware 24.80 Balance 1208.20\r\n" \
        "123 Flowers 93.50 Balance 1114.70\r\n" \
        "127 Meat 120.90 Balance 993.80\r\n" \
        "120 Picture 34.00 Balance 959.80\r\n" \
        "124 Gasoline 11.00 Balance 948.80\r\n" \
        "123 Photos 71.40 Balance 877.40\r\n" \
        "122 Picture 93.50 Balance 783.90\r\n" \
        "132 Tyres 19.00 Balance 764.90\r\n" \
        "129 Stamps 13.60 Balance 751.30\r\n" \
        "129 Fruits 17.60 Balance 733.70\r\n" \
        "129 Market 128.00 Balance 605.70\r\n" \
        "121 Gasoline 13.60 Balance 592.10\r\n" \
        "Total expense  640.90\r\n" \
        "Average expense  53.41"

# print(balance(b2), b2sol)