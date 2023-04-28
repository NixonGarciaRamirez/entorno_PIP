import matplotlib.pyplot as plt

def grafica_pie(x,y):
    fig, ax = plt.subplots()
    ax.pie(x , labels= y)
    plt.savefig('.pie.png')
    plt.close()
    