# Exam 1 — Test 1 Practice (Basics & OOP)

This is a **practice test** for Test 1. It mirrors the format and difficulty of
the real exam and covers everything from Assignments 1-2 plus Review 1. Try to
work without peeking at earlier solutions.

> 🧭 **No terminal.** Edit in **Codespaces**, run the **Testing** panel (🧪),
> commit/push, then open + merge a PR on GitHub.com.

## What is on this practice test

- `count_long_words(words, min_length=4)` — a loop, a comparison, and a
  **default** parameter.
- `count_up_to(n)` — a simple **`while` loop** that builds the list `1..n`.
- `Employee` / `Manager` — **inheritance** and **overriding** (and a method that
  calls another so subclasses describe themselves correctly).
- `hire(name, manager=False)` — **create the right instance** based on a flag.

## Exam tips

- Read each docstring carefully — it tells you the exact expected behavior.
- Handle the **edge cases** the tests check (empty lists, `count_up_to(0)`, and
  values where the `while` loop should never run, etc.).
- A **default** parameter (`min_length=4`, `manager=False`) lets a caller leave
  an argument out — but they can still override it.

## Worked example (concept only — not the answer)

Overriding plus a shared method gives you flexible behavior for free:

```text
Employee.describe() returns "<name>: <role()>" — it ASKS role() for the word.
Manager overrides role() to return "manager".
So Manager("Pat").describe() is "Pat: manager" even though describe() was
never rewritten — it simply calls the Manager's version of role().
```

Your `Employee` / `Manager` follow this pattern: override only what differs and
let the inherited method use it. You write the Python.

## When you are done

Green checks ✓ → commit, push, PR, merge → Dashboard card
unlocks. Good luck on the real Test 1! 🎉
