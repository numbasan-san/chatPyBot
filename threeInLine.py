import time, random, os

def inicio_juego ():
    print ("_________________________________________________________\n\n" + 
           "/*------------------3 en Raya------------------*/\n" + 
           "_________________________________________________________\n" + 
           "")
    time.sleep (1)

    while True:
        ficha = input ("Elije una ficha: X / O.\n")
        ficha = ficha.upper ()

        if ficha == "X":
            humano = "X"
            ordenador = "O"
            break

        elif ficha == "O":
            humano = "O"
            ordenador = "X"
            break

        else:
            print ("Por favor, elije una de las dos fichas.")

    return humano, ordenador

def tablero ():
    print ("         |         |         ")
    print ("7   {}    |8   {}    |9   {}    ".format (matriz [6], matriz [7], matriz [8]))
    print ("         |         |         ")
    print ("-----------------------------")
    print ("         |         |         ")
    print ("4   {}    |5   {}    |6   {}    ".format (matriz [3], matriz [4], matriz [5]))
    print ("         |         |         ")
    print ("-----------------------------")
    print ("         |         |         ")
    print ("1   {}    |2   {}    |3   {}    ".format (matriz [0], matriz [1], matriz [2]))
    print ("         |         |         \n")

def empate (matriz):
    empate = True
    i = 0

    while (empate == True and i < 9):

        if matriz [i] == " ":
            empate = False

        i = i + 1

    return empate

def victoria (matriz):

    if (
    matriz [0] == matriz [1] == matriz [2] != " " or 
    matriz [3] == matriz [4] == matriz [5] != " " or 
    matriz [6] == matriz [7] == matriz [8] != " " or 
    matriz [0] == matriz [3] == matriz [6] != " " or 
    matriz [1] == matriz [4] == matriz [7] != " " or 
    matriz [2] == matriz [5] == matriz [8] != " " or 
    matriz [0] == matriz [4] == matriz [8] != " " or 
    matriz [2] == matriz [4] == matriz [6] != " "):
        return True

    else:
        return False

def movimiento_jugador ():

    while True:
        posiciones = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        casilla = int ( input ("Tú: Casilla #"))

        if casilla not in posiciones:
            print ("Jugada imposible.")
        
        else:

            if matriz [casilla - 1] == " ":
                matriz [casilla - 1] = humano
                break

            else:
                print ("Jugada imposible.")

def movimiento_ordenador ():
    posiciones = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    casilla = 9
    parar = False

    for i in posiciones:
        copia = list (matriz)

        if copia [i] == " ":
            copia [i] = ordenador

            if victoria (copia) == True:
                casilla = i

    if casilla == 9:

        for j in posiciones:
            copia = list (matriz)

            if copia [j] == " ":
                copia [j] = humano

                if victoria (copia) == True:
                    casilla = j
    
    if casilla == 9:

        while not parar:
            casilla = random.randint (0, 8)

            if matriz [casilla] == " ":
                parar = True
    
    matriz [casilla] = ordenador

while True:
    matriz = [" "] * 9
    os.system ("cls")
    humano, ordenador = inicio_juego ()
    partida = True
    ganador = 0
        
    while partida == True:
        ganador = ganador + 1
        os.system ("cls")
        tablero ()
        
        if victoria (matriz):
        
            if ganador % 2 == 0:
                print ("/*      Gana el Jugador      */\n" + 
                       "/*       Fin del Juego       */\n" + 
                       "/*     Regresando al chat    */")
                time.sleep (5)
                partida = False
                os.system ("cls")
                os.system ("python main.py")
                break
        
            else:
                print ("/*      Gana Mirko      */\n" + 
                       "/*     Fin del Juego    */\n" + 
                       "/*  Regresando al chat  */")
                time.sleep (5)
                partida = False
                os.system ("cls")
                os.system ("python main.py")
                break
            
        elif empate (matriz):
            print ("/*           Empate           */\n" + 
                   "/*        Fin del Juego       */\n" + 
                   "/*     Reiniciando partida   */")
            time.sleep (5)
            partida = True
            break
            
        elif ganador % 2 == 0:
            print ("Mirko: Estoy pensando, espera.")
            time.sleep (2)
        
            movimiento_ordenador ()

        else:
            movimiento_jugador ()