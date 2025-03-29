# Escreva um programa para gerar as sequências a seguir:

# Sequência 1                 Sequência 2
# 137                         358
# 134                         356
# 157                         354
# 154                         758
# 177                         756
# 174                         754
# 237                         1158
# 234                         1156
# 257                         1154
# 254
# 277
# 274

for x in range(1,3):
    for y in range(3,8,2):
        for z in range(7,3,-3):
            print(x,y,z,sep="")

print()
print()

for x in range(3,12,4):
    for z in range(8,3,-2):
        print(x,5,z,sep="")