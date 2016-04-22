#Class for data generation
import sineSignal
import gaussianNoise
import numpy as np

class DataGenerator:
    def __init__(self, numberOfPoints, amplitude):
        self.numberOfPoints = numberOfPoints
        self.sigmaNoise = 1
        self.xCoordinate=[]
        self.signal=[]
        self.noise =[]
        self.signalAndNoise = []
        self.range=[0.,2*np.pi]
        self.amplitude = amplitude


    def setSigmaNoise(self,signoise):#set sigma for the noise simulation(gausssian)
        self.sigmaNoise = signoise

    def generate(self):#generate signal+noise and return the sum of those two
        sig = sineSignal.SineSignal(self.amplitude)
        ns = gaussianNoise.GaussianNoise(self.sigmaNoise)

        for i in range(0,self.numberOfPoints):
            x = (self.range[1]-self.range[0])/self.numberOfPoints*i
            y = sig.generateSignal(x)
            numberOfEntriesForBin = np.random.randint(5,10)#set number of entries for each x bin
            for k in range(0, numberOfEntriesForBin):
                nois = ns.generateNoise()
                self.xCoordinate.append(x)
                self.signal.append(y)
                self.noise.append(nois)
                self.signalAndNoise.append((y+nois))


        return {'y':self.signalAndNoise, 'x':self.xCoordinate}