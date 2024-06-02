import matplotlib.pyplot as plt
import numpy as np

def plot_linear(m, b):
    x = np.linspace(-10, 10, 400)
    y = m * x + b
    plt.plot(x, y, '-r', label=f'y={m}x+{b}')
    plt.title('Graph of Linear Equation')
    plt.xlabel('x', color='#1C2833')
    plt.ylabel('y', color='#1C2833')
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend(loc='upper left')
    plt.show()

m = float(input("Enter the slope (m): "))
b = float(input("Enter the y-intercept (b): "))
plot_linear(m, b)
