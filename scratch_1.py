vogais = {
    'a':0,
    'e':0,
    'i':0,
    'o':0,
    'u':0,
}

texto = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua 
Ut enim ad minim veniam quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat 
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur 
Excepteur sint occaecat cupidatat non proident sunt in 
culpa qui officia deserunt mollit anim id est laborum'''

for letra in texto.lower():
    if letra in vogais.keys():
        vogais[letra] +=1

print(vogais)
