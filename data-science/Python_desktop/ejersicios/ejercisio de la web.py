#escriba un algoritmo que sume los números ingresados por el usuario y cuando la suma sea superior a 100 deje de pedir números y muestre el total.

while True:
	try:
		suma = 0
		numero = (int(input("Ingrese un número: ")))
	except ValueError:
		print("Debe ingresar caracteres numericos")
	
	while True:
		try:
			suma=suma+numero		
		except NameError:
			print("Error de definicion")

		print("La suma es " + str(suma))

		if suma>=100:
			break 
		
		try:
			numero = (int(input("Ingrese un número: ")))
		except ValueError:
			print("Debe ingresar caracteres numericos")

			numero = (int(input("Ingrese un número: ")))

	print("Se supero o llego al valor de 100. Fin de las sumas.")
	
	

#Testeado XDD
		






	




