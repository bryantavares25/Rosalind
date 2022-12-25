print("="*20, "DNA & RNA sequence", "="*20)

#Entrada
print("\n- - - Conversão da sequência de DNA para RNA - - -")
seqdna = str(input("Sequência de DNA:"))

#Infos sobre a sequência de DNA
print(f"\nA sequência apresenta {len(seqdna)} nucleotídeos.")
print(f"A: {seqdna.count('A')}\nT: {seqdna.count('T')}\nC: {seqdna.count('C')}\nG: {seqdna.count('G')}")

#Transformando a sequência de DNA em RNA
seqrna = seqdna.replace("T", "U")
print(f"A sequência de DNA transformada em sequência de RNA: {seqrna}")

#Sequências complementares do DNA e RNA
print("\n- - - Conversão para sequências complementares da sequência de DNA e RNA - - -")

dnacomp = seqdna.replace("A", "t").replace("T","a").replace("C","g").replace("G","c")
print(f"\nDNA original: {seqdna}")
print(f"DNA Complementar: {dnacomp.upper()}")

rnacomp = seqrna.replace("A", "u").replace("U","a").replace("C","g").replace("G","c")
print(f"\nRNA original: {seqrna}")
print(f"RNA complementar: {rnacomp.upper()}")
