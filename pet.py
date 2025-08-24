class Pet:
    def __init__(self, name, breed, age, description=""):
        self._name = name
        self._breed = breed
        self._age = age
        self._description = description
        self._is_adopted = False
    
    @property
    def name(self):
        return self._name
    
    @property
    def breed(self):
        return self._breed
    
    @property
    def age(self):
        return self._age
    
    @property
    def description(self):
        return self._description
    
    @property
    def is_adopted(self):
        return self._is_adopted
    
    def adopt(self):
        self._is_adopted = True
    
    def get_details(self):
        return f"{self._name} ({self._breed}, {self._age} years old)"
    
    def __str__(self):
        return self.get_details()