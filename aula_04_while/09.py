# Escreva um programa que leia as notas dos alunos e calcule a média da classe. A entrada de
# dados termina quando for digitado o valor -1.

soma=0
qtd=0
nota = float(input("Digite nota: "))
while nota != -1:
    soma+=nota
    qtd +=1
    nota = float(input("Digite nota: "))
print(f"media = {soma/qtd}")