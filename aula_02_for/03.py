# Escreva um programa que leia um número de 1 a 10, e mostre a tabuada desse número

numero = int(input("Digite o número: "))
for i in range(1,11):
    print (f"{numero} x {i} = {numero*i}")