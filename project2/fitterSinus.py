#Fit sine function to the data
import fitter
import numpy as np


class FitterSinus(fitter.Fitter, object):

    def __init__(self,data):
        fitter.Fitter.__init__(self, data)
        return

    @classmethod
    def function(self, x, a, b):
        return np.sin(x+b)*a


