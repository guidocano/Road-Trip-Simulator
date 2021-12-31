
repeticion = False
companion = ""
nafta = False
arrancar = False
yerba = False
aceite = False
aire = False
vamos = False
agua = False
mapa = False
celular = False
cambio = False
comida = False
musicaviaje = False
bolsos = False
yerba2 = False
frenos = False

contador = 0
rta1 =""

hora = ""
musica = ""
import time
import sys
a = 1.5
b = 1
c = 0.06
d = 0.3


print()
print(" =================================================")
print("||                _.---------._                  ||")
print("||              ,'.-----------.',                ||")
print("||             /='-------------`=\               ||")
print("||           .F_______....._______Y.             ||")
print("||           |(_)(_) _______ (_)(_)|             ||")
print("||           (....__|RTS.014|__....)             ||")
print("||            | |    ~~~~~~~    | |              ||")
print("||            `-'               `-'              ||")
print("||      Bienvenidos a Road Trip Simulator!       ||")
print(" =================================================")
print()
time.sleep(1)


while True:

    def path12():
        time.sleep(b)
        print()
        print("Avanzamos por la Ruta 2.")

        time.sleep(b)
        print()
        print("Continuará.")
        print()
        print("===========================================================================================")
        time.sleep(b)
        print()


    def path11():
        time.sleep(a)
        print()
        print("          {")
        print("      {    }")
        print("       }__{ __{")
        print("    .-{   }    }-.")
        print("   (   }      {   )")
        print("   |`-..______..-'|")
        print("   |              ;--.")
        print("   |             (__  \\")
        print("   |              | )  )")
        print("   |              |/  /")
        print("   |              /  /")
        print("   |             (  /")
        print("   \              y'")
        print("    `-..______..-'")
        print()
        print()
        d1 = '"Pero este café es como un indulto, che, algo terriblemente conciliatorio."'
        for character in d1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
        print()
        d2 = '"Y las medialunas no están nada mal."'
        for character in d2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
        time.sleep(b)
        print()
        print()
        print("Pronto seguiremos camino.")
        path12()




    def path10():
        print()
        bar = input ("Quieres entrar al bar? (si/no) ")
        if bar == "si" or bar == "s":
            path11()
        elif bar == "no" or bar == "n":
            time.sleep(b)
            print()
            print("No nos demoramos y seguimos camino.")
            path12()
        else:
            path10()





    def path9():
        if hora == "mañana":
            print("No hay tanta gente estacionada.")
            print("La mañana está agradable, y tenemos todo el día por delante.")
            print("La ruta sigue tranquila. Creo que estoy listo para un buen desayuno antes de seguir.")
            print("Haces un chequeo rápido del auto, todo está en orden. [salud +1]")
            path10()
        elif hora == "tarde":
            print("El estacionamiento está repleto.")
            print("Cerca nuestro una familia se baja del auto, son 4, y un perro.")
            print("Se escuchan bocinas desde la ruta. Comienza a hacer un poco de calor.")
            print("Haces un chequeo rápido del auto, todo está en orden. [salud +1]")
            path10()
        else:
            print("La noche está tranquila y solo hay otros dos autos estacionados.")
            print("Todo está en silencio. Un gran camión pasa rápidamente por la ruta.")
            print("El cielo está despejado y comienzan a verse algunas formaciones de estrellas.")
            print("Haces un chequeo rápido del auto, todo está en orden. [salud +1]")
            path10()




    def path8():
        parador = input("Qué deseas hacer? (parar/seguir) ")

        if parador == "parar" or parador == "p" or parador == "estacionar" or parador == "e":
            time.sleep(b)
            print()
            print("Una pausa suena como una buena idea. Tomar un café, recargar energías.")
            print("Tomamos la primera salida, aparcamos y bajamos del coche.")
            print("Tus piernas te lo agradecen.")
            time.sleep(b)
            print()
            path9()
            
          
        elif parador == "seguir" or parador == "s":
            time.sleep(b)
            print()
            print("Aún no estoy cansado, será mejor seguir por ahora.")
            time.sleep(b)
            path12()

        else:
            time.sleep(b)
            path8()


    def path7():
        time.sleep(b)
        print()
        print("A lo lejos se divisa el gran cartel blanco y negro del parador.")
        print("Tal vez podríamos detenernos y estirar un poco las piernas.")
        time.sleep(b)
        print()
        path8()


    def path6():
        time.sleep(b)
        print()
        charla = input("De qué quieres hablar? (planes/salud/viaje) ")

        if charla == "planes" or charla == "p":
            print()
            d2 = '"Desde que regresé a Buenos Aires me costó adaptarme un poco...'
            for character in d2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(c)
            print()
            d3 = 'Encontrar donde vivir, volver a conseguir trabajo, recuperar mis vínculos.'
            for character in d3:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(c)
            print()
            d4 = 'Una vez que volví a acomodarme todo fue haciéndose más fácil...'
            for character in d4:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(c)
            print()
            d4a = 'Y pude volver a mirar hacia adelante.'
            for character in d4a:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(c)
            print()
            d5 = 'Mis planes? '
            for character in d5:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(c)
            time.sleep(d)
            d5a = 'Te los diré cuando los sepa!'
            for character in d5a:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(c)
            print()
            d6 = 'Pero seguro que tengo algunas buenas ideas!"'
            for character in d6:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(c)
            time.sleep(b)
            print()
            path7()

        elif charla == "salud" or charla == "s":
            print()
            e1 = '"No ha sido fácil...'
            for character in e1:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(c)
            print()
            e2='Al principio la medicación me adormecía mucho...'
            for character in e2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(c)
            print()
            e3='No podía estudiar, no quería ver a nadie. Me aislé.'
            for character in e3:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(c)
            print()
            e4='Hasta que de a poco fui haciendo pie y buscando más ayuda.'
            for character in e4:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(c)
            print()
            e5='Ahora tengo mis días. No te voy a decir que está todo espectacular, pero...'
            for character in e5:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(c)
            print()
            e6='...estoy mucho mejor. Trato de rodearme de lo que me hace bien.'
            for character in e6:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(c)
            print()
            e7='Un poco como este viaje, no?"'
            for character in e7:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(c)
            time.sleep(b)
            print()
            path7()
            
        elif charla == "viaje" or charla == "v":
            print()
            e8 = '"Por qué vine? '
            for character in e8:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(c)
            time.sleep(d)
            e9 = 'Cuando me invitaste estaba en uno de esos momentos...'
            for character in e9:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(c)
            print()
            e10= 'Digamos que necesitaba tomar aire...'
            for character in e10:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(c)
            print()
            e11= 'Te escuché tan entusiasmado con el plan que no pude resistirme.'
            for character in e11:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(c)
            print()
            e12= 'Me lo vendiste tan bien que en algún punto hasta pensé que había sido mi idea.'
            for character in e12:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(c)
            print()
            e13= 'Y mirá, acá estamos. Nada mal, eh?"'
            for character in e13:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(c)
            time.sleep(b)
            print()
            path7()
        else:
            print()
            print("Mejor pregunta algo diferente.")
            path6()

    def path5():
        time.sleep(b)
        print()
        print("La charla fluye mientras pasan los temas de " + musica + ", y " + companion + " resultó ser una buena compañía.")
        print("Antes de darnos cuenta ya estamos avanzando por la Ruta 2.")
        path6()

    def path4():
        radio = input("Quieres cambiar la música? (si/no) ").lower().strip()
        if radio[0] == "s":
            if companion == "juanma" or companion == "Juanma" or companion == "JUANMA":
                time.sleep(b)
                print()
                j4 = companion + ': "Ah... bueno..."'
                for character in j4:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(c)
                print()
                pathJ()
            else:
                path3()
        elif radio[0] == "n":
            path5()
        else:
            path3()


    def pathJ():
        global musica
        time.sleep(b)
        print()
        musica = input("Qué deseas escuchar? ").lower().strip()
        if musica == "red hot chili peppers" or musica == "rhcp" or musica == "red hot" or musica == "chili peppers" or musica == "red hot chili pepers":
            time.sleep(b)
            musica1 = "♫ Suena 'Scar Tissue', de los Red Hot Chili Peppers. ♫"
            print()
            print(musica1)
            time.sleep(b)
            print()
            j2 = (companion + ': "Altísima banda, no? Uh es un discazo este, un tema mejor que el otro."')
            for character in j2:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(c)
            print()
            j3 = '        "Escuchá lo que es este solo de Frusciante, una locura."'
            for character in j3:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(c)
            musica = "los Red Hot Chili Peppers"
            time.sleep(b)
            print()
            print()
            path4()
        else:
            time.sleep(b)
            musica1 = ': "Ah no querés escuchar los Red Hot...? Otra cosa? Uh perdón no traje nada, pensé que no íbamos a necesitar."'
            print()
            j = (companion + musica1)
            for character in j:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(c)
            print()
            pathJ()   

    def path3a():
        if companion == "juanma" or companion == "Juanma" or companion == "JUANMA":
            pathJ()
        else:
            path3()



    def path3():
        global musica
        global contador
        time.sleep(b)
        print()
        musica = input("Qué deseas escuchar? ").lower().strip()

        if musica == "red hot chili peppers" or musica == "rhcp" or musica == "red hot" or musica == "chili peppers" or musica =="red hot chilli peppers" or musica =="red hot chili pepers":
                time.sleep(b)
                musica1 = "♫ Suena 'Scar Tissue'. ♫ "
                print()
                print(musica1)
                print("No hay otro tema mejor para un viaje en la ruta.")
                print()
                musica = "los Red Hot Chili Peppers"
                path4()
        elif musica == "strokes" or musica == "the strokes":
            time.sleep(b)
            musica1 = "♫ Suena 'You Only Live Once.' ♫"
            print()
            print(musica1)
            print("Qué gran banda!")
            print()
            musica = "The Strokes"
            path4()
        elif musica == "bowie" or musica == "david bowie":
            time.sleep(b)
            musica1 = "♫ Suena 'The Man Who Sold The World'. ♫"
            print()
            print(musica1)
            print("Leyenda.")
            print()
            musica = "Bowie"
            path4()
        elif musica == "beatles" or musica == "the beatles" or musica == "los beatles":
            time.sleep(b)
            musica1 = "♫ Suena 'Strawberry Fields Forever'. ♫"
            print()
            print(musica1)
            print("Living is easy with eyes closed.")
            print()
            musica = "los Beatles"
            path4()
        elif musica == "taylor swift" or musica == "taylor" or musica == "swift":
            time.sleep(b)
            musica1 = "♫ Suena 'I Knew You Were Trouble (Taylor's Version)'. ♫"
            print()
            print(musica1)
            print("Me pregunto qué habrá sido de esa bufanda.")
            print()
            musica = "Taylor Swift"
            path4()
        elif musica == "queen" or musica == "freddie" or musica == "freddie mercury" or musica == "freddy":
            time.sleep(b)
            musica1 = "♫ Suena 'Don't Stop Me Now'! ♫"
            print()
            print(musica1)
            print("Y el auto parece un karaoke.")
            print()
            musica = "Queen"
            path4()
        elif musica == "gorillaz" or musica == "gorilaz":
            time.sleep(b)
            musica1 = "♫ Suena 'Feel Good Inc'. ♫"
            print()
            print(musica1)
            print("Feel Good.")
            print()
            musica = "Gorillaz"
            path4()
        elif musica == "coldplay":
            time.sleep(b)
            musica1 = "♫ Suena 'The Scientist'. ♫"
            print()
            print(musica1)
            print("Come up to meet you, tell you I'm sorryyyyy, you don't know how lovely you aaaaaaaaare. Justo en el cora.")
            print()
            musica = "Coldplay"
            path4()
        elif musica == "dua lipa" or musica == "dualipa" or musica == "dua":
            time.sleep(b)
            musica1 = "♫ Suena 'Love Again'. ♫"
            print()
            print(musica1)
            print("Nada mal.")
            print()
            musica = "Dua Lipa"
            path4()
        elif musica == "bersuit" or musica == "bersuit vergarabat":
            time.sleep(b)
            musica1 = "♫ Suena 'Toco y Me Voy'. ♫"
            print()
            print(musica1)
            print("Escuchaba mucho esta banda en sus buenos días.")
            print()
            musica = "Bersuit"
            path4()
        elif musica == "redondos" or musica == "patricio rey" or musica == "los redondos" or musica == "indio" or musica == "indio solari":
            time.sleep(b)
            musica1 = "♫ Suena 'Ella Debe Estar Tan Linda'. ♫"
            print()
            print(musica1)
            print("Conduje toda la noche! Reventando los cambios! Con mis ojos de durax las ti ma dos! Qué banda.")
            print()
            musica = "los Redondos"
            path4()
        elif musica == "wos" or musica == "wosito":
            time.sleep(b)
            musica1 = "♫ Suena 'Melón Vino.' ♫"
            print()
            print(musica1)
            print("Tengo estudio y un colchón, tengo amigos un montón.")
            print()
            musica = "Wos"
            path4()
        elif musica == "rolling stones" or musica == "stones" or musica == "rolling" or musica == "los stones":
            time.sleep(b)
            musica1 = "♫ Suena 'Start Me Up.' ♫"
            print()
            print(musica1)
            print()
            musica = "los Rolling Stones"
            path4()
        elif musica == "billie" or musica == "billie eilish" or musica == "bilie eilish" or musica == "bilie":
            time.sleep(b)
            musica1 = "♫ Suena 'Whish You Were Gay.' ♫"
            print()
            print(musica1)
            print()
            path4()
        elif musica == "cowboy bebop" or musica == "yoko kanno" or musica == "seatbelts" or musica == "the seatbelts":
            time.sleep(b)
            musica1 = "♫ Suena 'TANK.' ♫"
            print()
            print(musica1)
            print("OK 3, 2, 1 LETS JAM")
            print()
            musica = "Cowboy Bebop"
            path4()
        elif musica == "evangelion" or musica == "opening evangelion" or musica == "neon genesis evangelion" or musica == "zankoku na tenshi" or musica == "zankoku":
            time.sleep(b)
            musica1 = "♫ Suena el opening de Evangelion, 'Cruel Angel's Thesis' ♫"
            print()
            print(musica1)
            print("Congratulations!")
            print()
            musica = "Evangelion"
            path4()

        elif musica == "miranda" or musica == "miranda!":
            time.sleep(b)
            musica1 = "♫ Suena 'Traición'. ♫"
            print()
            print(musica1)
            print("Y estamos cantando en el auto.")
            print()
            musica = "Miranda"
            path4()

        elif musica == "greenday" or musica == "green day":
            time.sleep(b)
            musica1 = "♫ Suena 'Jesus of Suburbia' ♫"
            print()
            print(musica1)
            print("I'm the son of rage and love!")
            print()
            musica = "Green Day"
            path4()

        elif musica == "madonna" or musica == "madona":
            time.sleep(b)
            musica1 = "♫ Suena 'Hung Up' ♫"
            print()
            print(musica1)
            print("La reina del pop.")
            print()
            musica = "Madonna"
            path4()

        elif musica == "daft punk" or musica == "daftpunk" or musica == "daft":
            time.sleep(b)
            musica1 = "♫ Suena 'One More Time'. ♫"
            print()
            print(musica1)
            print("Este tema nunca pasa de moda.")
            print()
            musica = "Daft Punk"
            path4()

        elif musica == "lo fi" or musica == "lo fi hip hop" or musica == "lofi" or musica == "lofi hip hop" or musica == "lofi hip hop" or musica == "lofihiphop" or musica == "low fi" or musica == "lowfi" or musica == "lo fi radio" or musica == "lo fi hip hop radio" or musica == "lofi radio":
            time.sleep(b)
            musica1 = "♫ Suena 'Lofi Hip Hop Radio' ♫"
            print()
            print(musica1)
            print("Beats to relax/study. Nunca falla.")
            print()
            musica = "Lofi Hip Hop Radio"
            path4()

        elif musica == "ayuda" or musica == "help" or musica == "lista" or musica == "opciones" or musica == "..." or musica == "no se" or musica == "cualquiera" or musica == "algo" or musica == "cualquier cosa":
            time.sleep(b)
            print()
            print("===========================================================================================")
            print("Pongamos un poco de música!")
            print("Si no has encontrado nada aún, prueba con las bandas más famosas y no fallarás.")
            print("Yo comenzaría con algo de Bowie, Madonna, los Beatles o tal vez los Stones.")
            print("Prueba con diferentes artistas!")
            print("===========================================================================================")
            path3()

        elif musica == "z":
            time.sleep(b)
            print()
            print("ATAJO")
            path7()


        elif musica == "CAMBIAR" or musica == "CAMBIARR" or musica == "CAMBIARRR":
            time.sleep(b)
            musica1 = "♫ Cambiar ♫"
            print()
            print(musica1)
            print("Cambiar")
            print()
            musica = "Nombre"
            path4()
            
        elif musica == "rock" or musica == "pop" or musica == "cumbia" or musica == "punk" or musica == "musica clasica" or musica == "clasica" or musica == "metal" or musica == "cuarteto":
            time.sleep(b)
            print()
            musica1 = "Qué banda?"
            print(musica1)
            path3()
                
        else:
            if contador == 0:
                time.sleep(b)
                contador = contador +1
                print()
                print("No hay señal y no traje conmigo nada de esa banda.")
                path3()
            elif contador == 1:
                time.sleep(b)
                contador = contador +1
                print()
                print("Prueba escribir el nombre de tu artista o banda favorita.")
                path3() 
            elif contador == 2:
                time.sleep(b)
                contador = contador +1
                print()
                print("Si no has tenido suerte intenta con los más conocidos y no fallarás.")
                path3()
            elif contador == 3:
                time.sleep(b)
                contador = contador +1
                print()
                print("Aún nada?")
                path3()  
            elif contador == 4:
                time.sleep(b)
                contador = contador +1
                print()
                print("Si lo deseas puedes escribir 'ayuda'.")
                path3()  
            else: 
                time.sleep(b)
                contador = contador +1
                print()
                print("Lo siento! No tengo nada de ellos.")
                path3()  






    def path2():
        global hora
        print()
        hora = input("El viaje comenzó a la (mañana/tarde/noche) ").lower().strip()
        time.sleep(b)
        print()
        if hora != "mañana" and hora != "tarde" and hora != "noche" and hora != "m" and hora != "t" and hora != "n":
            path2()
        else:
            if hora == "mañana" or hora == "m":
                hora = "mañana"
                print("Fue la decisión correcta. Hay poco tráfico y estoy despierto para manejar.")
                print("Tal vez podríamos desayunar algo en ese conocido parador cuando lleguemos ahí.")
                print("La " + hora + " es perfecta para poner un poco de música.")
                path3a()
            elif hora == "tarde" or hora == "t":
                hora = "tarde"
                print("Podríamos haber salido antes, pero los preparativos llevaron más tiempo del esperado.")
                print("Hay tráfico. La fila de autos llega hasta donde la vista puede alcanzar.")
                print("Tal vez podríamos detenernos en el conocido parador de la ruta y esperar que cambie un poco.")
                print("La " + hora + " es perfecta para poner un poco de música.")
                path3a()
            else:
                hora = "noche"
                print("Creo que fue la mejor decisión. Casi no hay otros autos, la mayoría seguro saldrá mañana.")
                print("Nos deslizamos por la autopista rápidamente, y ya pronto estaremos en la ruta.")
                print("Tal vez luego podamos tomar un café en ese conocido parador.")
                print("La " + hora + " es perfecta para poner un poco de música.")
                path3a()


    def path1():
        global nafta
        global arrancar
        global yerba
        global vamos
        global aire
        global aceite
        global agua
        global mapa
        global celular
        global cambio
        global comida
        global musicaviaje
        global bolsos
        global yerba2
        global frenos
        secondPath = input("Qué deseas hacer? No olvides nada! (nafta/cubiertas/aceite/vamos!/.../ayuda) ").lower().strip()


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

        elif secondPath == "frenos" or secondPath == "pastilla de frenos":
            if frenos == True:
                print()
                print("Funcionan correctamente.")
                path1()
            else:
                print()
                print("Todo parece estar en orden. Revisé los frenos con mi mecánico antes de salir.")
                frenos = True
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

        elif secondPath == "agua" or secondPath == "gaseosa" or secondPath == "jugo" or secondPath == "hielo":
            if agua == True:
                print()
                print("Ya tengo.")
                path1()
            else:
                print()
                print("Botellas de agua listas y bien frías.")
                agua = True
                path1()

        elif secondPath == "mapa" or secondPath == "direccion" or secondPath == "direcciones" or secondPath == "mapas":
            if mapa == True:
                print()
                print("Mapa preparado!")
                path1()
            else:
                print()
                print("Llevaré mi viejo y confiable mapa de las rutas argentinas. Por si hay problemas de señal.")
                mapa = True
                path1()

        elif secondPath == "celular" or secondPath == "celu" or secondPath == "telefono" or secondPath == "gps":
            if celular == True:
                print()
                print("Celular listo y cargado.")
                path1()
            else:
                print()
                print("Mejor no olvidar mi teléfono. Mi gps vive allí.")
                celular = True
                path1()

        elif secondPath == "cambio" or secondPath == "monedas" or secondPath == "dinero" or secondPath == "plata" or secondPath == "efectivo" or secondPath == "billetes":
            if cambio == True:
                print()
                print("Dinero en efectivo, listo.")
                path1()
            else:
                print()
                print("Agarro un poco de dinero y me aseguro de tener cambio para los peajes.")
                cambio = True
                path1()

        elif secondPath == "comida" or secondPath == "alimento" or secondPath == "alimentos" or secondPath == "sandwich" or secondPath == "sandwiches" or secondPath == "sandwichs" or secondPath == "pan" or secondPath == "galletas" or secondPath == "galletitas" or secondPath == "fruta" or secondPath == "frutas" or secondPath == "chocolate" or secondPath == "sandwiches de miga" or secondPath == "sandwichitos de miga" or secondPath == "almuerzo" or secondPath == "vianda" or secondPath == "bianda" :
            if comida == True:
                print()
                print("Sandwiches listos en el bolso.")
                path1()
            else:
                print()
                print("Preparé unos sandwiches para el camino, mejor no olvidarlos.")
                comida = True
                path1()

        elif secondPath == "musica" or secondPath == "spotify" or secondPath == "temas" or secondPath == "cds":
            if musicaviaje == True:
                print()
                print("Ya llevo música, de todo un poco.")
                path1()
            else:
                print()
                print("Música lista y cargada en el celu.")
                musicaviaje = True
                path1()

        elif secondPath == "bolsos" or secondPath == "bolso" or secondPath == "valija" or secondPath == "valijas" or secondPath == "maleta" or secondPath == "maletas" or secondPath == "equipaje":
            if bolsos == True:
                print()
                print("Los bolsos ya están en el  baúl.")
                path1()
            else:
                print()
                print("Valijas listas y en el baúl.")
                bolsos = True
                path1()

        elif secondPath == "flores" or secondPath == "verde" or secondPath == "maria" or secondPath == "charuto" or secondPath == "thc" or secondPath == "marihuana" or secondPath == "hierva" or secondPath == "hierba" or secondPath == "fafafa" or secondPath == "fasito" or secondPath == "faso" or secondPath == "prensado" or secondPath == "mariguana" or secondPath == "droga" or secondPath == "drogas" or secondPath == "canabis" or secondPath == "cannabis" or secondPath == "porrito" or secondPath == "porro" or secondPath == "porros":
            if yerba2 == True:
                print()
                print("Flores listas, de mi cosecha. Huelen bien!")
                path1()
            else:
                print()
                print("Casi lo olvido! Llevaré unas flores para cuando lleguemos a destino.")
                yerba2 = True
                path1()

        elif secondPath == "z":
                print()
                print("ATAJO")
                path7()

        elif secondPath == "...":
                print()
                print("► Prueba diferentes cosas que te sirvan en tu viaje, o puedes escribir 'ayuda'. ◄")
                path1()

        elif secondPath == "ayuda" or secondPath == "help":
                time.sleep(b)
                print()
                print("===========================================================================================")
                print("Road Trip Simulator (2022) - Versión 0.14")
                print("Autor: Guido Cano ")
                print("===========================================================================================")
                print("► Bienvenidos a RTS! ◄")
                print("Falta poco para salir! Prueba escribir diferentes cosas que te ayudarán en tu viaje")
                print("Intenta con términos simples, de una o dos palabras.")
                print("Si no sabes cómo seguir, tal vez sea una buena idea subirse al auto y ponerlo en marcha.")
                print("Luego, las opciones prefijadas pueden responderse escribiendo solo su primera letra.")
                print("Presiona 'ayuda' cada vez que lo necesites.")
                print("Espero que lo disfrutes!")
                print("===========================================================================================")
                time.sleep(b)
                print()
                path1()                   


        elif secondPath == "vamos" or secondPath == "salir" or secondPath == "vamos!" or secondPath == "salir" or secondPath == "partir" or secondPath == "v":
            if vamos == True and arrancar == False:
                print()
                print("Ya están sentados y listos. El auto no está en marcha.")
                path1()
            elif arrancar == True:
                time.sleep(b)
                print()
                print("Todo listo!!")
                time.sleep(b)
                print()
                print("El auto acelera por Avenida San Juan y se abre paso por las calles de Buenos Aires.")
                print("Pronto están en la 9 de Julio subiendo a la autopista.")
                print("Aún con las ventanillas altas se escucha el sonido del asfalto.")
                print(companion + " bromea sobre una imágen que ve en su celular.")
                print("La imágen compara un perro grande y un perro chiquito con diferentes tipos de plantas.")
                print("Hace una voz graciosa:")
                print('"Me regaste y el agua estaba muy fría, ahora debo morir." Ambos ríen.')
                print("Memes, el nuevo lenguaje universal.")
                time.sleep(b)
                path2()
            else:
                print()
                print("Se suben al auto. Por dentro también reluce, y huele a lavanda. No está en marcha.")
                vamos = True
                path1()
                    
        else:
            path1()


    def inicio():
        global repeticion
        global rta1
        rta1 = ""
        while rta1 != "si" and rta1 != "no" and rta1 != "n" and rta1 != "s" and rta1 != "z":
            if repeticion == True:
                time.sleep(b)
                rta1 = input ("Quieres volver a viajar? (si/no) ").lower().strip()
            else:
                time.sleep(b)
                rta1 = input ("Quieres comenzar un viaje? (si/no) ").lower().strip()
        return rta1[0]

    if inicio() == "s":
        repeticion = True
        print()
        time.sleep(b)
        print("Te decides y comienzas con los preparativos!")
        print("Realizas los controles necesarios y le haces una visita a tu mecánico de confianza.")
        print("Pasas por el lavadero y te tomas un café mientras esperas, mirando a la gente pasar por Avenida Rivadavia.")
        print("Pronto tendrás unos días libres, y has decidido pasarlos en la costa.")
        print()
        time.sleep(b)
        companion = input("Desde el comienzo sabías a quién le dirías que te acompañe. (Nombre) ")
        print()
        time.sleep(b)
        print("Se lo preguntaste una tarde entre mate y mate, y " + companion + " aceptó de inmediato.")
        print()
        time.sleep(b)
        d1 = '"Un viaje a la costa, y manejás vos?'
        for character in d1:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
        time.sleep(d)
        d2 = ' Dónde firmo?"'
        for character in d2:
            sys.stdout.write(character)
            sys.stdout.flush()
            time.sleep(c)
        print()
        print()
        print("                       ---")
        print()
        time.sleep(b)
        print("Llegó el día, y ya está casi todo listo.")
        print("Pasas por la casa de " + companion + " y cargan su bolso en el baúl.")
        print()
        path1()
        
    else:
        if rta1 == "z":
            path7()
        else:
            time.sleep(b)
            print()
            print("Será en otro momento!")
            print()


# print()
# print(" =================================================")
# print("||                _.---------._                  ||")
# print("||              ,'.-----------.',                ||")
# print("||             /='-------------`=\               ||")
# print("||           .F_______....._______Y.             ||")
# print("||           |(_)(_) _______ (_)(_)|   (         ||")
# print("||           (....__|RTS.013|__....)    )        ||")
# print("||            | |    ~~~~~~~    | |   c[]        ||")
# print("||            `-'               `-'              ||")
# print("||      Bienvenidos a Road Trip Simulator!       ||")
# print(" =================================================")
# print()
# time.sleep(1)
