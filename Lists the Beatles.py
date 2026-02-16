
beatles = []
print(f"\nStep 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print(f"\nStep 2:", beatles)

for miembros in range(2):
    beatles.append(input("Introduce el nombre de un nuevo miembro: "))

print(f"\nStep 3:", beatles)

del beatles[-1]
del beatles[-1]
print(f"\nStep 4:", beatles)

beatles.insert(0, "Ringo Starr")
print(f"\nEl grupo finalmente es: {beatles}")
print(f"\nLa cantidad de los miembros del grupo son: {len(beatles)}")

print(f"\nStep 5:", beatles)
print (f"\nEstas viendo Programación en Python con el curso de Píldoras Informáticas")

print("Programming","By LUISMA79","in" , sep="***", end="...")
print("Python")   