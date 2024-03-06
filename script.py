# actividad nombres de jugadores , elegir forma, aleatoriamente elige quien arranca
# despues de hacer una jugada mostrar el tablero despues de cada jugada
from random import *
tablero = [['','',''],
           ['','',''],
           ['','','']]
jugadores = [input('ingresa el nombre de uno de los jugadores'),input('ingresa el nombre de el otro jugador')]
primero = choice(jugadores)
print(f'el jugador que va a comenzar es:{primero}')
piezaPrimero = input('elige con que figura deseas jugar X , O')
if piezaPrimero == 'X':
    PiezaSegundo = 'O'
else: PiezaSegundo = 'X'

jugar()


def mostrar (tablero):
        for an in range(3):
            print('------')
            print(f'|' {tablero[0][an]})
            print(f'|' {tablero[0][an]})
            print(f'|' {tablero[0][an]})
            print('|' "n/")
            print('------')
            print(f'|' {tablero[1][an]} '|' {tablero[1][an]} '|' {tablero[1][an]} '|')
            print('------')
            print(f'|' {tablero[2][an]} '|' {tablero[2][an]} '|' {tablero[2][an]} '|')
            print('------')
def jugar (forma):
    a = True
    while a:
        alto = input('eligue en que piso vas a jugar desde el 0 a la 2')
        ancho = input('que tan a la derecha pondras tu pieza? del 0 al 2')
        if tablero[alto][ancho] == 'X' or tablero[alto][ancho] == 'O':
            print('lo siento esta posicion ya esta ocupada, intenta elegir otra')
        else:
            a = False
            tablero[alto][ancho] = forma
            mostrar(tablero)
def termino():
    if tablero[0][0] == tablero[1][1] and tablero[1][1] == tablero[2][2] or tablero[0][2] == tablero[1][1] and tablero[1][1] == tablero[2][0]:
        return True
    for i in range(3):
        if tablero[i][0] == tablero[i][1] and tablero[i][1] == tablero[i][2]:
                return True
        if tablero[0][i] == tablero[1][i] and tablero[1][i] == tablero[2][i]:
                return True
        for e in range(3):
            if not(tablero[i][e] == 'X' or tablero[i][e] == 'O'):
                return False
            
    return True

