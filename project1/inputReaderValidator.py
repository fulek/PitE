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
            return float(x) > 0
        except ValueError:
            pass


    def delayTime(self):#get delay time
        delay = False
        while not delay:

            x = raw_input("Give delay in [s]: ")
            delay = self.checkIfFloat(x)
            if delay:
                return float(x)

