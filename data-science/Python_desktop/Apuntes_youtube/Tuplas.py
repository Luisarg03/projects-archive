mituple1=("juan", "lucas", "lucas", "lucas", "lucas", "lucas", "lucas")
print(mituple1[:])

milista=list(mituple1) #convierto la tupla en lista, defino una variable, "milista", y alamaceno la tupla y la convierto en lista
print(milista)

conversion_tuple=tuple(milista) #convierto la lista a tuple

print(conversion_tuple)

print(mituple1.count("lucas")) #cuenta cuantas veces se repite el elemento en la lista

print(len(mituple1)) #indica cantiadad total de elementos en la lista

#desempaquetado de tuple

tuple2=(1993, "junio", 25, "luis")

anio, mes, dia, nombre=tuple2

print(nombre); print(dia, mes, anio)