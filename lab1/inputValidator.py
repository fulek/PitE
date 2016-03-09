import os.path
import numbers
class InputValidator:
    def checkIfInt(self,x):#check if number is int

        return x.isdigit()

    def checkIfFloat(self,x):#check if number is float
        try:
            float(x)
            return True
        except ValueError:
            pass


    def checkSteps(self,st): #check if #steps is >0 and if it's int
        if not (self.checkIfInt(st) and int(st)>0):
                print ("number of steps "+st+" < 1 or is not an integer")
                return False
        return True

    def checkParametersRange(self,par, rgpar):#check if parameters/range are float/int
        for x in par:
            if not (self.checkIfFloat(x) or self.checkIfInt(x)):
                print (rgpar+" "+x+" is not float or integer")
                return False
        return True

    def checkIffile(self,file):#check whether file exists

        return os.path.isfile(file)

    def validateInput(self,inp):#check whether input is not empty
        if len(inp) is 0:
            print("Input seems to be empty")
            return False

        return True

    def check1LineChanged(self,firstline):#check whether first line is present
        line = ['Down', 'Up', 'Steps', 'Par0']

        return  set(line) <= set(firstline)

    def checkIf4Numbers(self,line):#check whether we have at least 4 numbers (range*2, steps, param)
        if len(line)<4:
            print("Line has < 4 numbers")
            return False
        return True

