# Single inheritance
class A:
    def greetA(self):
        print("Greet from class A")

class B(A):
    def greetB(self):
        print("Greet from class B")

class C(B):
    def greetC(self):
        print("Greet from class C")        

a=A()
a.greetA()

print("============")

b=B()
b.greetA()
b.greetB()

print("============")

c=C()
c.greetA()
c.greetB()
c.greetC()