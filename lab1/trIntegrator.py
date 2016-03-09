import scipy.integrate

#class to integrate the given poly function
class TriIntegrator:
    def __init__(self, steps, coefficients, range):
        self.steps = steps
        self.coefficients = coefficients
        self.range = range

#calculate poly
    def function(self,x):
        bx = 0.
        npower=0
        for i in self.coefficients:
            bx+=i*(x**npower)
            npower+=1
        return bx
#calculate the integral using scipy
    def integrateScipy(self):

        return scipy.integrate.quad(self.function, self.range[0], self.range[1])[0]

#calculate the integral using trapezoidal method

    def integrateTrapezoidal(self):
        h = float(self.range[1] - self.range[0]) / self.steps
        y = 0.0
        y += (self.function(self.range[0])+self.function(self.range[1]))/2.0
        for i in range(1, self.steps):
            y += self.function(self.range[0] + i*h)
        return y * h
