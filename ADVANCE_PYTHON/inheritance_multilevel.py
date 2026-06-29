# class Grandfather:
#     def __init__(self, grandfathername):
#         self.grandfathername = grandfathername

# class Father(Grandfather):
#     def __init__(self, fathername, grandfathername):
#         self.fathername = fathername
#         Grandfather.__init__(self, grandfathername)

# class Son(Father):
#     def __init__(self, sonname, fathername, grandfathername):
#         self.sonname = sonname
#         Father.__init__(self, fathername, grandfathername)

#     def print_name(self):
#         print("Grandfathername:", self.grandfathername)
#         print("Fathername:", self.fathername)
#         print("Sonname:", self.sonname)

# s1 = Son('Prince', 'Rampal', 'Lal mani')

# print(s1.grandfathername)
# s1.print_name()


class Grandfather:
    def __init__(self,grandfathername):
        self.grandfathername=grandfathername

class Father(Grandfather):
    def __init__(self, grandfathername,fathername):
        super().__init__(grandfathername)
        self.fathername=fathername

class Son(Father):
    def __init__(self, grandfathername, fathername,sonname):
        super().__init__(grandfathername, fathername)
        self.sonname=sonname

    def print_name(self):
        print(f"the name of grandfather is {self.grandfathername}")
        print(f"the name of father is {self.fathername}")
        print(f"the name of son is {self.sonname}")

s1 = Son("Ravi","Pravin","Pratham")
s1.print_name()