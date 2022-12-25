print("="*30, "Genes", "="*30)

#Abrir arquivo fasta
print("Abrindo sequência fasta...")
arq = open("sequence.fasta","r")

#Ler arquivo fasta
cab = arq.readline()
seq = arq.readlines()

#Arrumando a sequência fasta
seqDNA = seq[0]
print(f"\nCabeçalho:{cab}Sequência:{seqDNA}")

#Transformando a sequência de DNA em RNA"
mRNA = seqDNA.replace("T","U")
print(f"Sequência:{mRNA}")

#Fases de leitura
f1 = []
f2 = []
f3 = []
for c in range(0,len(mRNA),3):
    f1.append(mRNA[c:c+3])
    f2.append(mRNA[c+1:c+4])
    f3.append(mRNA[c+2:c+5])

#Sequências de RNA traduzidas
def teste(x = []):
    cds = []
    for d, e in enumerate(x):
        if e == "AUG":
            try:
                uag = x.index("UAG", d)
                uga = x.index("UGA", d)
                uaa = x.index("UAA",d)
                fim = min(uag, uga, uaa)
                cds.append(x[d:fim])
            except:
                break
    return cds
#Dicionário
def traducao(x = []):
    dicio = {"UUU":"Fenil-alanina", "UUC":"Fenil-alanina", "UUA":"Leucina", "UUG":"Leucina", "CUU":"Leucina", "CUC":"Leucina", "CUA":"Leucina", "CUG":"Leucina", "AUU":"Isoleucina", "AUC":"Isoleucina", "AUA":"Isoleucina", "AUG":"Start codon", "GUU":"Valina", "GUC":"Valina", "GUA":"Valina", "GUG":"Valina", "UCU": "Serina", "UCC":"Serina", "UCA":"Serina", "UCG":"Serina", "CCU":"Prolina", "CCC":"Prolina", "CCA":"Prolina", "CCG":"Prolina", "ACU":"Treonina", "ACC":"Treonina", "ACA":"Treonina", "ACG":"Treonina", "GCU":"Alanina", "GCC":"Alanina", "GCA":"Alanina", "GCG":"Alanina", "UAU":"Tirosina", "UAC":"Tirosina", "UAA":"Parada", "UAG":"Parada", "CAU":"Histidina", "CAC":"Histidina", "CAA":"Glutamina", "CAG":"Glutamina", "AAU":"Asparagina", "AAC":"Asparagina", "AAA":"Lisina", "AAG":"Lisina", "GAU":"Ácido aspártico", "GAC":"Ácido aspártico", "GAA":"Ácido glutâmico", "GAG":"Ácido glutâmico", "UGU":"Cisteina", "UGC":"Cisteína", "UGA":"Parada", "UGG":"Triptofano", "CGU":"Arginina", "CGC":"Arginina", "CGA":"Arginina", "CGG":"Arginina", "AGU":"Serina", "AGC":"Serina", "AGA":"Arginina", "AGG":"Arginina", "GGU":"Glicina", "GGC":"Glicina", "GGA":"Glicina", "GGG":"Glicina"}
    fora = []
    for a in range(0,len(x)):
        trad = []
        for c in range(0, len(x[a])):
            trad.append(dicio[x[a][c]])
        fora.append(trad[:])
    return fora

cdsf1 = teste(f1)
cdsf2 = teste(f2)
cdsf3 = teste(f3)

print("="*10, "Sequências de mRNA traduzidas de acordo com os códons nas diferentes fases de leitura", "="*10)
print("\n - Peptídeos a partir da primeira fase de leitura - \n")
w1 = traducao(cdsf1)
for q in range(0,len(w1)):
    print(w1[q])
print("\n - Peptídeos a partir da segunda fase de leitura - \n")
w2 = traducao(cdsf2)
for q in range(0,len(w2)):
    print(w2[q])
print("\n - Peptídeos a partir da terceira fase de leitura - \n")
w3 = traducao(cdsf3)
for q in range(0,len(w3)):
    print(w3[q])

print("\n", "="*20, "STOP CODON PROGRAM!", "="*20)
