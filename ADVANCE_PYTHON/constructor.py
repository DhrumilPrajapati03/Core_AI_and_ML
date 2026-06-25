class Employee:
    
    def __init__(self,company, salary, role):
        self.company = company
        self.salary = salary
        self.role = role

    def get_info(self):
        print(f"info of employee:\n salary: {self.salary}, company: {self.company}, role: {self.role}")
    
    @staticmethod
    def get_details():
        print(f"info of employee:\n salary: company: {harry.company} , role: {harry.role} ")

    @staticmethod
    def add(a,b):
        return a+b
    
harry = Employee("google", 500000, "SDE")
# print(harry.role)
harry.get_info()
harry.get_details()
print(harry.add(5,6))

sam = Employee("Anthropic", 900000, "AI Developer")
# print(sam.company)
sam.get_info()