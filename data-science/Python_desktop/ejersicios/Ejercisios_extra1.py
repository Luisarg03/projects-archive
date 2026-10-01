#Cual es el numero mas grande

while True:	
		try:
			num1=(int(input("Ingresa un numero:")))
			num2=(int(input("Ingresa otro numero:")))

			if  num1<num2:
				print("El " + str(num2) + " es mayor que el " + str(num1))
			if  num2<num1:
				print("El " + str(num1) + " es mayor que el " + str(num2))

		except ValueError:
			print("Debe ingresar un numero")
		except NameError:
			print("Error")