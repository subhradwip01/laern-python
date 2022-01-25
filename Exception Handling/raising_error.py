from multiprocessing.sharedctypes import Value


def increment(num):
    try:
        return int(num)+1
    except:
        raise ValueError("This is not possible")


try:
    a= increment("10a")
    print(a)            
except Exception as e:
    print(e.args)    

print("Well done!!!")    