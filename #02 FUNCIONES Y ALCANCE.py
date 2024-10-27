# EJERCICIO:
#  * - Crea ejemplos de funciones básicas que representen las diferentes
#  *   posibilidades del lenguaje:
#  *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
#  * - Comprueba si puedes crear funciones dentro de funciones.
#  * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
#  * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
#  * - Debes hacer print por consola del resultado de todos los ejemplos.
#  *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
#  *

# Sin retorno
def ejemplo1():
    print("Función sin retorno")

ejemplo1()

# Con retorno
def ejemplo2(numero):
    return f"El numero que elegiste es {numero}"

print(ejemplo2(55))

# Retorno con varios argumentos
def ejemplo3(a, b, c):
    return f"La suma de tus numeros es: {a + b +c}"

print(ejemplo3(5, 5, 5))

# Con un argumento predeterminado
def default_arg_greet(name="Python"):
    print(f"Hola, {name}!")

default_arg_greet("Christian")
default_arg_greet()

# Con retorno de varios valores


def multiple_return_greet():
    return "Hola", "Python"


greet, name = multiple_return_greet()
print(greet)
print(name)

# Con un número variable de argumentos
def variable_arguments(*names):
    for name in names:
        print(f"Hola, {name}!")


variable_arguments("Python", "Brais", "MoureDev", "comunidad")

# Con un número variable de argumentos con palabra clave
def variable_key_arguments(**names):
    for key, value in names.items():
        print(f"{value} ({key})!")


variable_key_arguments(
    language="Python",
    name="Brais",
    alias="MoureDev",
    age=36
)


# Funciones dentro de funciones
def outer_function():
    def inner_function():
        print("Función interna: Hola, Python !")
    inner_function()


outer_function()


# Funciones del lenguaje (built-in)
print(len("ChristianBustamante"))
print(type(36))
print("ChristianBustamante".upper())


# Variables locales y globales

global_var = "Python"


def hello_python():
    local_var = "Hola"
    print(f"{local_var}, {global_var}!")


print(global_var)

# print(local_var) No se puede acceder desde fuera de la función

hello_python()


#  * DIFICULTAD EXTRA (opcional):
#  * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
#  * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
#  *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
#  *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
#  *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
#  *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
#  *
#  * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
#  * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
#  */


def dificultadExtrema(parametro1, parametro2):
    contador = 0
    for n in range(1, 101):
        if n % 3 == 0 and n % 5 == 0:
            print(parametro1 + parametro2)
        elif n % 3 == 0:
            print(parametro1)
        elif n % 5 == 0:
            print(parametro2)
        else:
            print(n)
            contador += 1
        
    return contador

prueba = dificultadExtrema("Fizz", "Buzz")

print(f"Numeros impresos: {prueba}")
