# Escreva um programa que leia um número de 1 a 10, e mostre a tabuada desse número

numero = int(input("Digite o número: "))
i=1
while i <=10:
    print (f"{numero} x {i} = {numero*i}")
    i+=1