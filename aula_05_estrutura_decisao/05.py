# Relatório classe

soma_notas=0
cont_aluno=0
cont_inf3=0
cont_sup8=0
maior_nota = 0
menor_nota = 10
nota = float(input(f"Digite nota do aluno 1: "))
while nota>=0:
    cont_aluno+=1
    soma_notas+=nota
if nota < 3: cont_inf3 += 1
if nota > 8: cont_sup8 += 1
if nota > maior_nota: maior_nota = nota
if nota < menor_nota: menor_nota = nota
nota = float(input(f"Digite nota do aluno {cont_aluno+1}: "))

print(f"Média das notas = {soma_notas/cont_aluno}" )
print("Quantidade de alunos com nota inferior a 3,0 = ", cont_inf3)
print("Porcentagem de pessoas com nota superior a a 8,0 = {100*cont_sup8/cont_aluno:.2f}%")
print("Maior nota = ", maior_nota)
print("Menor nota = ", menor_nota)