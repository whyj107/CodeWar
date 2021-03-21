# DNA to RNA Conversion
# https://www.codewars.com/kata/5556282156230d0e5e000089/train/python

# 나의 풀이
def dna_to_rna(dna):
    return dna.replace('T', 'U')

print(dna_to_rna("TTTT"), "UUUU")
print(dna_to_rna("GCAT"), "GCAU")
print(dna_to_rna("GACCGCCGCC"), "GACCGCCGCC")