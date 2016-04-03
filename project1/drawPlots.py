#Draw plots
import inputReaderValidator
import dataStore
import variablesIntoDB
class DrawPlots:
    def __init__(self, flightNo):
        self.flightNo = flightNo
        self.time = []
        self.distance = []
        self.velocity = []
        self.altitude = []
        self.roll = []
        self.pitch = []
        self.var = variablesIntoDB.variablesDB

    def prepareData(self):
        dtStore = dataStore.DataStore(self.flightNo)
        dtStore.unpackTargzFile()
        self.variables = dtStore.readData()
        dtStore.removeTxt()
        self.appendVariables()

    def appendVariables(self):
        inpt = inputReaderValidator.InputReaderValidator()
        for x in self.variables:
            appendToList = False
            for key, value in x.iteritems():#check if floats
                if not inpt.checkIfFloat(value):
                    print key+" is not float: "+str(value)
                    appendToList = 'True'

            if appendToList:
                continue
            self.time.append(x.get(self.var.time))
            self.distance.append(x.get(self.var.distanceGone))
            self.velocity.append(x.get(self.var.velocity))
            self.altitude.append(x.get(self.var.altitude))
            self.roll.append(x.get(self.var.roll))
            self.pitch.append(x.get(self.var.pitch))

    def draw(self):

        return