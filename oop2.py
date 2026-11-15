#Encapsulation
# 1.public members:
class Mobile:
    def __init__(self,name):
        self.name = name
m = Mobile("apple")
print(m.name)
m.name = "nokia" #can modify directly
print(m.name)
# 2. Protected members:
print()
class Car:
    def __init__(self,brand,speed):
        self.brand = brand
        self._speed = speed #protected member
    def display_speed(self):
        print(f"Brand: {self.brand}, Speed: {self._speed} km/h")
car = Car("Toyota", 120)
car.display_speed()

#3. private members:
print()
class bike:
    def __init__(self,mileage,speed):
        self.mileage = mileage
        self.__speed = speed #private
    def get_speed(self):
        return self.__speed,self.mileage
    def setSpeed(self,speed):
        if speed > 0:
            self.__speed = speed
        else:
            print("Enter the positive speed")
b = bike(15,150)
print(b.get_speed()) # tuple me print hoga kyuki do value krna hai isliye
b.setSpeed(200)
print(b.get_speed())
