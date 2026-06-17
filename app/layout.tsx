import type { Metadata } from "next";
import { IBM_Plex_Sans } from "next/font/google";
import "./globals.css";

// IBM Plex Sans is a corporate identity typeface — it gives the app the crisp,
// businesslike feel of a memo on company letterhead.
const plexSans = IBM_Plex_Sans({
  subsets: ["latin"],
  weight: ["400", "500", "600", "700"],
  display: "swap",
  variable: "--font-plex-sans",
});

export const metadata: Metadata = {
  title: "Data Structures & Algorithms Visualizer",
  description:
    "Companion app for the course \"Design, Analysis, and Essential Properties of Algorithms\".",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={plexSans.variable}>
      <body className="min-h-screen">{children}</body>
    </html>
  );
}
