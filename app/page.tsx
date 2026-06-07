import Link from "next/link";

export default function Home() {
  return (
    <main className="mx-auto flex min-h-screen max-w-3xl flex-col items-center justify-center gap-8 px-6 text-center">
      <div>
        <p className="mb-2 text-sm font-semibold uppercase tracking-widest text-brand">
          Design, Analysis, and Essential Properties of Algorithms
        </p>
        <h1 className="text-4xl font-bold tracking-tight sm:text-5xl">
          Data Structures &amp; Algorithms Visualizer
        </h1>
        <p className="mt-4 text-lg text-slate-600">
          A semester-long, Python-powered journey through fundamental computer
          science concepts. Complete each assignment to unlock its interactive
          visualization on the dashboard.
        </p>
      </div>
      <Link
        href="/dashboard"
        className="rounded-lg bg-brand px-6 py-3 text-base font-semibold text-white shadow-sm transition hover:bg-brand-dark"
      >
        Open the Dashboard →
      </Link>
    </main>
  );
}
