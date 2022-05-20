"""
clientes = [
	{"Nombre": "Hector", "Apellidos": "Costa Guzman", "DNI": "111111111A"},
	{"Nombre": "Juan", "Apellidos": "Gonzalez Marquez", "DNI": "2222222B"}
]

def mostrar_clientes (clientes, dni):
	for c in clientes:
		if (dni == c["DNI"]):
			print("\t{} {}".format(c["Nombre"],c["Apellidos"]))
			return
	print("\tCliente no encontrado")

def borrar_cliente(clientes, dni):
	for i,c in enumerate(clientes):
		if (dni == c["DNI"]):
			del (clientes[i])
			print(str(c), "> BORRADO")
			return
	print("\tCliente no encontrado")

borrar_cliente(clientes, "111111111A")
"""


"""
class Cliente:

	def __init__(self, dni, nombre, apellidos):
		self.dni = dni
		self.nombre = nombre
		self.apellidos = apellidos

	def __str__(self):
		return "{} {}".format(self.nombre, self.apellidos)

class Empresa:

	def __init__(self, clientes=[]):
		self.clientes = clientes

	def mostrar_clientes(self, dni=None):
		for c in self.clientes:
			if c.dni == dni:
				print("\t",c)
				return
		print("\tCliente no encontrado")

	def borrar_cliente (self, dni=None):
		for i, c in enumerate(self.clientes):
			if c.dni == dni:
				del (self.clientes[i])
				print(str(c),"> BORRADO")
				return
		print("\tCliente no encontrado")

	def __str__(self):
		lista_clientes = ", ".join(str(cliente) for cliente in self.clientes)
		return "Clientes: {}".format(lista_clientes)

	def mostrar_lista(self):
		return self.clientes

hector = Cliente(nombre = "Hector", apellidos = "Costa Guzman", dni = "11111a")
juan = Cliente("22222b", "Juan", "Gonzalez Marquez")

empresa = Empresa(clientes=[hector, juan])

print("\n==LISTADO DE CLIENTES==")
print(empresa)

print("\n==MOSTRAR CLIENTES POR DNI==")
empresa.mostrar_clientes("11111a")
empresa.mostrar_clientes("11111z")

print("\n==BORRAR CLIENTES POR DNI==")
empresa.borrar_cliente("22222v")
empresa.borrar_cliente("22222b")

print("\n==LISTADO DE CLIENTES==")
print(empresa)

"""



"""
class Producto:
	def __init__(self, referencia, tipo, nombre, pvp, descripción, productor=None, distribuidor = None, isbn=None, autor= None):
		self.referencia = referencia
		self.tipo = tipo
		self.nombre = nombre
		self.pvp = pvp
		self.descripción = descripción
		self.productor = productor
		self.distribuidor = distribuidor
		self.isbn = isbn
		self.autor = autor

adorno = Producto("000A", "ADORNO", "Vaso Adornado", 15, "Vaso de porcelana con dibujos")

print(adorno)
print(adorno.tipo)
"""




"""
class Producto:
	def __init__(self, referencia, nombre, pvp, descripcion):
		self.referencia = referencia
		self.nombre = nombre
		self.pvp = pvp
		self.descripcion = descripcion

	def __str__(self):
		return f"REFERENCIA\t {self.referencia}\n" f"NOMBE\t\t {self.nombre}\n" f"PVP\t\t {self.pvp}\n" f"DESCRIPCIÓN\t {self.descripcion}\n"
class Adorno(Producto):
	pass

adorno = Adorno(2034, "Vaso adornado", 15, "Vaso de porcelana")
print(adorno)

class Alimento(Producto):
	productor =  ""
	distribuidor = ""

	def __str__(self):
		return f"REFERENCIA\t {self.referencia}\n" f"NOMBRE\t\t {self.nombre}\n" f"PVP\t\t {self.pvp}\n" f"DESCRIPCIÓN\t {self.descripcion}\n" f"PRODUCTOR\t\t {self.productor}\n" f"DISTRIBUIDOR\t\t {self.distribuidor}\n"

class Libro(Producto):
	isbn = ""
	autor = ""

	def __str__(self):
		return f"REFERENCIA\t {self.referencia}\n" f"NOMBRE\t\t {self.nombre}\n" f"PVP\t\t {self.pvp}\n" f"DESCRIPCIÓN\t {self.descripcion}\n" f"ISBN\t\t {self.isbn}\n" f"AUTOR\t\t {self.autor}\n"

alimento = Alimento(2035, "Botella de Aceite de Oliva", 5, "250 ml")
alimento.productor = "La Aceitera"
alimento.distribuidor = "Distribuciones SA"
print(alimento)

libro = Libro(2036, "Cocina Mediterranea", 9, "Recetas sanas y buenas")
libro.isbn = "0-123456-78-9"
libro.autor = "Doña Juana"
print(libro)

productos = [adorno, alimento]
productos.append(libro)

print(productos)

for producto in productos:
	print(producto, "\n")

for producto in productos:
	print(producto.referencia, producto.nombre)

for producto in productos:
	if (isinstance (producto, Adorno)):
		print (producto.referencia, producto.nombre)
	elif (isinstance (producto, Alimento)):
		print(producto.referencia, producto.nombre, producto.productor)
	elif (isinstance (producto, Libro)):
		print(producto.referencia, producto.nombre, producto.isbn)
print("============================")
def rebajar_producto(producto, rebaja):
	producto.pvp = producto.pvp - (producto.pvp/100 * rebaja)

print(alimento, "\n")
rebajar_producto(alimento, 10)
print(alimento)
"""


"""
class Figura:
	def __init__(self, area):
		self.area = area

	def retornar_area(self):
		print("\tEl área de la figura es: ", self.area)

class Poligono(Figura):
	def __init__(self, lados, area):
		Figura.__init__(self, area)
		self.lados = lados

	def retornar_lados(self):
		print("\tLos lados del polígono son: ", self.lados)

class Cuadrilatero(Poligono):
	def __init__(self, area):
		Poligono.__init__(self, 4, area)

figura = Figura(4)
print(figura.retornar_area())
#poligono = Poligono(5, 4)
#print(poligono.retornar_lados())
#cuadrilatero = Cuadrilatero(8)
#print(cuadrilatero)
"""


"""
class Persona:
	def inicializar(self, nom):
		self.nom = nom

	def mostrar(self):
		print("Nombre: ", self.nom)

persona1 = Persona()
persona1.inicializar("Marcos")
persona1.mostrar()

persona2 = Persona()
persona2.inicializar("Ivan")
persona2.mostrar()
"""


"""
class Vehiculo():
	def __init__(self, color, ruedas):
		self.color = color
		self.ruedas = ruedas

	def __str__(self):
		return "color {}, {} ruedas".format(self.color, self.ruedas)

class Coche(Vehiculo):
	def __init__(self, color, ruedas, velocidad, cilindrada):
		Vehiculo.__init__(self, color, ruedas)
		self.velocidad = velocidad
		self.cilindrada = cilindrada

	def __str__(self):
		return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

c = Coche("azul", 4, 150, 1200)
print(c)
"""

#Aplicando superclase


"""
class Vehiculo():
	def __init__(self, color, ruedas):
		self.color = color
		self.ruedas = ruedas

	def __str__(self):
		return "color {}, {} ruedas".format(self.color, self.ruedas)

class Coche(Vehiculo):
	def __init__(self, color, ruedas, velocidad, cilindrada):
		super().__init__(color, ruedas)
		self.velocidad = velocidad
		self.cilindrada = cilindrada

	def __str__(self):
		return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

c = Coche("azul", 4, 150, 1200)
print(c)
"""


"""
class Alumno:
	nombre = None

	def __init__(self, nombre):
		self.nombre = nombre

	def decir_mi_nombre(self):
		return f"Mi nombre es {self.nombre}"

x = Alumno("Juan")

y = Alumno("Pedro")


print(x.decir_mi_nombre())
print(y.decir_mi_nombre())
"""



"""
class Vehiculo():

	def __init__(self, color, ruedas):
		self.color = color
		self.ruedas = ruedas

	def mostrar_color(self):
		print(f"Mi color es {self.color}")

	def mostrar_ruedas (self):
		print(f"Mi vehiculo tiene {self.ruedas} ruedas")


class Coche(Vehiculo):

	def __init__(self, color, ruedas, velocidad, cc):
		super().__init__(color, ruedas)
		self.velocidad = velocidad
		self.cc = cc

	def mostrar_velocidad(self):
		print(f"La velocidad es {self.velocidad} km/h")

	def mostrar_cc(self):
		print(f"La cilindrada es de {self.cc} cc")


color = input("\tCual es el color del vehiculo?\n")
ruedas = input("\tCuantas ruedas tiene?\n")
velocidad = input("\tCual es la velocidad maxima?\n")
cc = input("\tCual es la cilindrada?\n")

auto = Coche(color, ruedas, velocidad, cc)
auto.mostrar_color()
auto.mostrar_ruedas()
auto.mostrar_velocidad()
auto.mostrar_cc()
"""



"""
class Persona:
	def __init__(self, nombre="Pablo", apellido="Ramirez"):
		if nombre.isalpha() and apellido.isalpha():
			self.nombre = nombre
			self.apellido = apellido
		else:
			raise Exception("Nombre no valido")

persona1 = Persona("Juan", "Perez")

print(persona1.apellido)

persona2 = Persona()
print(persona2.apellido)

persona3 = Persona("Sandra","Gomez")
print(persona3.apellido)

persona4 = Persona("$andra", "#aafo")
print(persona4.apellido)
"""

"""
class Almacen:
	
	def __init__(self):
		self.lista_bebidas = []

	def agregar_bebida(self, bebida):
		test = isinstance(bebida, AguaMineral) or isinstance(bebida, Gaseosa)
		
		if not test:
			raise Exception("\tTipo de dato no permitido")

		for b in self.lista_bebidas:
			if b.id == bebida.id:
				raise Exception("\tID existente")
		self.lista_bebidas.append(bebida)

	def obtener_total(self, marca=None):
		total = 0
		if marca is None:
			for b in self.lista_bebidas:
				total += b.get_precio()
		else:
			for b in self.lista_bebidas:
				if b.marca == marca:
					total += b.get_precio()
		return total

	def eliminar_producto(self, id):
		for b in self.lista_bebidas:
			if b.id == id:
				self.lista_bebidas.remove(b)

	def ver_info(self):
		for b in self.lista_bebidas:
			b.ver_info()



class Bebida:
	
	def __init__(self, id, can_litros, marca, precio):
		self.id = id
		self.can_litros = can_litros
		self.marca = marca
		self.precio= precio

	def get_precio(self):
		return self.precio

	def ver_info(self):
		print("ID: %s" % (self.id))
		print("CANTIDAD DE LITROS: %s" % (self.can_litros))
		print("MARCA: %s" % (self.marca))
		print("PRECIO: %s" % (self.precio))

class AguaMineral(Bebida):
	
	def __init__(self, id, can_litros, marca, precio, origen):
		super().__init__(id, can_litros, marca, precio)
		self.origen = origen

	def ver_info(self):
		super().ver_info()
		print("ORIGEN: %s" % (self.origen))

class Gaseosa(Bebida):
	
	def __init__(self, id, can_litros, marca, precio, p_azucar, tiene_descuento):
		super().__init__(id, can_litros, marca, precio)
		self.p_azucar = p_azucar
		self.tiene_descuento = tiene_descuento
		self.descuento = 0.1

	def get_precio(self):
		if self.tiene_descuento:
			return self.precio * (1 - self.descuento)
		return self.precio

	def ver_info(self):
		super().ver_info()
		print("PORCENTAJE DE AZUCAR: %s " % (self.p_azucar))
		print("TIENE DESCUENTO: %s " % ("Si" if self.tiene_descuento else "No"))
		print("DESCUENTO: %s " % (self.descuento))
"""

"""
import random
import time

class Game:
	def __init__(self):
		self.secuencia_puntos = [0, 15, 30, 40]
		self.puntos_j1 = 0
		self.puntos_j2 = 0

		self.deuce = False
		self.ganador = None

	def ganador_punto(self):
		return random.randint(1, 2)

	def jugar_game(self):
		ganador = self.ganador_punto()
		print("Punto ganado por Jugador %s" % ganador)

		puntos_antes_del_game = getattr(self, "puntos_j"+str(ganador))

		if self.deuce:
			if self.puntos_j1 > self.puntos_j2 and ganador==1:
				setattr(self, "puntos_j"+str(ganador), puntos_antes_del_game+1)
				print("GANO EL JUGADOR 1")
			elif self.puntos_j1 > self.puntos_j2 and ganador==2:
				self.puntos_j1 = self.puntos_j1 - 1
			elif self.puntos_j2 > self.puntos_j1 and ganador==2:
				setattr(self, "puntos_j"+str(ganador), puntos_antes_del_game+1)
				print("GANO EL JUGADOR 2")
			elif self.puntos_j2 > self.puntos_j1 and ganador==1:
				self.puntos_j2 = self.puntos_j2 - 1
			else:
				setattr(self, "puntos_j"+str(ganador), puntos_antes_del_game + 1)
		else:
			setattr(self, "puntos_j"+str(ganador), puntos_antes_del_game+1)

		self.check_deuce()

	def check_deuce(self):
		if not self.deuce and (self.puntos_j1 == self.puntos_j2 == len(self.secuencia_puntos)-1):
			self.deuce = True

	def fin(self):
		es_fin = False

		x = (self.puntos_j1 > self.puntos_j2 and self.puntos_j1 == len(self.secuencia_puntos)) or (self.puntos_j2> self.puntos_j1 and self.puntos_j2== len(self.secuencia_puntos))

		if not self.deuce and (x):
			es_fin = True

		if self.deuce and ( (self.puntos_j1 > self.puntos_j2 and self.puntos_j1 == len(self.secuencia_puntos)+1) or (self. puntos_j2 > self.puntos_j1 and self.puntos_j2 == len(self.secuencia_puntos)+1)):
			es_fin = True

		if es_fin:
			if self.puntos_j1 > self.puntos_j2:
				self.ganador = 1
			else:
				self.ganador = 2
		return self.ganador
		print("El ganador del game es el Jugador %s" % (self.ganador))
		

	def ver_puntuacion(self):
		if self.deuce and self.puntos_j1 > self.puntos_j2:
			ptos_j1 = "VENTAJA JUGADOR 1"
		elif self.puntos_j1 < len(self.secuencia_puntos) - 1:
			ptos_j1 = self.secuencia_puntos[self.puntos_j1]
		else:
			ptos_j1 = self.secuencia_puntos[len(self.secuencia_puntos)-1]

		if self.deuce and self.puntos_j2 > self.puntos_j1:
			ptos_j2 = "VENTAJA JUGADOR 2"
		elif self.puntos_j2 < len(self.secuencia_puntos) - 1:
			ptos_j2 = self.secuencia_puntos[self.puntos_j2]
		else:
			ptos_j2 = self.secuencia_puntos[len(self.secuencia_puntos)-1]
		print("===================")
		print("JUGADOR 1 |  %s  " % (ptos_j1))
		print("JUGADOR 2 |  %s  " % (ptos_j2))
		print("===================")

class Set():
	def __init__(self, can_games=3):
		self.puntos_j1 = 0
		self.puntos_j2 = 0

		self.can_games = can_games
		self.games = []
		self.game_actual = 0

		self.ganador = None

	def jugar_set(self):
		nuevo_game = Game()
		self.game_actual += 1
		while not nuevo_game.fin():

			nuevo_game.jugar_game()
			nuevo_game.ver_puntuacion()

			time.sleep(2)

		setattr(self, "puntos_j"+str(nuevo_game.ganador), getattr(self,"puntos_j"+str(nuevo_game.ganador))+1)

		self.games.append(nuevo_game)

	def ver_puntuacion(self):
		print("===================")
		print("JUGADOR 1: %s" % (self.puntos_j1))
		print("JUGADOR 2: %s" % (self.puntos_j2))
		print("===================")

	def fin(self):
		es_fin = False
		if self.game_actual >= self.can_games:
			if self.puntos_j1 > self.puntos_j2:
				es_fin = True
				self.ganador = 1
			elif self.puntos_j2 > self.puntos_j1:
				es_fin = True
				self.ganador = 2

		return es_fin


class Partido():
	def __init__(self, sets=1, games=3):
		self.puntos_j1 = 0
		self.puntos_j2 = 0

		self.games = games

		self.can_sets = sets

		self.sets = []

		self.ganador = None
		self.set_actual = 0

	def ver_puntuacion(self):
		print("========= SET %s ==========" % (self.set_actual))
		print("JUGADOR 1: %s" % (self.puntos_j1))
		print("JUGADOR 2: %s" % (self.puntos_j2))
		print("===================")

	def jugar(self):
		for nro_set in range(1, self.can_sets + 1):
			self.set_actual = nro_set
			nuevo_set = Set(can_games = self.games)
			while not nuevo_set.fin():
				nuevo_set.jugar_set()
				nuevo_set.ver_puntuacion()
				time.sleep(2)

			if nuevo_set.ganador == 1:
				self.puntos_j1 += 1
			else:
				self.puntos_j2 += 1

			self.ver_puntuacion()
		self.sets.append(nuevo_set)

		if self.puntos_j1 > self.puntos_j2:
			self.ganador = 1
		else:
			self.ganador = 2


p = Partido()

p.jugar()

print("FIN DEL JUEGO")
print("GANADOR")
print("JUGADOR " + str(p.ganador))
"""
"""
class Triangulo():
	def __init__(self, lado1, lado2, lado3):
		self.lado1 = lado1
		self.lado2 = lado2
		self.lado3 = lado3

	def __str__(self):
		return "El lado mas grande vale: {}".format(max(self.lado1, self.lado2, self.lado3))

	def tipo(self):
		if self.lado1==self.lado2==self.lado3:
			print("Equilatero")
		elif self.lado1==self.lado2 or self.lado1==self.lado3 or self.lado2==self.lado3:
			print("Isosceles")
		else:
			print("Escaleno")

triangulo = Triangulo(7, 6, 7)
print(triangulo)
triangulo.tipo()
"""
"""
agenda = {}


class Admin():

	def __init__(self, dni, nombre, telefono, email):
		self.dni = dni
		self.nombre = nombre
		self.telefono = telefono
		self.email = email


	def agregar(self):
		global agenda
		agenda[self.dni] = [self.nombre, self.telefono, self.email]

	def __str__(self):
		return "El menu"


contacto = Admin("34898748", "Pablo", "3794028414", "pablo.and")
print(contacto)
contacto.agregar()
print(agenda)
"""
"""
class Tiempo():

	def __init__(self, horas, minutos = None, segundos = None):
		self.horas = horas
		self.minutos = minutos
		self.segundos = segundos

	def __str__(self):
		if self.minutos == self.segundos == None:
			return "{} horas".format(self.horas)
		elif self.minutos != None and self.segundos == None:
			return "{} horas {} minutos".format(self.horas, self.minutos)
		else:
			return "{} horas {} minutos {} segundos".format(self.horas, self.minutos, self.segundos)


tiempo = Tiempo(10, 5, 59)
print(tiempo)
"""
"""
class Productos():

	def __init__(self, nombre, cantidad, entidades):
		self.nombre = nombre
		self.cantidad = cantidad
		self.entidades = entidades

	def Calcular(self):
		test = isinstance(producto, Alimento_Perecedero)
		cantidad_entidad = int(self.cantidad/self.entidades)
		if test:
			if self.dias_caducidad < 10:
				print("El producto se entregará el dia actual")
			else:
				print("El producto puede entregarse hasta una semana despues de la fecha actual")
		else:
			print(f"Se entregaran {cantidad_entidad} unidades por entidad y se pueden entregar hasta un mes a partir de la fecha actual")
		print(f"Se entregaran {cantidad_entidad} unidades para cada entidad")
		if (self.cantidad % self.entidades) != 0:
			print(f"Se reservara {self.cantidad % self.entidades} unidades para la proxima donacion")


class Alimento_Perecedero(Productos):

	def __init__(self, nombre, cantidad, entidades, dias_caducidad):
		super().__init__(nombre, cantidad, entidades)
		self.dias_caducidad = dias_caducidad

class Alimento_No_Perecedero(Productos):

	def __init__(self, nombre, cantidad, entidades, tipo):
		super().__init__(nombre, cantidad, entidades)
		self.tipo = tipo


producto = Alimento_No_Perecedero("Sal", 200, 14, "Despensa")
producto.Calcular()
"""
"""
dicconario = dict()


class Cuenta():

	
	def __init__(self, titular, cantidad = None):
		self.titular = titular
		self.cantidad = cantidad
		global dicconario
		if self.titular not in dicconario:
			dicconario[self.titular] = self.cantidad

	def mostrar(self):
		global dicconario
		print(f"El/La titular {self.titular} de la cuenta posee ${dicconario[self.titular]} pesos argentinos")

	def ingresar(self, cantidad):
		if cantidad < 0:
			cantidad = 0
		global dicconario
		dicconario[self.titular] += cantidad

	def retirar(self, cantidad):
		global dicconario
		dicconario[self.titular] -= cantidad

pablo = Cuenta("Pablo", 0)
roberto = Cuenta("Roberto", 0)
pablo.mostrar()
pablo.ingresar(187.8)
pablo.mostrar()
pablo.ingresar(187.8)
pablo.mostrar()
roberto.mostrar()
roberto.retirar(525.8)
roberto.mostrar()
roberto.ingresar(610)
roberto.mostrar()
"""

class Libro():

	def __init__(self, titulo, autor, num_paginas, calificacion):
		self.titulo = titulo
		self.autor = autor
		self.num_paginas = num_paginas
		self.calificacion = calificacion
		
	def __str__(self):
		return "El libro se llama {}, su autor es {}, tiene {} numero de páginas, y yo lo valoro con un {} ".format(self.titulo, self.autor, self.num_paginas, self.calificacion)

	def modificar(self, titulo):
		self.autor = input("Favor corrija el nombre del autor:\n")
		self.num_paginas = input("Cuantas páginas tiene el libro:\n")
		self.calificacion = input("Cual es la nueva calificacion:\n")


class Biblioteca():

	def __init__(self):
		self.biblioteca = dict()

	def aniadir_libro(self, libro):
		self.biblioteca[libro.titulo] = {"Autor": libro.autor, "Paginas": libro.num_paginas, "Calificacion": libro.calificacion}

	def eliminar_libro(self, titulo=None, autor=None):
		if titulo == None:
			for i in biblioteca:
				try:
				 	i.pop(autor)
				except Exception as e:
				 	pass
		else:
			self.biblioteca.pop(self.titulo)

	def mostrar_libro(self, titulo):
		print("El libro {} tiene los siguientes datos:\nAutor:\t{}\nPáginas:\t{}\nCalificacion:\t{}\n".format(titulo, biblioteca[titulo["Autor"]], titulo[libro["Paginas"]], titulo[libro["Calificacion"]]))

	def mostrar_todo(self):
		for lib in self.biblioteca.keys():
			print(f"El libro {lib}")


biblioteca = Biblioteca()

while True:
	print("\tLA BIBLIOTECA DEL TIO COSA\n")
	inicio = input("Si quiere agregar un libro presione 1\nSi quiere mostrar los datos de un libro presione 2\nSi quiere modificar un libro presione 3\nSi quiere eliminar algun libro presione 4\nSi quiere mostrar los mejores o peores puntuados libros presione 5\nSi quiere mostrar toda la biblioteca presione 6\nPresione cualquier tecla para salir\n")
	if inicio == "1":
		titulo = input("Cual es el titulo del libro:\n")
		autor = input("Cual es el autor del libro:\n")
		num_paginas = input("Cuantas paginas tiene:\n")
		calificacion = input("Cual es tu calificacion:\n")
		libro = Libro(titulo, autor, num_paginas, calificacion)
		biblioteca.aniadir_libro(libro)
	elif inicio == "2":
		titulo = input("Cual es el titulo del libro que desea mostrar:\n")
		biblioteca.mostrar_libro(titulo)

	elif inicio == "6":
		biblioteca.mostrar_todo()

		