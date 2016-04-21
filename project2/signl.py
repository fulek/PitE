import abc
class Signl( object ):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        return

    @abc.abstractmethod
    def generateSignal(self):
        return

