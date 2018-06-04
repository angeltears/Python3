class Dog():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title() + " is now sitting. ")
    def roll_over(self):
        print(self.name.title() + " rolled over")
        
my_dog = Dog('willie',6)
my_dog.sit()       

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odmeter_reading = 0
    def get_descriptive_name(self):
        long_name = str(self.year) + '  ' + self.make + ' '+self.model
        return long_name.title();
    def read_odometer(self):
        print("this car has " + str(self.odmeter_reading) + " miles on it.")
    def updata_odometer(self, mileage):
        if mileage >= self.odmeter_reading:
            self.odmeter_reading = mileage
        else:
            print("you can't roll back an odometer!")
    def increment_odometer(self, miles):
        self.odmeter_reading += miles
        
        
class ElectricCar(Car):
    def __init__(self, make, model, year) :
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla','model_s',2016)
print(my_tesla.get_descriptive_name())
