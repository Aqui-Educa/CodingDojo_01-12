# Faça um Programa que peça um número inteiro 
# e determine se ele é par ou impar.


num1 = int(input("Digite um número:   "))

resto = 0

if num1 % 2 == 0:
    print("Esse número é par")
else:
    print("Esse número é impar")