
#equivalente a    def generanumeros():
					#return numero

# generador sintaxys      Def generaNumeros():
							#yield numeros 

# se genera un objeto iterable(que se puede repetir) y guarda el valor y entra en suspencion en vez de generar una lista entera como en una funcion tradicional
#si volvemos a llamar al generador, vuelve a extrar de la funcion un nuevo valor. lo almacena y entra en suspencion hasta que sea llamado otra vez.
#devuelve valores de uno en uno
#ventaja de eficiencia, velocidad, menor concumo de memoria y recursos

#ejemplo, programa que genere numeros pares

def pares(limite):

	num=1

	lista=[]

	while num<limite:

		lista.append(num*2) #num vale 1, llega al while, se multiplica *2 y se guarda en la lista

		num+=1 #incremento en 1 la variable num para que entre nuevamente al while

	return lista 

print(pares(10)) #el 10 es un limite, nos devuelve 9 numeros pares, si no pusiera un argumento seria una lista infinita