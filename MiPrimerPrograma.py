nombreDeUsuario = input("¿Cuál es tu nombre?")
print (nombreDeUsuario)
numeros = (22, 15, 44, 107)
print (f"Lista de número: {numeros}")
print ("¿Qué número es mayor?")
mayor = max(numeros)
print (mayor)

numero1 = int(input("Introduce el primer número"))
numero2 = int(input("Introduce el segundo número"))
numero3 = int(input("Introduce el tercer número"))

mayor = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)

print (f"El número mayor es: {mayor}")
print (f"El número menor es: {menor}")

# f-strings
nombreDeUsuario = input("¿Cuál es tu nombre?")
print(f"Hola, {nombreDeUsuario}!")

numeros = (22, 15, 44, 107)
print("¿Qué número es mayor?")
mayor = max(numeros)
print(f"El número mayor es: {mayor}")

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero3 = int(input("Introduce el tercer número: "))

mayor = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")