# ----------------------------------------------------------------------------
# Title:   Crear gráfico con barra de error
# Author:  Federico Iza
# ----------------------------------------------------------------------------
import numpy as np
import os
import sys
import matplotlib.pyplot as plt
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # Agregar path para usar config.py
from config import config_plots


def main():
    # Cargar datos
    data = np.loadtxt('data.csv')
    x, y, y_err = data[:, 0], data[:, 1], data[:, 2]

    # Generar gráfico
    fig, ax = plt.subplots()
    ax.minorticks_on()
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_xlim(0, 10)
    ax.set_xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ax.set_ylim(0, 20)
    plt.errorbar(x, y, y_err, fmt='o', elinewidth=.75, capsize=2, markersize=1)
    plt.show()
    fig.savefig('errores.pdf')


if __name__ == '__main__':
    config_plots()
    main()
