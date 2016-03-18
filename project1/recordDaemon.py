#Here is the daeomon which is recording the flight (will use python-daemon)
import runDaemon

class RecordDaemon:
    def __init__(self,delay):
        self.delay = delay
        self.maxNumberOfPlanes = 5

    def newPlane(self):
        thread = runDaemon.RunDaemon(self.delay)
        thread.start()

   #def
aa = RecordDaemon(1)
aa.newPlane()