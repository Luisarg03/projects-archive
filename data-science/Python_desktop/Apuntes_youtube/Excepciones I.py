
#exepciones

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

		return "operacion erronea"

variable1=(int(input("Ingresa un numero:")))
variable2=(int(input("ingresa otro numero:")))

operacion=input("Escribe la operacion a realizar (suma, resta, multiplicacion,division):")

while operacion:

	if operacion=="suma":
		print(suma(variable1,variable2))

	elif operacion=="resta":
		print(resta(variable1,variable2))

	elif operacion=="multiplicacion":
		print(multiplicacion(variable1,variable2))

	elif operacion=="division":
		print(division(variable1,variable2))

	else:
		print("operacion introducida no contemplada")
	break;

print("operacion finalizada")
