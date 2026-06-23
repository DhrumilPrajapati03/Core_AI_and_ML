class Employee:
    
    def __init__(self,company, salary, role):
        self.company = company
        self.salary = salary
        self.role = role

    def get_info(self):
        print(f"info of employee:\n salary: {self.salary}, company: {self.company}, role: {self.role}")

harry = Employee("google", 500000, "SDE")
# print(harry.role)
harry.get_info()

sam = Employee("Anthropic", 900000, "AI Developer")
# print(sam.company)
sam.get_info()