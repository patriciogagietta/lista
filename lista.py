def criterio(dato, campo=None):
    dic = {}
    if(hasattr(dato, '__dict__')):
        dic = dato.__dict__
    if(campo is None or campo not in dic):
        return dato
    else:
        return dic[campo]


class nodoLista():
    info, sig, sublista = None, None, None


class Lista():

    def __init__(self):
        self.__inicio = None
        self.__tamanio = 0


    def insertar(self, dato, campo=None):
        nodo = nodoLista()
        nodo.info = dato
        nodo.sublista = Lista()

        if(self.__inicio is None or criterio(nodo.info, campo) < criterio(self.__inicio.info, campo)):
            nodo.sig = self.__inicio
            self.__inicio = nodo
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while(actual is not None and criterio(nodo.info, campo) > criterio(actual.info, campo)):
                anterior = anterior.sig
                actual = actual.sig

            nodo.sig = actual
            anterior.sig = nodo

        self.__tamanio += 1

    def lista_vacia(self):
        return self.__inicio is None

    def tamanio(self):
        return self.__tamanio

    def barrido(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info)
            aux = aux.sig
    
    def barrido_entrenador_mas_tres(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.torneos_ganados > 3):
                print(aux.info)
            aux = aux.sig
    
    def barrido_lista_lista(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info)
            print('sublista:')
            aux.sublista.barrido()
            # aux1 = aux.sublista.__inicio
            # while(aux1 is not None):
            #     print('  ', aux1.info)
            #     aux1 = aux1.sig

            aux = aux.sig
    
    def barrido_armadura_traje(self):
        aux = self.__inicio
        while(aux is not None):
            if('traje' in aux.info.bio or 'armadura' in aux.info.bio):
                print(aux.info)
            aux = aux.sig

    def barrido_anterior_1963(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.aparicion < 1963):
                print(aux.info)
            aux = aux.sig
    
    def barrido_jedi_master(self):
        aux = self.__inicio
        while(aux is not None):
            if('yoda' in aux.info.maestro or 'luke skywalker' in aux.info.maestro):
                print(aux.info)
            aux = aux.sig

    def barrido_comienza_con(self, iniciales=[]):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.nombre[0] in iniciales):
                print(aux.info)
            aux = aux.sig

    def barrido_porcentaje_victorias(self):
        aux = self.__inicio
        while(aux is not None):
            total = aux.info.batallas_ganadas + aux.info.batallas_perdidas
            if(aux.info.batallas_ganadas / total >= 0.79):
                print(aux.info)
            aux = aux.sig

    def busqueda(self, buscado, campo=None):
        pos = None
        aux = self.__inicio
        while(aux is not None and pos is None):
            if(criterio(aux.info, campo) == buscado):
                pos = aux
            aux = aux.sig

        return pos

    def eliminar(self, clave, campo=None):
        dato = None
        if(criterio(self.__inicio.info, campo) == clave):
            dato = self.__inicio.info
            self.__inicio = self.__inicio.sig
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while(actual is not None and criterio(actual.info, campo) != clave):
                anterior = anterior.sig
                actual = actual.sig

            if(actual is not None):
                dato = actual.info
                anterior.sig = actual.sig
        if dato:
            self.__tamanio -= 1 

        return dato

    def obtener_elemento(self, indice):
        if(indice <= self.__tamanio-1 and indice >= 0):
            aux = self.__inicio
            for i in range(indice):
                aux = aux.sig
            return aux.info            
        else:
            return None

    def contar_por_casa(self):
        marvel, dc = 0, 0

        aux = self.__inicio
        while(aux is not None):
            if(aux.info.casa.capitalize() == 'Marvel'):
                marvel += 1
            if(aux.info.casa.capitalize() == 'Dc'):
                dc += 1
            aux = aux.sig

        return marvel, dc
    
    def mayor_de_lista(self, campo):
        mayor = self.__inicio
        aux = self.__inicio
        while(aux is not None):
            if(criterio(aux.info, campo) > criterio(mayor.info, campo)):
                mayor = aux
                break
            aux = aux.sig
        return mayor

    def barrido_dinosaurios_filtrado(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.name == "Tyrannosaurus Rex" or aux.info.name == "Spinosaurus" or aux.info.name == "Giganotosaurus"):
                if (aux.info.alert_level == "critical" or aux.info.alert_level == "high"):
                    print(aux.info)
            aux = aux.sig

    def barrido_dinosaurios_raptors(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.name == "Raptors (Dromaeosauridae)" or aux.info.name == "Carnotaurus"):
                print(aux.info)
            aux = aux.sig

    def barrido_codigo_Compsognathus(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.name == "Compsognathus"):
                print(aux.info.zone_code)
            aux = aux.sig
    

    def barrido_tipo_entrenador(self):
        aux = self.__inicio
        while(aux is not None):
            aux1 = aux.sublista.__inicio
            while (aux1 is not None):
                if (aux1.info.tipo == "planta" and aux1.info.subtipo == "tierra"):
                    print(aux.info)   
                    break             
                aux1 = aux1.sig
            aux = aux.sig


    def suma_niveles(self):
        aux = self.__inicio
        niveles = 0
        while(aux is not None):
            niveles = niveles + aux.info.nivel
            aux = aux.sig
        return niveles


    def barrido_pokemon_buscado(self,buscado):
        aux = self.__inicio
        while(aux is not None):
            aux1 = aux.sublista.__inicio
            aux2 = 0
            while (aux1 is not None):
                if (buscado in aux1.info.nombre):
                    print(aux.info.nombre)
                    aux2 = aux2 + 1
                    break
                aux1 = aux1.sig
            aux = aux.sig

    def barrido_entrenadores_poke_repetidos(self):
        aux=self.__inicio
        while(aux is not None):
            pokemon = aux.sublista
            aux2 = pokemon.__inicio
            pokemon_sig = aux2.sig
            while(pokemon_sig is not None):
                if (aux2.info.nombre == pokemon_sig.info.nombre):
                    print(aux.info.nombre)
                    break    
                aux2 = aux2.sig
                pokemon_sig = pokemon_sig.sig
            aux=aux.sig

    def barrido_pokemones_Tyrantrum_Terrakion_Wingull(self):
        aux = self.__inicio
        while(aux is not None):
            pokemon = aux.sublista
            aux2 = pokemon.__inicio
            while(aux2 is not None):
                if(aux2.info.nombre == 'Tyrantrum' or aux2.info.nombre == 'Terrakion' or aux2.info.nombre == 'Wingull'):
                    print(f'entrenador {aux.info.nombre} tiene un {aux2.info.nombre}.')
                aux2 = aux2.sig
            aux = aux.sig 

    def barrido_anio(self,anio_buscado):
        aux = self.__inicio
        aux2 = True
        while(aux is not None):
            if (aux.info.anio == anio_buscado):
                print(aux.info.nombre)
                aux2 = False
            aux = aux.sig
        if (aux2):
            print("el anio buscado no se encuentra")

    def barrido_recaudacion(self):
        aux = self.__inicio
        max = aux.sig
        while(aux is not None):
            if (aux.info.recaudacion > max.info.recaudacion):
                max = aux
            aux = aux.sig
        print(f'datos pelicula que mas recaudo {max.info}')

    def barrido_valoracion_publico(self):
        aux = self.__inicio
        max = aux.sig
        while(aux is not None):
            if (aux.info.valoracion > max.info.valoracion):
                max = aux
            aux = aux.sig
        print(f'datos pelicula con mas valoracion del publico: {max.info}')


    def barrido_padawan_yoda(self):
        aux = self.__inicio
        aux2 = True
        while(aux is not None):
            if(aux.info.maestro == "Yoda"):
                print(aux.info)
                aux2 = False
            aux = aux.sig

        if aux2:
            print('el jedi no tiene padawan')

    def barrido_padawan_luke(self):
        aux = self.__inicio
        aux2 = True
        while(aux is not None):
            if(aux.info.maestro == "Luke Skywalker"):
                print(aux.info)
                aux2 = False
            aux = aux.sig

        if aux2:
            print('el jedi no tiene padawan')

    def barrido_padawan_QuiGonJin(self):
        aux = self.__inicio
        aux2 = True
        while(aux is not None):
            if(aux.info.maestro == "Qui-Gon Jin"):
                print(aux.info.nombre)
                aux2 = False
            aux = aux.sig

        if aux2:
            print('el jedi no tiene padawan')

    def barrido_padawan_MaceWindu(self):
        aux = self.__inicio
        aux2 = True
        while(aux is not None):
            if(aux.info.maestro == "Mace Windu"):
                print(aux.info.nombre)
                aux2 = False
            aux = aux.sig

        if aux2:
            print('el jedi no tiene padawan')

    def barrido_especie_humana(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.especie == 'humana'):
                print(aux.info.nombre)
            aux = aux.sig

    def barrido_especie_twilek(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.especie == 'twilek'):
                print(aux.info.nombre)
            aux = aux.sig


    def barrido_jedi_conmienza_con_A(self):
        aux = self.__inicio
        while(aux is not None):
            if(aux.info.nombre[0] == 'A'):
                print(aux.info.nombre)
            aux = aux.sig

    def barrido_jedi_mas_de_un_color(self):
        aux = self.__inicio
        while(aux is not None):
            if(len(aux.info.color_sable) > 1):
                print(f'{aux.info.nombre} - {aux.info.color_sable}')
            aux = aux.sig


    def barrido_jedi_amarillo_violeta(self):
        aux = self.__inicio
        while(aux is not None):
            if('amarillo' in aux.info.color_sable or 'violeta' in aux.info.color_sable):
                print(f'{aux.info.nombre} - {aux.info.color_sable}')
            aux = aux.sig
