# Faça um programa que imprima a seguinte sequência:
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999

for x in range(1,10):
    for y in range(x):
        print(x,end=" ")
    print()