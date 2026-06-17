import Link from "next/link";
import { ASSIGNMENTS, type AssignmentMeta } from "@/lib/assignments";
import { getTestStatus, unitStatus } from "@/lib/testStatus";
import { Visualization } from "@/components/Visualization";

// Each unit kind gets a quietly tinted label; the card itself stays uniform.
const KIND_LABEL_STYLES: Record<AssignmentMeta["kind"], string> = {
  assignment: "text-accent",
  review: "text-ochre",
  exam: "text-clay",
};

const KIND_LABELS: Record<AssignmentMeta["kind"], string> = {
  assignment: "Assignment",
  review: "Review",
  exam: "Exam",
};

export default function DashboardPage() {
  // A unit's card unlocks when all of its tests pass. Results are computed at
  // build time and imported from lib/test-status.json (see lib/testStatus.ts).
  const testStatus = getTestStatus();

  const completedCount = ASSIGNMENTS.filter(
    (a) => unitStatus(testStatus, a.id).passed
  ).length;
  const progress = Math.round((completedCount / ASSIGNMENTS.length) * 100);

  return (
    <main className="mx-auto max-w-6xl px-6 py-14">
      <header className="mb-12 flex flex-col gap-3">
        <Link
          href="/"
          className="text-sm text-accent transition hover:text-accent-dark"
        >
          ← Home
        </Link>
        <h1 className="text-3xl font-semibold tracking-tight text-ink-strong">
          Course Dashboard
        </h1>
        <p className="max-w-2xl leading-relaxed text-ink-muted">
          Each card unlocks automatically once{" "}
          <strong className="font-semibold text-ink">
            all of that assignment&apos;s unit tests pass
          </strong>
          . Tests run as part of the Vercel build; merge your work and the card
          reveals its visualization.
        </p>

        {/* Reading-progress through the course. */}
        <div className="mt-2 flex flex-col gap-2">
          <p className="text-xs uppercase tracking-[0.18em] text-ink-faint">
            {completedCount} of {ASSIGNMENTS.length} completed
          </p>
          <div className="h-1.5 w-full max-w-sm overflow-hidden rounded-full bg-paper-sunken">
            <div
              className="h-full rounded-full bg-sage transition-all"
              style={{ width: `${progress}%` }}
            />
          </div>
        </div>
      </header>

      <section className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3">
        {ASSIGNMENTS.map((assignment) => {
          const status = unitStatus(testStatus, assignment.id);
          const unlocked = status.passed;
          const passing = status.tests - status.failures - status.errors;

          return (
            <article
              key={assignment.id}
              className={`flex flex-col rounded-lg border border-paper-edge bg-paper-raised p-5 shadow-paper-sm transition ${
                unlocked ? "" : "opacity-90"
              }`}
            >
              <div className="mb-3 flex items-start justify-between gap-2">
                <span
                  className={`text-xs font-semibold uppercase tracking-[0.16em] ${
                    KIND_LABEL_STYLES[assignment.kind]
                  }`}
                >
                  {KIND_LABELS[assignment.kind]}
                </span>
                {unlocked ? (
                  <span className="inline-flex items-center gap-1 rounded-full bg-sage-soft px-2.5 py-0.5 text-xs font-medium text-sage">
                    ✓ Completed
                  </span>
                ) : (
                  <span className="inline-flex items-center gap-1 rounded-full border border-paper-edge px-2.5 py-0.5 text-xs font-medium text-ink-faint">
                    Locked
                  </span>
                )}
              </div>

              <h2 className="text-lg font-semibold leading-snug text-ink-strong">
                {assignment.title}
              </h2>
              <p className="mt-1.5 text-sm leading-relaxed text-ink-muted">
                {assignment.summary}
              </p>

              <div className="mt-4 flex-1">
                {unlocked ? (
                  <Visualization topic={assignment.topic} />
                ) : (
                  <div className="flex h-24 items-center justify-center rounded-md border border-dashed border-paper-edge bg-paper/60 px-4 text-center text-xs text-ink-faint">
                    Pass all unit tests to reveal the visualization.
                  </div>
                )}
              </div>

              <p className="mt-4 border-t border-paper-edge pt-3 text-xs text-ink-faint">
                <code>assignments/{assignment.id}</code>
                {status.tests > 0
                  ? ` · ${passing}/${status.tests} tests passing`
                  : " · no test results yet"}
              </p>
            </article>
          );
        })}
      </section>
    </main>
  );
}
