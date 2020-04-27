import Ice
import SmartHome

class OvenI(SmartHome.Oven):
    def __init__(self):
        self.turnedOn = False
        self.heat = 0
        self.humidity = 0

    def heatUp(self, heat, current=None):
        if not self.turnedOn:
            raise SmartHome.DeviceIsOffException

        self.heat += heat
        if self.heat > 300:
            print("Temperature is at maximum")
            self.heat = 300
        print("Heat went up to " + str(self.heat))

    def heatDown(self, heat, current=None):
        if not self.turnedOn:
            raise SmartHome.DeviceIsOffException

        self.heat -= heat
        if self.heat < 0:
            print("Temperature is at minimum")
            self.heat = 0
        print("Heat went down to " + str(self.heat))

    def humidityUp(self, humidity, current=None):
        if not self.turnedOn:
            raise SmartHome.DeviceIsOffException

        self.humidity += humidity
        if self.humidity > 100:
            print("Humidity is at maximum")
            self.humidity = 100
        print("Humidity went up to " + str(self.humidity))

    def humidityDown(self, humidity, current=None):
        if not self.turnedOn:
            raise SmartHome.DeviceIsOffException

        self.humidity -= humidity
        if self.humidity < 0:
            print("Humidity is at minimum")
            self.humidity = 0
        print("Humidity went down to " + str(self.humidity))

    def turnOn(self, current=None):
        if self.turnedOn:
            raise SmartHome.AlreadyTurnedOnException
        self.turnedOn = True
        print("Oven turned on")

    def turnOff(self, current=None):
        if not self.turnedOn:
            raise SmartHome.AlreadyTurnedOffException
        self.turnedOn = False
        self.humidity = 0
        self.heat = 0
        print("Oven turned off")

    def getStatus(self, current=None):
        return SmartHome.OvenStatus(self.heat, self.humidity)