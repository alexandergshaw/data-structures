# Data Structures &amp; Algorithms Visualizer

Companion project for the semester-long course **“Design, Analysis, and
Essential Properties of Algorithms.”** You learn fundamental computer-science
concepts in **Python**, and each assignment you complete **unlocks an
interactive visualization** in a **Next.js** web app you deploy to **Vercel**.

> 🧭 **No terminal required — ever.** Everything is done with buttons and panels
> in the **GitHub website** and **GitHub Codespaces**: the **Source Control**
> panel, the **Testing** panel, and Pull Requests on GitHub.com.

---

## 🚀 Quick start (students)

New here? Start with **[`assignments/assignment0/INSTRUCTIONS.md`](assignments/assignment0/INSTRUCTIONS.md)**.
It is an 11-step, beginner-friendly onboarding guide that walks you through:

1. Forking this repository
2. Deploying your fork to Vercel
3. Opening the project in Codespaces
4. Creating a branch (Source Control panel)
5. Opening the assignment files
6. Editing `solution.py`
7. Running tests in the Testing panel (🧪)
8. Committing (Source Control panel)
9. Publishing / syncing your branch
10. Opening a Pull Request on GitHub.com
11. Merging the Pull Request

---

## 📚 Course schedule

| Folder | Topic |
| --- | --- |
| `assignment0` | Environment Setup (Onboarding) |
| `assignment1` | Basic Python (Variables / Loops) |
| `assignment2` | OOP Implementation (Classes / Inheritance) |
| `review1` | Review of Basics &amp; OOP |
| `exam1` | Test 1 Practice (Basics &amp; OOP) |
| `assignment3` | Complexity Analysis (Big O) |
| `assignment4` | Linked List Implementation |
| `assignment5` | Stack / Queue Application |
| `review2` | Review of Analysis &amp; Linear Structures |
| `exam2` | Test 2 Practice (Analysis, Lists, Stacks, Queues) |
| `assignment6` | Recursive Algorithms |
| `assignment7` | BST Implementation |
| `assignment8` | Sorting Efficiency |
| `review3` | Review of Recursion, Trees, Sorting |
| `exam3` | Test 3 Practice (Recursion, Trees, Algorithms) |

Every folder contains:

- **`INSTRUCTIONS.md`** — a verbose, beginner-friendly guide with worked examples
  (the examples explain the concept; they never give away the answer).
- **`solution.py`** — the single file you edit.
- **`test_assignment.py`** — Pytest tests that import from `solution.py`.

---

## ✅ How an assignment “unlocks” on the Dashboard

There is no manual flag — **a card unlocks when every one of that assignment’s
unit tests passes.** The flow is fully automatic:

1. You implement `solution.py` until the **Testing** panel is all green, then
   commit, push, and merge.
2. The merge triggers a Vercel deploy. During the build,
   [`scripts/vercel-build.sh`](scripts/vercel-build.sh) runs each unit’s tests
   (via [`scripts/generate_test_status.py`](scripts/generate_test_status.py)) and
   writes the results to [`lib/test-status.json`](lib/test-status.json) before
   `next build`.
3. The site imports that file (via
   [`lib/testStatus.ts`](lib/testStatus.ts)); when a unit is all-green the
   matching **Dashboard** card unlocks — showing a green **Completed** badge and
   revealing that topic’s visualization.

Because the status is baked into the build, the Dashboard updates on every
deploy with no extra commits. Visit **`/dashboard`** on your deployed site to see
your progress.

---

## 🛠️ Project layout

```
.
├── app/                  # Next.js App Router
│   ├── page.tsx          # Landing page
│   └── dashboard/page.tsx# Grid of assignment cards (reads test-status.json)
├── components/
│   └── Visualization.tsx # Per-topic visualizations
├── lib/
│   ├── assignments.ts    # Course schedule metadata
│   ├── testStatus.ts     # Imports test-status.json (which cards unlock)
│   └── test-status.json  # Per-unit pass/fail, regenerated each build
├── scripts/
│   ├── generate_test_status.py  # Runs pytest per unit, writes test-status.json
│   └── vercel-build.sh   # Build command: generate status, then `next build`
├── assignments/          # All course units (see table above)
├── vercel.json           # Vercel deployment config (buildCommand)
└── pytest.ini            # Pytest configuration
```

---

## 💻 For instructors / local development

The app is a standard Next.js project and is **Vercel-ready** (`vercel.json`).

- Web app: `npm install` then `npm run dev` (open http://localhost:3000).
- Build: `npm run build`.
- Tests: `pytest assignments` runs the whole course, or `pytest assignments/assignment4`
  runs a single unit. (Students use the Codespaces **Testing** panel instead of
  a terminal.)
- Unlock status: `python scripts/generate_test_status.py` regenerates
  `lib/test-status.json`. The committed copy is just a baseline — the Vercel build
  regenerates it on every deploy (see `scripts/vercel-build.sh`), so you normally
  never edit it by hand.

Deploy by importing the repository into Vercel and clicking **Deploy** — no extra
configuration needed.

> ℹ️ The build runs the Python test suite, so it relies on `python3` being
> present in Vercel’s build image (it is, by default). If it ever isn’t, the
> build falls back to the committed `lib/test-status.json` instead of failing.