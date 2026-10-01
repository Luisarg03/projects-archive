
while True:
	def division():
		try: #el try tiene que tener except o finally si o si
			num1=(float(input("introduce el primer numero:")))
			num2=(float(input("introduce el segundo numero:")))

			print("El resultado de la division es "+ str(num1/num2))

		except ZeroDivisionError:
			print("No se puede dividir un numero por cero.")

		except ValueError: #puedo "anidar" varias excepciones a la vez
			print("No se pueden ingresar caracteres que no sean del tipo numerico.")

		finally: #con finally la instruccion siempre!, siempre! se va a ejecutar
			print("fin de la operacion")

	division()