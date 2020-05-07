#this example shows magic methods in python

class PersonalInfo:

    def __init__ (self, firstName, lastName, age, ssn, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.ssn = ssn
        self.salary = salary


    def get_full_name(self):
        return f"{self.firstName} {self.lastName}"

    def is_senior(self):
        if self.age > 65:
            return True
        else: 
            return False 

    def is_middle_class(self):
        return self.salary > 75000 and self.salary < 100000

    def __str__ (self):
        return f"""firstname = {self.firstName} 
        lastname = {self.lastName}
        age = {self.age}
        ssn = {self.ssn}
        salary = {self.salary}"""

    def __ge__ (self, other):
        return self.age >= other.age



gaurav = PersonalInfo("Gaurav", "Dutta", 18, "832-917-3700", 0)

john = PersonalInfo("John", "Dutta", 24, "123-456-789", 80000)

print(gaurav)

if john >= gaurav:
    print("John's older than Gaurav")
else:
    print("John's younger than Gaurav")
