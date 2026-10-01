#AND, "y si ademas"
#OR, "o si no"

print("Asignacion de becas 2017")
print()

Distancia_escuela=int(input("Ingrese la distancia a la escuela en Km: "))
print()
Numero_de_hermanos=int(input("Indique la cantidad de hermanos: "))
print()
Ingresos=int(input("Indique sus ingresos en pesos: "))
print()
if Distancia_escuela>=25 and Numero_de_hermanos>=4 or Ingresos<=5000: #si la distancia a la escuela es mayor o igual a x, "y si" el numero de hermanos es mayor a y, "o si" (si cumple esta condicion se cancelan los anteriores) tiene un ingreso menor a z.
	
	print("Tienes derecho a la beca.")

else:
	print("No puedes recibir la beca.")