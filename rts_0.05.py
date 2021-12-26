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

repeticion = False
companion = ""
nafta = False
arrancar = False
yerba = False
aceite = False
aire = False
vamos = False
hora = ""
musica = ""

while True:

 

    def path5():
        print()
        print("Seguimos viaje. Continuara...")
        print()
        print("================================================")
        print()

    def path4():
        radio = input("Quieres cambiar la música? (si/no) ").lower().strip()
        if radio[0] == "s":
            if companion == "juanma" or companion == "Juanma" or companion == "JUANMA":
                print()
                print("_" + companion + ": Ah... bueno...")
                pathJ()
            else:
                path3()
        elif radio[0] == "n":
            path5()
        else:
            path3()


    def pathJ():
        global musica
        print()
        musica = input("Qué deseas escuchar? ").lower().strip()
        if musica == "red hot chili peppers" or musica == "rhcp" or musica == "red hot" or musica == "chili peppers" or musica == "red hot chili pepers":
            musica1 = "♫ Suena 'Scar Tissue', de los Red Hot Chili Peppers. ♫"
            print()
            print(musica1)
            print()
            print("_" + companion + ": Altísima banda, no? Uh es un discazo este, un tema mejor que el otro.")
            print("         Escuchá lo que es este solo de Frusciante, una locura.")
            print()
            path4()
        else:
            musica1 = ": Ah no querés escuchar los Red Hot...? Otra cosa? Uh perdón no traje nada, pensé que no íbamos a necesitar."
            print()
            print("_" + companion + musica1)
            pathJ()   

    def path3a():
        if companion == "juanma" or companion == "Juanma" or companion == "JUANMA":
            pathJ()
        else:
            path3()



    def path3():
        global musica
        print()
        musica = input("Qué deseas escuchar? ").lower().strip()

        if musica == "red hot chili peppers" or musica == "rhcp" or musica == "red hot" or musica == "chili peppers":
                musica1 = "♫ Suena 'Scar Tissue'. ♫ "
                print()
                print(musica1)
                print("No hay otro tema mejor para un viaje en la ruta.")
                print()
                path4()
        elif musica == "strokes" or musica == "the strokes":
            musica1 = "♫ Suena 'You Only Live Once.' ♫"
            print()
            print(musica1)
            print("Qué gran banda!")
            print()
            path4()
        elif musica == "bowie" or musica == "david bowie":
            musica1 = "♫ Suena 'The Man Who Sold The World'. ♫"
            print()
            print(musica1)
            print("Leyenda.")
            print()
            path4()
        elif musica == "beatles" or musica == "the beatles" or musica == "los beatles":
            musica1 = "♫ Suena 'Strawberry Fields Forever'. ♫"
            print()
            print(musica1)
            print("Living is easy with eyes closed.")
            print()
            path4()
        elif musica == "taylor swift" or musica == "taylor" or musica == "swift":
            musica1 = "♫ Suena 'I Knew You Were Trouble (Taylor's Version)'. ♫"
            print()
            print(musica1)
            print("Me pregunto qué habrá sido de esa bufanda.")
            print()
            path4()
        elif musica == "queen" or musica == "freddie" or musica == "freddie mercury":
            musica1 = "♫ Suena 'Don't Stop Me Now'! ♫"
            print()
            print(musica1)
            print("Y el auto parece un karaoke.")
            print()
            path4()
        elif musica == "gorillaz":
            musica1 = "♫ Suena 'Feel Good Inc'. ♫"
            print()
            print(musica1)
            print("Feel Good.")
            print()
            path4()
        elif musica == "coldplay":
            musica1 = "♫ Suena 'The Scientist'. ♫"
            print()
            print(musica1)
            print("Come up to meet you, tell you I'm sorryyyyy, you don't know how lovely you aaaaaaaaare. Justo en el cora.")
            print()
            path4()
        elif musica == "dua lipa" or musica == "dualipa" or musica == "dua":
            musica1 = "♫ Suena 'Love Again'. ♫"
            print()
            print(musica1)
            print("Nada mal.")
            print()
            path4()
        elif musica == "bersuit" or musica == "bersuit vergarabat":
            musica1 = "♫ Suena 'Toco y Me Voy'. ♫"
            print()
            print(musica1)
            print("Me gustaba mucho esta banda en sus buenos días.")
            print()
            path4()
        elif musica == "redondos" or musica == "patricio rey" or musica == "los redondos" or musica == "indio" or musica == "indio solari":
            musica1 = "♫ Suena 'Ella Debe Estar Tan Linda'. ♫"
            print()
            print(musica1)
            print("Conduje toda la noche! Reventando los cambios! Con mis ojos de durax las ti ma dos! Qué banda")
            print()
            path4()
        elif musica == "wos" or musica == "wosito":
            musica1 = "♫ Suena 'Melón Vino.' ♫"
            print()
            print(musica1)
            print("Tengo estudio y un colchón, tengo amigos un montón.")
            print()
            path4()
        elif musica == "rolling stones" or musica == "stones" or musica == "rolling" or musica == "los stones":
            musica1 = "♫ Suena 'Start Me Up.' ♫"
            print()
            print(musica1)
            print()
            path4()
        elif musica == "billie" or musica == "billie eilish" or musica == "bilie eilish":
            musica1 = "♫ Suena 'Whish You Were Gay.' ♫"
            print()
            print(musica1)
            print()
            path4()
        elif musica == "cowboy bebop" or musica == "yoko kanno" or musica == "seatbelts" or musica == "the seatbelts":
            musica1 = "♫ Suena 'TANK.' ♫"
            print()
            print(musica1)
            print("OK 3, 2, 1 LETS JAM")
            print()
            path4()
        elif musica == "evangelion" or musica == "opening evangelion" or musica == "neon genesis evangelion" or musica == "zankoku na tenshi" or musica == "zankoku":
            musica1 = "♫ Suena el opening de Evangelion, 'Cruel Angel's Thesis' ♫"
            print()
            print(musica1)
            print("ZAN KOKU NA TENSHI NO YOU NI")
            print("Congratulations!")
            print()
            path4()

        elif musica == "CAMBIAR" or musica == "CAMBIARR" or musica == "CAMBIARRR":
            musica1 = "♫ Suena 'CAMBIAR.' ♫"
            print()
            print(musica1)
            print("CAMBIAR")
            print()
            path4()
            
        elif musica == "rock" or musica == "pop" or musica == "cumbia" or musica == "punk" or musica == "musica clasica" or musica == "clasica" or musica == "metal" or musica == "cuarteto":
            musica1 = "Qué banda?"
            print(musica1)
            path3()
                
        else:
            musica1 = "No hay señal y no tengo conmigo nada de esa banda."
            print()
            print(musica1)
            path3()      




    def path2():
        global hora
        print()
        hora = input("El viaje comenzó a la (mañana/tarde/noche) ").lower().strip()
        if hora != "mañana" and hora != "tarde" and hora != "noche" and hora != "m" and hora != "t" and hora != "n":
            path2()
        else:
            if hora == "mañana" or hora == "m":
                hora = "mañana"
                hora1 = "Fue la decisión correcta. Hay poco tráfico, y funciono mejor a esta hora del día. Ya son casi las 10 am, tal vez podríamos desayunar algo en ese conocido parador cuando lleguemos allí."
                print(hora1)
                print("La " + hora + " es perfecta para poner un poco de música")
                path3a()
            elif hora == "tarde" or hora == "t":
                hora = "tarde"
                hora1 = "Podríamos haber salido más temprano, pero los preparativos llevaron más tiempo del que esperaba. Hay tráfico. La fila de autos se desplaza de forma fluída, pero llega hasta donde la vista puede alcanzar. Tal vez podríamos tomar algo cuando lleguemos al conocido parador y esperar que el tráfico cambie un poco."
                print(hora1)
                print("La " + hora + " es perfecta para poner un poco de música")
                path3a()
            else:
                hora = "noche"
                hora1 = "Creo que fue la mejor decisión. Practicamente no hay otros autos, la mayor parte de los que viajan seguro saldrá mañana. Nos deslizamos por la autopista rápidamente, y ya pronto estaremos en la ruta. Tal vez podríamos tomar un café en ese conocido parador cuando lleguemos allí."   
                print(hora1)
                print("La " + hora + " es perfecta para poner un poco de música")
                path3a()


    def path1():
        global nafta
        global arrancar
        global yerba
        global vamos
        global aire
        global aceite
        secondPath = input("Qué deseas hacer? No olvides nada! (nafta/cubiertas/aceite/vamos!/...) ").lower().strip()


        if secondPath == "arrancar" or secondPath == "encender" or secondPath == "poner en marcha" or secondPath == "encender auto" or secondPath == "contacto" or secondPath == "marcha" or secondPath == "llave" or secondPath == "prender" or secondPath == "x":
            if arrancar == True:
                print()
                print("El motor ya está en marcha. Listos para salir.")
                path1()
            else:
                print()
                print("Enciendes el auto y el motor vibra suavemente. Estamos listos para partir!")
                arrancar = True
                path1()

        elif secondPath == "nafta" or secondPath == "n":
            if nafta == True:
                print()
                print("Tanque lleno.")
                path1()
            else:
                print()
                print("Llenas el tanque, siempre es una buena idea antes de viajar.")
                nafta = True
                path1()

        elif secondPath == "cubiertas" or secondPath == "c" or secondPath == "aire":
            if aire == True:
                print()
                print("Aire listo.")
                path1()
            else:
                print()
                print("Chequeas las cubiertas en la estación de servicio, les agregas un poco de aire.")
                aire = True
                path1()

        elif secondPath == "aceite" or secondPath == "a":
            if aceite == True:
                print()
                print("Agua y aceite llenos.")
                path1()
            else:
                print()
                print("Levantas el capot y agregas un poco de agua y aceite.")
                aceite = True
                path1()

        elif secondPath == "yerba" or secondPath == "mate" or secondPath == "bombilla":
            if yerba == True:
                print()
                print("Todo listo para el mate.")
                path1()
            else:
                print()
                print("Mejor no olvidar la yerba! Un viaje no es un viaje sin unos buenos mates, eso dicen.")
                yerba = True
                path1()

        elif secondPath == "...":
                print()
                print("► Prueba diferentes palabras, o si lo necesitas escribe 'ayuda'. ◄")
                path1()

        elif secondPath == "ayuda" or secondPath == "help":
                print()
                print("===================================================================================================")
                print("Road Trip Simulator - 2021")
                print("Autor: Guido Cano")
                print("===================================================================================================")
                print("► Bienvenidos a RTS! ◄")
                print("A lo largo del juego, las opciones simples pueden accionarse escribiendo solo su primera letra.")
                print("Aquí debes escribir la palabra completa, prueba con diferentes cosas que te ayudarán en tu viaje.")
                print("Si no sabes cómo seguir, tal vez sea una buena idea subirse al auto y ponerlo en marcha.")
                print("Espero que disfrutes el viaje!")
                print("===================================================================================================")
                print()
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
                print("Pronto están en la 9 de Julio subiendo a la Autopista Buenos Aires - La Plata.")
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
        global repeticion
        path1 = ""
        while path1 != "si" and path1 != "no" and path1 != "n" and path1 != "s":
            if repeticion == True:
                path1 = input ("Quieres volver a viajar? (si/no) ").lower().strip()
            else:
                path1 = input ("Quieres comenzar un viaje? (si/no) ").lower().strip()
        return path1[0]

    if choose1() == "s":
        repeticion = True
        print()
        print("Finalmente te decides y comienzas con los preparativos!")
        print("Realizas los controles necesarios al auto y le haces una visita a tu mecánico de confianza.")
        print("Pasas por el lavadero y te tomas un cafe mientras terminan el trabajo, mirando a la gente pasar por Avenida Rivdavia.")
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



