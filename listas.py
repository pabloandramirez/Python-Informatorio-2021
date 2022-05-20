"""
numeros = [1, 1, 2, 3, 4, 5]
print(numeros.count(5))
"""
"""
def menu():
	print("\tMENU")
	print("\tOpcion A")
	print("\tOpcion B")
	print("\tOpcion C")
	print("\tOpcion D")
	print("\tOpcion E")
	print("\tIngrese otra letra para salir\n")
	return input()


def A(lista_numeros):
	numero = int(input("\tIngrese un número, si quiere finalizar ingrese 0\n"))
	while numero != 0:
		lista_numeros.append(numero)
		numero = int(input("\tIngrese un número, si quiere finalizar ingrese 0\n"))
	return lista_numeros

def B(lista_numeros):
	numero = int(input("\tIngrese un número a borrar, si quiere finalizar ingrese 0\n"))
	while numero != 0:
		if numero in lista_numeros:
			lista_numeros.remove(numero)
			break
		else:
			print("\tNo se puede eliminar ya que no se encuentra\n")
			break
	return lista_numeros

def C(lista_numeros):
	suma = 0
	for i in lista_numeros:
		suma += i
	print("\tLa suma es: ", suma)

def D(lista_numeros):
	nuevo_numero = int(input("\tIngrese un numero\n"))
	nueva_lista = []
	for i in lista_numeros:
		if i < nuevo_numero:
			nueva_lista.append(i)
	for i in nueva_lista:
		print(i, end= " ")

def E(lista_numeros):
	nueva_lista = list()
	for i in lista_numeros:
		tupla = (i,lista_numeros.count(i))
		if tupla not in nueva_lista:
			nueva_lista.append(tupla)
	print(nueva_lista)

numeros = list()
while True:
	op = menu()
	if op.lower() == "a":
		numeros = A(numeros)
	elif op.lower() == "b":
		numeros = B(numeros)
	elif op.lower() == "c":
		C(numeros)
	elif op.lower() == "d":
		D(numeros)
	elif op.lower() == "e":
		E(numeros)
	else:
		break
	print("\tLa lista quedo: ", numeros)
"""
"""
clientes = [1, 2, 3, 4, 4, 4, 5, 1, 5, 4]

regalos = ["regalo 1", "regalo 2", "regalo 3"]

clientes_sin_repetir = []

for i in clientes:
	if i not in clientes_sin_repetir:
		clientes_sin_repetir.append(i)
clientes_sin_repetir.sort()

for i in clientes_sin_repetir:
	regalo = 0
	cantidad_regalos = clientes.count(i)
	print("Cliente " , i)
	while (regalo <= cantidad_regalos - 1) and (regalo < len(regalos)):
		print("Regalo: "+ regalos[regalo])
		regalo += 1
"""
"""
verduras = ["papa", "cebolla", "rucula", "batata", "lechuga"]
print(f"Esta es la primera posicion: {verduras[-2]}")
"""
"""
palabra = input("\tFavor de ingresar la palabra:\n")
vocales = ["a", "e", "i", "o", "u"]

for vocal in vocales:
	cantidad = 0
	for letra in palabra:
		if letra.lower() == vocal:
			cantidad += 1
	print(f"\tLa vocal {vocal} aparece ", cantidad, " veces")
"""

"""
while True:
	numero_palabras = int(input("\tIngrese la cantidad de palabras que quiere agregar\n"))
	if numero_palabras < 2:
		print("\tDebe ingresar mas de una palabra!!!")
		continue
	else:
		lista = []
		for i in range(numero_palabras):
			print("\tIngrese la palabra ", (i+1))
			palabra = input()
			lista.append(palabra)
		print("\tLa lista creada es ", lista)
		pass
	buscar = input("\tLa palabra a buscar es:\n")
	reemplazar = input("\tLa palabra a reemplazar es:\n")
	for i in range(len(lista)):
		if buscar.lower() == lista[i].lower():
			lista[i] = reemplazar
	print("\tLa nueva lista es: ", lista)
	break
"""
"""
lista = list()

while True:
	ingresar = input("\tIngrese un numero para la lista, ingrese 0 para salir:\n")
	if ingresar.isdigit() and ingresar != "0":
		ingresar = int(ingresar) **2
		lista.append(ingresar)
	elif ingresar == "0":
		print("\tFIN")
		break
	else:
		print("\tDebe ingresar un numero")

print("\tLa lista final es: ", lista)
"""
"""
lista = list()

while True:
	ingresar = input("\tIngrese un numero para la lista, ingrese Exit para salir:\n")
	if ingresar.lstrip("-").isdigit() and ingresar.lower() != "exit":
		ingresar = int(ingresar)
		if ingresar < 0:
			ingresar = 0
			lista.append(ingresar)
		else:
			lista.append(ingresar)
	elif ingresar.lower() == "exit":
		print("\tFIN")
		break
	else:
		print("\tDebe ingresar un numero")

print(f"\tLa lista es {lista}")
"""
"""
numero = 6

lista = list()

while True:
	ingresar = input("\tIngrese un numero para la lista, ingrese Exit para salir:\n")
	if ingresar.lstrip("-").isdigit() and ingresar.lower() != "exit":
			ingresar = int(ingresar)
			lista.append(ingresar)
	elif ingresar.lower() == "exit":
		print("\tFIN")
		break
	else:
		print("\tDebe ingresar un numero")


print(f"\tLa lista antes del filtro: {lista}")

for i in lista.copy():
	if i == numero:
		lista.remove(i)

print(f"\tLa lista despues del filtro: {lista}")
"""

"""
lista1 = [9,7,5,3,1]
lista2 = [10,8,6,4,2]

lista1.extend(lista2)
lista1.sort()

print(lista1)
"""
"""
lista = [11,25,57,89,47]
suma = 0

for i in reversed(lista):
	if lista.index(i) % 2:
		print(i)
		pass
	else:
		suma = suma + i

print(f"La suma es {suma}")
"""

"""
lista = [154, 159, 165, 847, 854, 892, 974, 356, 354, 254, 258, 251, 237, 871, 874]

nueva_lista = list()

for i in lista:
	if i % 2:
		pass
	else:
		nueva_lista.append(i*2)

print(nueva_lista)
"""

