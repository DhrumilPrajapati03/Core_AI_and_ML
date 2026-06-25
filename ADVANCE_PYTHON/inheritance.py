#PARENT CLASS = BASE CLASS = SUPER CLASS
#CHILD CLASS = DERIVED CLASS = SUB CLASS
#Inheritance is way of extending a new class from an extisting class

#Base class(SuperClass)(Parent) --> Derived class(SubClass)(Child)

'''Syntax

Class BaseClass:
    Body of base class
Class DerivedClass(BaseClass): <-- INHERITANCE
    Body of Derived class'''

class Father:
    def __init__(self,name,car):
        self.name= name
        self.car = car
    
    def showDetails(self):
        print(f"The name is {self.name} and car is {self.car}")

class son(Father):  #INHERIT
    def sonDetails(self):
        print(f"The name of son is Aakash")

A = Father("raj","audi")
A.showDetails()

s = son("Aakash","audi")
s.showDetails()
s.sonDetails