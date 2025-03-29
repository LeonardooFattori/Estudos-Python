# Loja em promoção

total = 0
qtd = int(input("Informe a quantidade do produto: "))
while qtd>0:
    valor= float(input("Informe o valor do produto: "))
    total += qtd*valor
    qtd = int(input("Informe a quantidade do produto: "))
print(f"Total da compra: R${total:.2f}")

if total<=100:
    p_desconto = 5
elif total<=200:
    p_desconto = 10
else:
    p_desconto = 20
desconto = total*p_desconto/100
valor_final = total - desconto
print(f"Desconto ({p_desconto}%): R${desconto}")
print(f"Total com desconto: R${valor_final}")