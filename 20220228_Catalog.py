# Catalog
# 6kyu
# https://www.codewars.com/kata/59d9d8cb27ee005972000045/train/python

# 나의 풀이
import re
def catalog(s, article):
    result = []
    s = s.split("</prod>")
    for i in s:
        if article in i:
            name = re.search(r'<name>(.+?)</name>', i).group(0).replace('<name>', '').replace('</name>', '')
            prx = re.search(r'<prx>(.+?)</prx>', i).group(0).replace('<prx>', '').replace('</prx>', '')
            qty = re.search(r'<qty>(.+?)</qty>', i).group(0).replace('<qty>', '').replace('</qty>', '')
            result.append(f'{name} > prx: ${prx} qty: {qty}')
    return '\r\n'.join(result) if result != [] else 'Nothing'

# 다른 사람의 풀이
import xml.etree.ElementTree as ET
def catalog1(s, article):
    root = ET.fromstring('<cat>' + s + '</cat>')

    resp = []

    for child in root:
        name = child.find('name').text
        price = child.find('prx').text
        quantity = child.find('qty').text
        if article in name:
            resp.append(name + ' > prx: $' + price + ' qty: ' + quantity)
    if resp:
        return '\r\n'.join(resp)
    else:
        return 'Nothing'

PATTERN = re.compile(r"<prod><name>(?P<name>.+?)</name><prx>(?P<prx>[\d.]+?)</prx><qty>(?P<qty>\d+?)</qty></prod>")
def catalog2(s, article):
    return '\r\n'.join("{} > prx: ${} qty: {}".format(*m.groups()) for m in PATTERN.finditer(s) if article in m.group('name')) or 'Nothing'

def catalog3(s, article):
    lst=re.findall("<name>(.*"+article+".*)</name><prx>(.*)</prx><qty>(.*)</qty>",s)
    return '\r\n'.join('{} > prx: ${} qty: {}'.format(*e) for e in lst) or "Nothing"

s = "<prod><name>drill</name><prx>99</prx><qty>5</qty></prod>" \
    "<prod><name>hammer</name><prx>10</prx><qty>50</qty></prod>" \
    "<prod><name>screwdriver</name><prx>5</prx><qty>51</qty></prod>" \
    "<prod><name>table saw</name><prx>1099.99</prx><qty>5</qty></prod>" \
    "<prod><name>saw</name><prx>9</prx><qty>10</qty></prod>" \
    "<prod><name>chair</name><prx>100</prx><qty>20</qty></prod>" \
    "<prod><name>fan</name><prx>50</prx><qty>8</qty></prod>" \
    "<prod><name>wire</name><prx>10.8</prx><qty>15</qty></prod>" \
    "<prod><name>battery</name><prx>150</prx><qty>12</qty></prod>" \
    "<prod><name>pallet</name><prx>10</prx><qty>50</qty></prod>" \
    "<prod><name>wheel</name><prx>8.80</prx><qty>32</qty></prod>" \
    "<prod><name>extractor</name><prx>105</prx><qty>17</qty></prod>" \
    "<prod><name>bumper</name><prx>150</prx><qty>3</qty></prod>" \
    "<prod><name>ladder</name><prx>112</prx><qty>12</qty></prod>" \
    "<prod><name>hoist</name><prx>13.80</prx><qty>32</qty></prod>" \
    "<prod><name>platform</name><prx>65</prx><qty>21</qty></prod>" \
    "<prod><name>car wheel</name><prx>505</prx><qty>7</qty></prod>" \
    "<prod><name>bicycle wheel</name><prx>150</prx><qty>11</qty></prod>" \
    "<prod><name>big hammer</name><prx>18</prx><qty>12</qty></prod>" \
    "<prod><name>saw for metal</name><prx>13.80</prx><qty>32</qty></prod>" \
    "<prod><name>wood pallet</name><prx>65</prx><qty>21</qty></prod>" \
    "<prod><name>circular fan</name><prx>80</prx><qty>8</qty></prod>" \
    "<prod><name>exhaust fan</name><prx>62</prx><qty>8</qty></prod>" \
    "<prod><name>window fan</name><prx>62</prx><qty>8</qty></prod>"

print(catalog(s, 'ladder'), 'ladder > prx: $112 qty: 12')
print(catalog(s, 'saw'), 'table saw > prx: $1099.99 qty: 5\r\nsaw > prx: $9 qty: 10\r\nsaw for metal > prx: $13.80 qty: 32')
print(catalog(s, 'wood pallet'), 'wood pallet > prx: $65 qty: 21')