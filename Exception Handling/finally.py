
# finally block will be executed alwayes if there is any error,expection or no error,exception
try:
    i=int(input("Enter a number: "))
    c=1/i
except Exception as e:
    print(e)
finally:
    print("Done!!")     