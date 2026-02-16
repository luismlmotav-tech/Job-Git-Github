lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
print(f'La longitud de la lista es: {len(lista)}')  # Imprime la longitud de la lista
#es lo primero que se hace para saber cuantas posiciones tiene la lista, ya que el indice va desde 0 hasta n-1, =donde n es la longitud de la lista

suma = 0
for i in lista :
    suma += i
print(f'La suma de los elementos de la lista es: {suma}')  # Imprime la suma de los elementos de la lista