# ejercicio 1
for i in range(0, 101):
    print(i)

# ejercicio 2
numero = input("Ingrese un número entero: ").lstrip("-")
contador = 0
for _ in numero:
    contador += 1
print(f"El número tiene {contador} dígito(s).")

# ejercicio 3
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
suma = 0
for i in range(min(a, b) + 1, max(a, b)):
    suma += i
print(f"La suma de los números entre {a} y {b} es: {suma}")


# ejercicio 4
total = 0
while True:
    numero = int(input("Ingrese un número entero (0 para salir): "))
    if numero == 0:
        break
    total += numero
print(f"La suma total es: {total}")

# ejercicio 5
import random

numero_secreto = random.randint(0, 9)
intentos = 0
adivinado = False

while not adivinado:
    intento = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1
    if intento == numero_secreto:
        adivinado = True

print(f"¡Correcto! Lo adivinaste en {intentos} intento(s).")

# ejercicio 6
for i in range(100, -1, -2):
    print(i)

# ejercicio 7
limite = int(input("Ingrese un número entero positivo: "))
suma = 0
for i in range(1, limite):
    suma += i
print(f"La suma de los números entre 0 y {limite} es: {suma}")

# ejercicio 8
pares = 0
impares = 0
positivos = 0
negativos = 0

for _ in range(100):
    numero = int(input("Ingrese un número entero: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

# ejercicio 9
cantidad = 100
suma = 0

for _ in range(cantidad):
    numero = int(input("Ingrese un número entero: "))
    suma += numero

media = suma / cantidad
print(f"La media de los {cantidad} números es: {media}")

# ejercicio 10
numero = int(input("Ingrese un número entero: "))
numero_invertido = 0

while numero != 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero //= 10

print(f"Número invertido: {numero_invertido}")





