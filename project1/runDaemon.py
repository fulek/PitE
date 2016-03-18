#Here is the thread class which creates new plane

import threading
import time
import flightSimulator

#exitFlag = 0

class RunDaemon (threading.Thread):
    def __init__(self, deltaTime):
        threading.Thread.__init__(self)

        self.deltaTime = deltaTime
        self.plane = flightSimulator.FlightSimulator(deltaTime)
        self.name = self.plane.run()

    def planeFly(self, delay):

        while self.plane.flight():
            #if exitFlag:
                #self.plane.run().exit()
            time.sleep(delay)
            print self.plane.run()
            print self.printFlightParameters()#self.plane.flightParameters()

    def run(self):
        print "Starting " + self.name
        self.planeFly(self.deltaTime)
        print "Exiting " + self.name

    def printFlightParameters(self):
        return self.plane.flightParameters()

'''
# Create new threads
thread1 = RunDaemon(1)
thread2 = RunDaemon(2)

# Start new Threads
thread1.start()
thread2.start()

print "Exiting Main Thread"'''