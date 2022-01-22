
# Use open() funtion to open the file in a partcular mode

#============ read mode ==> "r"
# file to be read must be exist
# f = open("sample.txt","r") #if you dont specify the open mode then it will open the file in read mode
# data1=f.read(10) # read all the charecters from file
# print(data1)
# data2 = f.read(20) # read only 5 charecter from file
# print(data2) 

# data3=f.readline() # Read the first line from the file
# print(data3)
# data4=f.readline() # Read the second line from the file
# print(data4)
# f.clod()

#============ write mode ==> "w"
# f=open("sample.txt","w") #it will override the existing content in a file
# f.write("New text")
# f1=open("another.txt","w") # if file is not presnt then it will create a new file
# f1.write("Another")
# f.close()
# f1.close()

# ============ Appendind mode ==> "a"
# f=open("another.txt","a") # it will appent new content to a file without overriding existing content
# f.write("Ne text added")
# f.close()

# ============ with statement ==> best way to open and close a file automaticaly
# with open("sample.txt","r") as f:
#     print(f.read())

# with open("another.txt","w") as f:
#     f.write("New content....")

# with open("sample.txt","a") as f:
#     f.write("New things added")  


for i in range(1,21):
    name=f"{i}.txt"
    with open(f"table/{name}","w") as f:
        for j in range(1,11):
            mul=i*j
            result=f"{i} X {j} = {mul}"
            f.write(f"{result}\n")