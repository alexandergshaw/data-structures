/**
 * Static metadata describing every unit in the course.
 *
 * The `id` matches the folder name under `/assignments`, e.g. `assignment0`.
 * The `kind` controls how the card is grouped/styled on the dashboard.
 * The `topic` string is shown on the card and used to pick a visualization.
 */

export type AssignmentKind = "assignment" | "review" | "exam";

export interface AssignmentMeta {
  id: string;
  title: string;
  kind: AssignmentKind;
  topic: string;
  summary: string;
}

export const ASSIGNMENTS: AssignmentMeta[] = [
  {
    id: "assignment0",
    title: "Assignment 0 — Environment Setup",
    kind: "assignment",
    topic: "onboarding",
    summary: "Fork, deploy to Vercel, and learn the no-terminal workflow.",
  },
  {
    id: "assignment1",
    title: "Assignment 1 — Basic Python",
    kind: "assignment",
    topic: "basics",
    summary: "Variables, loops, and simple functions.",
  },
  {
    id: "assignment2",
    title: "Assignment 2 — OOP Implementation",
    kind: "assignment",
    topic: "oop",
    summary: "Classes, objects, and inheritance.",
  },
  {
    id: "review1",
    title: "Review 1 — Basics & OOP",
    kind: "review",
    topic: "review-basics",
    summary: "Consolidate Python fundamentals and object-oriented design.",
  },
  {
    id: "exam1",
    title: "Exam 1 — Test 1 Practice",
    kind: "exam",
    topic: "exam-basics",
    summary: "Practice problems covering basics and OOP.",
  },
  {
    id: "assignment3",
    title: "Assignment 3 — Complexity Analysis",
    kind: "assignment",
    topic: "bigo",
    summary: "Build loops that meet a target Big O complexity.",
  },
  {
    id: "assignment4",
    title: "Assignment 4 — Linked List",
    kind: "assignment",
    topic: "linkedlist",
    summary: "Build a singly linked list from scratch.",
  },
  {
    id: "assignment5",
    title: "Assignment 5 — Stack / Queue",
    kind: "assignment",
    topic: "stackqueue",
    summary: "Implement and apply stacks and queues.",
  },
  {
    id: "review2",
    title: "Review 2 — Analysis & Linear Structures",
    kind: "review",
    topic: "review-linear",
    summary: "Consolidate complexity analysis and linear structures.",
  },
  {
    id: "exam2",
    title: "Exam 2 — Test 2 Practice",
    kind: "exam",
    topic: "exam-linear",
    summary: "Practice covering analysis, lists, stacks, and queues.",
  },
  {
    id: "assignment6",
    title: "Assignment 6 — Recursive Algorithms",
    kind: "assignment",
    topic: "recursion",
    summary: "Solve problems with recursion and base cases.",
  },
  {
    id: "assignment7",
    title: "Assignment 7 — Binary Search Tree",
    kind: "assignment",
    topic: "bst",
    summary: "Implement a binary search tree.",
  },
  {
    id: "assignment8",
    title: "Assignment 8 — Sorting Efficiency",
    kind: "assignment",
    topic: "sorting",
    summary: "Implement and compare sorting algorithms.",
  },
  {
    id: "review3",
    title: "Review 3 — Recursion, Trees, Sorting",
    kind: "review",
    topic: "review-advanced",
    summary: "Consolidate recursion, trees, and sorting.",
  },
  {
    id: "exam3",
    title: "Exam 3 — Test 3 Practice",
    kind: "exam",
    topic: "exam-advanced",
    summary: "Practice covering recursion, trees, and algorithms.",
  },
];
