# Escreva um programa que calcule a soma de uma sequência de números inteiros digitados pelo usuário.
# A sequência termina quando o usuário digitar zero.

soma = 0

n = int(input("Digite um número inteiro: "))

while(n!=0):
    soma = soma + n
    n = int(input("Digite um número inteiro: "))

print(f"A soma dos números digitados é {soma}")