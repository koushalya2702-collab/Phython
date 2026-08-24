#Abstraction
class Car:
    def start_engine(self):
        print("Engine started")
    def accelerate(self):
        print("car accelerating")
    def brake(self):
        print("car stops")
car=Car()
car.start_engine()
car.accelerate()
car.brake()