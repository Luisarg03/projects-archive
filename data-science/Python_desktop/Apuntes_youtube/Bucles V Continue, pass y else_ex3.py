email=input("introduce el email:")

for i in email:

	if i=="@":

		arroba=True

		break;

else: #esta a la altura del bucle for, forma parte del bucle for, no es un else de un condicional. osea, si no se cumple un condicional hay un salto al else.
	  #el else de los bucles se ejecuta cuando el bucle haya terminado de leer sus lineas, osea se ejecutan los dos, no como en el condicional que directamente se salta.
	arroba=False

print(arroba) 

#si escribo un email sin @, el "i" nunca valdra "@" ,no se leeran las lineas del if, y arroba no cambiara a true.
#cuando agrego un @ al email, ingresa al for, y arroba valdra true, luego el break finaliza el for junto al else
#el else finaliza porque es parte del ciclo for, y arroba no cambiara a False.