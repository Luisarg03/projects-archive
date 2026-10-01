
#num1=int(input("introduce un numero: "))
#num2=int(input("introduce otro numero numero mayor que el anterior: "))

#while num1<num2:

#	num1=num2
#	num2=int(input("introduce otro numero numero mayor que el anterior: "))

#print("El " + str(num2) + " " + "no es mayor que el " + str(num1))


num1=int(input("introduce un numero positivo: "))

contador=0

while num1>0:

	contador=num1+contador

	num1=int(input("introduce un numero positivo: "))
	

print("El numero introducido es menor a 0.")

print(contador)




