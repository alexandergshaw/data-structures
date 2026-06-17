# Review 1 — Basics & OOP

This review **consolidates** Assignments 1 and 2: `for` and `while` loops,
conditionals, functions that take parameters (including a **default** one), and
classes with **inheritance**, **overriding**, and **instances**. There is nothing
new here — it is practice to make the ideas stick before Exam 1.

> 🧭 **No terminal.** Edit in **Codespaces**, run the **Testing** panel (🧪),
> commit/push, then open + merge a PR on GitHub.com.

## What you will practice

- `count_above(numbers, threshold=0)` — a loop, a comparison, and a **default**
  parameter.
- `digit_sum(n)` — a **`while` loop** that peels off one digit at a time.
- `Shape` / `Rectangle` / `Square` — a small class family showing **inheritance**
  and **overriding**.
- `make_squares(sides)` — **create instances** (objects) inside a loop.

## Refresher

- A parameter can have a **default**: `def count_above(numbers, threshold=0)`
  lets callers leave `threshold` out.
- A **`while` loop** runs until its condition is False; `n % 10` is the last
  digit of `n` and `n // 10` removes it.
- A subclass **inherits** its parent's methods and may **override** them; you
  build an object by calling the class, e.g. `Square(5)`.

## Worked example (concept only — not the answer)

A subclass can reuse a parent's method without rewriting it:

```text
Rectangle stores width and height and has area() -> width * height.
Square(Rectangle) stores only one side... but a square IS a rectangle,
so it can use Rectangle's area() unchanged.
```

Your `Square` does exactly this: set its width and height to the same value and
let the **inherited** `area()` do the rest. We described the idea — you write it.

## When you are done

Green checks ✓ → commit, push, PR, merge → Dashboard card
unlocks. 🎉
