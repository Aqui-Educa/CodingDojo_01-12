# Considerando a seguinte lista: [178, 205, 212, 210, 215, 220, 223, 224, 230, 232, 235, 225]. Informe quantas vezes o numero aumentou do anterior.

lista = [178, 205, 212, 210, 215, 220, 223, 224, 230, 232, 235, 225]
per = 0
cont = 0

while per < len(lista):
    if lista[cont] < lista[cont+1]:
        cont += 1
    per += 1
    
print(cont)