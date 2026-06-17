import Link from "next/link";

export default function Home() {
  return (
    <main className="mx-auto flex min-h-screen max-w-2xl flex-col items-center justify-center gap-10 px-6 py-16 text-center">
      <div>
        <p className="mb-5 text-xs font-medium uppercase tracking-[0.3em] text-accent">
          Design, Analysis &amp; Essential Properties of Algorithms
        </p>

        <h1 className="text-balance text-4xl font-semibold leading-[1.1] tracking-tight text-ink-strong sm:text-5xl">
          Data Structures &amp;<br className="hidden sm:block" /> Algorithms
          Visualizer
        </h1>

        {/* A small printer's ornament, like a chapter divider. */}
        <div className="mx-auto mt-6 flex items-center justify-center gap-3 text-ink-faint">
          <span className="h-px w-12 bg-paper-edge" />
          <span className="text-[0.7rem]">❖</span>
          <span className="h-px w-12 bg-paper-edge" />
        </div>

        <p className="mx-auto mt-6 max-w-xl text-pretty text-lg leading-relaxed text-ink-muted">
          A semester-long, Python-powered journey through fundamental computer
          science concepts. Pass an assignment&apos;s tests to unlock its
          interactive visualization on the dashboard.
        </p>
      </div>

      <Link
        href="/dashboard"
        className="rounded-md bg-accent px-6 py-3 text-base font-medium text-paper-raised shadow-paper-sm transition hover:bg-accent-dark"
      >
        Open the Dashboard →
      </Link>

      <p className="text-xs uppercase tracking-[0.2em] text-ink-faint">
        15 units · Python · Next.js
      </p>
    </main>
  );
}
