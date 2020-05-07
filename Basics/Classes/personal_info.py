#The key word class is used to define a class, a class is a blueprint of an object, it defines the data and behavior of the object. 
#Objects provide following important characteristics:
#Data encapsulation - keep all related data for a single entity in one place
#Behavior - methods that provide operations on that data
#Data hiding - hides data from other parts of the program using private data members 

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

#objects are created by calling the class as a function which is called class constructor

john = PersonalInfo("John", "Dutta", 24, "123-456-789", 80000)


print(f"is john senior? {john.is_senior()}")
print(f"full name? {john.get_full_name()}")
print(f"full name? {PersonalInfo.get_full_name(john)}")

gaurav = PersonalInfo("Gaurav", "Dutta", 18, "832-917-3700", 0)


print(f"Full name: {gaurav.get_full_name()}")
print(f"Is Gaurav senior? {gaurav.is_senior()}")
print(f"Is Gaurav middle class? {gaurav.is_middle_class()}")
