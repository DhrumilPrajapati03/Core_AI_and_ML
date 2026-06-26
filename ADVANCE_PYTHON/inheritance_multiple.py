class Car :
    car = "BMW"
    def up (self):
        print(f"this car is {self.car}")

class House :
    home = "5bhk"
    def down (self):
        print(f"this is {self.home}")

class mine(Car,House):
    name = "Ron"
a = mine()
a.up()
a.down() 
print(a.car,a.home)

class father:
    house = "4bhk"
    car = "BMW"

    def properties(self):
        print(f"{self.car} and {self.house}")

class mother:
    Bike = "Hunter 650"
    visa = "Austrailia"

    def property2(self):
        print(f"{self.Bike} and {self.visa}")

class son(father,mother):
    name = 'rohan'

    def info(self):
        print("Property inheritor")

s = son()
s.properties()
s.property2()
s.info()