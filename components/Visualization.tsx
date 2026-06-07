import type { AssignmentMeta } from "@/lib/assignments";

/**
 * Lightweight, dependency-free visualizations rendered inside a card once an
 * assignment is completed. Each branch is a small SVG / flexbox illustration of
 * the data structure or concept the assignment teaches.
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
    default:
      return <ConceptBadge />;
  }
}

function NodeChain({ labels }: { labels: string[] }) {
  return (
    <div className="flex items-center gap-1 overflow-x-auto">
      {labels.map((label, i) => (
        <div key={label} className="flex items-center gap-1">
          <span className="flex h-9 w-9 items-center justify-center rounded-md bg-brand text-sm font-semibold text-white">
            {label}
          </span>
          {i < labels.length - 1 ? (
            <span className="text-slate-400">→</span>
          ) : (
            <span className="text-xs text-slate-400">→ null</span>
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
          className="rounded bg-emerald-500/90 px-3 py-1 text-xs font-medium text-white"
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
      <line x1="80" y1="20" x2="40" y2="55" stroke="#94a3b8" />
      <line x1="80" y1="20" x2="120" y2="55" stroke="#94a3b8" />
      {[
        { cx: 80, cy: 20, t: "8" },
        { cx: 40, cy: 60, t: "3" },
        { cx: 120, cy: 60, t: "10" },
      ].map((n) => (
        <g key={n.t}>
          <circle cx={n.cx} cy={n.cy} r="14" fill="#4f46e5" />
          <text
            x={n.cx}
            y={n.cy + 4}
            textAnchor="middle"
            fontSize="11"
            fill="white"
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
          className="w-6 rounded-t bg-brand"
          style={{ height: `${(v / max) * 100}%` }}
          title={String(v)}
        />
      ))}
    </div>
  );
}

function NestedBoxes({ depth }: { depth: number }) {
  let node = (
    <div className="rounded bg-brand px-2 py-1 text-xs text-white">base</div>
  );
  for (let i = 0; i < depth; i += 1) {
    node = (
      <div className="rounded border border-brand/40 p-2">{node}</div>
    );
  }
  return <div className="text-xs">{node}</div>;
}

function GrowthCurves() {
  return (
    <svg viewBox="0 0 160 90" className="h-24 w-full">
      <polyline
        points="0,80 160,70"
        fill="none"
        stroke="#22c55e"
        strokeWidth="2"
      />
      <polyline
        points="0,80 80,40 160,10"
        fill="none"
        stroke="#f59e0b"
        strokeWidth="2"
      />
      <polyline
        points="0,80 40,60 80,30 120,12 160,2"
        fill="none"
        stroke="#ef4444"
        strokeWidth="2"
      />
      <text x="2" y="88" fontSize="8" fill="#64748b">
        O(1) · O(n) · O(n²)
      </text>
    </svg>
  );
}

function ConceptBadge() {
  return (
    <div className="flex h-24 items-center justify-center rounded bg-slate-100 text-sm font-medium text-slate-500">
      Concept unlocked ✓
    </div>
  );
}
