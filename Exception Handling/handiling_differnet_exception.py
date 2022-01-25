
from cmath import exp

done=False
while(not done):
    try:
        a=int(input("Enter value of a: "))
        b=int(input("Enter value of b: "))
        c=a/b
        print(f"a/b = {c}")
        done=True
    except ValueError as e:
        print("Enter a valid value...")
    except ZeroDivisionError as e:
        print("Division by 0 is not possible...") 
    except Exception as e:
        print("You have eneted something wrong please cheack it once..")    

print("Well done!!!")       