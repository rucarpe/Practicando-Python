# ---------------- CONVERSIONES --------------- #

# Fórmulas conversión de grados
# Cº a Fº
## (x × 9 / 5) + 32 = y
# Fº a Cº
## (x - 32) * 5/9 = y
#
#  Lógica
#	En la escala Celsius:
#	•	El agua se congela a 0 °C y hierve a 100 °C.
#	•	En la escala Fahrenheit:
#	•	El agua se congela a 32 °F y hierve a 212 °F.
# Esto significa que:
#	•	El punto de congelación del agua es 32 grados más alto en Fahrenheit que en Celsius.
#	•	Por eso, sumamos o restamos 32 en las fórmulas para ajustar este desplazamiento.
#	2.	Diferencia entre los intervalos:
#	•	En la escala Celsius, el intervalo entre el congelamiento y la ebullición del agua es de 100 grados.
#	•	En la escala Fahrenheit, ese mismo intervalo es de 180 grados.
# Esto implica que:
#	•	1 °C equivale a  180/100 = 9/5  °F.
#	•	1 °F equivale a  100/180 = 5/9  °C.

print ("Conversor de grados Cº a Fº")
grados = input("Introduce los grados Cº: ")
resultadof = (int(grados)*9/5)+32
print (resultadof)

print ("Conversor de grados Fº a Cº")
grados = input("Introduce los grados Cº: ")
resultadoc = (int(grados)-32)*5/9
print (resultadoc)

# ---------------- MONEDA --------------- #
