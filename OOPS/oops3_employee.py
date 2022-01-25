from re import sub


class Employee:
    company = "Google" # Class atribute

subh = Employee()
ritesh = Employee()

# Creating instamce attribute
subh.salary=3000000 # Instance attribute
ritesh.salary = 4000000 # Instance attribute
print(subh.company)
print(subh.salary)
print(ritesh.company)
print(ritesh.salary)


# Employee.company="Youtube" # Chnaging class attribute

# print(subh.company)
# print(ritesh.company)
