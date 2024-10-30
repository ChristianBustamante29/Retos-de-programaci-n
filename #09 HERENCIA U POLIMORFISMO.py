"""
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
"""

class Animal:

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} hace {self.sound}")

class Dog(Animal):

    def __init__(self, name):
        super().__init__(name, "Guau!")

class Cat(Animal):

    def __init__(self, name):
        super().__init__(name, "Miau!")

my_dog = Dog("Julius")
my_dog.make_sound()

my_cat = Cat("Percival")
my_cat.make_sound()
        

# Extra

class Empleado:

    def __init__(self, id, name, task, staff):
        self.id = id
        self.name = name
        self.task = task
        self.staff = staff

    def presentation(self):
        print(f"Mi nombre es {self.name}")

    def tasks(self):
        print(f"Mis tareas son {self.task}")

    def staffteam(self):
        print(f"Estoy a cargo de: {self.staff}")


class Gerentes(Empleado):

    def __init__(self, id, name):
        super().__init__(id, name, {"Obtener clientes", "Ventas"}, {"Gerente de proyectos", "Programadores"})

class GerenteDeProyecto(Empleado):

    def __init__(self, id, name):
        super().__init__(id, name, {"Abrir tickets", "Delegar tareas"}, {"Programadores"})

class Programador(Empleado):

    def __init__(self, id, name):
        super().__init__(id, name, {"Resolver tickets", "Juntas"}, {"No tiene empleados a cargo"})

gerente1 = Gerentes("123", "Juan")
gerente1.presentation()
gerente1.staffteam()
gerente1.tasks()

gerenteP1 = GerenteDeProyecto("234", "Carlos")
gerenteP1.presentation()
gerenteP1.staffteam()
gerenteP1.tasks()

programador1 = Programador("345", "Christian")
programador1.presentation()
programador1.staffteam()
programador1.tasks()


