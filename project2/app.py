import dataGenerator
import plotter
import fitterSinus
import statAnalyzer
import fitterLinear
import fitterPol3
import dataPreparation
#Manager app

gen = dataGenerator.DataGenerator(100, 100)#generate 100 points with amplitude =100
gen.setSigmaNoise(10.)#set sigma level for noise (mu > 0 && mu < sigma)
data = gen.generate()

#prepare data for fit and chi2 test
dprep = dataPreparation.DataPreparation(data)
prepData = dprep.prepareData()


model = 'sine'
function = None
coeff = None
ndof = None
#Choose the function and fit it
if model == 'sine':
    fitsine = fitterSinus.FitterSinus(prepData)
    coeff = fitsine.fit()
    function = fitterSinus.FitterSinus.function
    ndof = len(prepData.get('x'))-2
elif model == 'linear':
    fitlin = fitterLinear.FitterLinear(prepData)
    coeff = fitlin.fit()
    function = fitterLinear.FitterLinear.function
    ndof = len(prepData.get('x'))-2

elif model == 'pol3':
    fitpol3 = fitterPol3.FitterPol3(prepData)
    coeff = fitpol3.fit()
    function = fitterPol3.FitterPol3.function
    ndof = len(prepData.get('x'))-4

try:
#Analyze fitted function (chi2/ndf)
    anal = statAnalyzer.StatAnalyzer(prepData,function, coeff, ndof)
    print "mode: "+model
    print "coefficients: "+str(coeff)
    chi2ndf = anal.calculateChi2()
    print "chi2/ndf = "+str(chi2ndf)
    plt = plotter.Plotter(data,function, coeff)
    plt.draw()
except TypeError:
    print 'Type error: probably bad model'