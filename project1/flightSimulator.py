#Simple flight simulator
import numpy
import random
import math
class FlightSimulator:

    def __init__(self, deltaTime):
        self.deltatime = deltaTime#s
        self.height =0.
        self.heightMax=10.e3
        self.cw  = 0.02
        self.rho = 0.8 #Should depend on temperature pressure
        self.Area = 50
        self.Thrust = 281.e3#Should not be constant
        self.mass = 185.e3
        self.Gravity = 9.81*self.mass
        self.angle = 0.5#30degrees just for basic simulation
        self.maxVelocity = 900.*1000./3600.


        self.distance = random.uniform(100e3, 10e6)#in meters
        self.time = 0.
        self.distanceGone = 0.
        self.velocity =0.
        self.altitude =0.
        self.launched = False
        self.distanceLand = 0

    def run(self):#set flight number
        self.flightNumber=numpy.random.randint(10e3,100e3,1)
        return self.flightNumber[0]

    def flight(self):#simulate launch, cruise and landing
        if self.altitude< 10e3 and not self.launched:
            self.startLaunch()
            self.distanceLand=self.distanceGone
            return True
        elif self.distanceGone < (self.distance-self.distanceLand):
            self.launched = True
            self.cruise()
            self.landingDistance = math.sqrt(math.pow(self.distance-self.distanceGone,2)+math.pow(self.altitude,2))
            self.deceleration = pow(self.velocity,2)/(2.*self.landingDistance)
            return True
        elif self.velocity>0:
            self.landing()
            return True
        return False

    def flightParameters(self):#get flight parameters
        return {'velocity':self.velocity, 'altitude':self.altitude, 'time':self.time, 'distanceGone':self.distanceGone,'distance':self.distance}

    def cruise(self):#cruise
        self.time=self.time+self.deltatime
        self.distanceGone=self.distanceGone+self.velocity*self.deltatime

    def landing(self):#simulate landing
        self.velocity=self.velocity-self.deceleration*self.deltatime
        self.distanceGone=self.distanceGone+self.velocity*self.deltatime*math.cos(self.angle)
        self.altitude=self.altitude-self.velocity*self.deltatime*math.sin(self.angle)
        self.time=self.time+self.deltatime

    def startLaunch(self):#simulate launch
        airFriction = self.cw*0.5*self.rho*self.velocity*self.velocity*self.Area
        forceY = (self.Thrust-airFriction)*math.sin(self.angle)-self.Gravity
        forceX = (self.Thrust-airFriction)*math.cos(self.angle)
        aX = forceX/self.mass
        aY = forceY/self.mass

        if(self.velocity<self.maxVelocity):
            self.velocity=self.velocity+math.sqrt(math.pow(aX,2)+math.pow(aY,2))*self.deltatime
        self.distanceGone=self.distanceGone+self.velocity*self.deltatime*math.cos(self.angle)
        self.altitude=self.altitude+self.velocity*self.deltatime*math.sin(self.angle)
        self.time=self.time+self.deltatime