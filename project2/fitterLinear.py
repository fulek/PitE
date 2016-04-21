#Fit linear function to the data
import fitter
class FitterLinear(fitter.Fitter, object):
    def __init__(self,data):
        fitter.Fitter.__init__(self, data)
        return

    @classmethod
    def function(self, x, a, b):
        return a*x+b