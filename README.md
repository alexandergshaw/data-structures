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
| `assignment9` | Final Project Prototype (Advanced Data Structures) |
| `review3` | Review of Recursion, Trees, Sorting |
| `exam3` | Test 3 Practice (Recursion, Trees, Algorithms) |

Every folder contains:

- **`INSTRUCTIONS.md`** — a verbose, beginner-friendly guide with worked examples
  (the examples explain the concept; they never give away the answer).
- **`solution.py`** — the single file you edit.
- **`test_assignment.py`** — Pytest tests that import from `solution.py`.

---

## ✅ How an assignment “unlocks” on the Dashboard

When you finish an assignment and your tests pass, set this line in that
assignment’s `solution.py`:

```python
isCompleted = True
```

The website reads each `solution.py` (via the `importSolution(assignmentId)`
helper in [`lib/importSolution.ts`](lib/importSolution.ts)) and, when it sees
`isCompleted = True`, the matching card on the **Dashboard** unlocks — showing a
green **Completed** badge and revealing that topic’s visualization.

Visit **`/dashboard`** on your deployed site to see your progress.

---

## 🛠️ Project layout

```
.
├── app/                  # Next.js App Router
│   ├── page.tsx          # Landing page
│   └── dashboard/page.tsx# Grid of assignment cards (reads solution.py status)
├── components/
│   └── Visualization.tsx # Per-topic visualizations
├── lib/
│   ├── assignments.ts    # Course schedule metadata
│   └── importSolution.ts # Reads solution.py and detects isCompleted
├── assignments/          # All course units (see table above)
├── vercel.json           # Vercel deployment config
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

Deploy by importing the repository into Vercel and clicking **Deploy** — no extra
configuration needed.