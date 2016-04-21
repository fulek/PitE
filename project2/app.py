import dataGenerator
import plotter
import fitterSinus
import statAnalyzer
import fitterLinear
import fitterPol3
#Manager app

gen = dataGenerator.DataGenerator(1000, 100)#generate 1000 points with amplitude =100
gen.setSigmaNoise(10.)#set sigma level for noise
data = gen.generate()

model = 'sine'
function = None
coeff = None
ndof = None
#Choose the function and fit it
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
#Analyze fitted function (chi2/ndf)
    anal = statAnalyzer.StatAnalyzer(data,function, coeff, ndof)
    print "mode: "+model
    print "coefficients: "+str(coeff)
    chi2ndf = anal.calculateChi2()
    print "chi2/ndf = "+str(chi2ndf)
    plt = plotter.Plotter(data,function, coeff)
    plt.draw()
except TypeError:
    print 'Bad model'