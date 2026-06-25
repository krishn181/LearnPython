class Vehicle:
    def startEngine(self):
        pass
class Bike(Vehicle):
    def startEngine(self):
        return "Bike engine start"
    
class Car(Vehicle):
    def startEngine(self):
        return "Car engine start"

class Truck(Vehicle):
    def startEngine(self):
        return "Truck engine start"

t = Truck()
c = Car()
b = Bike()
print(t.startEngine())
print(c.startEngine())
print(b.startEngine())