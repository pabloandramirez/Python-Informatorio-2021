# Ingresar una edad y que diga si es mayor de edad

edad = int(input("Favor ingresa tu edad: \n"))

if edad >= 18:
	print("Usted es mayor de edad \n")
else:
	print("Usted es menor de edad \n")


# Cantidad de preguntas y cantidad de respuestas correctar para calcular porcentaje de aprobación 

cantidad_preguntas = int(input("Favor de colocar la cantidad de preguntas:\n"))
cantidad_respuestas_correctas = int(input("Favor de colocar la cantidad de respuestas correctas:\n"))
porcentaje_respuestas_correctas  = cantidad_respuestas_correctas*100 / cantidad_preguntas

if porcentaje_respuestas_correctas >= 90:
	print("Excelente\n")
elif porcentaje_respuestas_correctas >= 70:
	print("Bueno\n")
elif porcentaje_respuestas_correctas >= 60:
	print("Aprobado\n")
else:
	print("No alcanzo")
print("El porcentaje de su calificación es ", porcentaje_respuestas_correctas)

#Ingresar la venta de 2 dias, e indicar en que dia se vendio mas o si se vendio igua en los dos

dia_1 = int(input("Indicar cuanto se vendio el dia 1:\n$"))
dia_2 = int(input("Indicar cuanto se vendio el dia 2:\n$"))

if dia_1 > dia_2:
	print("Se vendio más el dia 1 por una diferencia de $", dia_1-dia_2)
elif dia_2 > dia_1:
	print("Se vendio más el dia 2 por una diferencia de $", dia_2-dia_1)
else:
	print("En los dos días se vendio lo mismo\n")


#El cliente debe elegir si desea comer una pizza vegetariana o no, y que ingrediente desea agregar además de la mozzarella y el tomate. Ingredientes vegetarianos: pimiento o rúcula. Ingredientes no vegetariano: panceta o jamón.

print("\tPIZZAS EL NAPOLITANO\t")
elegir_tipo_pizza = int(input("Confirme por favor que tipo de pizza desea:\n1_Vegetariana\nó\n2_No Vegetariana\n"))

if elegir_tipo_pizza == 1:
	elegir_ingrediente = int(input("Además del tomate y la mozzarella que otro ingrediente desea:\n1_Pimiento\nó\n2_Rúcula\n"))
	if elegir_ingrediente == 1:
		confirmar = input("Su pizza elegida es Vegetariana con estos ingredientes:\nTomate\nMozzarella\nPimiento\nDesea confirmar? Si o No\n")
		if confirmar.lower() == "si":
			print("Gracias por su compra")
		else:
			print("Pedido cancelado")
	else:
		confirmar = input("Su pizza elegida es Vegetariana con estos ingredientes:\nTomate\nMozzarella\nRúcula\nDesea confirmar? Si o No\n")
		if confirmar.lower() == "si":
			print("Gracias por su compra")
		else:
			print("Pedido cancelado")
else:
	elegir_ingrediente = int(input("Además del tomate y la mozzarella que otro ingrediente desea:\n1_Panceta\nó\n2_Jamón\n"))
	if elegir_ingrediente == 1:
		confirmar = input("Su pizza elegida NO es Vegetariana con estos ingredientes:\nTomate\nMozzarella\nPanceta\nDesea confirmar? Si o No\n")
		if confirmar.lower() == "si":
			print("Gracias por su compra")
		else:
			print("Pedido cancelado")
	else:
		confirmar = input("Su pizza elegida es NO Vegetariana con estos ingredientes:\nTomate\nMozzarella\nJamón\nDesea confirmar? Si o No\n")
		if confirmar.lower() == "si":
			print("Gracias por su compra")
		else:
			print("Pedido cancelado")


#Estudiantes de un curso se han dividido en dos grupos de A y B de acuerdo al turno y al nombre. El grupo A esta formado por estudiantes del turno tarde con un nombre anterior a la M y estudiantes del turno noche con un nombre posterios a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y turno, y muestre por pantalla el grupo que le corresponde.

nombre = input("Favor de ingresar su nombre:\n")
turno = input("Favor de ingresar su turno:\n")
if turno.capitalize() == "T":
	if nombre.capitalize() < "M":
		print("Usted pertenece al grupo A")
	else:
		print("Usted pertenece al grupo B")
else:
	if nombre.capitalize() > "N":
		print("Usted pertenece al grupo A")
	else:
		print("Usted pertenece al grupo B")
		