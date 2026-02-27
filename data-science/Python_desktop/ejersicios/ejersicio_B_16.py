
email=input("ingrese la clave:")

contadorarroba=0
contadorpunto=0

for i in range(len(email)):

	if email[i]=="@":
		contadorarroba=contadorarroba+1

	if email[i]==".":
		contadorpunto=contadorpunto+1

if contadorarroba!=1 or contadorpunto==0 

	print("email incorrecto")
else:
	print("email correcto")
		



#print(f"valor de la variable{i}")  funcion de tipo f, nos deja unis strings con variables
#    end="palabla/espacio o algo" sirve para que el for no haga saltos de linea
#Len()  cuenta cantidad de letras en el string