#variavel
Error=True
#laço de repetição
while Error == True:
#Entrada de dados    
    Usuario=str(input("Digite seu Usuário: "))
    Senha=str(input("Digite sua senha: "))
#Condição
    if Usuario==Senha:
        print("Seu usuário e/ou senha estão incorretos!") 
    else:
        print("Cadastrado")
        Error = False
