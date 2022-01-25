

# Will go else block only if there is no excetipn means code uder try block has excuted properly
try:
    i=int(input("Enter a number: "))
    c=1/i
except Exception as e:
    print(e)
else:
    print("Successfull")    