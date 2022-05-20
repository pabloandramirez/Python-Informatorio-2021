"""
usuario = "Pablo19"
contraseña = "palomitas"
contador = 0

while contador != 5:
	ingresar_usuario = input("Coloque su usuario por favor:\n")
	ingresar_contraseña = input("Coloque su contraseña por favor:\n")
	if ingresar_usuario == usuario:
		if ingresar_contraseña == contraseña:
			print("BIENVENIDO GILIPOLLAS!!")
			break
		else:
			print("Usuario o contraseña incorrectos. Ingrese de nuevo por favor!!!")
			contador += 1
	else:
		print("Usuario o contraseña incorrectos. Ingrese de nuevo por favor!!!")
		contador += 1
else:
	print("Usuario bloqueado!!!. Contactese con el administrador")
"""
"""
cantidad_tapitas = int(input("Cuantas tapitas tiene para reciclar:\n"))
compra_cliente = int(input("Cuanto es la compra del cliente:\n"))

if cantidad_tapitas >= 20:
	total = compra_cliente * 0.6
elif cantidad_tapitas < 20 and cantidad_tapitas >= 10:
	total = compra_cliente * 0.75
else:
	total = compra_cliente

print("El total de la compra es de ", total)
"""
"""
patente = "ABD12311"
tiro_basura = 0
multado_antes = 0

if patente[6] == "1":
	print("Tiro Basura")
	tiro_basura += 1
else:
	print("No tiro basura")
if patente[7] == "1":
	print("Ya habia sido multado")
	multado_antes += 1
else:
	print("No fue multado antes")
"""
#Solicite al usuario el ingreso de 3 números, e imprímalos de mayor a menor.
"""
ingresar_numero1 = int(input("Favor de colocar el primer número:\n"))
ingresar_numero2 = int(input("Favor de colocar el segundo número:\n"))
ingresar_numero3 = int(input("Favor de colocar el tercer número:\n"))

if ingresar_numero1 > ingresar_numero2:
	if ingresar_numero2 > ingresar_numero3:
		print(ingresar_numero1)
		print(ingresar_numero2)
		print(ingresar_numero3)
	else:
		if ingresar_numero1 > ingresar_numero3:
			print(ingresar_numero1)
			print(ingresar_numero3)
			print(ingresar_numero2)
		else:
			print(ingresar_numero3)
			print(ingresar_numero1)
			print(ingresar_numero2)
else:
	if ingresar_numero1 > ingresar_numero3:
		print(ingresar_numero2)
		print(ingresar_numero1)
		print(ingresar_numero3)
	else:
		if ingresar_numero2 > ingresar_numero3:
			print(ingresar_numero2)
			print(ingresar_numero3)
			print(ingresar_numero1)
		else:
			print(ingresar_numero3)
			print(ingresar_numero2)
			print(ingresar_numero1)
"""

#Desarrolle un programa que permita determinar si un número X ingresado es par o impar.
"""
numero = int(input("Favor de colocar un numero:\n"))

if numero % 2:
	print("El numero es impar")
else:
	print("El numero es par")
"""

#Determinar si el primero de un conjunto de tres números dados, es menor que los otros dos
"""
ingresar1 = int(input("Ingresar el primer numero:\n"))
ingresar2 = int(input("Ingresar el segundo numero:\n"))
ingresar3 = int(input("Ingresar el tercer numero:\n"))

if ingresar1 < ingresar2:
	if ingresar1 < ingresar3:
		print("El primer numero es menor que el segundo y el tercero")
	else:
		print("El primer numero no es menor que los otros dos")
else:
	print("El primer numero no es menos que los otros dos")
"""
#Realizar un programa que sea capaz de, habiéndose ingresado dos números m y n, determine si n es divisor de m.
"""
numero_m = int(input("Ingresar el numero M\n"))
numero_n = int(input("Ingresar el numero N\n"))

if numero_m % numero_n:
	print("El numero N no es divisor de M")
else:
	print("El numero N es divisor de M")
"""

#Diseñar un programa que lea las longitudes de los tres lados de un triángulo (L1,L2,L3) y determine qué tipo de triángulo es, de acuerdo a los siguientes casos
"""
A = int(input("Indique la longitud en cm del lado mas grande:\n"))
B = int(input("Indique la longitud en cm del segundo lado:\n"))
C = int(input("Indique la longitud en cm del tercer lado:\n"))

if A >= (B + C):
	print("No se trata de un triangulo")
elif (A**2) == ((B**2) + (C**2)):
	print("Es un triangulo rectángulo")
elif (A**2) > ((B**2) + (C**2)):
	print("Es un triangulo obtusangulo")
else:
	print("Es un triangulo acutangulo")
"""
"""
Un equipo de fútbol ha tenido una buena campaña y desea premiar a sus jugadores con un aumento del salario para la siguiente campaña. Los sueldos deben ajustarse de la siguiente forma: 
0 – 6000							15%

6000 – 7900					   10%

7900 – 12000					6%

 Mas de 12000				   0%

sueldo_del_jugador = int(input("Sueldo del jugador\n"))
aumento = 0
sueldo_aumentado = 0

if sueldo_del_jugador > 0 and sueldo_del_jugador <= 6000:
	aumento = 15
	sueldo_aumentado = sueldo_del_jugador * 1.15
elif sueldo_del_jugador > 6000 and sueldo_del_jugador <= 7900:
	aumento = 10
	sueldo_aumentado = sueldo_del_jugador * 1.10
elif sueldo_del_jugador > 7900 and sueldo_del_jugador <= 12000:
	aumento = 6
	sueldo_aumentado = sueldo_del_jugador * 1.06
else:
	sueldo_aumentado = sueldo_del_jugador

print("El sueldo de jugador que es de $", sueldo_del_jugador, " recibira un aumento del ", aumento,"% y tendra un sueldo final de $", sueldo_aumentado)
"""

#Un comercio ofrece un descuento del 15% sobre el total de la compra si esta supera los $1000. Obtenga para determinado cliente cuánto deberá pagar finalmente por su compra y el descuento obtenido, si es que corresponde.
"""
compra = int(input("Ingrese la compra del cliente $:\n"))
compra_con_descuento = 0

if compra >= 1000:
	compra_con_descuento = compra * (1 - 0.15)
	print("El cliente tiene un descuento del 15% y su compra de $",compra," queda final a $", compra_con_descuento)
else:
	print("Compra sin descuento  de $", compra)
"""

#Calcular el número de pulsaciones que una persona debe tener por cada 10 segundos de ejercicio, si la fórmula es: Número de pulsaciones = (220 - edad)/10
"""
edad = int(input("Favor de ingresar su edad:\n"))
numero_pulsaciones = (220 - edad) / 10
print("Las pulsaciones cada 10 segundos para una persona de edad ", edad, "es de ", numero_pulsaciones, "cada 10 segundos.")
"""

"""
En un Centro Asistencial existen tres áreas: Pediatría, Traumatología y Kinesiología. El presupuesto anual del hospital se reparte conforme a la sig. tabla:

ÁREA 		PORCENTAJE

Pediatría					60%

Traumatología		20%

Kinesiología			20%

Obtener la cantidad de dinero que recibirá cada área, para cualquier monto presupuestal 		que se ingrese por teclado.
"""
"""
presupuesto = int(input("Favor ingrese el presupuesto para el Centro Asistencial:\n"))
pediatria = presupuesto * 0.6
traumatologia = presupuesto * 0.2
kinesiologia = presupuesto * 0.2

print("El presupuesto es de $",presupuesto," y $",pediatria," corresponde para Pediatria, $",traumatologia," corresponde para Traumatologia, y $",kinesiologia," corresponde para Kinesiologia")
"""

#Tres personas deciden invertir su dinero para fundar una empresa. Cada una de ellas invierte una cantidad distinta. Obtener el porcentaje que cada quien invierte con respecto a la cantidad total invertida.
"""
inversion1 = int(input("Cuanto invirtio la primer persona:\n$"))
inversion2 = int(input("Cuanto invirtio la segunda persona:\n$"))
inversion3 = int(input("Cuanto invirtio la tercera persona:\n$"))

total = inversion1 + inversion2 + inversion3

porcentaje1 = (inversion1 * 100) / total
porcentaje2 = (inversion2 * 100) / total
porcentaje3 = (inversion3 * 100) / total

print("El primer inversionista tiene un porcentaje del ",porcentaje1,"%, el segundo el ",porcentaje2,"% y el tercero el ",porcentaje3,"%.")
"""

#Un obrero necesita calcular su salario semanal, el cual se obtiene de la siguiente manera:
# i. Si trabaja 40 horas o menos se le paga $16 por hora
#ii. Si trabaja más de 40 horas se le paga $16 por cada una de las primeras 40 horas y $20 por cada hora extra.
"""
horas_trabajadas = int(input("\tIngrese cuantas horas trabajo en la semana:\n"))
if horas_trabajadas <= 40:
	pago = 40 * 16
else:
	pago = (40 * 16) + ((horas_trabajadas - 40) * 20)
	
print("El pago por las horas trabajadas es de $",pago)
"""

#Se leen tres números que son las longitudes de los lados de un triángulo. Determinar e informar si el mismo es equilátero (3 lados iguales), isósceles (2 lados iguales) o escaleno (3 lados distintos).
"""
longitud1 = int(input("Favor ingrese la primer longitud: "))
longitud2 = int(input("Favor ingrese la segunda longitud: "))
longitud3 = int(input("Favor ingrese la tercera longitud: "))

if longitud1 == longitud2 == longitud3:
	print("El triángulo es equilátero")
elif longitud1 == longitud2 or longitud1 == longitud3 or longitud2 == longitud3:
	print("El triángulo es isósceles")
else:
	print("El triángulo es escaleno")
"""
"""
numeros = []
maximo = 0

for i in range(1,11):
	numeros.append(int(input("Ingresar un numero ")))
for i in numeros:
	if i > maximo:
		maximo = i
print(maximo)
"""

# Desarrollar una solución que calcule la suma de los cuadrados de los n primeros números naturales: 1 + 22 + 32 +… + n2.
"""
acumulador = 0

for i in range(1,11):
	acumulador = acumulador + (i**2)
	print(acumulador)
"""

#Diseñar un programa que permita obtener el producto entre A y B mediante sumas sucesivas.
"""
A = int(input("Ingrese un numero:\n"))
B = int(input("Ingrese otro numero:\n"))

suma = 0

for i in range(0,B):
	suma = suma + A
	print(suma)

print(suma)
"""

#Diseñar un programa que imprima los números del 100 al 0 en orden decreciente.
"""
numero = 101

for i in range (1,numero):
	print(numero - i)
"""


#Solicitar el ingreso de números al usuario y emitir un mensaje para determinar si es par o impar. El ciclo debe finalizar cuando el usuario ingresa 0.
"""
interruptor = True

while interruptor:
	numero = int(input("Ingrese numero para saber si es par o impar. Ingrese 0 para terminar:\n"))
	if numero != 0:
		if numero % 2:
			print("El numero es impar")
		else:
			print("El numero es par")
	else:
		interruptor = False
"""

#Imprimir, contar y sumar los múltiplos de 2 que hay entre una serie de números, tal que el segundo sea mayor o igual que el primero.

"""
termometro = True
contador = 0
acumulador = 0


while termometro:
	A = int(input("Ingrese el primer numero\n"))
	B = int(input("Ingrese el segundo numero\n"))
	if B >= A:
		for i in range(A + 1,B):
			if i % 2:
				pass
			else:
				print(i)
				contador += 1
				acumulador = acumulador + i
		break
	else:
		print("El valor de B debe ser mayor o igual que A")

print(contador)
print(acumulador)
"""

#Realizar un programa que calcule y muestre la suma de los múltiplos de 5 comprendidos entre dos valores A y B. El programa no permitirá introducir valores negativos para A y B y verificará que A es menor que B. Si A es mayor que B, se deben intercambiar los valores.
"""
termometro = True
vacio = 0
suma = 0

while termometro:
	A = int(input("Ingrese el valor de A:\n"))
	B = int(input("Ingrese el valor de B:\n"))
	if A < 0 or B < 0:
		print("Favor de ingresar valores positivos para ambos numeros!")
	elif A >= B:
		vacio = A
		A = B
		B = vacio
		for i in range(A+1,B):
			if i % 5:
				pass
			else:
				suma = suma + i
	else:
		for i in range(A+1,B):
			if i % 5:
				pass
			else:
				print(i)
				suma = suma + i
	break

print(suma)
"""

#Diseñar un programa que permita calcular el total de una compra, ingresando cantidad y precio de los productos. El programa debe estar preparado para que el ingreso de los datos se produzca hasta que el usuario lo desee.
"""
interruptor = True
total = 0

while interruptor:
	inicio = int(input("\tPresione cualquier tecla para ingresar cantidad de productos y precios. Sino presione 0\n"))
	if inicio != 0:
		cantidad_productos = int(input("\tCantidad de productos:\n"))
		precio_productos = int(input("\tPrecio unidad producto:\n"))
		total = total + (precio_productos * cantidad_productos)
	else:
		print("\tGracias por elegirnos, vuelva pronto!")
		break
print("\tEl total a pagar es ",total)
"""

#Un censador recopila ciertos datos aplicando encuestas para el último Censo Nacional de Población y Vivienda. Desea obtener de todas las personas que alcance a encuestar en un día, que porcentaje tiene estudios de primaria, secundaria, carrera técnica, estudios profesionales y estudios de posgrado.
"""
interruptor = True
personas = 0
primaria = 0
secundaria = 0
tecnica = 0
profesionales = 0
posgrado = 0


while interruptor:
	inicio = input("Para anotar una persona presione cualquier tecla y luego enter. Para finalizar ingrese Exit\n")
	if inicio.capitalize() != "Exit":
		personas += 1
		estudios = int(input("Que estudios tiene cumplidos:\n1-Primaria\n2-Secundaria\n3-Tecnica\n4-Profesional\n5-Posgrado\n"))
		if estudios == 1:
			primaria +=1
		elif estudios == 2:
			secundaria +=1
		elif estudios == 3:
			tecnica += 1
		elif estudios == 4:
			profesionales += 1
		elif estudios == 5:
			posgrado += 1
		else:
			print("Valor ingresado incorrectamente, Intente nuevamente por favor!\n")
	else:
		print("Gracias por usar Censo Villas. No emo nieri\n")
		break
	if personas != 0:
		porcentaje_primaria = (primaria * 100) / personas
		porcentaje_secundaria = (secundaria * 100) / personas
		porcentaje_tecnica = (tecnica * 100) / personas
		porcentaje_profesionales = (profesionales * 100) / personas
		porcentaje_posgrado = (posgrado * 100) / personas

print("De un total de ",personas,"un ",porcentaje_primaria,"% termino la escuela primaria, un",porcentaje_secundaria,"% la escuela secundaria, un",porcentaje_tecnica,"% una escuela tecnica, un",porcentaje_profesionales,"% son profesionales y un ",porcentaje_posgrado,"% tienen posgrado")
"""
# Mostrar los perímetros de varios triángulos ingresados sus lados por teclado, hasta que ya no desee.
"""
boton = True

while boton:
	inicio = input("\tFavor de ingresar 1 para calcular perimetro o 0 para salir del prorama\n")
	if inicio == "1":
		lado1 = int(input("\tFavor de ingresar el primer lado en cm:\n"))
		lado2 = int(input("\tFavor de ingresar el segundo lado en cm:\n"))
		lado3 = int(input("\tFavor de ingresar el tercero lado en cm:\n"))
		if lado1 != 0 and lado2 != 0 and lado3 != 0:
			perimetro = lado1 + lado2 + lado3
			print("\tEl perimetro de este triangulo es de ",perimetro)
		else:
			print("\tNinguno de los lados puede ser 0, ingrese nuevamente")
	elif inicio == "0":
		print("\tGracias por utilizar Sabiondo. Hasta luego!!!\t")
		break
	else:
		print("\tValor incorrecto. Ingrese nuevamente")
"""

#Hacer un programa que permita determinar todos los divisores de un número ingresado por el teclado.

"""
divisores = []
boton = True
while boton:
	numero = input("\tIngrese el numero a calcular:\n")
	if numero.isdigit():
		for i in range (1,int(numero) + 1):
			if int(numero) % i:
				pass
			else:
				divisores.append(i)
		break
	else:
		print("\tFavor de ingresar un numero")

print(divisores)
"""

#Calcular el monto a pagar por cada cliente y total recaudado en una estación de servicio. Debe diseñar un programa que permita monto por cliente y el total recaudado por la gasolinera, tomando en cuenta lo siguiente:
#El precio del litro es para el Tipo A $50, para el Tipo B $ 55 y para el Tipo C $60
#El programa finaliza cuando se introduce una D como tipo de gasolina.
"""
total = 0
tipo_a = 50
tipo_b = 55
tipo_c = 60
boton = True

while boton:
	tipo = input("\tFavor de ingresar el tipo de gasolina (A,B o C), o presione D para salir\n")
	if tipo.capitalize() == "A":
		litros = int(input("\tIngrese cuantos litros de Tipo A compró\n"))
		total = total + (litros * tipo_a)
	elif tipo.capitalize() == "B":
		litros = int(input("\tIngrese cuantos litros de Tipo B compró\n"))
		total = total + (litros * tipo_b)
	elif tipo.capitalize() == "C":
		litros = int(input("\tIngrese cuantos litros de Tipo C compró\n"))
		total = total + (litros * tipo_c)
	elif tipo.capitalize() == "D":
		print("Dia de operaciones finalizado")
		break
	else:
		print("Valor incorrecto, ingrese nuevamente")

print("El total facturado del dia es de $",total)
"""

#Una pizzería, vende sus pizzas en tres tamaños: pequeña, mediana; y grandes. Una pizza puede ser sencilla (con sólo salsa y carne), o con ingredientes extras, tales como pepinillos, champiñones o cebollas. Desarrolle una solución que calcule el precio de venta de una pizza, dándole el tamaño y el número de ingredientes extras. El precio de venta será 1.5veces el costo total, que viene determinado por el tamaño, más el número de ingredientes. En particular el costo total se calcula sumando:
#un costo fijo de preparación.
#un costo variable que es proporcional al tamaño de la pizza.
#un costo adicional por cada ingrediente extra (por simplicidad se supone que cada ingrediente extra tiene el mismo costo).
"""
costo_fijo = 75
pizza_pequenia = 50
pizza_mediana = 75
pizza_grande = 100
boton = True

while boton:
	tamanio = input("\tLa pizza que desea preparar es:\n1-Pequeña\n2-Mediana\n3-Grande\n")
	total = 0
	if tamanio == "1":
		total = total + costo_fijo + pizza_pequenia
	elif tamanio == "2":
		total = total + costo_fijo + pizza_mediana
	elif tamanio == "3":
		total = total + costo_fijo + pizza_grande
	else:
		print("Favor de ingresar la opcion correcta")
		continue
	ingredientes = input("\tAdemas de la salsa y la carne tenemos ingredientes adicionales como pepinillos, champiñones o cebollas. Indique si desea agregar 1, 2 o las 3 opciones a la pizza ó 0 si solo desea lo básico\n")
	if ingredientes == "1":
		opcion = input("\tQue opcion desea agregar:\n1-Pepinillos\n2-Champiñones\n3-Cebollas\n")
		if opcion == "1":
			total = total + 50
		elif opcion == "2":
			total = total + 70
		elif opcion == "3":
			total = total + 30
		else:
			print("Favor de ingresar la opcion correcta")
			continue
	elif ingredientes == "2":
		opcion = input("\tQue opciones desea agregar:\n1-Pepinillos y Champiñones\n2-Champiñones y Cebollas\n3-Cebollas y Pepinillos\n")
		if opcion == "1":
			total = total + 120
		elif opcion == "2":
			total = total + 100
		elif opcion == "3":
			total = total + 80
		else:
			print("Favor de ingresar la opcion correcta")
			continue
	elif ingredientes == "3":
		total = total + 300
	elif ingredientes == "0":
		total = total
	else:
		print("Favor de ingresar la opcion correcta")
		continue
	print("\t*****************************************************")
	print("\tEl total de la pizza para vender es de $", total*1.5)
	print("\t*****************************************************")
"""

#Diseña un programa al que se proporcione como entradas dos enteros y un carácter. El programa deberá sumar, restar, multiplicar o dividir los valores de los dos primeros parámetros dependiendo del código indicado en el tercer parámetro, y devolver el resultado. Por ejemplo si el usuario ingresa la opción “S”, se deberán sumar los números.
"""
boton = True


while boton:
	letra = input("\tIngresar que operacion desea realizar:\n\tSumar (S)\n\tRestar (R)\n\tMultiplicar (M)\n\tDividir (D)\n\tSalir (Q)\n\t")
	if letra.capitalize() != "Q":
		numero1 = input("\tIngresar el primer número:\t")
		numero2 = input("\tIngresar el segundo número:\t")
		if numero1.isdigit() and numero2.isdigit():
			if letra.capitalize() == "S":
				total = int(numero1) + int(numero2)
				print("\tEl total de la suma es ",total)
			elif letra.capitalize() == "R":
				total = int(numero1) - int(numero2)
				print("\tEl total de la resta es ",total)
			elif letra.capitalize() == "M":
				total = int(numero1) * int(numero2)
				print("\tEl total del producto es ",total)
			elif letra.capitalize() == "D":
				total = int(numero1) / int(numero2)
				print("\tEl total del cociente es ",total)
			else:
				print("\tOpcion incorrecta, ingrese nuevamente por favor")
				continue
		else:
			print("\tValos incorrectos, verifique que ingresa números!!!")
	else:
		print("\tGracias por utilizar Neurus Calculator!!")
		break
"""

#Dados los datos de un municipio: zona, sexo y edad de cada uno de sus habitantes, encontrar:
#a) porcentaje de varones menores de 15 años para cada zona
#b) porcentaje de varones menores de 15 años para todo el municipio
#Los datos vienen ordenados por zona.Con dato de zona igual a 0, se indica el fin.

resistencia = 0
zona_sur = 0
zona_norte = 0
zona_oeste = 0
zona_este= 0
microcentro = 0


while True:
	zona = input("\tFavor de indicar a que zona pertenece la persona:\n")
	if zona.capitalize() == "Zona sur":
		zona_sur += 1
		resistencia += 1
	elif zona.capitalize() == "Zona norte":
		zona_norte += 1
		resistencia += 1
	elif zona.capitalize() == "Zona oeste":
		zona_oeste += 1
		resistencia += 1
	elif zona.capitalize() == "Microcentro":
		microcentro += 1
		resistencia += 1
	elif zona.capitalize() == "Zona este":
		zona_este += 1
		resistencia += 1
	else:
		print("\tZona incorrecta. Ingrese nuevamente por favor")
		continue
