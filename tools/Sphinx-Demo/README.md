
# Sphinx para autogeneración de documentación
#### ( Doc en progreso )
## Tabla de contenidos
1. [Que es Sphinx](#que-es-sphinx)
	- [Generador de documentación](#generador-de-documentación)
	- [ReStructuredText](#restructuredtext)
3. [Instalación](#instalación)
4. [Inicio rápido](#inicio-rápido)
5. [Referencias](#referencias)


## Que es Sphinx

### Generador de documentación

**Sphinx**  es un software  que convierte ficheros  [reStructuredText](https://es.wikipedia.org/wiki/ReStructuredText "ReStructuredText")  en  sitios web HTML  y otros formatos, incluyendo PDF, EPub y man. Saca provecho de la naturaleza extensible de [**reStructuredText**](https://docutils.sourceforge.io/rst.html) y sus extensiones (ej. para generar automáticamente documentación desde código fuente, escribir notación matemática o resalzar código). 
Se desarrolló y usó extensivamente por y para el Proyecto de documentación **Python**

Desde su introducción en 2008, Sphinx ha sido adoptado por muchos otros proyectos Python importantes, como  [SQLAlchemy](https://docs.sqlalchemy.org/en/14/contents.html),  [SciPy](https://docs.scipy.org/doc/scipy/reference/),  [Django](https://docs.djangoproject.com/en/4.0/)  y  [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html).

### ReStructuredText

Es un [lenguaje de marcas ligero](https://es.wikipedia.org/wiki/Lenguaje_de_marcas_ligero "Lenguaje de marcas ligero") creado para escribir textos con formatos definido de manera cómoda y rápida. Es parte del proyecto [Docutils](https://docutils.sourceforge.io/README.html#quick-start) dentro de la comunidad de Python. Su principal ventaja es que desde un texto con sintaxis sencilla puede usarse para generar documentos equivalentes en HTML, LaTeX, docbook, etc.

#### **Ejemplo de sintaxis rST**
```sh
An `example <http://example.com>`.

.. image:: Icon-pictures.png
    :alt: Image
![Image](Icon-pictures.png "icon")

::

 rST uses :: prior to a paragraph
 for blockquoting.
 Multiple paragraphs need to be prepended individually.

| Multi-line text can
| span in tables
| with a pipe character.
```

#### HTML producido por  rST

``` html
<p>An <a href="http://example.com">example</a>.</p>

<p><img alt="Image"src="Icon-pictures.png" /></p>

<blockquote>
<p>rST uses :: prior to a pargraph<br/> for blockquoting.<br/>Multiple paragraphs need to be prepended individually.</p>
</blockquote>

<p>Multi-line text can<br/>span in tables<br/>with a pipe character.</p>
```
#### Texto visto desde un navegador

An [example](http://example.com/).

![Image](https://upload.wikimedia.org/wikipedia/commons/5/5c/Icon-pictures.png "icon")

> rST uses :: prior to a paragraph  
> for blockquoting.  
> Multiple paragraphs need to be prepended individually.

Multi-line text can  
span in tables  
with a pipe character.


## Instalación
Recomendación: Generar un entorno virtual para la instalación de Sphinx y sus estilos de temas.

Versión Sphinx 4.3.2
```properties
pip install -U Sphinx==4.3.2
```
Estilo [Furo](https://sphinx-themes.org/sample-sites/furo/) ( Variedad de temas en [Sphinx Themes Gallery](https://sphinx-themes.org/) )
```properties
pip install furo
```

## Inicio rápido

1. Vista general del directorio de trabajo. El directorio **src** contiene el codigo documentado.

![alt text](./img/Selección_026.png)

2. Ejecutando el siguiente comando iniciara la creacion de los directorios relacionados a Sphinx, donde **docs** es el nombre que se le asigna al directorio raiz. (Por convencion se utiliza este nombre)

```properties
sphinx-quickstart docs
```
3. Nos pedira que seleccionemos algunas opciones, que la mayoria se pueden omitir y setear luego. Pero la mas importante es la opcion de **"Separar directorios fuente y compilado"**, donde ingresaremos **"y"** para mantener un orden en los directorios.

![alt text](./img/Selección_028.png)

Vista general de los directorios y files creados.

![alt text](./img/Selección_029.png)

4. El siguiente comando permite a Sphinx buscar el directorio donde se encuentran los codigos documentados y generar el file .rst que se utilizara para generar la documentacion en el formato que especifiquemos mas adelante.
Los argumentos seran los directorios OUTPUT ( docs/source/**rst** ) e INPUT. ( src/**modules** )

```properties
sphinx-apidoc -o docs/source/rst src/modules
```

Directorio generado con el file .rst generado por Sphinx.

![alt text](./img/Selección_031.png)

5. Configuracion del archivo **conf.py**

	a. Se deben descomentar las 3 primeras lineas de codigo y agregar el **path relativo** ( En este caso **../../src** ) donde se aloja la app. 
	Es posible agregar el path absoluto, pero no es recomendable.
	![alt text](./img/Selección_001.png)
	<br>

	b. Agregar las siguientes lineas.
	- La extencion **autodoc** es las extencion para la semi autodocumentacion.
	- **coverage** recoge estadísticas de la cobertura de la documentación.
	- Los docstrings del codigo estan en estilo NumPy, la extension **napoleon** reconoce este formato.
	- La extencion **viewcode** genera un link para visualizar los codigos en la documentacion final.


	```python
	'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode'
	```

	![alt text](./img/Selección_002.png)
	<br>

	c. Seteamos el nombre del tema instalado previamente, en este ejemplo **furo**.
	![alt text](./img/Selección_003.png)
	<br>

6. Posicionarse en "docs" y ejecutar el siguiente comando.
```properties
cd docs/
make clean html
```

7. Se habra generado varios .html dentro del directorio **docs/build/html** .
Se podra acceder a la documentacion generada desde **index.html** .

## Referencias
**documentación oficial** -> https://www.sphinx-doc.org/en/master/

https://en.wikipedia.org/wiki/Sphinx_(documentation_generator)

https://es.wikipedia.org/wiki/ReStructuredText

https://en.wikipedia.org/wiki/ReStructuredText

https://wiki.python.org/moin/DocumentationTools

[Tutoria Medium de Julie Elise](https://betterprogramming.pub/auto-documenting-a-python-project-using-sphinx-8878f9ddc6e9)

[Tutoria Medium de Michael Dunn](https://eikonomega.medium.com/getting-started-with-sphinx-autodoc-part-1-2cebbbca5365)

[Canal de Youtube soumilshah1995](https://www.youtube.com/watch?v=5s3JvVqwESA)

[Canal de Youtube {LP} WITH RAHMAT](https://www.youtube.com/watch?v=d_XeV6oyNvI&t)
