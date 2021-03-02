#Autor Luis Cano
#Este Programa es un Juego de Memorama
import random as rdm
import getpass

def instrucciones(): 
    '''Imprime las instrucciones'''
    print("Instrucciones:")
    print("Este juego es para dos jugadores. Tomarán turnos con objetivo de voltear los pares de cartas que sean iguales. Gana quien consiga más pares.")
    print("Si un jugador consigue un par, volverá a ser su turno.")
    print("Selecciona la carta que desees voltear escribiendo el numero de su fila y después el numero de su columna.")
    print("Si quieres empezar un juego nuevo escribe \"NUEVO\". Si en algún punto quieres terminar el juego escribe \"SALIR\".")

def accion(varx): 
    '''Revisa si se quiere hacer una acción diferente a jugar el juego'''
    i = 0
    while varx != "SALIR" and varx != "NUEVO":
        varx = input()
        if varx == "INFO":
            instrucciones()
        i += 1
        if i >= 3:
            print("Si necesitas ayuda escribe \"INFO\".")
            i = 1
    return varx

def compara(x,y): 
    '''Revisa si se hizo el input de "SALIR" o "NUEVO" cuando se pedia una fila o columna'''
    if x == "SALIR" or y == "SALIR":
        return "SALIR"
    elif x == "NUEVO" or y == "NUEVO":
        return "NUEVO"

def pnt_matriz(m,bs): 
    '''Imprime el tablero de juego con las cartas de manera ordenada'''
    if bs == "n":
        print("\n")
    for i in range(len(m)):
        for u in range(len(m[i])):
            print(m[i][u],"",end="")
        print("\n")

def turno(varx,matr,cart): 
    '''Pide la fila y columna y obtiene qué carta se desea voltear'''
    i = 0
    while i == 0:
        f = input("Fila: ")
        if compara(f,"") != "SALIR" and compara(f,"") != "NUEVO":
            c = input("Columna: ")
        else:
            c = f
        if compara(f,c) == "SALIR" or compara(f,c) == "NUEVO":
            varx = compara(f,c)
            CF = 0
            i = 1
        else:
            try:
                f = int(f)
                c = int(c)
                CF = f * 6 + c
                if 0<= f <=5 and 0<= c <=5:
                    if matr[f+1][c+1] == "- ":
                        i = 1
                        if cart[CF] < 10:
                            matr[f+1][c+1] = str(cart[CF]) + " "
                        else:
                            matr[f+1][c+1] = str(cart[CF])
                    else:
                        print("Elige OTRA carta que No haya sido volteada")
                else:
                    print("Celda fuera del rango, elige otra vez...")
            except:
                print("Ingresa un Numero para la fila y un Numero para la columna...")
    return varx,matr,CF,f,c

def Par_NoPar(varx,matr,cart): 
    '''Imprime la matriz con las cartas volteadas, y las compara checando si es par o no;
    si sí modifica el tablero de juego para mostrar el acierto'''
    print("Elige una carta")
    varx,matr,CF1,f1,c1 = turno(varx,matr,cart)
    result = ""
    if varx != "NUEVO" and varx != "SALIR":    
        pnt_matriz(matr,"n")
        print("Elige otra carta")
        varx,matr,CF2,f2,c2 = turno(varx,matr,cart)
        if varx != "NUEVO" and varx != "SALIR":
            pnt_matriz(matr,"n")
            if cart[CF1] == cart[CF2]:
                result = "Y"
            else:
                result = "N"
                matr[f1+1][c1+1] = "- "
                matr[f2+1][c2+1] = "- "
    return varx,result,matr

def score(px,s1,s2):
    '''Aumenta la puntuación del jugador que encontro un par'''
    if px == 1:
        s1 += 1
    elif px == 2:
        s2 += 1
    return s1,s2

def resultados(s1,s2):
    '''Muestra los resultados del juego'''
    if s1 > s2:
        print("Ganador: Jugador 1!!")
        print("Puntuacion:",s1,"Pares")
    elif s2 > s1:
        print("Ganador: Jugador 2!!")
        print("Puntuacion:",s2,"Pares")
    else:
        print("Empate...")
    return 1
    
def main():
    '''Corre el(los) Juego(s) utilizando todas las funciones previas'''
    print("Bienvenido al memorama!")
    print("Para leer las instrucciones escribe \"INFO\". Si quieres empezar un juego nuevo escribe \"NUEVO\". ", end="")
    print("Si quieres salir del juego escribe \"SALIR\".")
    varx = accion("")
    juego = 0
    while varx != "SALIR":
        if varx == "NUEVO":
            if juego == 1:
                print("\n\nJuego Nuevo\n\n")
            fin = 0
            player = 1
            score1 = 0
            score2 = 0
            varx = ""
            matriz = [["  ","0 ","1 ","2 ","3 ","4 ","5 "],
                    ["0 ","- ","- ","- ","- ","- ","- "],
                    ["1 ","- ","- ","- ","- ","- ","- "],
                    ["2 ","- ","- ","- ","- ","- ","- "],
                    ["3 ","- ","- ","- ","- ","- ","- "],
                    ["4 ","- ","- ","- ","- ","- ","- "],
                    ["5 ","- ","- ","- ","- ","- ","- "]]
            pnt_matriz(matriz,"")
            cartas = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18]
            #para realizar pruebas puede comentar la siguiente línea, de manera que los pares salgan ordenados
            #rdm.shuffle(cartas)
            wait = getpass.getpass("- - Presiona ENTER para Continuar - -\n")
            #Se utiliza getpass para que si el jugador teclea algo no se muestre, y solo avance hasta presionar ENTER
            while fin != 1:
                print("Turno de jugador",player)
                varx,result,matriz = Par_NoPar(varx,matriz,cartas)
                if result == "Y":
                    print("Acertaste un par!")
                    wait = getpass.getpass("\n- - Presiona ENTER para Continuar - -\n")
                    score1,score2 = score(player,score1,score2)
                elif result == "N":
                    print("Fallaste...")
                    wait = getpass.getpass("\n- - Presiona ENTER para Continuar - -\n")
                    #si deseas eliminar la regla "despues de conseguir un par le vuelve a tocar al jugador":
                    #saca la siguiente línea del elif
                    player += 1
                if varx != "NUEVO" and varx != "SALIR":
                    pnt_matriz(matriz,"")
                if player > 2:
                    player = 1
                if score1 + score2 >= 18:
                    fin = resultados(score1,score2)
                    juego = 1
                elif varx == "NUEVO" or varx == "SALIR":
                    fin = 1
                    juego = 1
        varx = accion(varx)

main()
