#Crea una variable numérica y si esta entre 0 y 10, mostrar un mensaje indicándolo.
#Añadir al anterior ejercicio, que si esta entre 11 y 20, muestre otro mensaje diferente y si esta entre 21 y 30 otro mensaje.


while True:
	while True:
		try:
			num=(float(input("Ingresa un numero:")))

			break

		except ValueError:
			print()
			print("Valores introducidos incorrectos. Ingrese valores numericos.")

	if num>0 and num<=10:

		print("El " + str(num) + " esta entre el 0 y el 10.")

	elif num>=11 and num<=20:
		
		print("El " + str(num) + " esta entre el 11 y el 20.")

	elif num>=21 and num<=30:
		
		print("El " + str(num) + " esta entre el 21 y el 30.")

	else:
		print("El " + str(num) + " no esta contemplado.")
