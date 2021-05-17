import numpy as np
import matplotlib.pyplot as plt

def estimate_b0_b1(x, y):
    n = np.size(x)
    #Obtenemos los promedios de X y de Y
    m_x, m_y = np.mean(x), np.mean(y)

    #Calcular suma
    suma_xy = np.sum( (x - m_x) * (y - m_y) )
    suma_xx = np.sum( (x - m_x) ** 2 )

    #coeficientes de regresión
    b_1 = suma_xy / suma_xx
    b_0 = m_y - b_1 * m_x

    return b_0, b_1

def plot_regression(x, y, b):
    plt.scatter(x, y, color = 'g', marker = 'o', s = 30)

    y_pred = b[0] + b[1] * x
    plt.plot(x,y_pred, color='b')

    #Etiquetado
    plt.xlabel('X')
    plt.xlabel('Y')
    plt.show()

#Codigo Main
def run():
    #Dataset
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 3, 5, 6, 5])

    #Obtenemos la estimación
    b = estimate_b0_b1(x, y)
    print(f'Los valores son b0 = {b[0]}, b1 = {b[1]}')

    #Graficamos la línea de regresión
    plot_regression(x, y, b)

if __name__ == '__main__':
    run()