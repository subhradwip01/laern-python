class Employee:
    company="Google"
    language="All"
    def showDetails(self):
        print(f"This is an Employee of {self.company}")

class Programmer(Employee): # Programmer ==> child class/derived class and Employee==> parent class/base class
    language="Python"
    def getName(self):
        print(f"The language is {self.language}")
    def showDetails(self):
        print("This is a programmer")

# Obeject of Employee class
e=Employee()
e.showDetails()
print(e.language)

print("===================")

# Object of Programmer class
p=Programmer()
p.showDetails()
print(p.language)
p.getName()
