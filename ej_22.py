""" Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros,
colores de sable de luz usados y especie. implementar las funciones necesarias para resolver las
actividades enumeradas a continuación:
a. listado ordenado por nombre y por especie;
b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
d. mostrar los Jedi de especie humana y twi'lek;
e. listar todos los Jedi que comienzan con A;
f. mostrar los Jedi que usaron sable de luz de más de un color;
g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron. """

from lista import Lista

class Jedis:

    def __init__(self, nombre, maestro, color_sable, especie):
        self.nombre = nombre
        self.maestro = maestro
        self.color_sable = color_sable
        self.especie = especie
    
    def __str__(self):
         return f"{self.nombre} - {self.maestro} - {self.color_sable} - {self.especie}"

lista_jedis = Lista()
lista_jedis_2 = Lista()

jedis = [
        {'nombre': 'Aayla Secura','maestro': "Qui-Gon Jin" ,'color_sable': ['rojo',"azul"],'especie':'humana'},
        {'nombre': 'Wolverine','maestro': "Yoda" ,'color_sable': ['amarillo'] ,'especie':'humana'},
        {'nombre': 'Ahsoka Tano','maestro': "Luke Skywalker" ,'color_sable': ['verde'] ,'especie':'twilek'},
        {'nombre': 'Dr Strange','maestro': "Luke Skywalker" ,'color_sable': ['violeta'] ,'especie':'otra'},
        {'nombre': 'Capitana Marvel','maestro': "Mace Windu" ,'color_sable': ['naranja',"gris"] ,'especie':'twilek'},
        {'nombre': 'Kit Fisto','maestro': "Yoda" ,'color_sable': ['rosa',"blanco" ],'especie':'humana'},
        {'nombre': 'Flash','maestro': "Mace Windu" ,'color_sable': ['violeta'] ,'especie':'otra'},
        {'nombre': 'Star-Lord','maestro': "Luke Skywalker",'color_sable': ['amarillo'] ,'especie':'humana'}
]

for jedi in jedis:
    lista_jedis.insertar(Jedis(jedi['nombre'],
                               jedi['maestro'],
                               jedi['color_sable'],
                               jedi['especie']), 'nombre')

    lista_jedis_2.insertar(Jedis(jedi['nombre'],
                                 jedi['maestro'],
                                 jedi['color_sable'],
                                 jedi['especie']), 'especie')

# A
print('lista ordenada por nombre')
lista_jedis.barrido()
print()

print('lista ordenada por especie')
lista_jedis_2.barrido()
print()

# B
pos = lista_jedis.busqueda('Ahsoka Tano', 'nombre')
if pos:
    print(f'información de Ahsoka Tano: {pos.info}')
else:
    print('Ahsoka Tano no esta')

pos2 = lista_jedis.busqueda('Kit Fisto', 'nombre')
if pos2:
    print(f'información de kit fisto: {pos2.info}')
else:
    print('Kit Fisto no esta')
print()


# C
print('padawan de Yoda')
lista_jedis.barrido_padawan_yoda()
print()

print('padawan de Luke Skywalker')
lista_jedis.barrido_padawan_luke()
print()

# D
print('jedis especie humana')
lista_jedis.barrido_especie_humana()
print()

print('jedis especie twilek')
lista_jedis.barrido_especie_twilek()
print()

# E
print('jedis que comienzan con A')
lista_jedis.barrido_jedi_conmienza_con_A()
print()

# F
print('Jedi que usaron sable de luz de más de un color')
lista_jedis.barrido_jedi_mas_de_un_color()
print()

# G
print('Jedi que utilizaron sable de luz amarillo o violeta')
lista_jedis.barrido_jedi_amarillo_violeta()
print()

# H
print('nombre padawans de Qui-Gon Jin')
lista_jedis.barrido_padawan_QuiGonJin()
print()

print('nombre padawans de Mace Windu')
lista_jedis.barrido_padawan_MaceWindu()
print()
