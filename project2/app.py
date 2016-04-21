import dataGenerator
import plotter
import fitterSinus
import statAnalyzer
import fitterLinear
import fitterPol3


gen = dataGenerator.DataGenerator(1000, 100)
gen.setSigmaNoise(10.)
data = gen.generate()

model = 'pol3'
function = None
coeff = None
ndof = None
if model == 'sine':
    fitsine = fitterSinus.FitterSinus(data)
    coeff = fitsine.fit()
    function = fitterSinus.FitterSinus.function
    ndof = len(data.get('x'))-2
elif model == 'linear':
    fitlin = fitterLinear.FitterLinear(data)
    coeff = fitlin.fit()
    function = fitterLinear.FitterLinear.function
    ndof = len(data.get('x'))-2

elif model == 'pol3':
    fitpol3 = fitterPol3.FitterPol3(data)
    coeff = fitpol3.fit()
    function = fitterPol3.FitterPol3.function
    ndof = len(data.get('x'))-4

try:

    anal = statAnalyzer.StatAnalyzer(data,function, coeff, ndof)
    print "mode: "+model
    print "coefficients: "+str(coeff)
    chi2ndf = anal.calculateChi2()
    print "chi2/ndf = "+str(chi2ndf)
    plt = plotter.Plotter(data,function, coeff)
    plt.draw()
except TypeError:
    print 'Bad model'