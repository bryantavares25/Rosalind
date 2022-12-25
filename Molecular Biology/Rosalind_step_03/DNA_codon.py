print("="*20, "DNA & mRNA & AA", "="*20)

#Entrada
while True:
    seqdna = str(input("Entrada de uma sequência de DNA: "))

    #Códons completos?
    a = len(seqdna)%3
    #Quantos códons?
    b = int(len(seqdna)/3)

    if (a==0):
        break
    else:
        print(f"\nA sequência de DNA apresenta {b} códon(s). Falta(m) {3-a} nucleotídeos para completar mais um códon.\n")

#Transformando a sequência de DNA na sequência de RNA complementar
seqrna = seqdna.replace("A","u").replace("T","a").replace("C","g").replace("G","c").upper()
print(f"DNA original: {seqdna}")
print(f"RNA complementar: {seqrna}")

#Encontrando os códons
codons = []
for c in range(0,len(seqrna), 3):
    d = seqrna[c]+seqrna[c+1]+seqrna[c+2]
    codons.append(d)
print(f"\nCódons: {codons}")

#Dicionário de códons
dicio = {"UUU":"Fenil-alanina", "UUC":"Fenil-alanina", "UUA":"Leucina", "UUG":"Leucina", "CUU":"Leucina", "CUC":"Leucina", "CUA":"Leucina", "CUG":"Leucina", "AUU":"Isoleucina", "AUC":"Isoleucina", "AUA":"Isoleucina", "AUG":"Start codon", "GUU":"Valina", "GUC":"Valina", "GUA":"Valina", "GUG":"Valina", "UCU": "Serina", "UCC":"Serina", "UCA":"Serina", "UCG":"Serina", "CCU":"Prolina", "CCC":"Prolina", "CCA":"Prolina", "CCG":"Prolina", "ACU":"Treonina", "ACC":"Treonina", "ACA":"Treonina", "ACG":"Treonina", "GCU":"Alanina", "GCC":"Alanina", "GCA":"Alanina", "GCG":"Alanina", "UAU":"Tirosina", "UAC":"Tirosina", "UAA":"Parada", "UAG":"Parada", "CAU":"Histidina", "CAC":"Histidina", "CAA":"Glutamina", "CAG":"Glutamina", "AAU":"Asparagina", "AAC":"Asparagina", "AAA":"Lisina", "AAG":"Lisina", "GAU":"Ácido aspártico", "GAC":"Ácido aspártico", "GAA":"Ácido glutâmico", "GAG":"Ácido glutâmico", "UGU":"Cisteina", "UGC":"Cisteína", "UGA":"Parada", "UGG":"Triptofano", "CGU":"Arginina", "CGC":"Arginina", "CGA":"Arginina", "CGG":"Arginina", "AGU":"Serina", "AGC":"Serina", "AGA":"Arginina", "AGG":"Arginina", "GGU":"Glicina", "GGC":"Glicina", "GGA":"Glicina", "GGG":"Glicina"}

#Aminoácidos correspondentes
print("\nAminoáciodos correspondentes aos códons:")
for e in range(0, len(codons)):
    print(dicio[codons[e]])
