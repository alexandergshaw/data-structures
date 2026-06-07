"""Assignment 2 — OOP Implementation (Classes & Inheritance).

This is the ONLY file you edit. Implement the classes, run the tests, then set
isCompleted = True at the bottom.
"""

# Flip to True after all tests pass (unlocks the Dashboard card).
isCompleted = False


class Animal:
    """A basic animal.

    Construct with a name. `speak()` should return "<name> makes a sound".
    """

    def __init__(self, name: str) -> None:
        # TODO: store name on the instance (self.name = name)
        raise NotImplementedError("Implement Animal.__init__")

    def speak(self) -> str:
        # TODO: return f"{self.name} makes a sound"
        raise NotImplementedError("Implement Animal.speak")


class Dog(Animal):
    """A Dog is an Animal. Override speak() to return "<name> says Woof"."""

    def speak(self) -> str:
        # TODO: return f"{self.name} says Woof"
        raise NotImplementedError("Implement Dog.speak")


class Cat(Animal):
    """A Cat is an Animal. Override speak() to return "<name> says Meow"."""

    def speak(self) -> str:
        # TODO: return f"{self.name} says Meow"
        raise NotImplementedError("Implement Cat.speak")
