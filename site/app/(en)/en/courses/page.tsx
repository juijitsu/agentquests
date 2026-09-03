import type { Metadata } from "next";
import Home from "@/app/_pages/Home";
import { dictFor } from "@/lib/i18n";

// The layout title is about agents and would be untrue on this shelf.
const dict = dictFor("en");

export const metadata: Metadata = {
  title: `${dict.coursesTitle} — AgentQuests`,
  description: dict.coursesLead,
};

export default function Page() {
  return <Home lang="en" section="courses" />;
}
