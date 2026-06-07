import Link from "next/link";
import { ASSIGNMENTS, type AssignmentMeta } from "@/lib/assignments";
import { importSolution, type SolutionModule } from "@/lib/importSolution";
import { Visualization } from "@/components/Visualization";

// Read solution.py files at request time on the server.
export const dynamic = "force-dynamic";

const KIND_STYLES: Record<AssignmentMeta["kind"], string> = {
  assignment: "border-brand/30",
  review: "border-amber-300",
  exam: "border-rose-300",
};

const KIND_LABELS: Record<AssignmentMeta["kind"], string> = {
  assignment: "Assignment",
  review: "Review",
  exam: "Exam",
};

export default async function DashboardPage() {
  // For each unit, read its solution.py status via the importSolution helper.
  const statuses: SolutionModule[] = await Promise.all(
    ASSIGNMENTS.map((a) => importSolution(a.id))
  );

  const completedCount = statuses.filter((s) => s.isCompleted).length;

  return (
    <main className="mx-auto max-w-6xl px-6 py-12">
      <header className="mb-10 flex flex-col gap-2">
        <Link href="/" className="text-sm text-brand hover:underline">
          ← Home
        </Link>
        <h1 className="text-3xl font-bold tracking-tight">Course Dashboard</h1>
        <p className="text-slate-600">
          Each card unlocks when you set <code>isCompleted = True</code> in that
          assignment&apos;s <code>solution.py</code>.
        </p>
        <p className="text-sm font-medium text-brand">
          {completedCount} / {ASSIGNMENTS.length} completed
        </p>
      </header>

      <section className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {ASSIGNMENTS.map((assignment, index) => {
          const status = statuses[index];
          const unlocked = status.isCompleted;

          return (
            <article
              key={assignment.id}
              className={`flex flex-col rounded-xl border bg-white p-5 shadow-sm transition ${
                KIND_STYLES[assignment.kind]
              } ${unlocked ? "" : "opacity-80"}`}
            >
              <div className="mb-3 flex items-start justify-between gap-2">
                <span className="rounded-full bg-slate-100 px-2 py-0.5 text-xs font-semibold uppercase tracking-wide text-slate-500">
                  {KIND_LABELS[assignment.kind]}
                </span>
                {unlocked ? (
                  <span className="inline-flex items-center gap-1 rounded-full bg-emerald-100 px-2 py-0.5 text-xs font-semibold text-emerald-700">
                    ✓ Completed
                  </span>
                ) : (
                  <span className="inline-flex items-center gap-1 rounded-full bg-slate-100 px-2 py-0.5 text-xs font-semibold text-slate-500">
                    🔒 Locked
                  </span>
                )}
              </div>

              <h2 className="text-lg font-semibold">{assignment.title}</h2>
              <p className="mt-1 text-sm text-slate-600">
                {assignment.summary}
              </p>

              <div className="mt-4 flex-1">
                {unlocked ? (
                  <Visualization topic={assignment.topic} />
                ) : (
                  <div className="flex h-24 items-center justify-center rounded-lg border border-dashed border-slate-200 text-center text-xs text-slate-400">
                    Complete this assignment to reveal the visualization.
                  </div>
                )}
              </div>

              <p className="mt-4 text-xs text-slate-400">
                Folder: <code>assignments/{assignment.id}</code>
                {!status.exists ? " (missing)" : ""}
              </p>
            </article>
          );
        })}
      </section>
    </main>
  );
}
