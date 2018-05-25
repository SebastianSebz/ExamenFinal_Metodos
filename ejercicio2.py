# Ejercicio 2
# Complete el siguiente codigo para recorrer la lista `x` e imprima
# los numeros impares y que pare de imprimir al encontrar un numero mayor a 800
import numpy as np

x = np.int_(np.random.random(100)*1000)
#print(x)

lista=[]
numeroBreaker = 0;
for i in range(100):
    if(x[i]<=800 and x[i]%2==0):
        lista.append(x[i])
    elif(x[i]>800):
        numeroBreaker= x[i]
        break
print (lista, 'el numeroBreaker es: ' ,numeroBreaker)





