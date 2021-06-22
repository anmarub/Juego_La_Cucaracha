import menuGame as mu
import db as db
import core as co
from rich.console import Console
console = Console()

Opcion = 0
QtyDados = 5
LOOP = True

#Menu principal del juego en donde se decide la cantidad de jugadores.
mu.principal()
def MenuIni(Opcion, LOOP):
    while LOOP:
        VlrVerdad = True
        Opcion = console.input('[bold green][i]Opcion[/i][/] 👉 ')
        if Opcion == '1':
            n = 2
            co.limpiarPantalla()
            co.ValueEntity(db.players, n)
            print(db.players)
            while VlrVerdad:
                for ip in range(n):
                    name_player = db.players[ip][1]
                    co.limpiarPantalla()
                    mu.lance_player(name_player)
                    co.lanzamiento_dados(ip, QtyDados, db.dados)
                    print(f'Termino el turno del {name_player}')
                    co.limpiarPantalla()
                    Vacias = co.CountVacias(db.players)
                    VlrVerdad = co.SeguirLanzamientos(Vacias)
            print('Juego Terminado')
            totalCase = co.totalPremio(db.players)
            mu.win_game(name_player, totalCase)
            LOOP = False
        else:
            if Opcion == '2':
                n = 3
                co.limpiarPantalla()
                co.ValueEntity(db.players, n)
                print(db.players)
                while VlrVerdad:
                    for ip in range(n):
                        name_player = db.players[ip][1]
                        co.limpiarPantalla()
                        mu.lance_player(name_player)
                        co.lanzamiento_dados(ip, QtyDados, db.dados)
                        print(f'Termino el turno del {name_player}')
                        co.limpiarPantalla()
                        Vacias = co.CountVacias(db.players)
                        VlrVerdad = co.SeguirLanzamientos(Vacias)
                print('Juego Terminado')
                totalCase = co.totalPremio(db.players)
                mu.win_game(name_player, totalCase)
                LOOP = False
            else:
                if Opcion == '3':
                    n = 4
                    co.limpiarPantalla()
                    co.ValueEntity(db.players, n)
                    print(db.players)
                    while VlrVerdad:
                        for ip in range(n):
                            name_player = db.players[ip][1]
                            co.limpiarPantalla()
                            mu.lance_player(name_player)
                            co.lanzamiento_dados(ip, QtyDados, db.dados)
                            print(f'Termino el turno del {name_player}')
                            co.limpiarPantalla()
                            Vacias = co.CountVacias(db.players)
                            VlrVerdad = co.SeguirLanzamientos(Vacias)
                    print('Juego Terminado')
                    totalCase = co.totalPremio(db.players)
                    mu.win_game(name_player, totalCase)
                    LOOP = False
                else:
                    if Opcion == '4':
                        n = 5
                        co.limpiarPantalla()
                        co.ValueEntity(db.players, n)
                        print(db.players)
                        while VlrVerdad:
                            for ip in range(n):
                                name_player = db.players[ip][1]
                                co.limpiarPantalla()
                                mu.lance_player(name_player)
                                co.lanzamiento_dados(ip, QtyDados, db.dados)
                                print(f'Termino el turno del {name_player}')
                                co.limpiarPantalla()
                                Vacias = co.CountVacias(db.players)
                                VlrVerdad = co.SeguirLanzamientos(Vacias)
                        print('Juego Terminado')
                        totalCase = co.totalPremio(db.players)
                        mu.win_game(name_player, totalCase)
                        LOOP = False
                    else:
                        if Opcion == '5':
                            n = 6
                            co.limpiarPantalla()
                            co.ValueEntity(db.players, n)
                            print(db.players)
                            while VlrVerdad:
                                for ip in range(n):
                                    name_player = db.players[ip][1]
                                    co.limpiarPantalla()
                                    mu.lance_player(name_player)
                                    co.lanzamiento_dados(ip, QtyDados, db.dados)
                                    print(f'Termino el turno del {name_player}')
                                    co.limpiarPantalla()
                                    Vacias = co.CountVacias(db.players)
                                    VlrVerdad = co.SeguirLanzamientos(Vacias)
                            print('Juego Terminado')
                            totalCase = co.totalPremio(db.players)
                            mu.win_game(name_player, totalCase)
                            LOOP = False
                            if Opcion == '6':
                                exit()
                            else:
                                input('Intente de Nuevo.. Eliga una de las Opciones')

MenuIni(Opcion, LOOP)
