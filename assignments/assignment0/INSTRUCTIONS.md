# Assignment 0 — Environment Setup (Onboarding)

Welcome to **Design, Analysis, and Essential Properties of Algorithms**! 🎉

This first assignment does **not** ask you to write any tricky code. Instead, it
walks you through setting up everything you need for the rest of the semester.
By the end you will have:

- Your **own copy** of the course project (a *fork*).
- A **live website** of your project running on **Vercel**.
- Confidence using **GitHub Codespaces**, the **Testing** panel, and the
  **Source Control** panel — all from your web browser.

> 🧭 **No terminal, ever.** You will never need to type commands into a black
> terminal window. Everything in this course is done with buttons and panels in
> the GitHub website and in Codespaces. If a guide online ever tells you to
> "open a terminal," you can ignore it for this course.

---

## Before you start: a quick tour of the words we use

| Word | What it means in plain English |
| --- | --- |
| **Repository (repo)** | A project folder that lives on GitHub. |
| **Fork** | Your personal copy of someone else's repository. |
| **Branch** | A safe, separate workspace inside your repo where you make changes. |
| **Commit** | A saved snapshot of your changes, with a short message. |
| **Pull Request (PR)** | A request to merge your branch's changes into the main branch. |
| **Merge** | Combining your finished changes into the main branch. |
| **Codespaces** | A full code editor that runs in your browser — no install needed. |
| **Vercel** | A service that turns your repo into a live website automatically. |

---

## The 11 Steps

Follow these in order. Each step says exactly which **button** or **panel** to
use. Screenshots in the course portal match these steps.

### Step 1 — Fork the repository

A *fork* is your own copy of the project that you are allowed to change.

1. Open the course repository page on **GitHub.com** in your browser.
2. In the **top-right corner**, click the **`Fork`** button.
3. On the "Create a new fork" screen, leave the settings as they are and click
   the green **`Create fork`** button.
4. Wait a few seconds. GitHub will send you to **your** copy. You can tell it is
   yours because the name at the top will read **`your-username/data-structures`**.

> ✅ **Checkpoint:** The page title shows *your* username, and just under it you
> see the text *"forked from …"*.

### Step 2 — Deploy your fork to Vercel

This makes your project into a real, shareable website.

1. In a new browser tab, go to **vercel.com** and click **`Sign Up`** (or
   **`Log In`**).
2. Choose **`Continue with GitHub`** and approve the access request.
3. On the Vercel dashboard, click **`Add New…`** ▸ **`Project`**.
4. Find **`data-structures`** in the list of your repositories and click
   **`Import`**.
5. Leave every setting at its default value and click the big **`Deploy`**
   button.
6. Wait for the confetti 🎉. Click **`Visit`** to open your live site.

> ✅ **Checkpoint:** You can see the **Data Structures & Algorithms Visualizer**
> home page at a `your-project.vercel.app` web address.

### Step 3 — Open your repository in GitHub Codespaces

Codespaces is the editor you will use to change files.

1. Go back to **your fork** on GitHub.com (the `your-username/data-structures`
   page).
2. Click the green **`< > Code`** button.
3. Select the **`Codespaces`** tab in the little pop-up.
4. Click **`Create codespace on main`**.
5. Wait about a minute while your editor loads in the browser.

> ✅ **Checkpoint:** A code editor (it looks like VS Code) is open in your
> browser, with a list of files on the left.

### Step 4 — Create a new branch (using the Source Control panel)

Never change files directly on `main`. Always work on a branch.

1. Look at the **very bottom-left corner** of the Codespaces window. You will
   see a small label that says **`main`** (next to a branch icon).
2. **Click that `main` label.**
3. A menu opens at the top. Click **`+ Create new branch…`**.
4. Type the branch name exactly: **`assignment0`** and press **Enter**.
5. The bottom-left label now reads **`assignment0`** — you are on your new
   branch.

> ✅ **Checkpoint:** The bottom-left corner shows **`assignment0`**, not `main`.

### Step 5 — Open the assignment files

1. In the file list on the **left**, click the folder **`assignments`**.
2. Click the folder **`assignment0`**.
3. You will see three files. Click each to read it:
   - **`INSTRUCTIONS.md`** — this guide.
   - **`solution.py`** — the file you edit.
   - **`test_assignment.py`** — the tests that check your work.

> ✅ **Checkpoint:** `solution.py` is open in the editor.

### Step 6 — Edit `solution.py`

For this onboarding assignment you only need to do two tiny things:

1. Find the function called **`hello_course`** and make it **return** the exact
   text shown in the worked example below.
2. Change the line **`isCompleted = False`** to **`isCompleted = True`**.

Codespaces saves automatically, but you can also press the usual save shortcut.

> ✅ **Checkpoint:** `solution.py` now has `isCompleted = True` near the top.

### Step 7 — Run the tests using the Testing panel

This is how you check your work **without a terminal**.

1. On the **far-left vertical bar** of Codespaces, click the **Testing** icon —
   it looks like a **flask / Erlenmeyer beaker** 🧪.
2. The first time, click **`Configure Python Tests`** if asked, choose
   **`pytest`**, and then choose the **`assignments`** folder.
3. You will now see your tests listed. Press the **▶ Run Tests** button at the
   top of the Testing panel.
4. Watch each test get a **green check ✓** (pass) or a **red ✗** (fail).
5. If something is red, click it to read the message, fix `solution.py`, and run
   the tests again.

> ✅ **Checkpoint:** Every test for `assignment0` shows a **green check**.

### Step 8 — Commit your changes (using the Source Control panel)

A *commit* saves a snapshot of your work.

1. On the far-left vertical bar, click the **Source Control** icon — it looks
   like **three dots connected by lines** (a little branch shape).
2. You will see your changed files listed under **"Changes."**
3. Hover over each file and click the **`+`** (Stage Changes) button, or click
   the **`+`** next to the word "Changes" to stage them all.
4. In the **message box** at the top, type a short message such as:
   **`Complete assignment 0 onboarding`**.
5. Click the blue **`✓ Commit`** button.

> ✅ **Checkpoint:** The "Changes" list is now empty — your snapshot is saved.

### Step 9 — Publish / Sync your branch to GitHub

Your commit is currently only inside Codespaces. Send it up to GitHub.

1. Still in the **Source Control** panel, click the blue button that says
   **`Publish Branch`** (it may instead say **`Sync Changes`** if the branch
   already exists).
2. If asked to publish to "origin," confirm by clicking **`OK`** /
   **`Publish`**.

> ✅ **Checkpoint:** The button no longer says *Publish Branch*; your
> `assignment0` branch now exists on GitHub.com.

### Step 10 — Open a Pull Request on the GitHub website

A *Pull Request* (PR) proposes merging your branch into `main`.

1. Go back to **your fork** on **GitHub.com** in your browser.
2. GitHub usually shows a yellow banner: **"assignment0 had recent pushes"** with
   a **`Compare & pull request`** button — click it. (If you do not see the
   banner, click the **`Pull requests`** tab, then **`New pull request`**, and
   choose **base: `main`** ← **compare: `assignment0`**.)
3. Give the PR a clear **title**, for example: **`Assignment 0 — Onboarding`**.
4. Click the green **`Create pull request`** button.

> ✅ **Checkpoint:** You are looking at a Pull Request page with your changes
> listed under the **"Files changed"** tab.

### Step 11 — Merge the Pull Request

1. On the Pull Request page, scroll down to the merge box.
2. Click the green **`Merge pull request`** button.
3. Click **`Confirm merge`**.
4. (Optional, tidy) Click **`Delete branch`** to clean up.

> ✅ **Checkpoint:** The PR shows a purple **"Merged"** label. Vercel will now
> automatically rebuild your live site, and your **Dashboard** card for
> Assignment 0 will unlock with a **"Completed"** badge! 🎉

---

## Worked Example (read this — it is not the answer to copy/paste)

Below is an example of the **idea** you will use in `solution.py`. It shows the
*shape* of a function that returns a value. Your task asks for a specific
sentence, which you will type yourself.

```text
A function that "returns" a value hands that value back to whoever called it.

Example shape (NOT your answer):

    def favorite_color():
        return "blue"

Calling favorite_color() now gives back the text "blue".
```

For this assignment, `hello_course()` should **return** the exact sentence:

> `Hello, Algorithms!`

Notice we are describing *what* the function must give back, not writing the
finished function for you. Type it yourself in `solution.py` — that is how the
learning sticks. 💪

---

## How "Completed" works on the Dashboard

The website reads each `solution.py` file and looks for this exact line:

```python
isCompleted = True
```

When it finds it, the matching card on the **Dashboard** unlocks, shows a green
**Completed** badge, and reveals that topic's visualization. So always remember
to flip `isCompleted` to `True` **after** your tests pass.

---

## Troubleshooting

- **I don't see the Testing beaker icon.** Wait for Codespaces to finish
  loading, then reload the browser tab.
- **All tests are red and mention "import".** Make sure you are editing the file
  inside `assignments/assignment0/` and that you did not rename anything.
- **My Vercel site didn't update.** Vercel rebuilds after a merge. Give it a
  minute, then refresh. Check the Vercel dashboard's **Deployments** tab.
- **I'm stuck on a step.** Re-read the **Checkpoint** for that step — it tells
  you what success looks like.

You're all set. See you in Assignment 1! 🚀
