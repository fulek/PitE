#Here is the main program which manages all the rest of the filght parameters recorder
import flightSimulator

sda = flightSimulator.FlightSimulator(0.1)
#sda.simulateFlight()
sda.run()
aaa = True
while aaa:
    aaa=sda.flight()
    print sda.flightParameters()