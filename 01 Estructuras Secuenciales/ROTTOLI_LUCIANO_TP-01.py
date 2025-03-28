# ejercicio 1
print("Hola Mundo!")

# ejercicio 2
nombre = input("ingresar nombre ")
print(f"Hola {nombre}")

# ejercicio 3
nombre_usuario = input("ingresar nombre ")
apellido_usuario = input("ingresar apellido ")
edad_usuario = input("ingresar edad ")
lugar_usuario = input("ingresar lugar ")
print(f"Soy {nombre_usuario} {apellido_usuario}, tengo {edad_usuario} años y vivo en {lugar_usuario}")

# ejercicio 4
radio = float(input("ingresar radio "))
area = 3.14 * (radio ** 2)
perimetro = 2 * 3.14 * radio
print(f"area: {area}, perimetro: {perimetro}")

# ejercicio 5
segundos = input("ingresar cantidad de segundos ")
horas = int(segundos) / 60
print(f"la cantidad ingresado equivale a {horas} horas")

# ejercicio 6
numero = int(input("Ingrese un número: "))

print(f"Tabla de multiplicar del {numero}:")
print(f"{numero} x 1 = {numero * 1}")
print(f"{numero} x 2 = {numero * 2}")
print(f"{numero} x 3 = {numero * 3}")
print(f"{numero} x 4 = {numero * 4}")
print(f"{numero} x 5 = {numero * 5}")
print(f"{numero} x 6 = {numero * 6}")
print(f"{numero} x 7 = {numero * 7}")
print(f"{numero} x 8 = {numero * 8}")
print(f"{numero} x 9 = {numero * 9}")
print(f"{numero} x 10 = {numero * 10}")

# ejercicio 7
num1 = int(input("Ingrese el primer número (distinto de 0): "))
num2 = int(input("Ingrese el segundo número (distinto de 0): "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2

print("Resultados:")
print(f"{num1} + {num2} = {suma}")
print(f"{num1} - {num2} = {resta}")
print(f"{num1} * {num2} = {multiplicacion}")
print(f"{num1} / {num2} = {division}")

# ejercicio 8
altura = float(input("ingresar altura: "))
peso = float(input("ingresar peso: "))
imc = peso / (altura ** 2)
print(f"su IMC es {imc}")

# ejercicio 9
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius}°C equivale a {fahrenheit:.2f}°F")

# ejercicio 10
num_1 = int(input("ingresar numero: "))
num_2 = int(input("ingresar numero: "))
num_3 = int(input("ingresar numero: "))
promedio = (num_1 + num_2 + num_3) / 3
print(f"el promedio es: {promedio}")