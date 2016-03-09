import inputValidator
class InputReader:

    def setFileOrConsole(self,fileOrConsole):#set file or console
        self.fileOrConsole=fileOrConsole

    def checkIfQuit(self,quit):# check if quit

        return quit=='!q'

    def readFileOrConsole(self):#check if read params. from  file or console
        while True:
            input_str = raw_input("File or console F/C? (!q quit) ")
            if input_str == 'F':
                self.setFileOrConsole(True)
                return True
            elif input_str == 'C':
                self.setFileOrConsole(False)
                return True
            elif self.checkIfQuit(input_str):
                return False

    def read(self):#read input
        if(self.fileOrConsole):
            return self.readFile()
        else:
            return self.readConsole()

    def fileName(self):#get file name

        return self.readFromConsole("Please give file name: ")

    def readFromConsole(self, comment):#read anything from console

        return raw_input(comment)

    def readFile(self):#read input from file
        while True:
            fname = self.fileName()
            if self.checkIfQuit(fname):
                return False
            validator = inputValidator.InputValidator()
            if validator.checkIffile(fname):
                self.fname = fname
                return self.readParameters()
            else:
                print("Wrong file name")

    def readParameters(self):#read lines from file and split them into variables
        f = open(self.fname)
        lineAndParameters = []
        lines = f.readlines()
        for i in range(0,len(lines)):
            lineAndParameters.append([])
            words = lines[i].split()
            for word in words:
                lineAndParameters[i].append(word)
        return self.validateAndGiveOutput(lineAndParameters)

    def validateAndGiveOutput(self,inpt):#validate and give the proper output for the integral calc.
        vald = inputValidator.InputValidator()
        if not vald.validateInput(inpt):
            return 0
        rangeTab=[]
        step=[]
        param=[]
        Nline =0
        for i in range(0, len(inpt)):
            if i == 0 and vald.check1LineChanged(inpt[i]):
                continue
            Nline+=1
            print("Validating line: "+str(Nline))
            if not vald.checkIf4Numbers(inpt[i]):
                continue
            rangeTabOne=[inpt[i][0],inpt[i][1]]
            stepOne=inpt[i][2]
            paramOne=[]
            for j in range (3, len(inpt[i])):
                paramOne.append(inpt[i][j])
            if vald.checkParametersRange(rangeTabOne, "Range") and vald.checkSteps(stepOne) and vald.checkParametersRange(paramOne, "Parameter") :
                param.append([float(i) for i in paramOne])
                step.append(int(stepOne))
                rangeTab.append([float(i) for i in rangeTabOne])

        return {'range':rangeTab, 'steps':step,'coefficients':param}

    def multi_input(self):#multiline input from console
        input_list = []

        while True:
            input_str = raw_input(">")
            if self.checkIfQuit(input_str):
                break
            else:
                inpVar=[]
                input_str=input_str.split()
                for word in input_str:
                   inpVar.append(word)
                input_list.append(inpVar)
        return input_list

    def readConsole(self):# method for reading parameters from console
        print('Please give range (up down), #steps, parameters - all should be separated with space (!q to finish):')
        inpVar = self.multi_input()
        return self.validateAndGiveOutput(inpVar)
