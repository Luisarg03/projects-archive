#Lanzamientos de excepciones
#instruccion "Raise"
#creacion de excepciones propias

def evalua_edad(edad):

	if edad<0:
		raise typeError("No se permiten edades negativas") #mi errro personalizado

	if edad>50:
		return("Estas viejo")

	elif edad<50:
		return("Aun eres joven")

	elif edad<=5:
		return("Que haces programando?!")

print(evalua_edad(45)) #puedo agregar numeros negativos y eso no es correcto en las edades