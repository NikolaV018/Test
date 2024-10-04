def dna_string (dna):
    c = {"A" : "T", "T" : "A", "G" : "C", "C" : "G"}
    return ''.join([c[base] for base in dna])

#input
dna = input("Input a DNA string: ")
dna = dna.upper()
stampa = dna_string(dna)
print(stampa)


