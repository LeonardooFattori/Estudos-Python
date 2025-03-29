# Faça um algoritmo que leia 3 notas de um aluno, onde a primeira nota possui peso um, a segunda possui peso
# dois e a terceira peso três. Calcule a média ponderada do aluno baseada nos pesos e escreva na tela.

nota1 = float(input("Digite a nota 1 do aluno: "))
nota2 = float(input("Digite a nota 2 do aluno: "))
nota3 = float(input("Digite a nota 3 do aluno: "))

media_ponderada = ((nota1) + (nota2 * 2) + (nota3 * 3)) / 6

print(f"A média ponderada do aluno é {media_ponderada}")