# Hëävÿ Mëtäl Ümläüts
# https://www.codewars.com/kata/57d4e99bec16701a67000033/train/python

# 나의 풀이
# A = Ä = \u00c4     E = Ë = \u00cb     I = Ï = \u00cf
# O = Ö = \u00d6     U = Ü = \u00dc     Y = Ÿ = \u0178
# a = ä = \u00e4     e = ë = \u00eb     i = ï = \u00ef
# o = ö = \u00f6     u = ü = \u00fc     y = ÿ = \u00ff

def heavy_metal_umlauts(boring_text):
    return boring_text.translate(boring_text.maketrans("AEIOUYaeiouy", "ÄËÏÖÜŸäëïöüÿ"))


# 다른 사람의 풀이
UMLAUTS = {'A': 'Ä', 'E': 'Ë', 'I': 'Ï', 'O': 'Ö', 'U': 'Ü', 'Y': 'Ÿ',
           'a': 'ä', 'e': 'ë', 'i': 'ï', 'o': 'ö', 'u': 'ü', 'y': 'ÿ'}
def heavy_metal_umlauts1(s):
    return ''.join(UMLAUTS.get(a, a) for a in s)

print(heavy_metal_umlauts("Announcing the Macbook Air Guitar"), "Ännöüncïng thë Mäcböök Äïr Güïtär")
print(heavy_metal_umlauts("Facebook introduces new heavy metal reaction buttons"), "Fäcëböök ïntrödücës nëw hëävÿ mëtäl rëäctïön büttöns")
print(heavy_metal_umlauts("Strong sales of Google's VR Metalheadsets send tech stock prices soaring"), "Ströng sälës öf Gööglë's VR Mëtälhëädsëts sënd tëch stöck prïcës söärïng")
print(heavy_metal_umlauts("Vegan Black Metal Chef hits the big time on Amazon TV"), "Vëgän Bläck Mëtäl Chëf hïts thë bïg tïmë ön Ämäzön TV")
