#Here is the daeomon which is recording the flight (will use python-daemon)
import runDaemon
import signal
class RecordDaemon:
    def __init__(self,delay):
        self.delay = delay

    def newPlane(self):
        try:
            thread = runDaemon.RunDaemon(self.delay)
            thread.daemon=True
            thread.start()
            while thread.isAlive():
                thread.join(1)
        except (KeyboardInterrupt):
            print '\n! Received keyboard interrupt, quitting thread.\n'

