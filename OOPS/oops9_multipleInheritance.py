# multiple inheritance
class A:
    def greet(self):
        print("Greet from class A")


class B:
    def greet(self):
        print("Greet from class B")


class C(B, A):
    pass


c = C()
# it will call the metjod depends upon the class declaration
# if it is decleared as class C(B,A) ==> call class B's greet(method) 
# if it is delcleard as C(A,B) ==> it will call class A's greet() method
c.greet()  
