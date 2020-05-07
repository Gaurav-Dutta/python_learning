class Animal:
    

    def __init__(self, name, location, diet, continents, species):
        self.name = name
        self.location = location
        self.diet = diet
        self.continents = continents
        self.species = species
        


    def is_found_in_continent(self, continent_name):
        return continent_name in self.continents
    

    



animal1 = Animal("Dog", "Forest", "Meat", ["Asia", "Africa"], ["Dalmation", "Husky"])
print(animal1.name)
print(f"Is found in Europe? {animal1.is_found_in_continent('Asia')}")

animal2 = Animal("Cat", "Desert", "Fish", [])