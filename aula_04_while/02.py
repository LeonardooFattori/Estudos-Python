# Escreva um programa que leia a nota de 10 alunos e calcule a média da classe.

S=0
N = 10
x=1
while x <=N:
    nota = float(input(f"Digite a nota do aluno {x}: "))
    S += nota
    x += 1
print (f"Média da classe = {S/N}")