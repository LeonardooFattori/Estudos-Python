# Faça um programa para calcular as raízes da equação do 2º grau (ax2+bx + c=0).

print("Digite os coeficientes da equação")
a= float(input("a: "))
b= float(input("b: "))
c= float(input("c: "))
if a==0:
    print("essa não é uma equação do 2o grau")
else:
    delta = b*b-4*a*c

if delta < 0:
    print("não existe solução no conjunto de números reais")
elif delta==0:
    x= -b/(2*a)
    print("existe uma solução única x=",x)
else:
    x1= (-b - delta**0.5)/(2*a)
    x2= (-b + delta**0.5)/(2*a)
    print("Solução: x1 =", x1," x2 =", x2)