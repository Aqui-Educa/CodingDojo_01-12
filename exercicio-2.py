# Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#                           Até 5 Kg           Acima de 5 Kg
#     Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
#     Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra 
# ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
# Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade 
# (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. 

peso_maca = float(input("Informe peso da maça: "))
peso_morango = float(input("Informe peso do morango: "))
valor_maca = 0
valor_morango = 0
valor_total = 0

if peso_maca <= 5: 
    print(f'O valor a ser pago é R${peso_maca*1.80}')
    valor_maca = peso_maca*1.80
elif (peso_maca > 5):
    print(f'O valor a ser pago é R${peso_maca*1.50}')
    valor_maca = peso_maca*1.50

if peso_morango <= 5:
    print(f'O valor a ser pago é R${peso_morango*2.50}')
    valor_morango = peso_morango*2.50
elif peso_morango > 5:
    print(f'O valor a ser pago é R${peso_morango*2.20}')
    valor_morango = peso_morango*2.20

if (peso_maca + peso_morango) > 8 or (valor_maca + valor_morango) > 25:
    valor_total = (valor_maca + valor_morango)*0.90
    print(f"valor_total")   

    