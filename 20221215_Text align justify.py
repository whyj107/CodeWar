# Text align justify
# https://www.codewars.com/kata/537e18b6147aa838f600001b/train/python

# 나의 풀이 : 못 풀었다.
def justify1(text, width):
    text = text.split(' ')
    line = []
    tmp, cnt = [], 0
    for t in text:
        if cnt + (len(t)+1) > width:
            l_t = len(tmp)
            a, b = divmod(width-(cnt-l_t), l_t-1)
            tt = [i + (' ' if b-1 > idx else '') for idx, i in enumerate(tmp)]
            line.append((' ' * a).join(tt))
            tmp, cnt = [], 0

        cnt += (len(t)+1)
        tmp.append(t)
    line.append(' '.join(tmp))
    return '\n'.join(line)

# 다른 사람의 풀이
def justify(text, width):
    length = text.rfind(' ', 0, width+1)
    if length == -1 or len(text) <= width: return text
    line = text[:length]
    spaces = line.count(' ')
    if spaces != 0:
        expand = (width - length) // spaces + 1
        extra = (width - length) % spaces
        line = line.replace(' ', ' '*expand)
        line = line.replace(' '*expand, ' '*(expand+1), extra)
    return line + '\n' + justify(text[length+1:], width)

"""
print(justify('123 45 6', 7))
print('123  45\n6')
"""
string = "Lorem ipsum " \
         "dolor sit amet," \
         " consectetur " \
         "adipiscing " \
         "elit. " \
         "Vestibulum " \
         "sagittis dolor " \
         "mauris, at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et dolor."
print(justify(string, 15))
