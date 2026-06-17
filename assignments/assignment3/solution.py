"""Assignment 3 — Complexity Analysis (Big O).

This is the ONLY file you edit. Implement the functions, then run the tests.

Big O is just a way of describing how the *amount of work* a function does grows
as its input gets bigger. In this assignment you don't merely label complexity —
you BUILD the loops that achieve a target growth rate. Each function names the
Big O it should hit; your job is to write loops whose shape matches it.

The tests check the exact result your loops must produce, so a clever one-line
formula won't pass — you have to actually construct the loops.
"""


def running_totals(numbers: list) -> list:
    """Return the "running total" at each position — the sum *so far*.

    Picture a bank statement: after every transaction it shows your balance up
    to that point, not just the latest amount. So for deposits ``[1, 2, 3]`` the
    running totals are ``[1, 3, 6]`` — that is ``1``, then ``1 + 2``, then
    ``1 + 2 + 3``.

    Target complexity — O(n) (linear): you should only need to look at each
    number once, in a single pass. Twice as many numbers means about twice the
    work, no more.

    Examples:
        running_totals([1, 2, 3]) == [1, 3, 6]
        running_totals([]) == []          # nothing in, nothing out

    Hint: as you move along the list you'll want to keep track of how much you've
    accumulated so far — think about what to carry from one number to the next.
    """
    raise NotImplementedError("Implement running_totals")


def all_pairs(items: list) -> list:
    """Return every ordered pair that can be formed from the list.

    Imagine a round-robin where everyone is matched against everyone — including
    against themselves. For ``[1, 2]`` the matchups are ``(1, 1)``, ``(1, 2)``,
    ``(2, 1)`` and ``(2, 2)``. Order matters here, so ``(1, 2)`` and ``(2, 1)``
    are both included.

    Target complexity — O(n^2) (quadratic): because every item must be paired
    with every item, ``n`` items create ``n * n`` pairs. Double the list and the
    work roughly *quadruples* — that fast growth is the whole point of this one.

    Examples:
        all_pairs([1, 2]) == [(1, 1), (1, 2), (2, 1), (2, 2)]
        all_pairs([]) == []

    Hint: the phrase "every item with every item" is your clue about how many
    times you'll need to walk through the list.
    """
    raise NotImplementedError("Implement all_pairs")


def halving_sequence(n: int) -> list:
    """Return the values you pass through while repeatedly halving n down to 1.

    This is the "guess the number" trick, where each guess cuts the range in
    half, or finding a word in a dictionary by splitting it in the middle: every
    step throws away about half of what's left. Starting at ``8`` you would see
    ``8``, then ``4``, then ``2``, then ``1``.

    Target complexity — O(log n) (logarithmic): halving shrinks things
    astonishingly fast. Even a list of a million items reaches 1 in only about
    twenty steps. That very slow growth is what "log n" describes.

    Examples:
        halving_sequence(8) == [8, 4, 2, 1]
        halving_sequence(1) == [1]        # already at the finish line
    Assume n >= 1.

    Hint: you can't know up front how many steps it will take, so this calls for
    the kind of loop that keeps running *while* there is still halving left to
    do.
    """
    raise NotImplementedError("Implement halving_sequence")
