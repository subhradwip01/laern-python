class Employee:
    company="Google"
    # __init__(self) ==> a speacial method that is called at first time when the object is created 
    # this is also callled constructor
    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Employee created")
        
    def getDetails(self):
        print(f"Name: {self.name}")    
        print(f"Company: {self.company}")    
        print(f"Subunit: {self.subunit}")
        print(f"Salry: {self.salary}")    

    def getSalary(self,signature): 
        print(f"Salry: {self.salary}\n{signature}")

    @staticmethod
    def greet():
        print("Good morning, sir")


subh=Employee("Subhradwip",30000000,"Youtube")
ritesh=Employee("Ritesh",32000000,"Marketing")
print("=====================")
subh.getDetails()
print("=====================")
ritesh.getDetails()

# tom=Employee() ==> it will throug an error => TypeError: __init__() missing 3 required positional arguments: 'name', 'salary', and 'subunit'
