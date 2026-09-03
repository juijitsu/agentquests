import { allLevels } from "@/lib/content";
import Level from "@/app/_pages/Level";

export function generateStaticParams() {
  return allLevels("ru").map((l) => ({ track: l.trackSlug, level: l.slug }));
}

export default async function Page({
  params,
}: {
  params: Promise<{ track: string; level: string }>;
}) {
  const { track, level } = await params;
  return <Level lang="ru" track={track} slug={level} />;
}
