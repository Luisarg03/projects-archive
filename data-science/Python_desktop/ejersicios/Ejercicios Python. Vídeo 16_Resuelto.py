
# def impares(limite):

#	num=1

#	lista=[]

#	while num<limite:
		
#		lista.append(num+2)

#		num+=2

#	return lista

# print(impares(99))

#Nice


#clave=input("Ingrese una clave: ")

#contador=0

#for i in range(len(clave)):

#	if clave[i]==" ":

#			contador=1

#if len(clave)<8 or contador>0:

#	print("Clave incorrecta")

#else:

#	print("Clave correcta")

correo=input("Ingrese su correo: ")

contadorpunto=0

contadorarroba=0

for i in range(len(correo)):

	if correo[i]=="@":

		contadorarroba=contadorarroba+1

	if correo[i]==".":

		contadorpunto=contadorpunto+1


if contadorpunto>0 and contadorarroba==1:

	print("Correo correcto")

else:
	print("Correo incorrecto")



