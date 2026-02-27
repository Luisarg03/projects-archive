
x=int(input("n1: "))
y=int(input("n2: "))

divison=x/y

resto=x%y #con % obtengo el resto de x/y

if resto==0:
	print ("El resultado de la division es: " + str(divison))
	print("Ambos numeros son divisibles.")
	print("El resto es 0")

else:
	print("Los numeros no son divisibles.")
	print("El resto obtenido es: " + str(resto))

