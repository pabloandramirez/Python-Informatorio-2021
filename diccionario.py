"""
alumnos = {
	34898748: "Pablo Ramirez",
	38018792: "Juan Martin Ramirez",
	40128479: "Gonzalo Ramirez"
}

print(alumnos)

alumnos[34898748] = "Andres Ramirez"

print(alumnos)

alumnos[17251259] = "Andres Ramirez"

print(alumnos)
"""
"""
alumnos = dict()

while True:
	bienvenida = "\tBIENVENIDO A LA LISTA DE ALUMNOS\n"
	print(bienvenida)
	print("\t" + "=" * len(bienvenida) + "\n")
	inicio = input("\tPara cargar la lista de alumnos presione 1 y enter, para salir presione 0 y enter\n")
	if inicio == "1":
		nombre = input("\tIngrese el nombre del Alumno\n")
		dni = int(input("\tIngrese el numero de Documento\n"))
		if dni not in alumnos:
			alumnos[dni] = nombre
		else:
			print("\tEste Documento ya esta registrado")
		print(alumnos)
	elif inicio == "0":
		print(alumnos)
		print("\tGracias y hasta pronto")
		break
	else:
		print("\tIngrese nuevamente por favor")
for i, v in alumnos.items():
	print("\tEl DNI es ", i, "y el nombre es ", v)
print(alumnos.items())
"""

"""
def modificar_nombre(un_diccionario):
	x = un_diccionario.copy()
	x["nombre"] = "Nuevo nombre"
	return x

d = {}
d["nombre"] = "Pablo"
d["apellido"] = "Ramirez"

print(modificar_nombre(d))
print(d)
"""
"""
def ingresar_datos():
	nombre = input("\tIngrese el nombre del cliente:\n")
	apellido = input("\tIngrese el apellido del cliente:\n")
	correo = input("\tIngrese el correo del cliente:\n")
	diccionario[dni] = {"nombre": nombre, "apellido": apellido, "correo": correo}

mensaje = "\tBienvenido al sistema de registro de clientes de Synodin\n"
print(mensaje)
print("\t" + "=" * len(mensaje) + "\n")


diccionario = dict()

while True:
	print("\tMENU PRINCIPAL\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Terminar\n")
	opcion = input("")
	if opcion in ["1","2","3"]:
		dni = input("\tIngrese el DNI del cliente:\n")
		if opcion == "1":
			if dni not in diccionario:
				ingresar_datos()
			else:
				mod = input("\tEste DNI ya esta registrado, desea modificarlo? S o N\n")
				while True:
					if mod.lower() == "s":
						ingresar_datos()
						break
					elif mod.lower() == "n":
						print("\tCliente sin modificar")
						break
					else:
						print("\tOpcion incorrecta, ingrese nuevamente")
			print(diccionario)
			print(diccionario[dni])
		elif opcion == "2" or opcion == "3":
			if dni in diccionario:
				if opcion == "2":
					del diccionario[dni]
				else:
					print(f"\tEl DNI {dni} es del cliente de nombre {diccionario[dni]['nombre']}, apellido {diccionario[dni]['apellido']} y correo {diccionario[dni]['correo']}")
			else:
				print("\tEl DNI ingresado no existe\n")
	elif opcion == "4":
		print(f"\tEl diccionario es {diccionario}")
		break
	else:
		print("\tOpcion incorrecta, ingrese nuevamente")
"""


"""
diccionario = {34898748: {"nombre" : "Pablo", "apellido": "ramirez"}}

print(diccionario[34898748]["nombre"])
"""