def sum(list):
    sum=0
    for i in range(len(list)):
        sum+=list[i]
    return sum

sum=sum([1,2,3,4,5])
print(sum)

# Default parameter value
def greet(name="Strager"):
    print(f"Good day, {name}")

greet("Subhradwip")
greet()