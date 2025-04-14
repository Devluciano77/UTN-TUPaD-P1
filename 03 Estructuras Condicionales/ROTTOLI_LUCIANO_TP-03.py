# ejercicio 1
edad = int(input("ingresar edad: "))

if edad >= 18:
    print("Es mayor de edad")

# ejercicio 2
nota = int(input("ingresar nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# ejercicio 3
numeroPar = int(input("ingresar numero: "))

if numeroPar % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

# ejercicio 4
edadUsuario = int(input("ingresar edad: "))

if edadUsuario < 12:
    print("Categoria: Niño/a")
elif edadUsuario >= 12 and edadUsuario < 18:
    print("Categoria: Adolescente")
elif edadUsuario >= 18 and edadUsuario < 30:
    print("Categoria: Adulto/a joven")
else:
    print("Categoria: Adulto/a")

# ejercicio 5
contraseña = input("ingresar contraseña: ")

if len(contraseña) >= 8 and len(contraseña) <= 14 :
    print("Ha ingresado una contraseña correcta")
else :
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# ejercicio 6
import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]
media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

if media > mediana and mediana > moda:
    print("La distribución tiene sesgo positivo (a la derecha).")
elif media < mediana and mediana < moda:
    print("La distribución tiene sesgo negativo (a la izquierda).")
elif media == mediana == moda:
    print("La distribución no tiene sesgo.")
else:
    print("No se puede determinar claramente el sesgo.")

# ejercicio 7
texto = input("Ingrese una frase o palabra: ")

if texto[-1].lower() in "aeiou":
    texto += "!"
print(texto)

# ejercicio 8
nombre = input("Ingrese su nombre: ")
opcion = int(input("seleccione una opcion: 1 - mayuscula , 2 - minuscula , 3 - primera letra mayuscula: "))

if opcion == 1 :
    print(nombre.upper())
elif opcion == 2 :
    print(nombre.lower())
elif opcion == 3 :
    print(nombre.title())
else :
    print("opcion incorrecto")

# ejercicio 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible)")
elif magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

# ejercicio 10
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").strip().upper()
mes = int(input("¿Qué mes es? (1-12): "))
dia = int(input("¿Qué día es? (1-31): "))

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"
else:
    estacion_norte = "Desconocido"
    estacion_sur = "Desconocido"

if hemisferio == "N":
    print(f"Te encuentras en {estacion_norte}.")
elif hemisferio == "S":
    print(f"Te encuentras en {estacion_sur}.")
else:
    print("Hemisferio no válido. Por favor ingresa 'N' o 'S'.")








