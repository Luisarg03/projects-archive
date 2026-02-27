
#def pares (n1=int(input("Ingresa un numero: "))):

#	if n1%2==0:
#		print ("Es un numero par.")
#	else:
#		print("No es un numero par.")

#pares()




def cuentraregresiva(x=3):
	if x==0:
		print("Despegue")
	else:
		print(x)
		cuentraregresiva(x-1)  #esto es una funcion recursiva

cuentraregresiva() #la funcion se llama a si misma!!! (recursividad)




