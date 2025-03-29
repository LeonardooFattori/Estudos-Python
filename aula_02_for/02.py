# Escreva um programa que leia a nota de 10 alunos e calcule a média da classe.

S=0
for x in range(10):
    nota = float(input("Digite a nota do aluno: "))
    S += nota
md=S/10
print(f"Média da classe = {md}")