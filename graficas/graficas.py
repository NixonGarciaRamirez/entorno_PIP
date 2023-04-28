import matplotlib.pyplot as plt

def grafica_pie(x,y):
    fig, ax = plt.subplots()
    ax.pie(y , labels= x)
    plt.savefig('.pie.png')
    plt.close()
    