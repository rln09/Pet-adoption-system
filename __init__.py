import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pet import Pet
from dog import Dog
from cat import Cat

def test_pet_creation():
    """Test that a Pet object is created with correct attributes"""
    pet = Pet("Buddy", "Golden Retriever", 3, "Friendly dog")
    assert pet.name == "Buddy"
    assert pet.breed == "Golden Retriever"
    assert pet.age == 3
    assert pet.description == "Friendly dog"
    assert not pet.is_adopted

def test_pet_adoption():
    """Test that a pet can be adopted"""
    pet = Pet("Buddy", "Golden Retriever", 3)
    pet.adopt()
    assert pet.is_adopted

def test_dog_inheritance():
    """Test that Dog inherits from Pet and has correct type"""
    dog = Dog("Max", "Labrador", 5)
    assert isinstance(dog, Pet)
    assert dog.type == "Dog"
    assert dog.speak() == "Woof!"

def test_cat_inheritance():
    """Test that Cat inherits from Pet and has correct type"""
    cat = Cat("Whiskers", "Siamese", 2)
    assert isinstance(cat, Pet)
    assert cat.type == "Cat"
    assert cat.speak() == "Meow!"

def test_pet_string_representation():
    """Test the string representation of pets"""
    dog = Dog("Buddy", "Golden Retriever", 3)
    assert "Buddy" in str(dog)
    assert "Golden Retriever" in str(dog)
    assert "3" in str(dog)