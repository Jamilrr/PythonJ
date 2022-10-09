#DECLARAÇÃO DE VARIÁVEIS
primeiroJogador=float(input("Digite a pontuação do jogador01: "))
segundoJogador=float(input("Digite a pontuação do jogador02: "))
terceiroJogador=float(input("Digite a pontuação do jogador03: "))
podium01=1.0
podium02=1.0
podium03=1.0

#MÉDIA DOS PONTOS
mediaPontos = (primeiroJogador+segundoJogador+terceiroJogador)/3

#ORDEM DECRESCENTE
if primeiroJogador > segundoJogador and primeiroJogador > terceiroJogador:
    podium01 = primeiroJogador
    if segundoJogador < primeiroJogador and segundoJogador > terceiroJogador:
        podium02 = segundoJogador
        if terceiroJogador < primeiroJogador and terceiroJogador < segundoJogador:
           podium03 = terceiroJogador

#MOSTRANDO 
print(podium01,podium02,podium03)

#APROVAÇÃO
if mediaPontos >=100:
    print("Equipe classificada")
else:
    print("Equipe desclassificada")    




