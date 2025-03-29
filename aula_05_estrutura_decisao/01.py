# Faça um programa que leia 3 valores inteiros e imprima-os em ordem crescente.

print("Digite 3 valores inteiros:")
a= int(input("--> "))
b= int(input("--> "))
c= int(input("--> "))

if a<=b and b<=c:
    print(a,b,c)
elif a<=c and c<=b:
    print(a,c,b)
elif b<=a and a<=c:
    print(b,a,c)
elif b<=c and c<=a:
    print(b,c,a)
elif c<=a and a<=b:
    print(c,a,b)
else:
    print(c,b,a)