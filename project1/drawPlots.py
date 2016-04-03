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
        return
    def appendVariables(self):
        for x in self.variables:
            self.time.append(x.get(self.var.time))
            self.distance.append(x.get(self.var.distanceGone))
            self.velocity.append(x.get(self.var.velocity))
            self.altitude.append(x.get(self.var.altitude))
            self.roll.append(x.get(self.var.roll))
            self.pitch.append(x.get(self.var.pitch))