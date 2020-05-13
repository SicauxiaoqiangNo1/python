# 类的创建
'''
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


my_dog = Dog('wille', 6)
your_dog = Dog('lucy', 3)
print("\nmy dog's name is " + my_dog.name.title() + '.')
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()

print("\nyour dog's name is " + your_dog.name.title() + '.')
print("your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
'''


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # 添加一个新的实例
        self.odometer_reading = 23

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("this cas has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.mileage = mileage
        else:
            print("Your can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


my_used_car = Car('subda', 'outback', '2013')
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()
