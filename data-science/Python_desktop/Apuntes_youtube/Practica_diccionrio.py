#un diccionario alamcena datos asociando una clave con un valor "clave:valor"
#sintaxis diccionario={"clave":"valor", "clave2:valor2"...}

diccionario1={"Nombre":"Luis", "Pais":"Argentina", "Provincia":"Buenos Aires"}#La diferencia en la lista y el tuple es que se usa "llaves"

print(diccionario1)

print(diccionario1["Pais"])

diccionario1["Localidad"]="Merlo"#Metodo para agregar una clave:valor, [clave]=valor

print(diccionario1)

diccionario1["Localidad"]="San Antonio de Padua"#sobrescribi la clave!! solo puede existir una clave a la vez

print(diccionario1)

del diccionario1["Localidad"]#manera de borrar una clave

print(diccionario1)

diccionario2={"Universidad":"UBA", "Ingreso":2015, "Materias aprobadas":5}#pued mezclar tipos de variables

print(diccionario2)

tupla1=("Universidad", "Ingreso", "Materias aprobadas")#crear un diccionario desde una lista/tuple

diccionario3={tupla1[0]:"UBA", tupla1[1]:2015, tupla1[2]:5}#agrego el nombre de lista/tuple juntos al [indice] como clave y elijo el "valor"

print(diccionario3)

diccionario4={"Universidad":"UBA", "Ingreso":2015, "Cantidad de materias aprobadas":["Anatomia", "Histo", "Salud mental", "BQ", "Fisio", "Bioetica"]}

print(diccionario4["Cantidad de materias aprobadas"]); print(diccionario4["Universidad"])

diccionario5={"Universidad":"UBA", "Ingreso":2015, "Cantidad de materias aprobadas":{5:["Anatomia", "Histo", "Salud mental", "BQ", "Fisio", "Bioetica"]}} 

#Creo un diccionario dentro de otro, cuidado con las llaves y donde las abro. clave:{valor:[datos]}

print(diccionario5)

print(diccionario5["Cantidad de materias aprobadas"])

print(diccionario5.keys())#muestra todas las claves del diccionario

print(diccionario5.values())#muestra todos los valores del diccionario

print(len(diccionario5))