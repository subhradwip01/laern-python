a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))

# if b=0 then the application be broke
# c=a/b
# print(c)


# if b=0 the application will not be broke 
# as here we are handling the exception
try:
    c=a/b
    print(f"a/b= {c}")
except Exception as e:
    print(f"Expection: {e}")   

print("Well done!!")
