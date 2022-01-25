class Employee:
    salary=100
    
    @classmethod
    def changeSalary(cls,sal):
        cls.salary=sal

print(Employee.salary)
e=Employee()
e.changeSalary(344)
print(e.salary)
print(Employee.salary)        