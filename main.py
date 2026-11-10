# Dado un número N, mirar si al los números del0 al N son pares o impares
import numpy as np

N = int(input("Dime un número natural"))

def par_impar(N):
    i = 0
    while i <= N:
        if i % 2 == 0:
            print(f"{i} es par")
        else:
            print(f"{i} es impar")
        i = i + 1 

def par_impar_lista(N):
    i = 0
    pares = []
    impares = []
    while i <= N:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
        i = i + 1 
    print(pares)
    print(impares)
    return pares, impares
if __name__ == "__main__":
    par_impar(N)   
    par_impar_lista(N)
    print