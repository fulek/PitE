#Analyze chi2/ndf
import numpy as np
class StatAnalyzer:
    def __init__(self, data, function, coeff, ndof):
        self.data = data
        self.function = function
        self.coeff =coeff
        self.ndof =ndof
        self.expected = []


    def fillExpected(self):#prepare data (observed and expected from function)
        for k in range(0, len(self.data.get('x'))):
            self.expected.append(self.function(self.data.get('x')[k],*self.coeff))
        return

    def calculateChi2(self):#calculate chi2/ndf
        self.fillExpected()
        print len(self.data.get('y'))
        chi2 = np.sum(((np.array(self.data.get('y'))-np.array(self.expected))/np.array(self.data.get('std')))**2)
        return chi2/self.ndof
