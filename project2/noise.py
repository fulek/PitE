import abc
class Noise(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        return

    @abc.abstractmethod
    def generateNoise(self):
        return

