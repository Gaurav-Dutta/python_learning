#create  a list of personal info objects and sort them by first name, and also by last name alphabetically
#this example shows sorting of objets by using key function, the key function returns a value for the object 
#which can be used to compare the object with another object of same type
class Info:

    def __init__ (self, firstName, lastName, age, zip, salary, education):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.zip = zip
        self.salary = salary
        self.education = education


    # def is_middle_class(self):
    #     return self.salary > 75000 and self.salary < 100000
    
    def __str__ (self):
        return f"""firstName = {self.firstName} 
        lastname = {self.lastName}
        age = {self.age}
        zip = {self.zip}
        salary = {self.salary}
        education  = {self.education}"""



def object_key(obj):
    return obj.firstName

def object_key_2(obj):
    return obj.lastName

    
bill = Info("Bill", "Bobily", 78, "77077", 892000, "highschool")
jean = Info("Jean", "Pierre", 34, "79823", 600000, "masters")
tina = Info("Tina", "Chen", 29, "77098", 89000, "bachelors")
ram = Info("Ram", "Ven", 19, "55273", 48000, "phd")
richard = Info("Richard", "Watkins", 18, "23043", 71000, "bachelors")

myList = [bill, jean, tina, ram, richard]


myList1 = sorted(myList, key=object_key)
for p in myList1:
    print( p.firstName)

print("----------")

myList2 = sorted(myList, key=object_key_2)
for p2 in myList2:
    print( p2.lastName)

print("----------")

myList2 = sorted(myList, key=object_key_2, reverse = True)
for p2 in myList2:
    print( p2.lastName)



