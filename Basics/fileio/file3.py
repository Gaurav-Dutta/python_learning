filepath = "C:\\Python_Learning\\Data\\Example1.txt"
with open(filepath) as myfile:
    myfile.write("Hello World\n")
    myfile.write("I am Gaurav\n")

with open(filepath) as myfile:
    print(myfile.read())

