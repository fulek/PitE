import inputReader
import trIntegrator


def printPoly(rang, stp, coef, lineNum):
    poly = ''
    for a in range(0,len(coef)):
        if a > 0:
            poly+=' + '
        poly+=str(coef[a])+'*x^'+str(a)
    print(str(lineNum) + ': integration a poly '+poly+' from '+str(rang[0])+' to '+str(rang[1])+' with '+str(stp)+' steps')

def printResult(sp, tm):#print Results
    print('scipy: '+format(sp,'.3g'))
    print('trapezoidal method: '+format(tm,'.3g'))

while True:
    # Read input
    reader = inputReader.InputReader()
    quit = reader.readFileOrConsole()  # check file or console
    if not quit:
        break
    inpt = reader.read()  # read parameters
    if not inpt == 0:
        for i in range(0, len(inpt['range'])):
            trint = trIntegrator.TriIntegrator(inpt['steps'][i], inpt['coefficients'][i], inpt['range'][i])
            printPoly(inpt['range'][i], inpt['steps'][i], inpt['coefficients'][i], i)
            sp = trint.integrateScipy()
            tm = trint.integrateTrapezoidal()
            printResult(sp,tm)

