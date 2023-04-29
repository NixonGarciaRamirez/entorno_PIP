import random as rd
#inicio
print('hola, ¿como esta?')
inicio = int(input('que te gustaria: intrucciones = 0 comenzar el juego = 1'))


if inicio == 0:
    print('la dinamica del juego es simple, lo unico que debes hacer es esribir en MINUCULAS, si vas a usar piedra, papel o '
          'tijera, ya despues el juego te dira si ganas o pierdes'
          'segun lo que saque el compuador')
    inicio2 = int(input('te gustariajgar?? si = 1 no = 0'))
    if inicio2 == 0:
        print('vale vuelve pronto')
    elif inicio2 == 1:
        # opciones del usuario
        rounds = 1
        contador_computador = 0
        contador_usuario = 0

        while True:
            print('*' * 10)
            print('ronda', rounds)
            print('*' * 10)

            opc_user = input("escoger piedra, tijera, papel ")
            opc_user = opc_user.lower()
            print("usuario escogio = ", opc_user)

            # opiones de la pc
            opciones = ("piedra", "tijera", "papel")
            opc_pc = rd.choice(opciones)
            print("pc escogio = ", opc_pc)

            # primera condcion

            if not opc_user in opciones:
                print('opcion de usuario no validad')
                continue
            # empate
            if opc_user == opc_pc:
                print("empate")
            # evaluar alternativas donde gana el usuario
            elif opc_user == "piedra" and opc_pc == "tijera":
                print("piedra gana tijera, gana  usuario")
                contador_usuario += 1

            elif opc_user == "tijera" and opc_pc == "papel":
                print("tijera gana papel, gana  usuario")
                contador_usuario += 1
            elif opc_user == "papel" and opc_pc == "piedra":
                print("papel gana piedra, gana  usuario")
                contador_usuario += 1
            # evaluar alternativas donde gana el computador
            elif opc_pc == "piedra" and opc_user == "tijera":
                print("piedra gana tijera, gana  pc")
                contador_computador += 1
            elif opc_pc == "tijera" and opc_user == "papel":
                print("tijera gana papel, gana  pc")
                contador_computador += 1
            elif opc_pc == "papel" and opc_user == "piedra":
                print("papel gana piedra, gana  pc")
                contador_computador += 1
            # opcion inexistente jaja
            else:
                ("perdiste")
            rounds = rounds + 1

            print('*' * 10)
            print('marcador')
            print('computador :', contador_computador)
            print('jugador :', contador_usuario)
            print('*' * 10)

            if contador_computador == 2:
                print('gano el computador')
                break
            if contador_usuario == 2:
                print('gano el jugador')
                break




elif inicio == 1:

    # opciones del usuario
    rounds = 1
    contador_computador = 0
    contador_usuario = 0

    while True:
        print('*'*10 )
        print('ronda', rounds)
        print('*'*10)

        opc_user = input("escoger piedra, tijera, papel ")
        opc_user = opc_user.lower()
        print("usuario escogio = ", opc_user)

        # opiones de la pc
        opciones = ("piedra", "tijera", "papel")
        opc_pc = rd.choice(opciones)
        print("pc escogio = ", opc_pc)

        # primera condcion

        if not opc_user in opciones:
            print('opcion de usuario no validad')
            continue
        # empate
        if opc_user == opc_pc:
            print("empate")
        # evaluar alternativas donde gana el usuario
        elif opc_user == "piedra" and opc_pc == "tijera":
            print("piedra gana tijera, gana  usuario")
            contador_usuario += 1

        elif opc_user == "tijera" and opc_pc == "papel":
            print("tijera gana papel, gana  usuario")
            contador_usuario += 1
        elif opc_user == "papel" and opc_pc == "piedra":
            print("papel gana piedra, gana  usuario")
            contador_usuario += 1
        # evaluar alternativas donde gana el computador
        elif opc_pc == "piedra" and opc_user == "tijera":
            print("piedra gana tijera, gana  pc")
            contador_computador += 1
        elif opc_pc == "tijera" and opc_user == "papel":
            print("tijera gana papel, gana  pc")
            contador_computador += 1
        elif opc_pc == "papel" and opc_user == "piedra":
            print("papel gana piedra, gana  pc")
            contador_computador += 1
        # opcion inexistente jaja
        else:
            ("perdiste")
        rounds = rounds+1

        print('*'*10)
        print('marcador')
        print('computador :', contador_computador)
        print('jugador :', contador_usuario)
        print('*'*10)

        if contador_computador == 2:
            print('gano el computador')
            break
        if contador_usuario == 2:
            print('gano el jugador')
            break

else:
    print(' por favor escoger una opcion correcta')
