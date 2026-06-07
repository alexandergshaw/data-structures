# Exam 1 — Test 1 Practice (Basics & OOP)

This is a **practice test** for Test 1. It mirrors the format and difficulty of
the real exam and covers everything from Assignments 1-2 plus Review 1. Try to
work without peeking at earlier solutions.

> 🧭 **No terminal.** Edit in **Codespaces**, run the **Testing** panel (🧪),
> commit/push, then open + merge a PR on GitHub.com.

## What is on this practice test

- `max_of(values)` — loops and comparisons (no built-in `max`).
- `count_words(sentence)` — string handling.
- `BankAccount` — a class with state **and** error handling (`ValueError`).

## Exam tips

- Read each docstring carefully — it tells you the exact expected behavior.
- Handle the **edge cases** the tests check (single-element lists, overdrawing an
  account, etc.).
- To signal an invalid operation, `raise ValueError("message")`.

## Worked example (concept only — not the answer)

Finding the largest value by hand:

```text
Assume the first item is the biggest so far.
Walk through the rest; whenever you see a bigger one, remember it instead.
At the end, the remembered value is the maximum.
```

The `BankAccount.withdraw` follows a guard pattern: **check** the bad condition
first and `raise`, otherwise do the normal update. You write the Python.

## When you are done

Green checks ✓ → `isCompleted = True` → commit, push, PR, merge → Dashboard card
unlocks. Good luck on the real Test 1! 🎉
