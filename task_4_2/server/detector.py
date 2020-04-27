import Ice
import SmartHome
import random

class HeatDetectorI(SmartHome.HeatDetector):
    def __init__(self):
        self.turnedOn = False
        self.readings = []
        self.generateReadings()

    def generateReadings(self):
        for i in range(random.randrange(2,20)):
            self.readings.append(random.uniform(-10, 40))

    def getReading(self, current=None):
        if not self.turnedOn:
            raise SmartHome.DeviceIsOffException

        print("Returning last reading of heat: " + str(self.readings[-1]))
        return self.readings[-1]

    def getAllReadings(self, current=None):
        if not self.turnedOn:
            raise SmartHome.DeviceIsOffException

        print("Returning every reading of heat:")
        for reading in self.readings:
            print('\t' + str(reading))
        return self.readings

    def turnOn(self, current=None):
        if self.turnedOn:
            raise SmartHome.AlreadyTurnedOnException
        self.turnedOn = True
        print("Heat detector turned on")

    def turnOff(self, current=None):
        if not self.turnedOn:
            raise SmartHome.AlreadyTurnedOffException
        self.turnedOn = False
        print("Heat detector turned off")


class HumidityDetectorI(SmartHome.HumidityDetector):
    def __init__(self):
        self.turnedOn = False
        self.readings = []
        self.generateReadings()

    def generateReadings(self):
        for i in range(random.randrange(2, 20)):
            self.readings.append(random.uniform(0, 100))

    def getReading(self, current=None):
        if not self.turnedOn:
            raise SmartHome.DeviceIsOffException

        print("Returning last reading of humidity: " + str(self.readings[-1]))
        return self.readings[-1]

    def getAllReadings(self, current=None):
        if not self.turnedOn:
            raise SmartHome.DeviceIsOffException

        print("Returning every reading of humidity:")
        for reading in self.readings:
            print('\t' + str(reading))
        return self.readings

    def turnOn(self, current=None):
        if self.turnedOn:
            raise SmartHome.AlreadyTurnedOnException
        self.turnedOn = True
        print("Humidity detector turned on")

    def turnOff(self, current=None):
        if not self.turnedOn:
            raise SmartHome.AlreadyTurnedOffException
        self.turnedOn = False
        print("Humidity detector turned off")


class LightDetectorI(SmartHome.LightDetector):
    def __init__(self):
        self.turnedOn = False
        self.readings = []
        self.generateReadings()

    def generateReadings(self):
        for i in range(random.randrange(2, 20)):
            self.readings.append(random.uniform(0, 1))

    def getReading(self, current=None):
        if not self.turnedOn:
            raise SmartHome.DeviceIsOffException

        print("Returning last reading of light: " + + str(self.readings[-1]))
        return self.readings[-1]

    def getAllReadings(self, current=None):
        if not self.turnedOn:
            raise SmartHome.DeviceIsOffException

        print("Returning every reading of light:")
        for reading in self.readings:
            print('\t' + str(reading))
        return self.readings

    def turnOn(self, current=None):
        if self.turnedOn:
            raise SmartHome.AlreadyTurnedOnException
        self.turnedOn = True
        print("Light detector turned on")

    def turnOff(self, current=None):
        if not self.turnedOn:
            raise SmartHome.AlreadyTurnedOffException
        self.turnedOn = False
        print("Light detector turned off")