# Binary to Text (ASCII) Conversion
# https://www.codewars.com/kata/5583d268479559400d000064/train/python

# 나의 풀이
def binary_to_string(binary):
    b = [int(binary[i:i+8], 2) for i in range(0, len(binary), 8)]
    return ''.join([chr(i) for i in b])

# 다른 사람의 풀이
def binary_to_string1(binary):
    return "".join(chr(int(binary[i:i+8],2)) for i in range(0,len(binary),8))

print(binary_to_string('0100100001100101011011000110110001101111'), 'Hello')
print(binary_to_string('00110001001100000011000100110001'), '1011')