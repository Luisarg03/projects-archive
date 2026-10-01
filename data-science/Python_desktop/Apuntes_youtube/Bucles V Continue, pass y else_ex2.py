
nombre="Estante de libros" #hay 17 caracteres y 15letras, el espacio en blanco es un caracter, con continue puedo hacer que cuente letras

contador=0

for i in nombre:
	
	if i==" ": #cuando "i" sea igual a un espacio en blanco no se toma en cuenta
		continue
 	
	contador+=1 #esta sintaxys es equivalente a contador=contador+1


print(contador)