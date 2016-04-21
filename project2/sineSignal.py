import signl
import numpy as np

class SineSignal(signl.Signl):

    def __init__(self, amplitude):
        super(signl.Signl, self).__init__()
        self.amplitude = amplitude

    def generateSignal(self, x):
        return self.amplitude*np.sin(x)