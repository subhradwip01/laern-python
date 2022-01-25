# Single inheritance
class A:
    def greetA(self):
        print("Greet from class A")

class B(A):
    def greetB(self):
        print("Greet from class B")

a=A()
a.greetA()

print("============")

b=B()
b.greetA()
b.greetB()