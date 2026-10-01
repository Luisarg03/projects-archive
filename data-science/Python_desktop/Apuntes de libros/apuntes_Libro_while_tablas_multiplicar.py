while True:
	def Multiplicacion(n):
		i=1
		while i<=10:		
			resultado=n*i
			print(i,"x",n,"=",resultado, end="")
			print()
			i=i+1

	try:		
		Multiplicacion(
			int(input("Ingrese un numero para saber la tabla: "))
			)
	except ValueError:
		print()
		print("Debe ingresar caracteres numericos por favor.")
		print()
