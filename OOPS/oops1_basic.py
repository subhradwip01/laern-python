class NumberOpt:
    def sum(self):
        return self.a+self.b

# Creating object of NumberOpt
num=NumberOpt()
num.a=12
num.b=13
s=num.sum()
print(s) 

num2=NumberOpt()
num2.a=14
num2.b=16
s=num2.sum()
print(s)