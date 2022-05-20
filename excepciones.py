"""
while True:
	try:
		n = int(input("\tIngrese un numero para dividir por 2:\n"))
		division = n / 2
		print(division)
		break
	except Exception as e:
		print("\tHa ocurrido un error =>", type(e).__name__)
"""
"""
while True:
	try:
		n = int(input("\tIngrese un numero para ser dividido por 5:\n"))
		division = 5 / n
		print(division)
		break
	except TypeError:
		print("\tNo se puede dividir el número entre una cadena")
	except ValueError:
		print("\tDebes introducir una cadena que sea un número")
	except ZeroDivisionError:
		print("\tNo se puede dividir por cero, prueba otro número")
	except Exception as e:
		print("\tHa ocurrido un error =>", type(e).__name__)
"""
"""
def mi_funcion(algo=None):
	try:
		if algo is None:
			raise ValueError("\tError! No se permite un valor nulo")
	except ValueError:
			print("\tError! No se permite un valor nulo (desde la excepción)")

mi_funcion()
"""

