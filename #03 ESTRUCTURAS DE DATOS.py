"""
- EJERCICIO:
- Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
- Utiliza operaciones de inserción, borrado, actualización y ordenación.
"""

# Append
lista = [1,2,3,4,5,6,7]
lista.append(8)
print(lista)

# Extend
lista.extend([9,10,11])
print(lista)

# Insert
lista.insert(12, "Doce")
print(lista)

# Remove
lista.remove(1)
print(lista)

# Pop
lista.pop()
print(lista)

# Clear
lista.clear()
print(lista)

# Index
lista2 = [10,20,30,40,50,60,70,80,90,10]
# Buscar el índice de la primera aparición de 20
indice = lista2.index(30)
print(indice)  # Salida: 1

# Buscar el índice de 20 comenzando desde el índice 2
indice_con_start = lista2.index(50, 2)
print(indice_con_start)  # Salida: 4

# Buscar el índice de 30 en un rango específico
indice_con_rango = lista2.index(20, 0, 4)
print(indice_con_rango)  # Salida: 2

# Count
contador = lista2.count(10)
print(contador)

# Sort
lista2.sort()
print(lista2)
# Sort reverse
lista2.sort(reverse=True)
print(lista2)
# Sort key
lista3 = ["Manzana", "Pera", "Ajo", "Mango", "Guayaba"]
lista3.sort(key=len)
print(lista3)
# Sort key reverse
lista3.sort(key=len, reverse=True)
print(lista3)

# Reverse
lista3.reverse()
print(lista3)

# Copy 
lista4 = ["Rojo", "Verde", "Azul", "Amarrillo", "Cafe"]
copia_lista4 = lista4.copy()

print(lista4)
print(copia_lista4)

copia_lista4.append("Morado")
print(lista4)
print(copia_lista4)

"""
- DIFICULTAD EXTRA (opcional):
- Crea una agenda de contactos por terminal.
- Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
- Cada contacto debe tener un nombre y un número de teléfono.
- El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
- los datos necesarios para llevarla a cabo.
- El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
- (o el número de dígitos que quieras)
- También se debe proponer una operación de finalización del programa.
"""



