print("Eleccion de asignaturas")
print("Asignaturas disponibles: Bioquimica - Fisiologia - Salud mental")

asignatura=input("Elige la asignatura: ")

if asignatura in ("Bioquimica", "Fisiologia", "Salud mental"):
	
		print("La asignatura elegida es "+asignatura)

else:
	
		print("La asignatura elegida no esta contemplada")


#Python es case sensitive, para que tome las palabras como mayuscula o minuscula se usa:

#lower()    transforma la palabra en minusculas

#upper()    trasnforma la palabra en mayuscula