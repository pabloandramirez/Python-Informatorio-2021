from POO import Almacen, AguaMineral, Gaseosa

a = Almacen()

x = AguaMineral(id=1, can_litros=2, marca="unaMarca", precio=12.3, origen="Manantial")
a.agregar_bebida(x)

y  = AguaMineral(id=2, can_litros=2, marca="otraMarca", precio=12.3, origen="Manantial")
a.agregar_bebida(y)


z = Gaseosa(id= 3, can_litros=1, marca="Marca X", precio=10, p_azucar=40, tiene_descuento=False)
a.agregar_bebida(z)

#print(a.obtener_total(marca = "Marca X"))

print(a.ver_info())