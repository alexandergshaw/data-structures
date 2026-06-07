import { promises as fs } from "fs";
import path from "path";

/**
 * The shape returned by {@link importSolution}.
 *
 * Because the assignment solutions are authored in Python (`solution.py`) and
 * this app runs in a JavaScript/TypeScript runtime, we cannot literally
 * `import` the Python module. Instead, we read the file from disk and inspect
 * its source for the completion marker that students flip on once they have
 * finished and tested their work:
 *
 * ```python
 * isCompleted = True
 * ```
 *
 * The dashboard uses the `isCompleted` flag to unlock the matching card.
 */
export interface SolutionModule {
  /** The assignment folder id, e.g. `assignment1`. */
  assignmentId: string;
  /** True when the student has set `isCompleted = True` in solution.py. */
  isCompleted: boolean;
  /** True when a `solution.py` file actually exists for this assignment. */
  exists: boolean;
}

const ASSIGNMENTS_DIR = path.join(process.cwd(), "assignments");

/**
 * Detects whether the Python source assigns `isCompleted` to a truthy value.
 *
 * Matches assignments such as `isCompleted = True` (case-insensitive on the
 * boolean, tolerant of surrounding whitespace) while ignoring comments and
 * the default `isCompleted = False`.
 */
export function parseIsCompleted(source: string): boolean {
  // Strip full-line comments so a commented marker does not count.
  const lines = source.split(/\r?\n/).filter((line) => {
    const trimmed = line.trim();
    return trimmed.length > 0 && !trimmed.startsWith("#");
  });

  const completionRegex = /^\s*isCompleted\s*=\s*(True|1)\s*(#.*)?$/i;
  return lines.some((line) => completionRegex.test(line));
}

/**
 * Reads `assignments/<assignmentId>/solution.py` and reports its status.
 *
 * This never throws for a missing file: a missing solution is simply reported
 * as `{ exists: false, isCompleted: false }` so the dashboard can render a
 * locked card.
 */
export async function importSolution(
  assignmentId: string
): Promise<SolutionModule> {
  const filePath = path.join(ASSIGNMENTS_DIR, assignmentId, "solution.py");

  try {
    const source = await fs.readFile(filePath, "utf8");
    return {
      assignmentId,
      isCompleted: parseIsCompleted(source),
      exists: true,
    };
  } catch {
    return { assignmentId, isCompleted: false, exists: false };
  }
}
