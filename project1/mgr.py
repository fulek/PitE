#Here is the main program which manages all the rest of the filght parameters recorder
import inputReaderValidator
import runDaemon
import mode
import modes


while True:
    mod = mode.Mode()
    mod.readMode()
    modeCurrent = mod.returnMode()
    inpt = inputReaderValidator.InputReaderValidator()
    #check mode: flight/read/quit
    if modeCurrent == modes.Modes.QUIT:
        break
    elif modeCurrent == modes.Modes.RECORDorNoPLANE:
        delay = inpt.delayTime()
        plane = runDaemon.RunDaemon(delay)
        plane.run()
    elif modeCurrent == modes.Modes.READorPlane:
        print "csd"

    #check if new flight or quit
    newPlane = inpt.newPlaneRecordRead(True)
    if newPlane is not modes.Modes.READorPlane:
        break


