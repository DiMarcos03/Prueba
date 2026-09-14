# Primer programa en Python
print("¡Hola, mundo!")

# Variables
nombre = "Marcos"
edad = 25
print(f"Mi nombre es {nombre} y tengo {edad} años.")

# Entrada de usuario
usuario = input("Escribe tu nombre: ")
print(f"Hola, {usuario}!")

# Condicional
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# Bucle for
for i in range(1, 6):
    print(i)

# Más ejemplos para principiantes

# Listas
frutas = ["manzana", "pera", "uva"]
print(frutas)
print(frutas[0])
frutas.append("banana")
print(frutas)

# Bucle while
contador = 0
while contador < 3:
    print("Contador:", contador)
    contador += 1

# Función simple
def saludar(nombre):
    return f"Hola, {nombre}!"

print(saludar("Marcos"))

# Diccionario
persona = {"nombre": "Marcos", "edad": 25}
print(persona["nombre"])
print(persona.get("edad"))

# Ejemplo con condicional anidado
numero = 10
if numero > 0:
    print("El número es positivo.")
elif numero == 0:
    print("El número es cero.")
else:
    print("El número es negativo.")

