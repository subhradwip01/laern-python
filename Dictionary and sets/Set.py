#Set
#Set is collection of uordered unique elements
a={1,1.0,2,3,4,5,6,10,"s"}
print(a)

# Emplty set
b=set()
# print(type(b))

# Adding element to set
b.add(5)
b.add(6)
b.add(10)
b.add(11)
b.add(-1)
print(b)

# Methods
# b.add(40) #Adding a value
# print(b)
# print(len(b))
# b.remove(10) # Remove a element if it is present in the set other wise it will throw an error
# print(b)
# print(b.pop()) # Remomve any random elemnet and return that
print(b.intersection(a)) # Returns the common elements b/w two sets
print(b.union(a)) # Returns all element of two sets
