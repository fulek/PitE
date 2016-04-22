import numpy as np

class DataPreparation:
    def __init__(self, data):
        self.data = data
        self.x =[]
        self.y =[]
        self.std =[]

    def appendData(self,valueX, valueY):
        self.x.append(valueX)
        self.y.append(np.mean(valueY))
        self.std.append( np.std( valueY ) )

    def prepareData(self):#prepare data for fit and chi2 calc (std+mean)
        valueX = -1
        valueY = []
        for i in range(0, len(self.data.get('x'))):
            if self.data.get('x')[i] == self.data.get('x')[i-1]:
                valueX = self.data.get('x')[i]
                valueY.append(self.data.get('y')[i])
                if (i+1) == len(self.data.get('x')):
                    self.appendData(valueX, valueY)
            else:
                if i!=0:
                    self.appendData(valueX, valueY)

                valueY =[]
                valueY.append(self.data.get('y')[i])
                valueX = self.data.get('x')[i]

        return {'x':self.x, 'y':self.y, 'std':self.std}