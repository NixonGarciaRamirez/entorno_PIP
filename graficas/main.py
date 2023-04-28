import graficas


def run(x,y):
    graficas.grafica_pie(x,y)




#ahora queremos que se ejecute como un scrip

if __name__ == '__main__':
    X = ['a','b','c']
    Y = [231,134,432]
    run(X,Y)