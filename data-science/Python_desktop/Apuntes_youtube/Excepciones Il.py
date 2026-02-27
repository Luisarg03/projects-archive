#controlar muchas exepciones a la vez

def suma(num1,num2):
	return num1+num2

def resta(num1,num2):
	return num1-num2

def multiplicacion(num1,num2):
		return num1*num2

def division(num1,num2): #al dividir por cero da el error zerodivisionerror, lo que hace estas lineas es omitir el error y que se siga el programa.
	try:
		return num1/num2

	except ZeroDivisionError:
		print("No se puede dividir entre cero")
		print()
		return "operacion erronea"

while True:	
	while True:
		try:
			variable1=(float(input("Ingresa un numero:")))
			print()
			variable2=(float(input("ingresa otro numero:")))

			break;

		except ValueError:
			print()
			print("Valores introducidos incorrectos. Ingrese valores numericos.")
	
	print()
	
	operacion=input("Escribe la operacion a realizar (suma, resta, multiplicacion,division):")

	if operacion=="suma":
			print()
			print(suma(variable1,variable2))
			

	elif operacion=="resta":
			print()
			print(resta(variable1,variable2))
		

	elif operacion=="multiplicacion":
			print()
			print(multiplicacion(variable1,variable2))
			

	elif operacion=="division":
			print()
			print(division(variable1,variable2))
			
	else:
			print()
			print("operacion introducida no contemplada")

	print()
	print("operacion finalizada")
	print()