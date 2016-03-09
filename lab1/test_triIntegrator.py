from unittest import TestCase
import trIntegrator

class TestTriIntegrator(TestCase):
    def test_function(self):
        coeff=[2,2,2]
        rang=[0,2.]
        stps =2
        tr = trIntegrator.TriIntegrator(stps,coeff,rang)
        expectedResult =16.1
        g = float("{0:.1f}".format(tr.function(2.2)))
        self.assertAlmostEqual(g,expectedResult)

    def test_integrateScipy(self):
        coeff=[2,2,2]
        rang=[0,2.]
        stps =2
        tr = trIntegrator.TriIntegrator(stps,coeff,rang)
        expectedResult =13.3
        g = float("{0:.1f}".format(tr.integrateScipy()))
        self.assertAlmostEqual(g,expectedResult)

    def test_integrateTrapezoidal(self):
        coeff=[2,2,2]
        rang=[0,2.]
        stps =2
        tr = trIntegrator.TriIntegrator(stps,coeff,rang)
        expectedResult =14
        g = float("{0:.1f}".format(tr.integrateTrapezoidal()))
        self.assertAlmostEqual(g,expectedResult)
