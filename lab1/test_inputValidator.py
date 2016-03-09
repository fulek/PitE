from unittest import TestCase
import inputValidator

class TestInputValidator(TestCase):
    def test_checkIfInt(self):
        inp = inputValidator.InputValidator()
        self.assertEqual(inp.checkIfInt("2232"),True)

    def test_checkIfFloat(self):
        inp = inputValidator.InputValidator()
        self.assertEqual(inp.checkIfFloat("2232.23"),True)

    def test_checkSteps(self):
        inp = inputValidator.InputValidator()
        self.assertEqual(inp.checkSteps("5"),True)

    def test_checkParametersRange(self):
        rangpar = [1,3,6,7]
        inp = inputValidator.InputValidator()
        self.assertEqual(inp.checkParametersRange(rangpar,"Range"),True)

    def test_checkIffile(self):
        inp = inputValidator.InputValidator()
        self.assertEqual(inp.checkIffile("inputReader.py"),True)

    def test_validateInput(self):
        inp = inputValidator.InputValidator()
        test = [[2,2],[1,3]]
        self.assertEqual(inp.validateInput(test),True)

    def test_check1LineChanged(self):
        line = ['Down', 'Up', 'Steps', 'Par0','Par1']
        inp = inputValidator.InputValidator()
        self.assertEqual(inp.check1LineChanged(line),True)

    def test_checkIf4Numbers(self):
        num=[1,2,3,4]
        inp = inputValidator.InputValidator()
        self.assertEqual(inp.checkIf4Numbers(num),True)
