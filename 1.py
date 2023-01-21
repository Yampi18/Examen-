from random import random

def matriz(n, m, mayor):
    M = []
    for i in range(n):
        lista = []
        for i in range(m):
            lista.append(random()* mayor)
        M.append(lista)
    
    return M

def impmatriz(M):
    for i in range(len(M)):
        for j in range(len(M[i])):
            print(M[i][j], end = "t")
    print()

n = int(input("Ingrese el numero de filas"))
m = int(input("Ingrese el numero de columnas"))
mayor = int(input("Ingrese el numero maximo del arreglo"))

M = matriz(n, m, mayor)
print(M)

if M[i][j] >= 9 :
    print("Se encontro el numero 9 en la posicion", i , "x" ,j ) 