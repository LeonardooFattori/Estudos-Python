# Escreva um programa para encontrar a soma S = 5 + 10 + 15 + …. + 555.

S=0
x=5
while x < 556:
    S+=x
    x+=5
print (f"Soma = {S}")