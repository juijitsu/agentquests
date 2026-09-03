import { allLevels } from "@/lib/content";
import Level from "@/app/_pages/Level";

export function generateStaticParams() {
  return allLevels("en").map((l) => ({ track: l.trackSlug, level: l.slug }));
}

export default async function Page({
  params,
}: {
  params: Promise<{ track: string; level: string }>;
}) {
  const { track, level } = await params;
  return <Level lang="en" track={track} slug={level} />;
}
