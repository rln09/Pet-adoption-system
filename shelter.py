import csv
from dog import Dog
from cat import Cat

class Shelter:
    def __init__(self):
        self._pets = []
    
    def add_pet(self, pet):
        self._pets.append(pet)
    
    def get_all_pets(self):
        return [pet for pet in self._pets if not pet.is_adopted]
    
    def search_by_type(self, pet_type):
        return [pet for pet in self._pets if pet.type.lower() == pet_type.lower() and not pet.is_adopted]
    
    def search_by_breed(self, breed):
        return [pet for pet in self._pets if breed.lower() in pet.breed.lower() and not pet.is_adopted]
    
    def search_by_age(self, age):
        return [pet for pet in self._pets if pet.age == age and not pet.is_adopted]
    
    def find_pet_by_name(self, name):
        for pet in self._pets:
            if pet.name.lower() == name.lower():
                return pet
        return None
    
    def adopt_pet(self, name):
        pet = self.find_pet_by_name(name)
        if pet and not pet.is_adopted:
            pet.adopt()
            return True
        return False
    
    def load_from_csv(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['type'].lower() == 'dog':
                        pet = Dog(row['name'], row['breed'], int(row['age']), row.get('description', ''))
                    else:
                        pet = Cat(row['name'], row['breed'], int(row['age']), row.get('description', ''))
                    self.add_pet(pet)
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def save_to_csv(self, filename):
        try:
            with open(filename, 'w', newline='') as file:
                fieldnames = ['name', 'type', 'breed', 'age', 'description', 'is_adopted']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for pet in self._pets:
                    writer.writerow({
                        'name': pet.name,
                        'type': pet.type,
                        'breed': pet.breed,
                        'age': pet.age,
                        'description': pet.description,
                        'is_adopted': pet.is_adopted
                    })
            print(f"Data successfully saved to {filename}")
        except Exception as e:
            print(f"Error saving data: {e}")