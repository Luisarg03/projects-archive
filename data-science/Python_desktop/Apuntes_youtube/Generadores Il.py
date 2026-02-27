# yield from

#simplifica el codigo de generadores en el caso de usar bubles anidados, osea bucles dentro de otros bucles.

#ej, el generador devuelve un elemento y quiero acceder a los datos de ese elemento extraido.(sub elementos).

def devuelve_ciudades(*ciudades): #el asterisco adelante del argumento de la funcion significa que no sabemos cuantos elementos recibira la funcion.

	for elemento in ciudades:

		#for subelemento in elemento:

		yield from elemento #equivalente a la linea de arriba

ciudades_devueltas=devuelve_ciudades("Buenos Aires", "Salta", "Mendoza", "Tucuman")

print(next(ciudades_devueltas))
 #el next hace que imprima los elementos uno a uno


#los sub elementos de la palabra Salta, son las letras, con bucles for aninados puedo acceder a esos elementos.
