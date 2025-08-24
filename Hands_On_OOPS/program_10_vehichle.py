
from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class ElectricVehicle(ABC):

    @abstractmethod
    def charge(self):
        pass

class GasVehicle(ABC):

    @abstractmethod
    def refuel(self):
        pass

class ElectricCar(Vehicle, ElectricVehicle):

    def start(self):
        print("Starting the Electric Car's Motor")

    def stop(self):
        print("Stopping the Electric Car's Motor")

    def charge(self):
        print("Charging the Electric Car's Battery")

class GasMotorCycle(Vehicle, GasVehicle):

    def start(self):
        print("Starting the Gas Motor Cycle's Engine")

    def stop(self):
        print("Stopping the Gas Motor Cycle's Engine")

    def refuel(self):
        print("Refueling the Gas Motor Cycle's fuel tank")


def main():

    ec = ElectricCar()
    gmc = GasMotorCycle()

    ec.start()
    ec.charge()
    ec.stop()

    print()

    gmc.start()
    gmc.refuel()
    gmc.stop()

if __name__ == "__main__":
    main()