# Decode the Morse code
# https://www.codewars.com/kata/54b724efac3d5402db00065e/train/python

# 나의 풀이
def decodeMorse(morse_code):
    morse_code = morse_code.replace('...---...', 'SOS')
    MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
                  '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
                  '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
                  '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
                  '-.--': 'Y', '--..': 'Z', '-.-.--': '!', '.-.-.-': '.', 'SOS': 'SOS'}
    return ''.join([MORSE_CODE.get(i, ' ') for i in morse_code.split(' ')]).replace('  ', ' ').strip()

# 다른 사람의 풀이
def decodeMorse1(morseCode):
    return ' '.join(''.join(MORSE_CODE[letter] for letter in word.split(' ')) for word in morseCode.strip().split('   '))

def test_and_print(got, expected):
    print("Got {}, expected {}</pre>".format(got, expected))

test_and_print(decodeMorse('.... . -.--   .--- ..- -.. .'), 'HEY JUDE')
test_and_print(decodeMorse('...---...'), 'SOS')