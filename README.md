# CTEDA - 2020 - Agustin Gimenez
Repositorio para practicas de la cátedra Complejidad Temporal, Estructuras de datos y Algoritmos.

# ¿Como se estructura el repositorio?
Las disintas practicas estarán distribuidas en el repositorio utilizando branches. En caso de que una practica sea terminada, se realizará un merge con la rama **master**.

# ¿Como ejecuto los tests?
Para ejecutar los tests, situandose en el directorio raiz, ejecutar el siguiente comando:
````bash
$ python -m unittest discover
````
Si quiere ejecutar los tests para cada practica individual, solo debe mencionar el directorio al final del comando (siempre situando la consola en la raiz del directorio):
````bash
$ python -m unittest discover practicaX
````
## ¿Por qué testing?
Para realizar las practicas se va a poner en practica las metodología TDD (Test Driven-Development).
## Estructura de los tests
Ya que las soluciones pedidas no requieren ningúna interacción con sistemas externos (bases de datos, APIs, etc) no se recurrira a pruebas de integración.
Las pruebas reemplazarán un posible archivo main para ejecutar el código.
Se intentó crear los tests de manera tal, que sean auto explicativos en lo que estan funcionando, y que reflejen el caso de uso o funcionalidad que estan impactando.

# Dependencias
En caso de que la solución requiera dependencias (esto significa que existe un archivo: requirements.txt), por favor utilziar el siguiente comando:
````bash
$ pip install requirements
````