# Faça um programa que leia dois inteiros x e y, e calcule e imprima o valor de z:

x = int(input("Digite o valor de x: "))
y = int(input("Digite o valor de y: "))

z = ((x**2 + y**2) / (x - y)**2)

print(f"O valor de z será: {z}")