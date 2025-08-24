from pet import Pet

class Cat(Pet):
    def __init__(self, name, breed, age, description=""):
        super().__init__(name, breed, age, description)
        self._type = "Cat"
    
    @property
    def type(self):
        return self._type
    
    def get_details(self):
        return f"{self._name} (Cat, {self._breed}, {self._age} years old)"
    
    def speak(self):
        return "Meow!"