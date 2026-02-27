import math

print("Los valores se tomaran en centimetros.")
print()

while True:
	def triangulo(cateto1,cateto2):
				
		sumacatetos=cateto1**2+cateto2**2
		hipotenusa=math.sqrt(sumacatetos)
		
		print("La hipotenusa del triangulo es "+ str(hipotenusa))
		print()
			

	try:

		triangulo(
			int(input("Longitud del primer cateto: ")),
			int(input("Longitud del segundo cateto: "))	
				)

	except ValueError:
		print()
		print("Debe ingresar caracteres numericos.")
		print()
