import pickle

# Base de datos de los Jugadores inicializada al comienzo del main
players = []

dados = []

# Guardar datos en archivos binarios
def Save_Data(players):
    #print(Clientes_id, Clientes_name)
    try:
        archivo = open('players', 'rb')
        players = pickle.load(archivo)
        archivo.close()
    except:
        print('El Archivo no Existe... Se crea uno')
        archivo = open('players', 'wb')
        pickle.dump(players, archivo)
# Cargar datos en archivos binarios

try:
    players = pickle.load(open('players', 'rb'))
except:
    print('El Archivo no Existe... Establezca uno')



