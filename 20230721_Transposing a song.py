# Transposing a song
# https://www.codewars.com/kata/55b6a3a3c776ce185c000021/train/python

# 나의 풀이
def transpose(song, i):
    n = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    f = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']
    return [n[(f.index(s)+i)%12] if s in f else n[(n.index(s)+i)%12] for s in song]

# 다른 사람의 풀이
def transpose1(song, interval):
    altern = {"Bb": "A#", "Db": "C#", "Eb": "D#", "Gb": "F#", "Ab": "G#"}
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    return [notes[(notes.index(altern.get(i, i)) + interval) % 12] for i in song]