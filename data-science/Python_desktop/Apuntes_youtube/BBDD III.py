import sqlite3 as sql

conexion=sql.connect("Base de datos3")

cursor=conexion.cursor()

#gestion automatica de id
#
cursor.execute('''
	
	CREATE TABLE PRODUCTOS(
	ID INTEGER PRIMARY KEY AUTOINCREMENT, #ID AUTOINCREMENTABLE
	NOMBRE_ART VARCHAR(50) UNIQUE, #NOMBRE UNICO PARA UN SOLO REGRISTRO
	PRECIO INTEGER,
	SECCION VARCHAR(20))
''')

productos=[
	
	("art1",34,"seccion1"),
	("art2",34,"seccion2"),
	("art3",34,"seccion3"),
	("art4",34,"seccion3"),
	("art5",34,"seccion2"),
	("art6",34,"seccion1"),
	("art7",34,"seccion3"),
	("art8",34,"seccion2"),
	("art9",34,"seccion1"),
	("art10",34,"seccion2")
]

#cuando quiero agrear varios registros debo usar executemany
#agregar null al autoincrementable
cursor.executemany("INSERT INTO PRODUCTOS VALUES(NULL,?,?,?)", productos)

conexion.commit()

conexion.close()