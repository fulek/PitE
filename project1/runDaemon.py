#Here is the thread class which creates new plane

import threading
import time
import flightSimulator


class RunDaemon (threading.Thread):
    def __init__(self, deltaTime):
        threading.Thread.__init__(self)

        self.deltaTime = deltaTime
        self.plane = flightSimulator.FlightSimulator(deltaTime)
        self.name = self.plane.run()
        self.stopThread = False

    def planeFly(self, delay):

        while self.plane.flight():
            time.sleep(delay)
            print self.printFlightParameters()

    def run(self):
        print "Starting " + self.name
        self.planeFly(self.deltaTime)
        print "Exiting " + self.name

    def printFlightParameters(self):
        return self.plane.flightParameters()


