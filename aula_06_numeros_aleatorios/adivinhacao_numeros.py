# Escreva um programa que sorteie um número de 0 a 500 e peça para o jogador acertar. 
# A cada tentativa, o programa informa se o número sorteado é menor ou maior que o que o jogador escolheu. 
# Ao final, o programa informa quantas tentativas foram necessárias para o jogador acertar a resposta.

from random import *
cont_tentativa = 1
numero_adivinhar = randint(0,500)

n = int(input("Digite qual número voce acha que é: "))

while n != numero_adivinhar:
    if n > numero_adivinhar:
        print("O número digitado é maior que o número sorteado.")
    elif n < numero_adivinhar:
        print("O número digitado é menor que o número sorteado.")
    cont_tentativa+=1
    n = int(input("Digite novamente: "))

print(f"O número sorteado era {numero_adivinhar}, e voce acertou em {cont_tentativa} tentativas.")