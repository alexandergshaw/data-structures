"""Assignment 2 — OOP Implementation (Classes & Inheritance).

This is the ONLY file you edit. Implement the classes, run the tests.
"""


class Animal:
    """A basic animal.

    Construct with a name. `speak()` should return "<name> makes a sound".
    """

    def __init__(self, name: str) -> None:
        # TODO: store name on the instance (self.name = name)
        raise NotImplementedError("Implement Animal.__init__")

    def speak(self) -> str:
        raise NotImplementedError("Implement Animal.speak")


class Dog(Animal):
    """A Dog is an Animal. Override speak() to return "<name> says Woof"."""

    def speak(self) -> str:
        raise NotImplementedError("Implement Dog.speak")


class Cat(Animal):
    """A Cat is an Animal. Override speak() to return "<name> says Meow"."""

    def speak(self) -> str:
        raise NotImplementedError("Implement Cat.speak")


def adopt(name: str, species: str) -> Animal:
    """Create and return the right animal INSTANCE for the species.

    "dog" -> a Dog, "cat" -> a Cat, anything else -> a plain Animal.
    Example: adopt("Rex", "dog").speak() == "Rex says Woof"
    """
    raise NotImplementedError("Implement adopt")


def make_animals(names: list) -> list:
    """Return a list of Animal INSTANCES, one per name (in the same order).

    Example: make_animals(["Spot"])[0].speak() == "Spot makes a sound"
    """
    raise NotImplementedError("Implement make_animals")
