#Generate gaussian noise
import noise
import numpy as np
class GaussianNoise(noise.Noise):

    def __init__(self, sigma):
        super(noise.Noise, self).__init__()
        self.sigma = sigma

    def generateNoise(self):
        y = np.random.normal(0,self.sigma,1)
        return y[0]