import math #si voy a usar una clase la importo!!!

numero=int(input("ingresa un numero:"))

intento=1

while numero<0:
	print("El numero ingresado debe ser mayor a cero.")

	if numero<0:

		intento=intento+1

	numero=int(input("ingresa un numero:"))

	if intento==3:

		print("Has realizado demasiados intentos.")
		break;

if intento<3:
	
	solucion=math.sqrt(numero) #introduccion a la clase math, sqrt (raiz cuadrada)

	print("La raiz cuadrada de " + str(numero) + " es "  + str(solucion))

