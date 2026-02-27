num1=int(input("Introcude un numero mayor a cero:"))

while num1<0:
	print("Numero incorrecto.")
	num1=int(input("Introcude un numero mayor a cero:"))

num2=int(input("Introduce un numero mayor a cero:"))

if num1>0 and num2>0:

	while num1>0 and num2>0:

		num1=num1+num2

		num2=int(input("Introduce un numero mayor a cero:"))

if num1<0 or num2<0:

	suma=num1
	print("El numero introducido es menor a 0.")
	print()
	print("La suma de los numeros positivos introducidos es:" + str(suma))

