# Faça um programa que receba nome do funcionário, o salário atual, o percentual de
# reajuste (em %) e apresenta o valor do aumento e novo salário após o reajuste.

nome_funcionario = input("Digite o nome do funcionario: ")
salario = float(input("Digite o salario atual do funcionario: "))
reajuste = float(input("Quantos porcentos de reajuste terá o salario do funcionario: "))

valor_aumento = salario * (reajuste / 100)
novo_salario = salario + valor_aumento

print(f"O valor do aumento será {valor_aumento}")
print(f"O novo salario será de {novo_salario}")