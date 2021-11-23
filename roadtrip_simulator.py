print()
print("================================================")
print("=                _.--------._                  =")
print("=              ,'.----------.',                =")
print("=             /='------------`=\               =")
print("=           .F_______...._______Y.             =")
print("=           |(_)(_) ______ (_)(_)|             =")
print("=           (....__|RTS021|__....)             =")
print("=            | |    ~~~~~~    | |              =")
print("=            `-'              `-'              =")
print("=      Bienvenido a Road Trip Simulator!       =")
print("================================================")
print()

while True:

    companion = ""
    nafta = False
    arrancar = False
    yerba = False
    aceite = False
    aire = False
    vamos = False
    hora = ""
    musica = ""
    

    def path5():
        print()
        print("Seguimos viaje. Continuara...")
        print()
        print("================================================")
        print()

    def path4():
        radio = input("Quieres cambiar la música? (si/no) ").lower().strip()
        if radio == "si":
            path3()
        elif radio == "no":
            path5()
        else:
            path3()


   
    def path3():
        global musica
        print()
        musica = input("Qué deseas escuchar? ").lower().strip()

        if companion == "juanma" or companion == "Juanma" or companion == "JUANMA":
            if musica == "red hot chili peppers" or musica == "rhcp" or musica == "red hot" or musica == "chili peppers":
                musica1 = "Suena 'Scar Tissue', de los Red Hot Chili Peppers."
                print()
                print(musica1)
                print("_" + companion + ": Altísima banda, no? Uh es un discazo este, un tema mejor que el otro. Escuchá lo que es este solo de Frusciante, una locura.")
                print()
                path4()
            else:
                musica1 = ": Ah no querés escuchar los Red Hot...? Otra cosa? Uh perdón no traje nada, pensé que no íbamos a necesitar."
                print()
                print("_" + companion + musica1)
                path3()

        if  companion != "Juanma" and companion != "juanma" and companion != "JUANMA":
            if musica == "red hot chili peppers" or musica == "rhcp" or musica == "red hot" or musica == "chili peppers":
                musica1 = "Suena 'Scar Tissue'. No hay otro tema mejor para un viaje en la ruta."
                print()
                print(musica1)
                path4()
        elif musica == "strokes" or musica == "the strokes":
            musica1 = "Suena 'You Only Live Once', qué gran banda!"
            print()
            print(musica1)
            path4()
        elif musica == "bowie" or musica == "david bowie":
            musica1 = "Suena The Man Who Sold The World, de Bowie. Leyenda."
            print()
            print(musica1)
            path4()
        elif musica == "beatles" or musica == "the beatles" or musica == "los beatles":
            musica1 = "Suena 'Strawberry Fields Forever.'"
            print()
            print(musica1)
            path4()
        elif musica == "taylor swift" or musica == "taylor" or musica == "swift":
            musica1 = "Suena 'I Knew You Were Trouble (Taylor's Version)'. No se si es mi estilo pero me pregunto qué habrá pasado con esa bufanda."
            print()
            print(musica1)
            path4()
        elif musica == "queen" or musica == "freddie" or musica == "freddie mercury":
            musica1 = "Suena 'Don't Stop Me Now'! Y el auto parece un karaoke."
            print()
            print(musica1)
            path4()
        elif musica == "gorillaz":
            musica1 = "'Feel Good' sonando."
            print()
            print(musica1)
            path4()
        elif musica == "coldplay":
            musica1 = "Come up to meet you, tell you I'm sorryyyyy, you don't know how lovely you aaaaaaaaare. Justo en el cora."
            print()
            print(musica1)
            path4()
        elif musica == "dua lipa" or musica == "dualipa" or musica == "dua":
            musica1 = "Suena 'Love Again'. Nada mal."
            print()
            print(musica1)
            path4()
        elif musica == "bersuit" or musica == "bersuit vergarabat":
            musica1 = "'Te la toco de primera, vos si querés me la das. Cada jugada que sueño se hace realidad.'"
            print()
            print(musica1)
            path4()
        elif musica == "redondos" or musica == "patricio rey" or musica == "los redondos" or musica == "indio" or musica == "indio solari":
            musica1 = "'Conduje toda la noche! Reventando los cambios! Con mis ojos de durax las ti ma dos!' Qué banda."
            print()
            print(musica1)
            path4()
            
        elif musica == "rock" or musica == "pop" or musica == "cumbia" or musica == "punk" or musica == "musica clasica" or musica == "clasica" or musica == "metal" or musica == "cuarteto":
            musica1 = "Qué banda?"
            print(musica1)
            path3()
                
        else:
            if companion != "Juanma" and companion != "juanma" and companion != "JUANMA":
                musica1 = "No hay señal y no tengo conmigo nada de esa banda."
                print()
                print(musica1)
                path3()      




    def path2():
        global hora
        print()
        hora = input("Finalmente comenzamos a viajar a la (mañana/tarde/noche) ").lower().strip()
        if hora != "mañana" and hora != "tarde" and hora != "noche":
            path2()
        else:
            if hora == "mañana":
                hora1 = "Fue la decisión correcta. Hay poco tráfico, y funciono mejor a esta hora del día. Ya son casi las 10 am, tal vez podríamos desayunar algo en ese conocido parador cuando lleguemos allí."
                print(hora1)
                print("La " + hora + " es perfecta para poner un poco de música")
                path3()
            elif hora == "tarde":
                hora1 = "Podríamos haber salido más temprano, pero los preparativos llevaron más tiempo del que esperaba. Hay tráfico. La fila de autos se desplaza de forma fluída, pero llega hasta donde la vista puede alcanzar. Tal vez podríamos tomar algo cuando lleguemos al conocido parador y esperar que el tráfico cambie un poco."
                print(hora1)
                print("La " + hora + " es perfecta para poner un poco de música")
                path3()
            else:
                hora1 = "Creo que fue la mejor decisión. Practicamente no hay otros autos, la mayor parte de los que viajan seguro saldrá mañana. Nos deslizamos por la autopista rápidamente, y ya pronto estaremos en la ruta. Tal vez podríamos tomar un café en ese conocido parador cuando lleguemos allí."   
                print(hora1)
                print("La " + hora + " es perfecta para poner un poco de música")
                path3()



    def path1():
        global nafta
        global arrancar
        global yerba
        global vamos
        global aire
        global aceite
        secondPath = input("Qué deseas hacer? No olvides nada! (nafta/aire/aceite/vamos!/...) ").lower().strip()

        if secondPath == "arrancar" or secondPath == "encender" or secondPath == "poner en marcha" or secondPath == "encender auto" or secondPath == "contacto" or secondPath == "a":
            if arrancar == True:
                print()
                print("El motor ya esta en marcha.")
                path1()
            else:
                print()
                print("Enciendes el auto y el motor vibra suavemente. Estamos listos para partir!")
                arrancar = True
                path1()

        elif secondPath == "nafta":
            if nafta == True:
                print()
                print("Tanque lleno.")
                path1()
            else:
                print()
                print("Llenas el tanque, siempre es una buena idea antes de viajar.")
                nafta = True
                path1()

        elif secondPath == "aire":
            if aire == True:
                print()
                print("Cubiertas listas.")
                path1()
            else:
                print()
                print("Chequeas las cubiertas en la estación de servicio, todo está en orden.")
                aire = True
                path1()

        elif secondPath == "aceite":
            if aceite == True:
                print()
                print("Aceite y agua llenos.")
                path1()
            else:
                print()
                print("Levantas el capot y el agua y el aceite están al máximo en los medidores.")
                aceite = True
                path1()

        elif secondPath == "yerba":
            print()
            print("Mejor no olvidar la yerba! Un viaje no es un viaje sin unos buenos mates, eso dicen.")
            path1()

        elif secondPath == "vamos" or secondPath == "salir" or secondPath == "vamos!" or secondPath == "v":
            if vamos == True and arrancar == False:
                print()
                print("Ya están sentados y listos. El auto no está en marcha.")
                path1()
            elif arrancar == True:
                print()
                print("Todo listo!! El auto acelera por Avenida San Juan y se abre paso por las calles de Buenos Aires.")
                print()
                print("Pronto están en la 9 de Julio y suben a la Autopista Buenos Aires - La Plata.")
                print("Aún con las ventanillas altas se escucha el ruido del asfalto bajo las cubiertas.")
                print(companion + " bromea sobre una imágen que ve en su celular.")
                print("La imágen compara un perro grande y un perro chiquito con diferentes tipos de plantas. Imita una voz divertida:")
                print("'Me regaste y el agua estaba muy fría, ahora debo morir.' Ambos ríen.")
                print("Memes, el nuevo lenguaje universal.")
                path2()
            else:
                print()
                print("Se suben al auto. Por dentro también reluce, y huele a lavanda. No está en marcha.")
                vamos = True
                path1()
                   
        else:
            path1()



    def choose1():
        path1 = ""
        while path1 != "si" and path1 != "no":
            path1 = input ("Quieres comenzar un viaje? (si/no) ").lower().strip()
        return path1

    if choose1() == "si":
        print()
        print("Finalmente te decides y comienzas con los preparativos!")
        print("Realizas los controles necesarios al auto, agregas agua y aceite, visitas a tu mecánico de confianza.")
        print("Pasas por el lavadero, y mientras terminan el trabajo te tomas un cortado, mirando a la gente pasar por Avenida Rivdavia.")
        print("Pronto tendrás unos días libres, y has decidido pasarlos en la costa.")
        print()
        companion = input("Desde el comienzo sabías a quién le dirías que te acompañe. (Nombre) ")
        print()
        print("Se lo preguntaste una tarde entre mate y mate, y " + companion + " aceptó de inmediato.")
        print("_Un viaje a la costa, y manejás vos? Dónde firmo?")
        print()
        print("---")
        print()
        print("Llega el día, y ya está casi todo listo.")
        print("Pasas por la casa de " + companion + " y cargan su bolso en el baúl.")
        path1()
    else:
        print("Será en otro momento!")
        print()
        print("================================================")
        print()



