#these examples show how to access the items in a list
#list elements can be accessed by indexing i.e. by using [index] where index is an integer denoting position

myList = ["dog", "cat", "penguin", "giraffe"]

#access the first item using index 0
print(myList[0])

#the last element can be accessed using posititon or index minus one
print(myList[3])
print(myList[-1])

#the format of the index is start: stop: step:
print(myList[1:3])
print(myList[:3])
print(myList[1:])
print(myList[1:2:1])
