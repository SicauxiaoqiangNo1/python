class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("yOu can not roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


# 类的继承
class ElectroCar(Car):
    def __init__(self, make, model, year):
        # super()的用法:父类也称之为超类，super是将父类和子类关联起来
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWh battery.")


my_tesla = ElectroCar('tesla', 'model s', "2016")
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
