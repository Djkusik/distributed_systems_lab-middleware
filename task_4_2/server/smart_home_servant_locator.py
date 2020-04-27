import Ice.ServantLocatorF_ice

from oven import OvenI
from detector import HeatDetectorI, HumidityDetectorI, LightDetectorI

class SmartHomeServantLocator(Ice.ServantLocator):
    def __init__(self, communicator):
        self.communicator = communicator

    def locate(self, curr):
        name = curr.id.name
        servant = self.switchServant(name)
        print(name)
        if servant is not None:
            curr.adapter.add(servant, self.communicator.stringToIdentity(f"SmartHome/{name}"))
            return servant, ""

    def switchServant(self, name):
        return {
            "Oven"              : OvenI(),
            "HeatDetector"      : HeatDetectorI(),
            "HumidityDetector"  : HumidityDetectorI(),
            "LightDetector"     : LightDetectorI()
        }.get(name, None)

    def finished(self, curr, servant, cookie):
        pass

    def deactivate(self, category):
        pass