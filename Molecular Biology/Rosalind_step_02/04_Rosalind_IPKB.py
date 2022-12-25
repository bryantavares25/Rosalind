AA = 2
Aa = 2
aa = 2

t = AA+Aa+aa

#Árvore de decisão
fAA = AA/t
fAa = Aa/t
faa = aa/t

#Escolha AA
t2 = (AA-1)+Aa+aa

fAA2 = (AA-1)/t2
fAa2 = Aa/t2
faa2 = Aa/t2

fen2 = 1*(fAA*fAA2)+(fAA*fAa2)+(fAA*faa2)

#Escolha Aa
t3 = AA+(Aa-1)+aa

fAA3 = AA/t3
fAa3 = (Aa-1)/t3
faa3 = aa/t3

fen3 = 1*(fAa*fAA3)+0.75*(fAa*fAa3)+0.5*(fAa*faa3)

#Escolha aa
t4 = AA+Aa+(aa-1)

fAA4 = AA/t4
fAa4 = Aa/t4
faa4 = (aa-1)/t4

fen4 = 1*(faa*fAA4)+0.5*(faa*fAa4)+0*(faa*faa4)

print(fen2+fen3+fen4)
