#Mode: recorder/reader
from modes import Modes
import inputReaderValidator
class Mode:

    def __init__(self):
        self.mode = Modes.RECORDorNoPLANE

    def returnMode(self):
        message=''
        if self.mode == Modes.RECORDorNoPLANE:
            message="RECORD MODE"
        elif self.mode == Modes.READorPlane:
            message="READ MODE"
        else:
            message="QUIT"
        print message
        return self.mode

    def readMode(self):
        inpt = inputReaderValidator.InputReaderValidator()
        self.mode = inpt.newPlaneRecordRead(False)