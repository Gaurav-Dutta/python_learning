#functions are typically defined by using positional parameters i.e. when the function is called the position of the arguments
#are used to determine the function arguments 

def get_full_name(firstName, middleInitial, lastName):
    return f"{firstName} {middleInitial} {lastName}"

x = get_full_name(firstName = "Gaurav", lastName = "Dutta", middleInitial = "Kumar")
print(x)