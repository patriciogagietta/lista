""" Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, can-
tidad de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y ade-
más la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver

las siguientes actividades utilizando lista de lista implementando las funciones necesarias:
a. obtener la cantidad de Pokémons de un determinado entrenador;
b. listar los entrenadores que hayan ganado más de tres torneos;
c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
d. mostrar todos los datos de un entrenador y sus Pokémos;
e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
(tipo y subtipo);
g. el promedio de nivel de los Pokémons de un determinado entrenador;
h. determinar cuántos entrenadores tienen a un determinado Pokémon;
i. mostrar los entrenadores que tienen Pokémons repetidos;
j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Te-
rrakion o Wingull;
k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
deberán mostrar los datos de ambos; """

from lista import Lista
from random import randint, choice

class Entrenador:

    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_ganadas = batallas_ganadas
        self.batallas_perdidas = batallas_perdidas
    
    def __str__(self):
        return f"{self.nombre} - {self.torneos_ganados} - {self.batallas_ganadas} - {self.batallas_perdidas} "

class Pokemon:

    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f"{self.nombre} - {self.nivel} - {self.tipo} - {self.subtipo}"

lista_entrenadores = Lista()

enternadores = [
    {'name': 'uno', 'tg': 15, 'bg': 45,  'bp': 11},
    {'name': 'dos', 'tg': 3, 'bg': 12,  'bp': 35},
    {'name': 'tres', 'tg': 0, 'bg': 50,  'bp': 50},
    {'name': 'cuatro', 'tg': 1, 'bg': 10,  'bp': 1},
    {'name': 'cinco', 'tg': 7, 'bg': 25, 'bp': 8},
]

pokemons = [
    {'name': 'Tyrantrum', 'nivel': 45, 'tipo': 'electrico', 'subtipo': 'normal'},
    {'name': 'pok2', 'nivel': 12, 'tipo': 'fuego', 'subtipo': 'dragon'},
    {'name': 'pok3', 'nivel': 90, 'tipo': 'volador', 'subtipo': 'lucha'},
    {'name': 'Terrakion', 'nivel': 20, 'tipo': 'agua', 'subtipo': None},
    {'name': 'pok5', 'nivel': 27, 'tipo': 'planta', 'subtipo': 'tierra'},
    {'name': 'pok6', 'nivel': 53, 'tipo': 'roca', 'subtipo': 'acero'},
]


for entrenador in enternadores:
    lista_entrenadores.insertar(Entrenador(entrenador['name'],
                                           entrenador['tg'],
                                           entrenador['bp'],
                                           entrenador['bg']), 'nombre')

for entrenador in enternadores:
    for i in range(randint(1, 5)):
        pokemon = choice(pokemons)
        pos = lista_entrenadores.busqueda(entrenador['name'], 'nombre')
        pos.sublista.insertar(Pokemon(pokemon['name'],
                                      pokemon['nivel'],
                                      pokemon['tipo'],
                                      pokemon['subtipo']), 'nombre')

lista_entrenadores.barrido_lista_lista() 
print()   


# A
entrenador = input('ingrese nombre del entrenador ')
pos = lista_entrenadores.busqueda(entrenador, 'nombre')
if(pos):
   print(f"el entrenador tiene {pos.sublista.tamanio()} pokemons")
else:
   print('el entrenador no esta en la lista')
print()


# B
print("entrenadores que hayan ganado más de tres torneos")
lista_entrenadores.barrido_entrenador_mas_tres()
print()

# C
print("Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados")
mayor = lista_entrenadores.mayor_de_lista('torneos_ganados')
print(mayor.info, mayor.sublista.mayor_de_lista('nivel').info)
print()

# D
entrenador = input('ingrese nombre del entrenador: ')
print("datos de un entrenador y sus Pokémos")
pos = lista_entrenadores.busqueda(entrenador, 'nombre')
if(pos):
    print(f"el entrenador tiene {pos.info}")
    print('sus pokemons')
    pos.sublista.barrido()
else:
    print('el entrenador no esta en la lista')
print()

# E
print("Porcentaje victorias % 79")
lista_entrenadores.barrido_porcentaje_victorias()

# F
print("entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador tipo y subtipo")
lista_entrenadores.barrido_tipo_entrenador()
print()

# G
entrenador = input("ingrese nombre del entrenador: ")
print("promedio de nivel de los Pokémons de un determinado entrenador")
pos = lista_entrenadores.busqueda(entrenador, "nombre")
if pos:
    print(f"promedio: % {pos.sublista.suma_niveles() / pos.sublista.tamanio()}")
else:
    print("el entrenador no esta en la lista")

print()

# H
pokemon = input("ingrese el nombre del pokemon: ")
print("entrenadores tienen a un determinado Pokémon")
lista_entrenadores.barrido_pokemon_buscado(pokemon)
print()

# I
print('entrenadores que tienen Pokémons repetidos')
lista_entrenadores.barrido_entrenadores_poke_repetidos()
print()

# J
print('entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull')
lista_entrenadores.barrido_pokemones_Tyrantrum_Terrakion_Wingull()
print()

# K
entrenador = input("ingrese nombre del entrenador: ")
pokemon = input("ingrese el nombre del pokemon: ")
print("entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador como del Pokémon deben ser ingresados")

pos = lista_entrenadores.busqueda(entrenador, "nombre")
if pos: 
    pos_aux = pos.sublista.busqueda(pokemon, "nombre")
    if pos_aux:
        print(f"datos del entrenador {pos.info} ")
        print(f"datos del pokemon {pos_aux.info} ")
    else:
        print("el entrenador no tiene al pokemon")
else:
    print("el entrenador no esta en la lista")
