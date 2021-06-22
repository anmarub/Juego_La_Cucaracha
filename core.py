import db as db
import random
import os
from rich.console import Console
console = Console()

# Funcion DataPlayers ejecuta las matriz de jugadores
# Necesaria para el juego
def DataPlayers(entity, qty):
    for i in range(qty):
        entity.append([])
        for j in range(1):
            idx = i
            entity[i].append(idx)
            name = f'Jugador {(i+1)}'
            entity[i].append(name)
            cover = 1000
            entity[i].append(cover)
            penalty = 0
            entity[i].append(penalty)
            carayAntenasCucaracha = [0,0,0,0,0,0,0]
            entity[i].append(carayAntenasCucaracha)
            cuerpoCucaracha = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            entity[i].append(cuerpoCucaracha)
            colaCucaracha = [0]
            entity[i].append(colaCucaracha)


    return entity


# Validacion de asignacion de ubicacion en la cucaracha ya sea sancion, cuerpo, cabeza o cola
def validacionInsertar(posicionPlayer, entity):
    try:
        if entity.count(1) == 0:
            console.print('[bold blue][i]Mejor suerte para la proxima [/i][/] 😔. [bold red][i]Pierde el turno y paga sancion 💸💸 [/i]')
            bc = db.players[posicionPlayer][3]
            db.players[posicionPlayer][3] = bc + 10
            console.input('[bold blue][i]presion Enter para continuar[/i][/] ▶️ ')
            return False
        else:
            if entity.count(1) == 1:
                console.print('[bold blue][i]se llena una posicion del cuerpo[/i][/] 🪳 🪳 🪳')
                bc = db.players[posicionPlayer][5].index(0)
                db.players[posicionPlayer][5][bc] = 1
                print(db.players[posicionPlayer][5])
                console.input('[bold blue][i]presion Enter para continuar[/i][/] ▶️ ')
                return True
            else:
                if entity.count(1) == 2:
                    console.print('[bold blue][i]se llena una posicion de la cabeza o antenas[/i][/]  🪳 🪳 🪳')
                    bc = db.players[posicionPlayer][4].index(0)
                    db.players[posicionPlayer][4][bc] = 1
                    print(db.players[posicionPlayer][4])
                    console.input('[bold blue][i]presion Enter para continuar[/i][/] ▶️ ')
                    return True
                else:
                    if entity.count(1) == 3:
                        console.print('[bold blue][i]se llena una posicion de la cola[/i][/]  🪳 🪳 🪳')
                        bc = db.players[posicionPlayer][6].index(0)
                        db.players[posicionPlayer][6][bc] = 1
                        print(db.players[posicionPlayer][6])
                        console.input('[bold blue][i]presion Enter para continuar[/i][/] ▶️ ')
                        return True
                    else:
                       return False
    except:
        print('Campo Lleno')

#Limpiar la pantalla del sistema
def limpiarPantalla():
    os.system('clear')

#Lanzamiento de dados con liberia y controla la cantidad de lanzamientos por jugador
def lanzamiento_dados(posicionPlayer, n_dados, entity):
    VlrVerdad = True
    while VlrVerdad:
        console.print('[bold blue][i]¿quieres Lanzar los Dados?[/i][/] 👀 ')
        vi = console.input('[bold green][i] 👍  SI [/i][/] o [bold red][i] 👎  NO[/i][/] [bold red][i] 🚪  SALIR[/i][/]: ').upper()
        vi = valueSiNO(vi,VlrVerdad)
        if vi == 'SI':
            entity = []
            for j in range(n_dados):
                dado = random.randint(1,6)
                entity.append(dado)
            n_dados -= 1
            console.print(f'[bold green][i]los {(n_dados +1)} dados giraron y obtuvo:[/i][/] 🎲 🎲 🎲 ', entity)
            VlrVerdad = validacionInsertar(posicionPlayer, entity)
        else:
            if vi == 'NO':
                VlrVerdad = False
                entity = []
                console.print('[bold green][i]¡¡¡Cediste el turno al siguiente jugador!!![/i][/]  😱')
                console.input('[bold blue][i]presion Enter para continuar[/i][/] ▶️ ')
            else:
                if vi == 'SALIR':
                    console.print('[bold red][i] Has Salido del Juego[/i]')
                    console.input('[bold blue][i]presion Enter para continuar[/i][/] ▶️ ')
                    db.Save_Data(db.players)
                    exit()
           
    return entity

#Evalua la respuesta ingresada en el input de los dados
def valueSiNO(valor, value):
    while value:
        if valor == 'SI' or valor == 'NO' or valor == 'SALIR':
            value = False
            return valor
        else:
            print('La opcion seleccionada no es correcta')
            console.print('[bold blue][i]¿quieres Lanzar los Dados?[/i][/] 👀 ')
            valor = console.input('[bold green][i] 👍  SI [/i][/] o [bold red][i] 👎  NO[/i][/] [bold red][i] 🚪  SALIR[/i][/]: ').upper()
    return value

# Contar valores iguales a 0 para validar el ganador
def CountVacias(entity):
    valueVacias = []
    sumPosicion = 0
    for i in range(len(entity)):
        j = entity[i][4].count(0)
        k = entity[i][5].count(0)
        l = entity[i][6].count(0)
        sumPosicion = j + k + l
        valueVacias.append(sumPosicion)
    return valueVacias    

#Validacion para continuar el juego con el siguiente jugador
def SeguirLanzamientos(entity):
    for i in entity:
        if i == 0:
            valor = False
        else:
            valor =  True
    return valor

#Totalizar el valor del premio de los jugadores
def totalPremio(entity):
    TotalPremio = 0
    for premio in range(len(entity)):
        tp = entity[premio][3]
        TotalPremio = TotalPremio + tp
    return TotalPremio

def ValueEntity(entity, n):
    if entity:
        console.print('[bold blue][i]Existe una Partida en Progreso ¿Desea Continuar?[/i][/] 👀 ')
        ve = console.input('[bold green][i] 👍  SI [/i][/] o [bold red][i] 👎  NO[/i][/] [bold red][i] 🚪  SALIR[/i][/]: ').upper()
        ve = valueSiNO(ve, True)
        if ve == 'SI':
            return entity
        else:
            if ve == 'NO':
                db.players = []
                #print(db.players)
                entity = DataPlayers(db.players, n)
                return entity
            else:
                if ve == 'SALIR':
                    db.Save_Data(db.players)
                    exit()
    else:
        entity = DataPlayers(db.players, n)
        return entity
                    

