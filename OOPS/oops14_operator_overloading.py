class Num:
    def __init__(self,num):
        self.num=num
    def __add__(self,num2):
        print("lets add")
        return self.num+num2.num

n1=Num(4)
n2=Num(6)
sum=n1+n2
print(sum)