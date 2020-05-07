#there are three types of strings in python
#   simple string
#   formatted string
#   raw string

#raw strings are useful to print/interpret a string as it is
a = r"I am Gaurav\tI live in Houston\n"
print(a)

#formatted strings are used to put variables inside a string
first_name = "Gaurav"
last_name = "Dutta"
city = "Houston"
amount = 10
message = f"My name is {first_name} {last_name}. I live in {city}.\nI have {amount} dollars."
print(message)

#string also can be formatted using string format method
s = "My name is {}, {}, I live in {}, I have {} dollars."
message = s.format(first_name, last_name, city, amount)
print(message)

#the format string also accepts positional parameters
s = "My name is {2}, {0}, I live in {1}, I have {3} dollars."
message = s.format(first_name, last_name, city, amount)
print(message)