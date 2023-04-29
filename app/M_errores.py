import csv
import functools

def lector(x):
    #Ela funcion open permite abrir archivos csv en este caso al escrivir 'r' decimos que solo sea para lectura
    with open(x, 'r') as csvfile:
        R = csv.reader(csvfile, delimiter = ',')
        #Esta funcion nos permite leer los encabezados de un archivo CSV
        Header = next(R)

        D= []
        #ahora lo que se hace es que se itera las filas y los encabezados en una
        #con el fin de que estos esten juntos como las llaves y los valores de un
        #diccionarios
        for row in R:
            #con esto ponemos los valores en tuplas
            iterable = zip(Header, row)
            #con esto volvelos las tuplas a diccionario usando diccionari comprenhencion
            paises = {K:V for K,V in iterable }
            #ahora le vamos a agregar valores a la lista vacia que generamos 'D'
            D.append(paises)
            #esto es un agregado mio, lo que hare es que ya convertido en diccionario el CSV , filtrare con un MAP todos los valores
            #de rank y los guardare dentro de una lista para despues ser sumados con un reduce, cabe resaltar que el INT es una
            #constante que se usa para convertir un numero STR a un numero INT , este se debe aplicar directamente a la variable
            #NO A LA LISTA ENTERA, DEBE OPERAR VARIABLE POR VARIABLE
            L = list(map(lambda x: int(x['Rank']), D))
            RR = functools.reduce(lambda i, c: i + c, L)
            #por ultimo retornamos lo unico que nos interesa, que es la lista con los valores

        return D

def FILTRAR_PAIS(D, C):
    R = list(filter(lambda x: x['Country/Territory'] == C, D))
    return R

# filtro por fila
def FILTRAR_FILA(D, C, caracteristica):
    R = list(filter(lambda x: x[C] == caracteristica, D))
    return R

# esta es una forma de ultrar columnas
def FILTRAR_2_COLUMNA(D, C1, C2):
    COLM1 = list(map(lambda x: x[C1], D))
    COLM2 = list(map(lambda x: x[C2], D))
    return COLM1, COLM2

def datos_de_paises(df):
    # PARA QUE ESTE MODULO FUNCIONE LE DEBES MANDAR UN DICCIONARIO ESPECIFICANDO SU POSICION
    D_P = {
        '2022': int(df['2022 Population']),
        '2020': int(df['2020 Population']),
        '2015': int(df['2015 Population']),
        '2010': int(df['2010 Population']),
        '1990': int(df['1990 Population']),
        '1980': int(df['1980 Population']),
        '1970': int(df['1970 Population'])
    }

    labels = D_P.keys()
    Values = D_P.values()
    return labels, Values


import matplotlib.pyplot as plt
def generacion_barras(L, V):
    fig, ax = plt.subplots()
    ax.bar(L, V)
    plt.savefig("bar.png")
    plt.close()

def generacion_pai(L, V):
    fig, ax = plt.subplots()
    ax.pie(V, labels=L)
    # esta parte es para decir que nos genere un
    # grafia de pai con el eje central y que sea un circulo
    ax.axis('equal')
    plt.title("grafico de paster")
    plt.savefig("pai.png")
    plt.close()




if __name__ == '__main__':
    #lecto de archivos csv
    P = lector('world_population.csv')


    #filtro de filas por paises
    R = FILTRAR_PAIS(P, 'Kazakhstan')

    # para que el modulo de datos de paises funcione, este le debemos especificar la posicion
    R2 = R[0]

    #filtro depoblacion
    l, v = datos_de_paises(R2)

    #generacion de grafico de barras
    generacion_barras(l,v)

    #filtro de fila , para esto tu necesitas (los datos, la columna a filtrar, la caracteristica que quieres filtrar)
    Ñ = FILTRAR_FILA(P, 'Continent', 'South America')

    #filtro de columnas , aqui lo que hace es que saca las 2 columnas que necesitas analisar
    C1, C2 = FILTRAR_2_COLUMNA(Ñ, 'Country/Territory', 'World Population Percentage')

    #generacion de grafico de pastel
    generacion_pai(C1, C2)