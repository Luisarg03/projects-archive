import math

def raiz_cuadrada(num):

	if num<0:
		raise ValueError("Debe usar numeros positivos")
	else:	
		return math.sqrt(num)
try:
	op=(float(input("Ingrese un numero:")))

except ValueError as ErrorDeCaracteres:
	print("Debe ingresar caracteres numericos.")

try:
	print(raiz_cuadrada(op))
except NameError as ErrorDeCaracteres:
	print("Error")
except ValueError as ErrorDeNumeroNegativo:
	print("No puede ingresar numero negativos")

	print("Fin del calculo")
	
