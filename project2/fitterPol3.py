#Fit pol3 function to the data
import fitter
import numpy as np
class FitterPol3(fitter.Fitter, object):
    def __init__(self,data):
        fitter.Fitter.__init__(self, data)
        return

    @classmethod
    def function(self, x, a, b,c, d):
        y = np.array(x)
        return a*y*y*y+b*y*y+c*y+d