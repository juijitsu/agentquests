import { allLevels } from "@/lib/content";
import Solve from "@/app/_pages/Solve";

export function generateStaticParams() {
  return allLevels("en")
    .filter((l) => l.runnable)
    .map((l) => ({ track: l.trackSlug, level: l.slug }));
}

export default async function Page({
  params,
}: {
  params: Promise<{ track: string; level: string }>;
}) {
  const { track, level } = await params;
  return <Solve lang="en" track={track} slug={level} />;
}
