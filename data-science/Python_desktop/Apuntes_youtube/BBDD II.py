import sqlite3 as sql

conexion=sql.connect("Base de datos2")

cursor=conexion.cursor()

#cursor.execute('''
	
#	CREATE TABLE PRODUCTOS (
#	CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
#	NOMBRE_ART VARCHAR(20),
#	PRECIO INT,
#	SECCION VARCHAR(20))

#	''')

productos=[
	("01","Pelota",20,"deportes"),
	("02","Jarron",20,"ceramicas"),
	("03","camion",20,"juguetes"),
	("04","pantalon",20,"confeccion"),
	("05","palo de golf",20,"deportes")
]

cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)

conexion.commit()

conexion.close()