
class Coche():
	
	largochacis=250 
	anchochacis=120
	ruedas=4
	enmarcha=False 
	
	def arrancar(self):  
		self.enmarcha=True

	def estado(self):

		if(self.enmarcha):
			return "El coche esta en marcha"

		else:
			return "El coche esta parado"

micoche=Coche()  

print("El largo del coche es:",micoche.largochacis)
print("Este coche tiene ",micoche.ruedas, " ruedas")

micoche.arrancar()
print(micoche.estado())

print()
print("------Creamos un segundo objeto de la clase Coche.-------")
print()

micoche2=Coche()

print("El largo del coche es:",micoche2.largochacis)
print("Este coche tiene ",micoche2.ruedas, " ruedas")

print(micoche2.estado())