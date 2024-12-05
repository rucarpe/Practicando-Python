## .format()
numeros = (22, 15, 44, 107)
print (f"Lista de número: {numeros}")
print ("¿Qué número es mayor?")
mayor = max(numeros)
print (mayor)

numero1 = int(input("Introduce el primer número 👉 "))
numero2 = int(input("Introduce el segundo número 👉 "))
numero3 = int(input("Introduce el tercer número 👉 "))

mayor = max(numero1, numero2, numero3)
menor = min(numero1, numero2, numero3)

print ("El número mayor entre {}, {} y {} es: {}".format(numero1, numero2, numero3,
                                                         max(numero1, numero2, numero3)))
print ("Y el número menor entre {}, {} y {} es: {}".format (numero1, numero2, numero3,
                                                            min(numero1, numero2, numero3)))