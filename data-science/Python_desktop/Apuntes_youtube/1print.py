#def numbre_funcion(parametros)
     #instruccion de la funcion
     #return (opcional)
def suma():
	num1=5
	num2=9
	print(num1+num2)

suma()

def texto():
	print("me equivo en una palabra y se rompe esto")
texto()

def suma_de_parametros(num1, num2):#funcion definiendo parametros, pueden ser muchos
	print(num1+num2)
suma_de_parametros(8, 9)
suma_de_parametros(9,10)
suma_de_parametros(8,9)

def suma_con_return(numero2, numero1, numero3):

	resultado=numero1+numero2+numero3#defino la variable

	return resultado

resultado_almacenado=suma_con_return(58, 98, 45)#guardo un resultado para el futuro, sirve para codigos largos

print(resultado_almacenado)