#Class inherited from Thread with the possibility of killing threads
import threading


class MyThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
        super(MyThread, self).__init__(group=group, name=name, verbose=verbose)
        self.target = target
        self.args = args
        self.kwargs = kwargs
        self.kill_received = False

    def run(self):
        if not self.kill_received:
            self.target(*(self.args))


