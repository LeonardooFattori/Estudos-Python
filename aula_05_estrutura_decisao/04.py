# Relatório medidas

S=0
Qtd1 = 0
Qtd2 = 0
for pessoa in range(10):
    idade = int(input("Informe a idade: "))
    peso = float(input("Informe o peso: "))
    altura = float(input("Informe a altura: "))
    S += idade
if peso > 60 and altura < 1.6:
    Qtd1 +=1
if idade >= 10 and idade<=30 and altura > 1.7:
    Qtd2 +=1
print("Média das idades = ",S/10)
print("Quantidade de pessoas com mais de 60 Kg e altura inferior a 1,60m = ",Qtd1)
print("Porcentagem de pessoas entre 10 e 30 anos que medem mais de 1,70m = ",100*Qtd2/10,"%",sep='')