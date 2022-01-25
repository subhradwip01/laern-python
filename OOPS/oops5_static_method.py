class Employee:
    company="Google"
    salary="300k"
    def getSalary(self,signature): 
        print(f"Salry: {self.salary}\n{signature}")

    # static method ==> can be called without object
    @staticmethod
    def greet():
        print("Good morning, sir")    

subh=Employee()
subh.salary="500k"
subh.getSalary("Thanks!")
subh.greet()