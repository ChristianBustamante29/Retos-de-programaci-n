"""
- EJERCICIO:
- Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
- Utiliza operaciones de inserción, borrado, actualización y ordenación.
"""


# Estructuras

# Listas
my_list: list = ["Amarrillo", "Negro", "Blanco", "Verde"]
print(my_list)
my_list.append("Rojo")  # Inserción
my_list.append("Cafe")
print(my_list)
my_list.remove("Negro")  # Eliminación
print(my_list)
print(my_list[1])  # Acceso
my_list[1] = "Morado"  # Actualización
print(my_list)
my_list.sort()  # Ordenación
print(my_list)
print(type(my_list))

# Tuplas
my_tuple: tuple = ("Daniel", "Christian", "@christian", "24")
print(my_tuple[1])  # Acceso
print(my_tuple[3])
my_tuple = tuple(sorted(my_tuple))  # Ordenación
print(my_tuple)
print(type(my_tuple))

# Sets
my_set: set = {"Christian", "Daniel", "@christian", "24"}
print(my_set)
my_set.add("christian@gmail.com")  # Inserción
my_set.add("christian@gmail.com")
print(my_set)
my_set.remove("Daniel")  # Eliminación
print(my_set)
my_set = set(sorted(my_set))  # No se puede ordenar
print(my_set)
print(type(my_set))

# Diccionario
my_dict: dict = {
    "name": "Christian",
    "surname": "Daniel",
    "alias": "@christian",
    "age": "24"
}
my_dict["email"] = "christian@gmail.com"  # Inserción
print(my_dict)
del my_dict["surname"]  # Eliminación
print(my_dict)
print(my_dict["name"])  # Acceso
my_dict["age"] = "25"  # Actualización
print(my_dict)
my_dict = dict(sorted(my_dict.items()))  # Ordenación
print(my_dict)
print(type(my_dict))


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

def agenda():

    agenda = {}

    def datos():
        phone = input("Introduce tu numero de teléfono: ")
        if phone.isdigit() and len(phone) > 0 and len(phone) <= 11:
            agenda[name] = phone
        else:
            print("Introduce un numero de teléfono valido")
    while True:

        print("")
        print("1, Buscar Contacto")
        print("2, Insertar Contacto")
        print("3, Actualizar Contacto")
        print("4, Eliminar Contacto")
        print("5, Salir")

        option = input("Elije una accion: ")

        match option:
            case "1":
                name = input("Introduce el nombre del contacto: ")
                if name in agenda:
                    print(f"El número de {name} es {agenda[name]}.")
                else:
                    print(f"El contacto {name} no existe")
            case "2":
                name = input("Introduce el nombre del contacto: ")
                datos()
            case "3":
                name = input("Introduce el contacto a actualizar: ")
                if name in agenda:
                    datos()
                else:
                    print(f"El contacto {name} no existe")
            case "4":
                name = input("Introduce el nombre del contacto a eliminar: ")
                if name in agenda:
                    del agenda[name]
                else:
                    print(f"El contacto {name} no existe")
            case "5":
                print("Saliendo de la agenda")
                break
            case _:
                print("Opción no valida. Elige una opción del 1 al 5")

agenda()


