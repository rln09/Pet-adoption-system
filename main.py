from shelter import Shelter
from dog import Dog
from cat import Cat
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    print("\n=== Welcome to the Pet Adoption System ===")
    print("\nPlease choose an option:")
    print("1. List all pets")
    print("2. Add a new pet")
    print("3. Search for a pet")
    print("4. Adopt a pet")
    print("5. Display pet details")
    print("6. Save shelter data")
    print("7. Load shelter data")
    print("8. Exit")
    return input("\nEnter your choice (1-8): ")

def list_all_pets(shelter):
    clear_screen()
    print("=== All Pets in the Shelter ===\n")
    pets = shelter.get_all_pets()
    if not pets:
        print("No pets available in the shelter.")
    else:
        for i, pet in enumerate(pets, 1):
            print(f"{i}. {pet.get_details()}")
    input("\nPress Enter to return to the main menu.")

def add_new_pet(shelter):
    clear_screen()
    print("=== Add a New Pet ===\n")
    try:
        name = input("Enter pet's name: ")
        pet_type = input("Enter pet type (dog/cat): ").lower()
        breed = input("Enter breed: ")
        age = int(input("Enter age: "))
        description = input("Enter description (optional): ")
        
        if pet_type == 'dog':
            pet = Dog(name, breed, age, description)
        elif pet_type == 'cat':
            pet = Cat(name, breed, age, description)
        else:
            print("Invalid pet type. Please enter 'dog' or 'cat'.")
            input("\nPress Enter to continue.")
            return
        
        shelter.add_pet(pet)
        print(f"\n{name} has been added to the shelter!")
    except ValueError:
        print("Invalid age. Please enter a number.")
    except Exception as e:
        print(f"Error adding pet: {e}")
    input("\nPress Enter to return to the main menu.")

def search_pets(shelter):
    clear_screen()
    print("=== Search for a Pet ===\n")
    print("Search criteria:")
    print("1. By type (dog/cat)")
    print("2. By breed")
    print("3. By age")
    
    try:
        choice = input("\nEnter your choice (1-3): ")
        results = []
        
        if choice == '1':
            pet_type = input("Enter pet type (dog/cat): ").lower()
            results = shelter.search_by_type(pet_type)
        elif choice == '2':
            breed = input("Enter breed: ")
            results = shelter.search_by_breed(breed)
        elif choice == '3':
            age = int(input("Enter age: "))
            results = shelter.search_by_age(age)
        else:
            print("Invalid choice.")
            input("\nPress Enter to return to the main menu.")
            return
        
        print(f"\nSearch Results ({len(results)} found):")
        for i, pet in enumerate(results, 1):
            print(f"{i}. {pet.get_details()}")
            
    except ValueError:
        print("Invalid input. Please enter a number for age.")
    except Exception as e:
        print(f"Error searching pets: {e}")
    
    input("\nPress Enter to return to the main menu.")

def adopt_pet(shelter):
    clear_screen()
    print("=== Adopt a Pet ===\n")
    name = input("Enter the pet's name to adopt: ")
    
    if shelter.adopt_pet(name):
        print(f"\nCongratulations! {name} has been adopted.")
    else:
        print(f"\nPet '{name}' not found or already adopted.")
    
    input("\nPress Enter to return to the main menu.")

def display_pet_details(shelter):
    clear_screen()
    print("=== Pet Details ===\n")
    name = input("Enter the pet's name: ")
    
    pet = shelter.find_pet_by_name(name)
    if pet:
        print(f"\nName: {pet.name}")
        print(f"Type: {pet.type}")
        print(f"Breed: {pet.breed}")
        print(f"Age: {pet.age} years")
        print(f"Description: {pet.description}")
        print(f"Status: {'Adopted' if pet.is_adopted else 'Available'}")
    else:
        print(f"\nPet '{name}' not found.")
    
    input("\nPress Enter to return to the main menu.")

def save_shelter_data(shelter):
    clear_screen()
    print("=== Save Shelter Data ===\n")
    filename = input("Enter filename to save (default: shelter_data.csv): ") or "shelter_data.csv"
    shelter.save_to_csv(filename)
    input("\nPress Enter to return to the main menu.")

def load_shelter_data(shelter):
    clear_screen()
    print("=== Load Shelter Data ===\n")
    filename = input("Enter filename to load (default: data/pets.csv): ") or "data/pets.csv"
    shelter.load_from_csv(filename)
    print("Data loaded successfully!")
    input("\nPress Enter to return to the main menu.")

def main():
    shelter = Shelter()
    # Load initial data
    shelter.load_from_csv("data/pets.csv")
    
    while True:
        clear_screen()
        choice = display_menu()
        
        if choice == '1':
            list_all_pets(shelter)
        elif choice == '2':
            add_new_pet(shelter)
        elif choice == '3':
            search_pets(shelter)
        elif choice == '4':
            adopt_pet(shelter)
        elif choice == '5':
            display_pet_details(shelter)
        elif choice == '6':
            save_shelter_data(shelter)
        elif choice == '7':
            load_shelter_data(shelter)
        elif choice == '8':
            print("Thank you for using the Pet Adoption System!")
            break
        else:
            print("Invalid choice. Please try again.")
            input("\nPress Enter to continue.")

if __name__ == "__main__":
    main()