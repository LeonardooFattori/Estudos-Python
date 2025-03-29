# Movimentos da Torre no Xadrez

print("Posição atual da torre")
lin = int(input("linha:"))
col = int(input("coluna:"))
for x in range(1,lin):
    print(x,col)
for x in range(lin+1,9):
    print(x,col)
for y in range(1,col):
    print(lin,y)
for y in range(col+1,9):
    print(lin,y)