#Base class for fitting
import abc
from scipy.optimize import curve_fit

class Fitter(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, data):
        self.x = data.get('x')
        self.y = data.get('y')


    @abc.abstractmethod
    def function(self):
        return

    def fit(self):#fitting curve
        popt, pcov = curve_fit(self.function, self.x, self.y)
        return popt