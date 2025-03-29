# Faça um programa que leia dois números inteiros X e Y e imprima todos os números de X
# até Y (considere que X sempre será menor que Y).

x = int(input("Digite o valor X: "))
y = int(input("Digite o valor Y: "))
for numero in range(x,y+1):
    print (numero,end = " ")