# Escreva um programa que leia um número inteiro positivo e imprima o fatorial desse número.

n = int(input("Digite um número inteiro: "))
fatorial = 1
for i in range(1,n+1):
    fatorial = fatorial * i
print(f"{n}! = {fatorial}")