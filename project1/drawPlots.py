#Draw plots
import inputReaderValidator
import dataStore
import variablesIntoDB


from rootpy.plotting import Canvas,Graph
import ROOT
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

    def prepareData(self):#prepare data for graphs
        dtStore = dataStore.DataStore(self.flightNo)
        dtStore.unpackTargzFile()
        self.variables = dtStore.readData()
        dtStore.removeTxt()
        self.appendVariables()

    def appendVariables(self):#append variables to lists
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

    def drawOneGraph(self,toDraw, name):#draw single graph
        gr1 = Graph(len(self.time))
        for i, (xx, yy) in enumerate(zip(self.time, toDraw)):
            gr1.SetPoint(i, xx, yy)
        gr1.GetXaxis().SetNdivisions(105)
        gr1.GetXaxis().SetLabelOffset(0.015)
        gr1.GetXaxis().SetNoExponent(1)
        gr1.GetYaxis().SetTitleSize(0.06)
        gr1.GetYaxis().SetTitleOffset(1.3)
        gr1.GetXaxis().SetTitleSize(0.06)
        gr1.GetXaxis().SetTitleOffset(0.7)
        gr1.GetYaxis().SetTitle(name)
        gr1.GetXaxis().SetTitle('time [s]')
        gr1.SetMarkerStyle(20)
        gr1.SetMarkerSize(0.01)
        gr1.SetMarkerColor(1)

        return gr1
    def draw(self):#draw graphs
        canv = Canvas(900, 600)
        canv.Divide(3,2)

        name = ('velocity [m/s]','altitude [m]', 'roll [rad]', 'pitch [rad]', 'distance [m]')
        toDraw = (self.velocity, self.altitude, self.roll, self.pitch, self.distance)
        graphs = []
        for x in range(0,5):
            canv.cd(x+1)
            ROOT.gPad.SetBottomMargin(0.15)
            ROOT.gPad.SetLeftMargin(0.2)
            graphs.append(self.drawOneGraph(toDraw[x], name[x]))
            graphs[x].Draw("AP1")
        raw_input("Press enter...")
        return