from unittest import TestCase
import inputReader

class TestInputReader(TestCase):
    def test_validateAndGiveOutput(self):
        inp = inputReader.InputReader()
        tab = [['1','2','10','5','6'], ['2','3','5','1']]
        rangeTab=[[1,2],[2,3]]
        step=[10,5]
        param=[[5,6],[1]]
        self.assertDictEqual(inp.validateAndGiveOutput(tab),{'range':rangeTab, 'steps':step,'coefficients':param})
