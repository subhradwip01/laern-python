class Employee:
    company="Google"
    salary="300k"
    def getSalary(self):  # self refer to the instance(obejct) of the class
        print(f"Salry: {self.salary}")

subh=Employee()
subh.salary="500k"
subh.getSalary() #  this function convert like ==> Empolyee.getSalary(subh), internally      
# Employee.getSalary(subh)