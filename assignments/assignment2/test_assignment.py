"""Tests for Assignment 2 — OOP Implementation."""

from solution import Animal, Dog, Cat, adopt, make_animals


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


def test_adopt_creates_correct_instances():
    dog = adopt("Rex", "dog")
    assert isinstance(dog, Dog)
    assert dog.speak() == "Rex says Woof"

    cat = adopt("Mia", "cat")
    assert isinstance(cat, Cat)
    assert cat.speak() == "Mia says Meow"

    other = adopt("Critter", "fish")
    assert isinstance(other, Animal)
    assert not isinstance(other, (Dog, Cat))
    assert other.speak() == "Critter makes a sound"


def test_make_animals_builds_instances():
    animals = make_animals(["Spot", "Whiskers"])
    assert len(animals) == 2
    assert all(isinstance(a, Animal) for a in animals)
    assert animals[0].speak() == "Spot makes a sound"
    assert make_animals([]) == []
