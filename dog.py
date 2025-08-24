from pet import Pet

class Dog(Pet):
    def __init__(self, name, breed, age, description=""):
        super().__init__(name, breed, age, description)
        self._type = "Dog"
    
    @property
    def type(self):
        return self._type
    
    def get_details(self):
        return f"{self._name} (Dog, {self._breed}, {self._age} years old)"
    
    def speak(self):
        return "Woof!"