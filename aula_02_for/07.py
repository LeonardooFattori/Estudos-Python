# Fazer um programa que apresenta o total da soma dos números pares até 100

S=0
for x in range(2,101,2):
    S+=x
print (f"Soma = {S}")