import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./lib/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        // Warm "paper" surfaces — a soft, e-reader sepia canvas.
        paper: {
          DEFAULT: "#fdfbf5", // page background (almost white, faint cream)
          raised: "#fbf8f2", // cards / raised surfaces
          sunken: "#ece4d6", // inset areas (locked placeholders, code)
          edge: "#e3d9c7", // hairline borders
        },
        // "Ink" text — warm dark grays, never pure black.
        ink: {
          DEFAULT: "#3b352b", // body copy
          strong: "#272219", // headings
          muted: "#867b69", // secondary text
          faint: "#a99e8b", // captions / metadata
        },
        // A single restrained accent: faded fountain-pen ink.
        accent: {
          DEFAULT: "#55648a",
          soft: "#8390ac",
          dark: "#41507a",
        },
        // Muted semantics that sit naturally on paper.
        sage: { DEFAULT: "#67734f", soft: "#e6e6d2" }, // "completed"
        ochre: { DEFAULT: "#a9803f" }, // reviews
        clay: { DEFAULT: "#a3654a" }, // exams
      },
      fontFamily: {
        sans: [
          "var(--font-plex-sans)",
          "Segoe UI",
          "system-ui",
          "-apple-system",
          "sans-serif",
        ],
        mono: [
          "ui-monospace",
          "SFMono-Regular",
          "Menlo",
          "Consolas",
          "monospace",
        ],
      },
      boxShadow: {
        // Soft, low-contrast shadows so cards feel like sheets of paper.
        paper:
          "0 1px 2px rgba(58, 49, 33, 0.05), 0 14px 30px -22px rgba(58, 49, 33, 0.35)",
        "paper-sm":
          "0 1px 1px rgba(58, 49, 33, 0.04), 0 4px 12px -10px rgba(58, 49, 33, 0.3)",
      },
    },
  },
  plugins: [],
};

export default config;
