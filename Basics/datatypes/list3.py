#many times we have to access each item in a list and do something with it, a process called list iteration
#the simplest way of doing list iteration is using for each method on the list

myList = ["dog", "cat", "penguin", "giraffe"]

for animal in myList:
    print(animal.capitalize())
    print("hello")

#adding other animals to the list

myList.append("monkey")
myList.append("bat")
print(myList)

#removing cat

myList.remove("cat")
print(myList)

#inserting animals 

myList.insert(1, "horse")
myList.insert(3, "elephant")

print(myList)