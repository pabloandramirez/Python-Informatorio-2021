"""
tamaños = (
	("pequeña", 250),
	("mediana", 300),
	("grande", 350)
	)

tipos = (
	("comun", 0),
	("especial", 50),
	("fugazzeta", 70),
	("anchoas", 100)
	)

print("\tOpciones tamaños: ")

for indice, tamaño in enumerate(tamaños):
	print(indice+1,"->", tamaño[0], "\t: $", tamaño[1])

opcion_tam = int(input("\tElegir tamaño:\n"))

print("\tOpciones tipos: ")

for indice, tipo in enumerate(tipos):
	print(indice+1, "->", tipo[0], "\t: $", tipo[1])

opcion_tipo = int(input("\tElegir tipo:\n"))

tupla_pedido = (tamaños[opcion_tam-1], tipos[opcion_tipo-1])
print("\tPedido: ", tupla_pedido)

print("\tCosto de la pizza: $", tupla_pedido[0][1]+ tupla_pedido[1][1])
"""