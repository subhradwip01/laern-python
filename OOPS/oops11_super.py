# Single inheritance
class A:
    def greet(self):
        print("Greet from class A")

class B(A):
    def greet(self):
        super().greet()
        print("Greet from class B")

a=A()
a.greet()

print("============")

b=B()
b.greet() 