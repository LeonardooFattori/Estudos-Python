# Escreva um programa em Python que leia uma frase e troque algumas letras por símbolos, conforme tabela a seguir:

frase = input("Digite uma frase: ")
nova_frase = ""

for i in frase:
    if i == "a":
        nova_frase+= "@"
    elif i == "c":
        nova_frase+= "+"
    elif i == "e":
        nova_frase+= "&"
    elif i == "i":
        nova_frase+= "%"
    elif i == "o":
        nova_frase+= "*"
    elif i == "r":
        nova_frase+= "#"
    elif i == "s":
        nova_frase+= "$"
    else:
        nova_frase+= i

print(nova_frase)