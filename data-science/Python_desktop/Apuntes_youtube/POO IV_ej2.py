class Coche():
	
	largochacis=250 
	anchochacis=120
	ruedas=4
	enmarcha=False 
	
	#el metodo dira el estado y si arrancara
	def arrancar(self,arrancamos):
		 self.enmarcha=arrancamos


		if(self.enmarcha):
			return "El coche esta en marcha"
			
		else:
			
			return "El coche esta parado"
		

	def estado(self):
		print("El coche tiene" , self.ruedas , " ruedas. Un anchi de " , self.anchochacis , 
			   "y un largo de " , self.largochacis)

micoche=Coche()  

print("El largo del coche es:",micoche.largochacis)
print("Este coche tiene ",micoche.ruedas, " ruedas")

print(micoche.arrancar(True))
micoche.estado()

print()
print("------Creamos un segundo objeto de la clase Coche.-------")
print()

micoche2=Coche()

	print("El largo del coche es:",micoche2.largochacis)
	print("Este coche tiene ",micoche2.ruedas, " ruedas")

	print(micoche2.arrancar(False))
	micoche2.estado()