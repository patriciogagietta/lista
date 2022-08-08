""" Se cuenta con una lista de películas de cada una de estas se dispone de los siguientes datos:

nombre, valoración del público –es un valor comprendido entre 0-10–, año de estreno y recau-
dación. Desarrolle los algoritmos necesarios para realizar las siguientes tareas:

a. permitir filtrar las películas por año –es decir mostrar todas las películas de un determina-
do año–;
b. mostrar los datos de la película que más recaudo;
c. indicar las películas con mayor valoración del público, puede ser más de una;
d. mostrar el contenido de la lista en los siguientes criterios de orden –solo podrá utilizar una
lista auxiliar–:
I. por nombre,
II. por recaudación,
III. por año de estreno,
IV. por valoración del público. """

from lista import Lista

class Pelicula:

    def __init__(self, nombre, valoracion, anio, recaudacion):
        self.nombre = nombre
        self.valoracion = valoracion
        self.anio = anio
        self.recaudacion = recaudacion
    
    def __str__(self):
        return f"{self.nombre} - {self.valoracion} - {self.anio} - {self.recaudacion}"

lista_peliculas = Lista()
lista_aux = Lista()

peliculas = [
    {'name':'busqueda implacable', 'vp':5, 'anio':2008, 'recaudacion':100},      
    {'name':'que paso ayer', 'vp':3, 'anio':2010, 'recaudacion':200},
    {'name':'inocente', 'vp':2, 'anio':2019, 'recaudacion':50},
    {'name':'ice road', 'vp':2, 'anio':2021, 'recaudacion':10},
    {'name':'matrix', 'vp':7, 'anio':2006, 'recaudacion':20},
]


for peli in peliculas:
    lista_peliculas.insertar(Pelicula(peli['name'],
                                      peli['vp'],
                                      peli['anio'],
                                      peli['recaudacion']), 'nombre')


#lista_peliculas.barrido()
print()

# A
anio_buscado = int(input("ingrese el anio "))
print('anio buscado: ')
lista_peliculas.barrido_anio(anio_buscado)
print()

# B
lista_peliculas.barrido_recaudacion()
print()

# C
lista_peliculas.barrido_valoracion_publico()
print()

# D
orden = input('ingrese por lo que quiere ordenar (nombre, valoracion, anio, recaudacion): ')

for peli in peliculas:
    lista_aux.insertar(Pelicula(peli['name'],
                                peli['vp'],
                                peli['anio'],
                                peli['recaudacion']), orden)

print(f'lista ordenada por {orden}')
print()
lista_aux.barrido() 
