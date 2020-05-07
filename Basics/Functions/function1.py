#a function is defined by using the ketyword "def". The block of code following the funciton definition is called function block
#function may or may not return a value if the function returns a value it uses the return keyword to return a value
#the first functionn below does not return any value, the second function returns the full name of a person given first name, middle
#initial, and last name
def print_personal_info(name, city):
    print(f"Hello {name}")
    print(f"I live in {city}")

print_personal_info("Gaurav", "Houston")
print_personal_info(name = "Indra", city = "Houston")

print(type(print_personal_info))

def get_full_name(firstName, middleInitial, lastName):
    #return firstName + " " + middleInitial + " " + lastName
    return f"{firstName} {middleInitial} {lastName}"

#the return value from a function should be assigned to a variable 
x = get_full_name("Gaurav", "Kumar", "Dutta")
print(x)