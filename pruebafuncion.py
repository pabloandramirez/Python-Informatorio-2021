def indeterminados(**kwargs):
	for kwarg in kwargs:
		print(kwarg, "=>", kwargs[kwarg])

indeterminados(n = 5, c = "Hola", l = [1,2,3,4,5])