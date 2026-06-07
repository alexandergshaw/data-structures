"""Tests for Assignment 2 — OOP Implementation."""

from solution import Animal, Dog, Cat


def test_animal_speaks():
    assert Animal("Critter").speak() == "Critter makes a sound"


def test_dog_overrides_speak():
    assert Dog("Rex").speak() == "Rex says Woof"


def test_cat_overrides_speak():
    assert Cat("Mia").speak() == "Mia says Meow"


def test_inheritance():
    assert issubclass(Dog, Animal)
    assert issubclass(Cat, Animal)
    assert isinstance(Dog("Rex"), Animal)
