class Employee:
    company = "google"
    salary = 5000000
    role = "SDE"

    def get_info(self):
        print(f"info of employee:\n salary: {self.salary}, company: {self.company}, role: {self.role}")

harry = Employee()
# print(harry.company)
# # print(harry.salary)
harry.company = "microsoft"
harry.role = "Devops"
harry.salary = 6000000
# print(harry.company)
harry.get_info()

sam = Employee()
sam.company =  "Opne AI"
sam.role = "AI Developer"
sam.salary = 9000000
# print(sam.company)
sam.get_info()

#class classname
    #attributes of class,methods,variables

class Person:
    name="Akash"
    id=101
    occupation="Developer"
    def info(self):
        print(f"{self.name} is a {self.occupation}")
    
x = Person()
x.name ="Ravi"
x.occupation="Cybersecurity Expert"
x.info()

y= Person()
y.name = "Kavya"
y.occupation="Teacher"
y.info()

z= Person()
z.name = "Kartik"
z.occupation="Painter"
z.info()