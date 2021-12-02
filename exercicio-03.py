# Considerando a seguinte lista: 
# [178, 205, 212, 210, 215, 220, 223, 224, 230, 232, 235, 225]. 
# Informe quantas vezes o numero aumentou do anterior.

lista = [178, 205, 212, 210, 215, 220, 223, 224, 230, 232, 235, 225]
cont = 0

for index in range(1, len(lista)):
    if(lista[index] > lista[index-1]):
        cont += 1

print(cont)