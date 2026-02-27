#Orden de ejecucion de los programas de de arriba hacia abajo, pero, puede alterarse cuando se agregan condicionales
#El condicional If es un bloque de codigo que analizara si las instrucciones declaradas son "verdaderas" o "falsas"

#instruccion
#instruccion 
#if condicion
    #instruccion
    #instruccion
#instruccion
#instruccion

#si el if toma como "verdadero" las condiciones declaradas, esta entra en el if
#si las declaracion resultara ser "falsa" salteara el if

print("Evalcuacion de alumno")

nota_alumno=input("Ingrese la nota del alumno: ") #cualquier cosa que ingresemos en los input se consideran texto, string

def evalcuacion(nota):
    
    valoracion="Desaprobado"

    if nota>=4: #El if solo se ejecutara si el condicional es "verdadero" #el if compara el dato ingresado en el input, pero este debe ser del mismo tipo de dato.

        valoracion="Aprobado" #si se cumple que la nota ingresada es mayor o igual a 4, la "valoracion" cambiara

    return valoracion #indico que devuelva la variable

print(evalcuacion(float(nota_alumno))) #transformo la variable ingresada en el tipo de dato necesario para que el if pueda compararla, en este caso un tipo numerico