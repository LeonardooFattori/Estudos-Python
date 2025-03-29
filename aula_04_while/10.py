# Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,10 metro e cresce 3
# centímetros por ano. Faça um programa que calcule quantos anos serão necessários para que Zé seja maior
# que Chico.

altura_chico = 1.5
cresc_chico = 0.02
altura_ze = 1.10
cresc_ze = 0.03
tempo = 0
while altura_ze <= altura_chico:
    altura_ze += cresc_ze
    altura_chico += cresc_chico
    tempo+=1
print(f"Serão necesários {tempo} anos para que Zé seja maior que Chico")