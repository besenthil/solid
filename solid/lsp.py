from abc import ABCMeta


class Vehicle:
    __metaclass__ = ABCMeta

    def start(self):
        print('Engine Started')

    def stop(self):
        print('Engine Stopped')

    def __init__(self):
        if type(self) == Vehicle:
            raise Exception("Vehicle must be subclassed.")

    def drive(self):
        print('Driving')

    def ride(self):
        pass


class Car(Vehicle):

    def __init__(self):
        pass

    def start(self):
        print('Car Engine Started')

    def stop(self):
        print('Car Engine Stopped')

    def drive(self):
        print('Driving a car')


class Bike(Vehicle):

    def __int__(self):
        pass

    def start(self):
        print('Bike Engine Started')

    def stop(self):
        print('Bike Engine Stopped')

    def ride(self):
        print('Riding a bike')

class VehicleController(object):

    def __init__(self,vehicle):
        self.vehicle = vehicle

    def start(self):
        self.vehicle.start()

    def stop(self):
        self.vehicle.stop()

    def drive(self):
        self.vehicle.drive()
