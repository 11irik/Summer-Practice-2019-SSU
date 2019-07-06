import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**(1/3)

x = np.linspace(1 , 125)

y1 = f(x)
plt.plot(x, y1, label='f(x)')

y2 = -f(x)
plt.plot(x, y2, color=('red'), label='-f(x)')

y3 = 2 * f(x)
plt.plot(x, y3, color=('green'), label='2f(x)')

plt.legend()
plt.grid()

plt.show()