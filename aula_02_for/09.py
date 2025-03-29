# Escreva um programa que calcule a média dos valores: 5, 19, 27, 2, 10, 15, 8.8, 17, 15.9 .

S=0
qtd=0
for valor in [5,19,27,2,10,15,8.8,17,15.9]:
    S+=valor
    qtd+=1
media=S/qtd
print(f"Média = {media}")