import type { AssignmentMeta } from "@/lib/assignments";

/**
 * Lightweight, dependency-free visualizations rendered inside a card once an
 * assignment is completed. Each branch is a small SVG / flexbox illustration of
 * the data structure or concept the assignment teaches, drawn in the muted
 * "paper" palette so it reads like a printed diagram.
 */
export function Visualization({ topic }: { topic: AssignmentMeta["topic"] }) {
  switch (topic) {
    case "linkedlist":
      return <NodeChain labels={["A", "B", "C"]} />;
    case "stackqueue":
      return <StackBars />;
    case "bst":
      return <TreeDiagram />;
    case "sorting":
      return <BarChart values={[2, 5, 1, 4, 3]} />;
    case "recursion":
      return <NestedBoxes depth={4} />;
    case "bigo":
      return <GrowthCurves />;
    case "onboarding":
      return <GreetingConsole />;
    case "basics":
      return <CountPositives />;
    case "oop":
      return <InheritanceTree />;
    case "review-basics":
      return <ReviewTags tags={["Variables", "Loops", "Classes"]} />;
    case "review-linear":
      return <ReviewTags tags={["Big O", "Linked lists", "Stacks & queues"]} />;
    case "review-advanced":
      return <ReviewTags tags={["Recursion", "Trees", "Sorting"]} />;
    case "exam-basics":
      return <ExamChecklist items={["Basics", "OOP"]} />;
    case "exam-linear":
      return <ExamChecklist items={["Analysis", "Lists", "Queues"]} />;
    case "exam-advanced":
      return <ExamChecklist items={["Recursion", "Trees", "Search"]} />;
    default:
      return <ConceptBadge />;
  }
}

function NodeChain({ labels }: { labels: string[] }) {
  return (
    <div className="flex items-center gap-1 overflow-x-auto">
      {labels.map((label, i) => (
        <div key={label} className="flex items-center gap-1">
          <span className="flex h-9 w-9 items-center justify-center rounded-md bg-accent text-sm font-semibold text-paper-raised">
            {label}
          </span>
          {i < labels.length - 1 ? (
            <span className="text-ink-faint">→</span>
          ) : (
            <span className="text-xs text-ink-faint">→ null</span>
          )}
        </div>
      ))}
    </div>
  );
}

function StackBars() {
  return (
    <div className="flex flex-col-reverse gap-1">
      {["push 1", "push 2", "push 3"].map((label) => (
        <div
          key={label}
          className="rounded bg-sage px-3 py-1 text-xs font-medium text-paper-raised"
        >
          {label}
        </div>
      ))}
    </div>
  );
}

function TreeDiagram() {
  return (
    <svg viewBox="0 0 160 90" className="h-24 w-full">
      <line x1="80" y1="20" x2="40" y2="55" stroke="#a99e8b" strokeWidth="1.5" />
      <line x1="80" y1="20" x2="120" y2="55" stroke="#a99e8b" strokeWidth="1.5" />
      {[
        { cx: 80, cy: 20, t: "8" },
        { cx: 40, cy: 60, t: "3" },
        { cx: 120, cy: 60, t: "10" },
      ].map((n) => (
        <g key={n.t}>
          <circle cx={n.cx} cy={n.cy} r="14" fill="#55648a" />
          <text
            x={n.cx}
            y={n.cy + 4}
            textAnchor="middle"
            fontSize="11"
            fill="#fbf8f2"
          >
            {n.t}
          </text>
        </g>
      ))}
    </svg>
  );
}

function BarChart({ values }: { values: number[] }) {
  const max = Math.max(...values);
  return (
    <div className="flex h-24 items-end gap-2">
      {values.map((v, i) => (
        <div
          key={i}
          className="w-6 rounded-t bg-accent"
          style={{ height: `${(v / max) * 100}%` }}
          title={String(v)}
        />
      ))}
    </div>
  );
}

function NestedBoxes({ depth }: { depth: number }) {
  let node = (
    <div className="rounded bg-accent px-2 py-1 text-xs text-paper-raised">
      base
    </div>
  );
  for (let i = 0; i < depth; i += 1) {
    node = <div className="rounded border border-accent/30 p-2">{node}</div>;
  }
  return <div className="text-xs">{node}</div>;
}

function GrowthCurves() {
  return (
    <svg viewBox="0 0 160 90" className="h-24 w-full">
      <polyline
        points="0,80 160,70"
        fill="none"
        stroke="#67734f"
        strokeWidth="2"
      />
      <polyline
        points="0,80 80,40 160,10"
        fill="none"
        stroke="#a9803f"
        strokeWidth="2"
      />
      <polyline
        points="0,80 40,60 80,30 120,12 160,2"
        fill="none"
        stroke="#a3654a"
        strokeWidth="2"
      />
      <text x="2" y="88" fontSize="8" fill="#867b69">
        O(1) · O(n) · O(n²)
      </text>
    </svg>
  );
}

function GreetingConsole() {
  return (
    <div className="rounded-md border border-paper-edge bg-paper-sunken px-3 py-2 font-mono text-xs leading-relaxed">
      <p className="text-ink-faint">&gt;&gt;&gt; hello_course()</p>
      <p className="text-ink-strong">&apos;Hello, Algorithms!&apos;</p>
    </div>
  );
}

function CountPositives() {
  const numbers = [-1, 4, 0, 2, -5];
  const positives = numbers.filter((n) => n > 0).length;
  return (
    <div className="flex flex-wrap items-center gap-1">
      {numbers.map((n, i) => (
        <span
          key={i}
          className={`rounded px-2 py-1 text-xs font-medium ${
            n > 0
              ? "bg-accent text-paper-raised"
              : "bg-paper-sunken text-ink-faint"
          }`}
        >
          {n}
        </span>
      ))}
      <span className="ml-1 text-xs text-ink-muted">→ {positives} positive</span>
    </div>
  );
}

function InheritanceTree() {
  const boxes = [
    { x: 70, y: 8, label: "Animal" },
    { x: 18, y: 58, label: "Dog" },
    { x: 122, y: 58, label: "Cat" },
  ];
  return (
    <svg viewBox="0 0 200 90" className="h-24 w-full">
      <line x1="100" y1="28" x2="48" y2="58" stroke="#a99e8b" strokeWidth="1.5" />
      <line x1="100" y1="28" x2="152" y2="58" stroke="#a99e8b" strokeWidth="1.5" />
      {boxes.map((b) => (
        <g key={b.label}>
          <rect x={b.x} y={b.y} width="60" height="20" rx="4" fill="#55648a" />
          <text
            x={b.x + 30}
            y={b.y + 14}
            textAnchor="middle"
            fontSize="11"
            fill="#fbf8f2"
          >
            {b.label}
          </text>
        </g>
      ))}
    </svg>
  );
}

function ReviewTags({ tags }: { tags: string[] }) {
  return (
    <div className="flex flex-wrap gap-1.5">
      {tags.map((tag) => (
        <span
          key={tag}
          className="rounded-full border border-accent/30 bg-paper px-2.5 py-1 text-xs font-medium text-accent"
        >
          {tag}
        </span>
      ))}
    </div>
  );
}

function ExamChecklist({ items }: { items: string[] }) {
  return (
    <ul className="space-y-1.5">
      {items.map((item) => (
        <li key={item} className="flex items-center gap-2 text-xs text-ink">
          <span className="text-sage" aria-hidden>
            ✓
          </span>
          {item}
        </li>
      ))}
    </ul>
  );
}

function ConceptBadge() {
  return (
    <div className="flex h-24 items-center justify-center rounded-md border border-paper-edge bg-paper-sunken text-sm font-medium text-ink-muted">
      Concept unlocked ✓
    </div>
  );
}
