#the basic way of reareading form a file is to call open/read/close methods
filepath = "C:\\Python_Learning\\Data\\Example1.txt"
myfile = open(filepath)

#print("first reading")
content = myfile.read()
print(content)

#the second reading doesn't read anything because the file pointer moves to the end after the first reading
#print("second reading")
#content = myfile.read()
#print(content)

#the pointer can be moved to the start location by calling seek(0)
#print("third reading")
#myfile.seek(0)
#content = myfile.read()
#print(content)

#file should be closed after usage to avoid memory leaks
myfile.close()
