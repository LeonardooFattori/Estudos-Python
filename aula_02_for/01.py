# Escreva um programa para encontrar a soma S = 5 + 10 + 15 + …. + 555.

S = 0
for x in range(5,556,5):
    S+=x
print (f"Soma = {S}")