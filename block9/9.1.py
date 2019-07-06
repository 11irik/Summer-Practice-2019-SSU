import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(1 , 125, 1250)
y = x**(1/3)
plt.plot(x, y)
plt.show()