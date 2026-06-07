# Review 1 — Basics & OOP

This review **consolidates** Assignments 1 and 2: variables, loops, conditionals,
and classes. There is nothing new here — it is practice to make the ideas stick
before Exam 1.

> 🧭 **No terminal.** Edit in **Codespaces**, run the **Testing** panel (🧪),
> commit/push, then open + merge a PR on GitHub.com.

## What you will practice

- `is_even(n)` — conditionals and the modulo operator `%`.
- `reverse_words(sentence)` — splitting and rejoining strings.
- `Counter` — a small class with state (`__init__`, methods).

## Refresher

- `n % 2 == 0` is the standard test for "is `n` even?".
- Strings can be split into a list of words and joined back together with a
  separator.
- A class stores state on `self` inside `__init__` and updates it in methods.

## Worked example (concept only — not the answer)

Reversing the **letters** of a single word demonstrates the slicing idea:

```text
"abc" reversed -> "cba"
```

Reversing **words** is the same idea one level up: split the sentence into a list
of words, reverse the list order, then join them back with spaces. We described
the steps — you write them.

## When you are done

Green checks ✓ → `isCompleted = True` → commit, push, PR, merge → Dashboard card
unlocks. 🎉
