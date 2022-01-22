#Dictionary
#Collection of key value pairs
myDict={
    "key1": 1,
    "key2" : "Subhradwip" ,
    "key3" : [1,2,3],
    "key4":(1,2,3),
    "anotherDict":{
        "nKey1":[12,1,2,1]
    }
}

# Empty Dictionary
# a={}

# Accessing value from dictionary using key
# print(myDict["key1"])
# print(myDict["anotherDict"]["nKey1"])

# Dictionary methods
# print(myDict.keys()) #Printing the keys of the the dictonary
# print(myDict.values()) #Printing value of the dictionary
# print(myDict.items()) #Printing a set like object(key , value) for of the dictionary's items
#updating the dict
# myNewDict={
#     "key5":"New Content"
# }
# myDict.update(myNewDict)
# myDict.update({
#     "Kkey6":"Another content",
#     "key7":"Good content"
# })
# print(myDict)

print(myDict.get("key77")) #it will give the value of a key but if the key is not present then it will just show none rather than showing error like myKey["Key77"]
