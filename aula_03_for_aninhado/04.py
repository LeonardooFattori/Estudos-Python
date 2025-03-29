# Escreva programas para desenhar as figuras a seguir:

# Retângulo

for x in range(10):
    for y in range(10):
        print(end="*")
    print()

print()
print()

# Quadrado

for x in range(5):
    for y in range(10):
        print(end="*")
    print()

print()
print()

# Triângulo 1

for x in range(1,10):
    for y in range(x):
        print(end="*")
    print()

print()
print()

# Triângulo 2

for x in range(1,10):
    for y in range(9-x):
        print(end=" ")
    for y in range(x):
        print(end="*")
    print()

print()
print()

# Triângulo 3

for x in range(1,20,2):
    for y in range((19-x)//2):
        print(end=" ")
    for y in range(x):
        print(end="*")
    print()

print()
print()

# Triângulo 4

for x in range(19,0,-2):
    for y in range((19-x)//2):
        print(end=" ")
    for y in range(x):
        print(end="*")
    print()