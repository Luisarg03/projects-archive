#Creando una clase

class Coche():
	#establecemos las propiedades, el estado y el comportamiento de la clase

	#propiedades

	largochacis=250 #en centimetros
	anchochacis=120
	ruedas=4
	enmarcha=False #todos los coches que creamos estaran parados por defecto

	#comportamiento, se establecen a travez de los "metodos", se establece con "def" para metodos, no es lo mismo que el "def" de funcion

	def arrancar(self):  #funcion, y parametro "self", referencia al objeto que pertenece a la clase
		pass

#construccion del objeto/s

micoche=Coche()   #creando una instancia//ejemplar de clase

print("El largo del coche es:",micoche.largochacis)
print("Este coche tiene ",micoche.ruedas, " ruedas")


