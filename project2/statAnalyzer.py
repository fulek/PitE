from scipy import stats
import math
class StatAnalyzer:
    def __init__(self, data, function, coeff, ndof):
        self.data = data
        self.function = function
        self.coeff =coeff
        self.ndof =ndof
        self.expected = []
        self.observed =[]

    def fillExpected(self):
        for k in range(0, len(self.data.get('x'))):
            self.expected.append(math.fabs(self.function(self.data.get('x')[k],*self.coeff)))
            self.observed.append(math.fabs(self.data.get('y')[k]))
        return

    def calculateChi2(self):
        self.fillExpected()
        chi2, p = stats.chisquare(self.observed, f_exp=self.expected, ddof=self.ndof)
        return chi2/self.ndof