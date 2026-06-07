# Assignment 2 — OOP Implementation (Classes & Inheritance)

Object-Oriented Programming (OOP) lets you bundle **data** and **behavior**
together into **classes**. In this assignment you build an `Animal` class and two
subclasses, `Dog` and `Cat`, that **inherit** from it.

> 🧭 **No terminal.** Work in **Codespaces**, run tests from the **Testing**
> panel (🧪), then commit/push and open + merge a PR on GitHub.com.

## What you will build

- `Animal(name)` with a method `speak()` → `"<name> makes a sound"`.
- `Dog(Animal)` that **overrides** `speak()` → `"<name> says Woof"`.
- `Cat(Animal)` that **overrides** `speak()` → `"<name> says Meow"`.

## Key ideas

- A **class** is a blueprint; an **object** (instance) is one thing built from it.
- `__init__` is the **constructor** — it runs when you create an object and is
  where you save data with `self.something = ...`.
- **Inheritance**: `class Dog(Animal)` means "a Dog *is an* Animal" and gets all
  of Animal's abilities for free.
- **Overriding**: a subclass can replace a method with its own version.

## Worked example (concept only — not the answer)

Imagine a `Vehicle` class and a `Car` subclass:

```text
Vehicle stores a `brand` in __init__ and has describe() -> "<brand> vehicle".
Car(Vehicle) overrides describe() -> "<brand> car".

So Vehicle("Acme").describe() gives "Acme vehicle"
and Car("Acme").describe()    gives "Acme car".
```

Your `Animal` / `Dog` / `Cat` follow this exact pattern — store the `name` in
`__init__`, and override `speak()` in each subclass. Write the Python yourself.

## When you are done

Pass all tests in the **Testing** panel, set `isCompleted = True`, then commit,
push, PR, and merge to unlock your Dashboard card. 🎉
