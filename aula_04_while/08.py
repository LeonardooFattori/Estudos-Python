# Escreva um programa que calcule a soma de uma sequência de números inteiros digitados
# pelo usuário. A sequência termina quando o usuário digitar zero.

soma=0
numero = int(input("Digite valor: "))
while numero !=0:
    soma+=numero
    numero = int(input("Digite valor: "))
print(f"soma = {soma}")