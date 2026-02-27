edad=int(input("Introduce la edad: "))

while edad<5 or edad>100 :

	print("Edad incorrecta")
	edad=int(input("Introduce la edad: "))

print("Edad correcta " + str(edad))