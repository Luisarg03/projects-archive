import math

while True:
	def distancia(x1,x2,y1,y2):
		
		calculo1=x2-x1
		calculo2=y2-y1
		#cuadrado1=calculo1**2
		#cuadrado2=calculo2**2
		cuadrado=calculo1**2+calculo2**2
		resultado=math.sqrt(cuadrado)

		print("El resultado de la distancia es: " + str(resultado))
		print()
		
	try:
		distancia(
			float(input("ingresa el valor para x1: ")),
			float(input("ingresa el valor para x2: ")),
			float(input("ingresa el valor para y1: ")),
			float(input("ingresa el valor para y2: "))
			)
	except ValueError:
		print()
		print("Debe ingresar caracteres numericos.")
		print()