#Here is the thread class which simulates plane and reads parameters

from multiprocessing import Queue
import time
import flightSimulator
import dataStore
import myThread
class RunDaemon():
    def __init__(self, deltaTime):
        self.deltaTime = deltaTime
        self.plane = flightSimulator.FlightSimulator(deltaTime)
        self.name = self.plane.run()
        self.file = dataStore.DataStore(self.name)
        self.counter = 0
        self.maxEvents = 1e4#max events in the single file

    def planeFlight(self, q,qfinish):#simulate flight
        while True:
            a = self.plane.flight()
            if not a:
                break
            self.counter+=1
            q.put(self.plane.flightParameters())
            qfinish.put(True)
            time.sleep(self.deltaTime)
        qfinish.put(False)
        return False

    def closeOpen(self):#close one txt file and open new
        self.file.closeFile()
        self.file.openNewFile(self.counter/self.maxEvents)

    def checkIfcloseFile(self):#check if close one txt file and open new
        if(self.counter%self.maxEvents==0):
                self.closeOpen()

    def readerParams(self, q, qfinish):#recorder function
        while qfinish.get():
            self.file.writeToFile(q.get())
            self.checkIfcloseFile()
            time.sleep(self.deltaTime)
        return False

    def runTwoprocesses(self):#run two threads - simulation of flight and recorder
        queue = Queue()
        queueFinish = Queue()
        threads = []
        p1 = myThread.MyThread(target = self.planeFlight, args = (queue,queueFinish))
        p2 = myThread.MyThread(target = self.readerParams, args = (queue,queueFinish))
        p1.daemon=True
        p2.daemon=True
        threads.append(p1)
        threads.append(p2)
        p1.start()
        p2.start()

        while len(threads) > 0:#kill threads if Keyboard Interrupt
            try:
                threads = [t.join() for t in threads if t is not None and t.isAlive()]
            except KeyboardInterrupt:
                print "Ctrl-c received! Sending kill to threads..."
                for t in threads:
                    t.kill_received = True

    def run(self):#run program in the recorder mode
        print "Starting " + str(self.name)
        self.file.openNewFile(self.counter/self.maxEvents)
        self.runTwoprocesses()
        self.file.closeFile()
        self.file.targzFile()
        print "Exiting " + str(self.name)