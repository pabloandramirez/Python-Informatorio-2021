"""
def iva():
    '''función básica para el calculo del IVA'''
    iva = 12
    costo = int(input('¿Cual es el monto a calcular?: '))
    calculo = costo * iva / 100
    print ("El calculo de IVA es: " , calculo , "\n")

mensaje = "Calcular el IVA de un monto"
print(mensaje)
print("=" * len(mensaje) + "\n")
iva()
"""

"""
def suma(numero1,numero2):
    '''función la cual suma dos números'''
    print (numero1 + numero2)
    print ("\n")


mensaje1 = "Suma de dos números"
print (mensaje1)
print ("=" * len(mensaje1) + "\n")
suma(13,37)
"""
"""
def imprime_fibonacci(n):
    '''escribe la sucesión Fibonacci hasta n'''
    resultado = []
    a, b = 0, 1
    while b < n:
        resultado.append(b)
        a, b = b, a + b
    return resultado

mensaje2 = "Sucesión de Fibonacci"
print (mensaje2)
print ("=" * len(mensaje2) + "\n")
print ("La sucesión Fibonacci hasta 10 es: ", imprime_fibonacci(10)) 
"""


"""
def devuelve_fibonacci(n): 
    '''devuelve la sucesión Fibonacci hasta n'''
    resultado = []
    a, b = 0, 1
    while b < n:
        resultado.append(b)
        a, b = b, a + b
    return resultado

print ("\nLa sucesión Fibonacci hasta 50 es: ", devuelve_fibonacci(50))
"""

"""
def​ mi_funcion(param1 =​ "Hola", param2 =​ 0​):
	#Estafunciónimprimelosdosvalorespasadoscomoparámetros ​
	print​(param1)    ​
	print​(param2)

mi_funcion()
"""
"""
def​ indeterminados (*args):
	#Esta función imprime los valores pasados como parámetro
	for​ ​arg​ ​in​ ​args​:
		return(​arg​)


indeterminados(​5​, ​“Hola”​, [​1​, ​2​, ​3​, ​4​, ​5​]​)
"""
"""
def​ resta(num1=​None​, num2=​None​):​
if​ a ==​​None​​ or​ b ==​​None​:
	print​(​"​Error, debes enviar dos números a la función​"​)
	return
return​​ (a - b)

resta​(​30​, ​10)
"""

"""
def hipotenusa(a,b):
	return ((a**2) + (b**2)) ** 0.5







titulo = "Ejercicio 1: Triángulo"
indicaciones = "Devolver Hipotenusa, ingresando los valores le los lados mas cortos de un triángulo Rectángulo"


a=int(input("Ingrese el primer lado : "))
b=int(input("Ingrese el segundo lado: "))

print("La longitud de la Hipotenusa es: %f" %hipotenusa(a,b))
"""

#def​ indeterminados(**kwargs):
	#Esta función imprime los valores pasados como parámetro
	#for​ ​kwarg ​in​ ​kwargs​:
		#print​(​kwarg, "=>", kwargs[kwarg]​)
"""
def indeterminados():

	print("Hola")
		
indeterminados(​n=​5​, c=​"Hola"​, l=[​1​, ​2​, ​3​, ​4​, ​5​]​)
"""
"""
def mi_funcion(param1 = "Hola", param2 = 0):
	print(param1)
	print(param2)
mi_funcion()
"""
"""
mi_variable_global1 = 20
mi_variable_global2 = 20

def funcion():
	global mi_variable_global1
	mi_variable_global1 = 10
	mi_variable_global2 = 10

funcion()
print(mi_variable_global2)
print(mi_variable_global1)
"""
"""
def prueba():
	#Esta funcion retorna varios valores
	return "Hola", 20, [1, 2, 3]

print(prueba())
x, y, z = prueba()
print(x)
print(y)
print(z)
"""
"""
def mensaje():
	#Esta función retorna el mensaje "Hola Mundo"
	return "Hola Mundo"

def saludar(nombre, saludo="Hola"):
	#Esta función imprime el mensaje "Hola Mundo" y un mensaje personalizado
	print(mensaje())
	print(saludo, nombre)

saludar("Juan")
"""
"""
def mensaje():
	#Eta función retorna el mensaje "Hola Mundo"
	return "Hola Mundo"

def llamada_de_retorno(funcion=""):
	#Llamada de retorno a nivel global
	return globals()[funcion]()

print(llamada_de_retorno("mensaje"))
nombre_de_la_funcion = "mensaje"
print(locals()[nombre_de_la_funcion])
"""
"""
def mensaje(nombre):
	#Esta función retorna un mensaje de saludo
	return "Hola " + nombre

def llamada_de_retorno(nombre, funcion=""):
	#Lllamada de retorno a nivel global
	return globals()[funcion](nombre)

print(llamada_de_retorno("Maria","mensaje"))
nombre_de_la_funcion = "mensaje"
print(locals()[nombre_de_la_funcion]("Pedro"))
"""
"""
def mensaje(nombre):
	#Esta función retorna un mensaje de saludo
	return "Hola" + nombre

def llamada_de_retorno(nombre, funcion="")
"""
"""
def saludar():
	print("Bienvenido!")
	return 1


print(saludar())
""" 
"""
def funcion(persona):
	return "Hola " + persona

print(funcion("Boludo"))
"""
"""
def calcular_volumen(base, altura=1, profundidad=1):
	return base*altura*profundidad

print(calcular_volumen(2))
"""
"""
def sumar(a,b,c,d):
	return a+b+c+d

print(sumar(2, 4, 6, 8))
"""
"""
def sumar(*arg):
	print(arg)

sumar(2,3,4)
"""
"""
def sumar(*args):
	sum = 0
	for x in args:
		sum += x
	return sum
print(sumar(2,4,6))
"""
"""
def saludar(*personas):
	for x in personas:
		print("Hola "+ x)

saludar("Sandra","Manuel","Leandro")
"""
"""
def config(**kwargs):
	for x in kwargs:
		print(x, ":", kwargs[x])

config(font="arial", color="red", size=12)
"""
#el orden es primero los parametros comunes, luego los que terminaran en tupla y por ultimo los que terminaran en diccionario
"""
def funcion(a, b, *args, **kwargs, c):
	print("a: ", a)
	print("b: ", b)
	print(args)
	print(kwargs)

funcion(3, 4, 5, "f", "a", color="rojo", size=12)
"""
#Primero los posicionales deben ir en argumentos, despues le pueden seguir los que son por clave
"""
def funcion(a, b, c):
	print("a: ", a)
	print("b: ", b)
	print("c: ", c)

funcion(4, c=4, b=3)
"""
#Cuando es **kwargs SI o SI con clave, como diccionario
"""
def funcion(*args):
	for item in args:
		print(item)
funcion(5, 4, "Hola")
"""


#Se solicita una función para que dado el ingreso de un elemento, se solicite tipo: Bolsa de plástico, botella PET, envase tetrabrik o chicle, e imprima la cantidad de años que tarda en degradarse.


"""
def degradarse():
	while True:
		inicio = "\tBIENVENIDO A BASURIN\n"
		print(inicio)
		print("\t" + "=" * len(inicio) + "\n")
		menu = input("\tSi desea tirar un residuo ingrese 1, de lo contrario ingrese 0\n")
		if menu == "1":
			tipo = input("\tSeleccione su tipo de residuo:\n1) Bolsa de plástico\n2) Botella PET\n3) Envase Tetrabrik ó\n4) Chicle\n")
			if tipo == "1":
				print("Su basura se degradara en: 150 años")
			elif tipo == "2":
				print("Su basura se degradara en: 1.000 años")
			elif tipo == "3":
				print("Su basura se degradara en: 30 años")
			elif tipo == "4":
				print("Su basura se degradara en: 5 años")
			else:
				print("Ingrese nuevamente")
		elif menu == "0":
			print("\tGracias por usar basurin. Hasta la proxima")
			break
		else:
			print("Ingrese nuevamente")

degradarse()
"""

#Realiza una función llamada relacion(a, b) que a partir de toneladas recicladas de dos ciudades se cumpla lo siguiente:
#Si el primer número es mayor que el segundo, debe devolver el nombre de la ciudad 1.
#Si el primer número es menor que el segundo, debe devolver el nombre de la ciudad 2.
#Si ambos números son iguales, debe devolver el nombre de ambas.
"""
def funcion(a,b):
	if a > b:
		print("\tResistencia\n")
	elif a < b:
		print("\tCorrientes\n")
	else:
		print("\tResistencia y Corrientes\n")


a = int(input("\tIngrese cuantas toneladas recicladas tiene la ciudad de Resistencia\n"))
b = int(input("\tIngrese cuantas toneladas recicladas tiene la ciudad de Corrientes\n"))

funcion(a, b)
"""

#Realiza una función separar(lista) que tome una lista que tenga datos de cantidad de árboles plantados en diferentes ciudades de Argentina durante la cuarentena. Luego la función debe devolver dos listas ordenadas. La primera con las cantidades que superen los 100 y la segunda con el resto.
#Qué cantidad de ciudades han plantado más de 100 árboles durante cuarentena.


"""
def lista():
	ciudades = {}
	while True:
		inicio = input("\tSi desea agregar al diccionario presione 1, si quiere salir 0\n")
		if inicio == "1":
			ciudades[input("\tIngrese el nombre de la ciudad\n")] = int(input("\tIngrese la cantidad de arboles plantados\n"))
		elif inicio == "0":
			print("\tFinalizado")
			break
		else:
			print("\tIngrese nuevamente")
	mayorcien = []
	menorcien = []
	for item in ciudades:
		if ciudades[item] > 100:
			mayorcien.append(item)
		else:
			menorcien.append(item)
	print("Las cantidad de ciudades que plantaron mas de 100 arboles fueron ", len(mayorcien))
	print("Las cantidad de ciudades que plantaron menos o 100 arboles fueron ", len(menorcien))
	print(ciudades)

lista()
"""

#Escriba una función que tome las longitudes de los dos lados más cortos de un triángulo rectángulo como sus parámetros y devuelva la hipotenusa del triángulo, calculada usando el teorema de Pitágoras, como resultado de la función. Incluya un programa principal que lea las longitudes de los lados más cortos de un triángulo rectángulo del usuario, use su función para calcular la longitud de la hipotenusa y muestre el resultado.

