
Sueldo_presidente=int(input("Ingrese el sueldo del presidente: "))
print()
print("EL sueldo del presidente es de " + str(Sueldo_presidente) + " dolares")
print()
Sueldo_vicepresidente=int(input("Ingrese el sueldo del vicepresidente: "))
print()
print("EL sueldo del vicepresidente es de " + str(Sueldo_vicepresidente) + " dolares")
print()
Sueldo_ejecutivo=int(input("Ingrese el sueldo del ejecutivo: "))
print()
print("EL sueldo del ejecutivo es de " + str(Sueldo_ejecutivo) + " dolares")

if Sueldo_presidente>Sueldo_vicepresidente>Sueldo_ejecutivo:
	print()
	print("No hay problemas en los salarios")

else:
	print()
	print("Algo esta mal en los salarios")

#Concatenacion de condicionales en el if. para comparar variables