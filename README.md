# TUSI-2021-Flask

Data de Escuelas obtenida aqui:
https://datos.gob.ar/dataset/educacion-padron-oficial-establecimientos-educativos/archivo/educacion_18.1
Es un csv bastante irregular.

Se proceso un poco,y se cargo a un base de datos (SQLITE, MYSQL y SQLITE)
Aun hay mejoras q hacer a los datos.

Usando Flask. acceso a SQLITE, MYSQL y SQLSERVER.
1er Comit habilita rutas para consulta de datos eb html y json.
Para seguir:
   EL Blog (con usuarios, registro, login, etc)
   Obtener reportes de la data propuesta en varios formatos.
   
   
Todo el flask esta basado en el tutorial del sitio oficial de flask:
https://flask.palletsprojects.com/en/2.0.x/tutorial/

Con los proximos commits iremos mejorandolo y completandolo.

Virtualizacion:

En el dir base de la app:
	python -m venv .
y despues
	. bin/activate

Agregado "requirements.txt" para instalar los paquetes necesarios:

Se usa asi, un vez activado el ambiente virtual:

1. cd to the directory where requirements.txt is located.
2. activate your virtualenv.
3. run: pip install -r requirements.txt in your shell.
