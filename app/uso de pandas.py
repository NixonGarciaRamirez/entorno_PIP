import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('world_population.csv', sep=',')
print(df.columns)
filtro = df[df['Continent'] == 'Africa']

paises = filtro['Country/Territory'].values
porcetaje_p = filtro['Density (per km²)']

def generacion_pai(L, V):
    fig, ax = plt.subplots()
    ax.pie(V, labels=L)

    plt.title("grafico de paster")

    plt.savefig('imagenes/africa.png')
    plt.close()

generacion_pai(paises,porcetaje_p)

