#function can have default parameters or arguments. if some arguments expected by the function aren't passed, 
#the function will assume default values

def get_full_name(firstName, lastName, middleInitial = "K"):
    return f"{firstName} {middleInitial} {lastName}"

print(get_full_name(firstName = "Gaurav", lastName = "Dutta"))
print(get_full_name(firstName = "Gaurav", lastName = "Dutta", middleInitial = "Kumar"))

