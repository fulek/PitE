import os
class InputReaderValidator:
    def checkYNq(self,inpt):# check Yes, No, quit
        if inpt=='Y':
            return 1
        elif inpt == 'N':
            return 0
        elif inpt == 'q':
            return 2
        else:
            return -1

    def newPlaneRecordRead(self, plane):#check if new plane, mode
        loop = True
        while loop:
            message = "New plane Y/N?" if plane else "Read mode Y/N/q?"
            loop= self.checkYNq(raw_input(message))
            if not loop==-1:
                return loop


    def checkIfFloat(self,x):#check if number is float
        try:
            float(x)
            return True
        except ValueError:
            pass

    def checkIfMoreThanZero(self,x):
        return float(x) > 0

    def delayTime(self):#get delay time
        delay = False
        while not delay:

            x = raw_input("Give delay in [s]: ")
            delay = (self.checkIfFloat(x) and self.checkIfMoreThanZero(x))
            if delay:
                return float(x)

    def fileName(self):#get flight number for read mode
        return self.checkIfTarGzFileExists(raw_input("Please give the flight number: "))

    def checkIfTarGzFileExists(self, flightNum):#check if tar.gz file exists
        PATH = "./"+flightNum+".tar.gz"

        if os.path.isfile(PATH) and os.access(PATH, os.R_OK):
            print "File for flight "+flightNum+" exists and is readable"
            return flightNum
        else:
            print "For flight "+flightNum+" either file is missing or is not readable"
            return -1

