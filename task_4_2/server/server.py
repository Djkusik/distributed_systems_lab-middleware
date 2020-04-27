import Ice
import sys

from smart_home_servant_locator import SmartHomeServantLocator

with Ice.initialize(sys.argv) as communicator:
    adapter = communicator.createObjectAdapterWithEndpoints("SmartHomeAdapter", "default -p 10000")
    adapter.addServantLocator(SmartHomeServantLocator(communicator), "SmartHome")
    adapter.activate()
    communicator.waitForShutdown()