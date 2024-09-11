
import time
import numpy as np

def insertion_sort(lista):
    for i in range(1, len(lista)): ##empezamos desde el 2do elem
        elementordenado = lista[i]
        j = i - 1
        while j >= 0 and elementordenado < lista[j]: ##comparar el elemento con los elementos a la izq suya
                                                     ##si es menor al elemento a su izq, se desplaza ese elemento a la derecha de elementordenado!
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = elementordenado ##cuando el elementordenado no es menor, lo insertamos a la derecha del elemento con el que lo estabamos comparando!!

def merge_sort(lista):
    if len(lista) > 1:
        medio = len(lista) // 2  
        izq = lista[:medio]  ##se divide en 2!!
        der = lista[medio:]

        merge_sort(izq)  ##se ordenan ambas mitades recursivamente
        merge_sort(der)  

        numder = 0
        numizq = 0
        numoriginal = 0

        ##se hacen 2 listas adicionales para ordenar
        while numizq < len(izq) and numder < len(der):
            if izq[numizq] < der[numder]:
                lista[numoriginal] = izq[numizq]
                numizq += 1
            else:
                lista[numoriginal] = der[numder]
                numder += 1
            numoriginal += 1

        ##chequear si quedan cosas en alguna de las 2 listas por el tema de tamanio desigual
        while numizq < len(izq):
            lista[numoriginal] = izq[numizq]
            numizq += 1
            numoriginal += 1

        while numder < len(der):
            lista[numoriginal] = der[numder]
            numder += 1
            numoriginal += 1

def particionar(lista, low, high): ##divide alrededor del pivote, donde high es el ultimo elemento y low el primero
    pivot = lista[high]
    i = low - 1 ##se van a mover las cosas mas chicas que el pivote

    for j in range(low, high):
        if lista[j] <= pivot: 
            i += 1
            lista[i], lista[j] = lista[j], lista[i] ##se recorre, si hay un elemento menor al pivote, se intercambiaA!

    lista[i + 1], lista[high] = lista[high], lista[i + 1]
    return i + 1

def quicksort_iterativo(arr):
    stack = [(0, len(arr) - 1)]
    
    while stack: ##si no está vacía, se sacan los low y high, para después seguir particionando con la función particionar!
        low, high = stack.pop()
        if low < high:
            pi = particionar(arr, low, high)
            stack.append((low, pi - 1))
            stack.append((pi + 1, high))

##esto lee el archivo, pero solo las lineas que son filas, y no matrices!!
def leer(archivo):
    cosas = []
    with open(archivo, "r") as file:
        for linea in file:
            lista = linea.strip()
            if lista =='[' or lista==']':
                break
            
            if lista:
                
                lista = lista.replace('[', '').replace(']', '')
                cosas.append(list(map(int, lista.split())))
    return cosas ##retorna una lista de listas

conjuntodelistas = leer('dataSEMI.txt') ##aqui solo se cambia el nombre del archivo por uno de los 3 que hay (para leer dataSEMI, dataPARCIAL, o dataALEATORIA)!!
n = 0
tiempo1 = tiempo2 = tiempo3 = tiempo4 =  0
for lista in conjuntodelistas:
    n+=1
    copia = lista.copy()

    start_time = time.perf_counter()
    insertion_sort(copia)
    end_time = time.perf_counter()
    tiempo1 += end_time-start_time

    start_time2 = time.perf_counter()
    merge_sort(copia)
    end_time2 = time.perf_counter()
    tiempo2 += end_time2-start_time2

    start_time3 = time.perf_counter()
    quicksort_iterativo(copia)
    end_time3 = time.perf_counter()
    tiempo3+= end_time3-start_time3
    
    start_time4 = time.perf_counter()
    sorted(copia)
    end_time4 = time.perf_counter()
    tiempo4+= end_time4-start_time4

    if n % 10 == 0: 
        print(f"Progreso: {n} listas procesadas")

print(n, 'ene')
print('Insertion sort: ', tiempo1/n,'\n', 'Merge Sort: ', tiempo2/n, '\n', 'Quicksort: ', tiempo3/n, '\n', 'Sorted de python: ', tiempo4/n) ##se imprimen los tiempos


#
#
#
#aquí empieza lo de las matrices!
#
#
def multiplicacion_tradicional(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)] ##se inicializa una matriz de la dimensión resultante con puros 0´s
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j] ##se suma la multiplicación de los elementos de las filas por las columnas
    return C

def transponer(M):
    n = len(M)
    MT = [[0] * n for _ in range(n)] ##se hace lo mismo, se inicializa la matriz transpuesta con sólo 0´s
    for i in range(n):
        for j in range(n):
            MT[j][i] = M[i][j] ##se cambian los índices, se invierten!!
    return MT

def multiplicacion_optimizada(A, B):
    
    n = len(A)##dimensión
    B_T = transponer(B)## transponer B por lo del caché
    C = [[0] * n for _ in range(n)]##inicializar la matriz con 0´s
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B_T[j][k] ##sumar los productos de filas con columnas
    
    return C


def strassen(A, B):
    
    n = len(A)##obtener la dimensión de las matrices CUADRADASSS y de dimensión que sea potencia de 2
    
    if n == 1:##el caso más fácil, multiplico nomás
        return A * B
    else:
        mid = n // 2 ##calculo el medio
        
        A11 = A[:mid, :mid] ##divido en 4 matrices más chicas
        A12 = A[:mid, mid:]
        A21 = A[mid:, :mid]
        A22 = A[mid:, mid:]
        
        B11 = B[:mid, :mid] ##hago lo mismo con la 2da matriz!
        B12 = B[:mid, mid:]
        B21 = B[mid:, :mid]
        B22 = B[mid:, mid:]
        
       
        M1 = strassen(A11 + A22, B11 + B22) ##calculo las multiplicaciones de las cosas chicas recursivamente
        M2 = strassen(A21 + A22, B11)
        M3 = strassen(A11, B12 - B22)
        M4 = strassen(A22, B21 - B11)
        M5 = strassen(A11 + A12, B22)
        M6 = strassen(A21 - A11, B11 + B12)
        M7 = strassen(A12 - A22, B21 + B22)
        
        
        C11 = M1 + M4 - M5 + M7 ##calculo las submatrices de la matriz C
        C12 = M3 + M5
        C21 = M2 + M4
        C22 = M1 - M2 + M3 + M6
        
        C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22)))) ##combino todas las c´s chicas en una grande!
        
        return C

    

def leercuadradas(archivo):

    matrices = []
    contador = 0

    with open(archivo, "r") as file:

        matrizactual = []
        leyendo_matriz = False ##uso una flag porque antes estaban las filas y matrices en el mismo archivo, ya no es necesario usarla pero bue...
        
        for linea in file:

            linea = linea.strip()

            if linea == '[':
                
                leyendo_matriz = True
                matrizactual = []
                contador+=1

            elif linea == ']': ##aquí appendedo pq llegaría al final de una matriz!!

                if matrizactual:
                    matrices.append(matrizactual)

                leyendo_matriz = False

            elif leyendo_matriz:

                linea = linea.replace('[', '').replace(']', '') ##reemplazo para que me queden sólo los números

                if linea:
                    fila = list(map(int, linea.split())) ##los junto
                    matrizactual.append(fila)
    print(contador)
    return matrices



conjuntodematrices = leercuadradas('dataset.txt')
n = 0
tiempo1 = tiempo2 = tiempo3 =  0

for lista in range(0, len(conjuntodematrices), 2): ##aquí leo las matrices del dataset y veo los tiempos!!
    n+=1
    print(n)

    A = np.array(conjuntodematrices[lista]) ##multiplico una matriz con la siguiente!
    B = np.array(conjuntodematrices[lista + 1])

    start_time = time.perf_counter()
    multiplicacion_tradicional(A,B)
    end_time = time.perf_counter()
    tiempo1 += end_time-start_time

    start_time2 = time.perf_counter()
    multiplicacion_optimizada(A,B)
    end_time2 = time.perf_counter()
    tiempo2 += end_time2-start_time2

    start_time3 = time.perf_counter()
    strassen(A,B)
    end_time3 = time.perf_counter()
    tiempo3+= end_time3-start_time3

    if n % 10 == 0: 
        print(f"Progreso: {n} matrices multiplicadas procesadas")

print(n) ##n es la cantidad de pares de matrices que multipliqué
print('Multiplicacion Tracicional: ', tiempo1/n,'\n', 'Multiplicacion Optimizada: ', tiempo2/n, '\n', 'Strassen: ', tiempo3/n, '\n')





   

