
import matplotlib.pyplot as plt
import numpy as np
class Plotter:

    def __init__(self,data, func, coeff):
        self.x = data.get('x')
        self.y = data.get('y')
        self.func = func
        self.coeff = coeff

    def draw(self):
        plt.scatter(self.x, self.y, 10)
        xfine = np.linspace(np.min(self.x), np.max(self.x), 100)
        plt.plot(xfine, self.func(xfine, *self.coeff), 'r-',linewidth=3.0)
        plt.ylabel('y')
        plt.xlabel('x')
        plt.show()


