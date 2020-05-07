filepath = "C:\\Python_Learning\\Data\\gaurav's_information.txt"

with open(filepath, "w") as myfile:
    myfile.write("First name: Gaurav\n")
    myfile.write("Last Name: Dutta\n")
    myfile.write("Phone: 832-917-3700\n")
    myfile.write("14215 Woodville Gardens Dr\n")

with open(filepath, "r") as myfile:
    print(myfile.read())
