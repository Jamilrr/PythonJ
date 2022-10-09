j1 = int(input("Informe os pontos do primeiro jogador: "))
j2 = int(input("Informe os pontos do segundo jogador: "))
j3 = int(input("Informe os pontos do terceiro jogador: "))

if j1>j2 and j1>j3:
    if j2>j3:
        print(j1,j2,j3)
    else:
        print(j1,j3,j2)
elif j2>j1 and j2>j3:
    if j1>j3:
        print(j2,j1,j3)
    else:
        print(j2,j3,j1)
else:
    if j2>j1:
        print(j3,j2,j1)
    else:
        print(j3,j1,j2)


soma = j1+j2+j3
if soma>100:
    print("Média: ", soma/3)
else:
    print("Equipe desclassificada!!")
