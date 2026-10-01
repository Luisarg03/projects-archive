
num1=int(input("Introduce un numero:"))
num2=int(input("Introduce un numero mayor a "+ str(num1)+ ":"))

while num1<num2:

	num1=num2

	num2=int(input("Introduce un numero mayor que " + str(num2) + ":"))

if num1>num2:

	print("El numero ingresado es menor al anterior.")
	