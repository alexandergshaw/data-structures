import statusJson from "./test-status.json";

/**
 * Per-unit test outcome, as recorded in `lib/test-status.json`.
 *
 * The course solutions are authored in Python and cannot be imported into this
 * JS/TS runtime, so we don't run pytest here. Instead, `test-status.json` is
 * regenerated during the build (see `scripts/vercel-build.sh`, which runs
 * `scripts/generate_test_status.py` before `next build`) and imported below, so
 * the unlock state is baked into the deployment — no file system reads at
 * request time, and nothing to keep in sync at runtime.
 *
 * A unit is `passed` only when it has at least one test and none of them fail or
 * error — i.e. the whole suite is green. That single flag is what unlocks the
 * matching Dashboard card.
 */
export interface UnitStatus {
  /** True when the unit has tests and every one of them passes. */
  passed: boolean;
  /** Total number of tests collected for the unit. */
  tests: number;
  /** How many of those tests failed. */
  failures: number;
  /** How many of those tests errored (e.g. raised before asserting). */
  errors: number;
}

export interface TestStatus {
  /** ISO timestamp of when the status file was generated, if known. */
  generatedAt: string | null;
  /** Map of assignment id (folder name) to its latest test outcome. */
  units: Record<string, UnitStatus>;
}

const LOCKED: UnitStatus = {
  passed: false,
  tests: 0,
  failures: 0,
  errors: 0,
};

// Normalize the imported JSON once. If the file is somehow malformed (e.g. an
// empty `{}`), fall back to an empty status so every card renders locked.
const raw = statusJson as Partial<TestStatus>;
const status: TestStatus = {
  generatedAt: raw.generatedAt ?? null,
  units: raw.units ?? {},
};

/** Returns the build-time test status for the whole course. */
export function getTestStatus(): TestStatus {
  return status;
}

/**
 * Returns the status for a single unit, defaulting to a locked state when the
 * unit has no recorded results yet.
 */
export function unitStatus(
  testStatus: TestStatus,
  assignmentId: string
): UnitStatus {
  return testStatus.units[assignmentId] ?? LOCKED;
}
