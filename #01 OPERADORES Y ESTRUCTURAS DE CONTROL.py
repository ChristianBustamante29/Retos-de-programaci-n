# Ejercicio

# Operadores aritméticos
print(f"La suma de 10 + 5 es: {10 + 5}")
print(f"La resta de 10 - 5 es: {10-5}")
print(f"La multiplicación de 10 * 5 es: {10 * 5}")
print(f"La división de 10 / 5 es: {10 / 5}")
print(f"El modulo de 10 % 5 es: {10 % 3}")
print(f"El exponente de 10 ** 3 es: {10**3}")
print(f"Division entera: 10 // 3 = {10 // 3}")

# Operadores de comparación
print(f"Igualdad == {10 == 10}")
print(f"Desigualdad 10 != 5 {10 != 5}")
print(f"Mayor que: 10 > 5 {10 > 5}")
print(f"Menor que: 5 < 10 {5 < 10}")
print(f"Mayor o igual que 10 >= 5 {10 >= 5}")
print(f"Menor o igual que 5 <= 10 {5 <= 10}")

# Operadores logicos
print(f"Operador AND &&: 10 == 5 and 5 > 3 {10 + 5 == 15 and 5 + 3 == 8}")
print(f"Operador OR ||: 10 + 5 == 15 or 5 + 5 == 10 {10 + 5 == 15 or 5 + 5 == 10}")
print(f"Operador NOT !: not 10 + 5 == 16 es {not 10 + 5 == 16}")

# Operador de asignación
my_number = 10
print(my_number)
my_number += 1
print(my_number)
my_number -= 1
print(my_number)
my_number *= 2
print(my_number)
my_number /= 2
print(my_number)
my_number %= 2
print(my_number)
my_number **= 2
print(my_number)
my_number //=2
print(my_number)

# Operadores de identidad
nuevo_numero = my_number
print(f"mi numero es mi nuevo numero {my_number is nuevo_numero}")
print(f"mi numero no es mi nuevo numero {my_number is not nuevo_numero}")

# Operadores de pertenencia
print(f"'e' in 'daniel' = {'e' in 'daniel'}")
print(f"'c' not in 'daniel' = {'c' not in 'daniel'}")

# Operadores de bit
a = 10  # 1010
b = 7  # 0111
print(f"AND: 10 & 3 = {10 & 3}")  # 0010
print(f"OR: 10 | 3 = {10 | 3}")  # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")  # 101000


# Estructuras de control


# Condicionales

my_string = "Brais"

if my_string == "Daniel":
    print("my_string es 'Daniel'")
elif my_string == "Christian":
    print("my_string es 'Christian'")
else:
    print("my_string no es 'Daniel' ni 'Christian'")

# Iterativas

for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1

# Manejo de excepciones
try:
    print(10 / 0)
except:
    print("Se ha producido un error")
finally:
    print("Ha finalizado el manejo de excepciones")




# Dificultad extrema

for n in range(10, 56):
    if n % 2 == 0 and not n == 16 and not n % 3 == 0:
        print(n)
