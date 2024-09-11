import random
import numpy as np

##funcion para generar listas con numeos random
def generar(numero, lista1, largo):
    for n in range(largo):
        lista1.append(random.randint(0, numero))

    return lista1
##funcion para ordenar parcialmente respecto a un porcentaje ordenar.
def datacoso(lista, ordenar):
    numerodecosas = len(lista)*ordenar
    if ordenar!=0:
        lista[:int(numerodecosas)] = sorted(lista[:int(numerodecosas)])
    return lista

'''def archivo(lista, nombre):
    with open(nombre, 'w') as file:
        for numero in lista:
            file.write(f"{numero} ")'''



##generar los datos parcialmente ordenados
file = open("dataPARCIAL.txt", 'w')
for n in range(10000):
    lista = datacoso(generar(random.randint(0,1000), [], random.randint(1,1000)), random.random())
    #print(lista, 'lisat')
    file.write("[")
    file.write(" ".join(map(str, lista))) #para unir los elementos d la listat en una cadena separada por espacios wii
    file.write("]\n")

    file.write("\n")
file.close()

##generar los datos aleatorios
file = open("dataALEATORIA.txt", 'w')
for n in range(10000):
    lista = datacoso(generar(random.randint(0,1000), [], random.randint(1,1000)), 0)
    #print(lista, 'lisat')
    file.write("[")
    file.write(" ".join(map(str, lista))) #para unir los elementos d la listat en una cadena separada por espacios wii
    file.write("]\n")

    file.write("\n")
file.close()

##generar los datos semi ordenados
file = open("dataSEMI.txt", 'w')
for n in range(10000):
    lista = []
    for n in range(random.randint(1,1000)):
        lista.append(n)
    pos = random.randint(0,n)
    lista.insert(pos, random.randint(0,1000))
    #print(lista, 'lisat')
    file.write("[")
    file.write(" ".join(map(str, lista))) #para unir los elementos d la listat en una cadena separada por espacios wii
    file.write("]\n")

    file.write("\n")
file.close()




##generar dos matrices de iguales dimensiones
def matrices(numeromatrices, filas, columnas, boo):
    matrices = []
    if boo == 0:
        
        tamaño = siguientepotencia(filas)
        for x in range(numeromatrices):
            matriz = np.random.randint(1, 15, size=(tamaño, tamaño))
            matriz2 = np.random.randint(1, 15, size=(tamaño, tamaño))
            matrices.append(matriz)
            matrices.append(matriz2)
            ##print(x,'equis1')
    return matrices


def siguientepotencia(n):

    potencia = 1
    while potencia < n:
        potencia *= 2
    return potencia
a = 0

##escribirlas en el archivo, se escriben 100!!!
file = open("dataset.txt", 'w')
potencias = [64,128,256,512]

for n in range(50):
    filas = random.randint(0,3)
    numero = potencias[filas]
    mat = matrices(1, numero, numero, 0)
    file.write("\n\n")
    for matriz in mat:
        file.write("[\n")
        for fila in matriz:
            file.write("[")
            file.write(" ".join(map(str, fila)))
            file.write("]\n")
        file.write("]\n\n")

print(mat)
file.close()