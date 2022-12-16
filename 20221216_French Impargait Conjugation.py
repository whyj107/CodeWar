# French Imparfait Conjugation
# https://www.codewars.com/kata/6394c1995e54bd00307cf768/train/python

# 나의 풀이
def to_imparfait(verb_phrase):
    dic = {'Je': 'ais', 'Tu': 'ais',
           'Il': 'ait', 'Elle': 'ait', 'On': 'ait',
           'Nous': 'ions', 'Vous': "iez",
           'Ils': 'aient', 'Elles': 'aient'}
    return verb_phrase[:-2] + dic[verb_phrase.split()[0]]

# 다른 사람의 풀이
# python 3.10의 새롭게 추가된 부분
def to_imparfait0(verb_phrase):
    match verb_phrase.split()[0]:
        case "Je" | "Tu":
            return f"{verb_phrase[:-2]}ais"
        case "Il" | "Elle" | "On":
            return f"{verb_phrase[:-2]}ait"
        case "Nous":
            return f"{verb_phrase[:-2]}ions"
        case "Vous":
            return f"{verb_phrase[:-2]}iez"
        case "Ils" | "Elles":
            return f"{verb_phrase[:-2]}aient"

print(to_imparfait("Je aller"), "Je allais")
print(to_imparfait("Je manger"), "Je mangais")
print(to_imparfait("Tu dormir"), "Tu dormais")
print(to_imparfait("Elle coder"), "Elle codait")
print(to_imparfait("Il parler"), "Il parlait")
print(to_imparfait("On rentre"), "On rentait")
print(to_imparfait("Nous aller"), "Nous allions")
print(to_imparfait("Vous partir"), "Vous partiez")
print(to_imparfait("Ils jouer"), "Ils jouaient")
print(to_imparfait("Elles gagner"), "Elles gagnaient")
print(to_imparfait("Je jwijefwijer"), "Je jwijefwijais")
print(to_imparfait("On irre"), "On irait")



