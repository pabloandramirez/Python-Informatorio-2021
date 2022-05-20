#Si la compra es por una cantidad mayor o igual a 10 remeras se hara un descuento del 80%
"""
cantidad_de_remeras = int(input("Cuanta cantidad de remeras compraste:\n"))
precio_unidad = int(input("Cuanto es el precio por remera:\n$"))
descuento = int(input("De cuanto es el descuento por 10 o mas remeras:\n"))
if cantidad_de_remeras >= 10:
	total = cantidad_de_remeras * precio_unidad * ( 1 - descuento*0.01)
	print("Tenes un descuento del: ", descuento, "%")
	print("El total a pagar es ", total)
else:
	total = cantidad_de_remeras * precio_unidad
	print("El total a pagar es ", total)
"""




#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programaque pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde
"""
print("\tBIENVENIDO A LA ASIGNACIÓN DE GRUPO!!!!!\t")

z = "s"

while z.lower() == "s" :
	nombre = input("Indique su nombre por favor:\n")
	sexo = input("Indique su sexo por favor: F ó M\n")
	if not nombre.isdigit() and not sexo.isdigit():
		if sexo.capitalize() == "F":
			if nombre.capitalize() < "M":
	 			print("Usted pertenece al grupo A\nBuen día!")
	 			break
			else:
	 			print("Usted pertenece al grupo B\nBuen día!")
	 			break
		else:
			if nombre.capitalize() > "N":
	 			print("Usted pertenece al grupo A\nBuen día!")
	 			break
			else:
	 			print("Usted pertenece al grupo B\nBuen día!")
	 			break
	else:
		print("Por favor ingrese caracteres correctos")
"""




#Programa que realice una suma y pregunte nuevamente si quiere reaizar una nueva suma
#z = "s"
"""
while z == "s":
	a = int(input("Favor de ingresar el primer numero:\n"))
	b = int(input("Favor de ingresar el segundo numero:\n"))
	suma = a + b
	print("La suma es de ", suma)
	desea_sumar = input("Desea realizar otra suma:\n")
	if desea_sumar.capitalize() == "No":
		break
"""

"""
Haremos un programa que genere una multipicación de dos números del 2 al 10 al azar, pregunte por el resultado y diga si se ha dado la respuesta correcta. Al inicio debe preguntar cuantas multiplicaciones se van a hacer. El programa debe llevar la cuenta de las respuestas correctas e incorrectas e indicar la nota correspondiente.
Si la nota es igual o mayor que 9, el programa felicitará al usiario por el resultado
Si se acierta la respuesta se contabilizará como 1
Si se acerca menos del 10% a la respuesta correcta, se contabilizará como 0.66.
Si se acerca entre el 10% y el 30%  la respuesta correcta, se contabilizará como 0.33.
Si se aleja más del 30% a la respuesta correcta, se contabilizará como 0.
"""
"""
from random import randrange

print("\tBIENVENIDO, A CONTINUACIÓN LE SOLICITAREMOS INGRESE LOS DATOS PARA CALCULAR LA MULTIPLICACIÓN\t")

cantidad_multiplicacion = int(input("Por favor indique cuantas multiplicaciones se van a realizar:\n"))
cantidad_aciertos = 0

for j in range(0, cantidad_multiplicacion):
	multiplicador = randrange(2,10)
	multiplicando = randrange(2,10)

	resultado_multiplicacion = multiplicando * multiplicador

	resultado = int(input("Ingrese por favor el resultado de {} x {}:\n".format(multiplicador,multiplicando)))
	desvio = (abs(resultado_multiplicacion - resultado)/resultado)*100
	if desvio == 0:
		cantidad_aciertos += 1
	elif desvio <= 10:
		cantidad_aciertos += 0.66
	elif desvio > 10 and desvio <= 30:
		cantidad_aciertos += 0.33
nota = (cantidad_aciertos/cantidad_multiplicacion)*100

print(f"La nota obtenida es {nota}")

if nota >= 90:
	print("\tFelicitaciones!! Has obtenido mas del 90 de aprobación\t")
"""

#Ejemplo break
"""
nombres = ["Araldo", "Ana", "Ano"]

for i in range(len(nombres)):
	print(nombres[i])
	if nombres[i] == "Ana":
		print("Se ha encontrado el nombre Ana")
		break

print("La iteración ha finalizado")
"""


#Ejemplo continue
"""
nombre = "Python"

for i in nombre:
	if i == "h":
		continue
	print("La letra es ", i)
"""

#Ejemplo pass
"""
for letra in "Python":
	if letra == "h":
		pass
		print("Esta letra esta bloqueada")
	print("Letra actual: ", letra)
"""
"""
Construya un algoritmo capaz de encontrar todas las cifras de tres dígitos que cumplan con la condición de que la suma de los cubos de sus dígitos sea igual al número que la cifra representa.
Ejemplo el 153

1**3 + 5**3 + 3**3 = 153
"""
"""
contador = 0

for i in range(100,1000):
	c = i // 100
	d = (i // 10) % 10
	u = i % 10
	contador = c**3 + d**3 + u**3
	if contador == i:
		print(i)
		contador = 0

for i in range(100,1000):
	s = str(i)
	suma = 0
	for digito in s:
		suma = suma + int(digito)**3
	if suma == i:
		print (i)
"""
"""
print("\tVERIFICACIÓN DE USO FERTILIZANTES\t")
compuesto = int(input("Ingrese cuánto es el porcentaje de compuesto en el suelo por hectárea:\n"))
matorral = input("Existe matorral en la hectárea:\n")

if compuesto >= 10:
	if matorral.capitalize() == "No":
		print("SI se puede utilizar fertilizante")
	else:
		print("NO se puede usar fertilizante")
else:
	print("NO se puede usar fertilizante")
"""

