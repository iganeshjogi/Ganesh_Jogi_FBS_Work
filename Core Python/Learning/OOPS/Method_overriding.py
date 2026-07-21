class Vehicle():
    def stop(self):
        print('Vehicle stopped.')

class Car(Vehicle):
    def stopcar(self):
        print('car stopped.')

c1 = Car()
c1.stop()