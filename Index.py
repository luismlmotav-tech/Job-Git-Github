lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
print(f'La longitud de la lista es: {len(lista)}')  # Imprime la longitud de la lista
#es lo primero que se hace para saber cuantas posiciones tiene la lista, ya que el indice va desde 0 hasta n-1, =donde n es la longitud de la lista

suma = 0
for i in lista :
    suma += i
print(f'La suma de los elementos de la lista es: {suma}')  # Imprime la suma de los elementos de la lista
print(f'El promedio de los elementos de la lista es: {suma/len(lista)}')  # Imprime el promedio de los elementos de la lista  
print(f'El valor máximo de la lista es: {max(lista)}')  # Imprime el valor máximo de la lista       
print(f'El valor mínimo de la lista es: {min(lista)}')  # Imprime el valor mínimo de la lista
print(f'El valor del indice 0 es: {lista[0]}')  # Imprime el valor del indice 0 de la lista
print(f'El valor del indice 1 es: {lista[1]}')  # Imprime el valor del indice 1 de la lista
print(f'El valor del indice 2 es: {lista[2]}')  # Imprime el valor del indice 2 de la lista                              

multiplicacion = 1
for i in lista :
    multiplicacion *= i
print(f'La multiplicación de los elementos de la lista es: {multiplicacion}')  # Imprime la multiplicación de los elementos de la lista

lista.append(4)
print(f'La lista después de agregar el número 4 es: {lista}')  # Imprime la lista después de agregar el número 4