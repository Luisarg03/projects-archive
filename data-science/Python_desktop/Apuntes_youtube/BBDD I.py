import sqlite3 as sql

#1) establesco conexion
conexion=sql.connect("Base_de_datos")

#2) creo el cursor

cursor=conexion.cursor()

# 3) ejecutar la consulta

#COMANDO PARA CREAR TABLA
#cursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ART VARCHAR(20), PRECIO INT, SECCION VARCHAR(20))")


#insertando valores a la tabla
#cursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',25,'JUGUETES')")


#insertando varios valores a la vez

#varios_productos= [

#	("camiseta",15,"deportes"),
#	("jarron",30,"ceramica"),
#	("camion",20,"jugueteria"),
#	("raqueta",40,"deportes")

#]

#cursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",varios_productos)#INSERTAR TANTAS INTERROGANTES COMO CAMPOS A CUBRIR EN LOS REGISTROS

cursor.execute("SELECT * FROM PRODUCTOS")

vista_datos=cursor.fetchall() #devuelve la consulta de sql

#print(vista_datos)
#

for producto in vista_datos:

	print(producto)


#confirmar que modificcamos la tabla
conexion.commit()

#cierro la conexion
conexion.close()