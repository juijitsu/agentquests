import type { Metadata } from "next";
import Home from "@/app/_pages/Home";
import { dictFor } from "@/lib/i18n";

// Заголовок макета говорит про агентов и на этой полке был бы неправдой.
const dict = dictFor("ru");

export const metadata: Metadata = {
  title: `${dict.coursesTitle} — AgentQuests`,
  description: dict.coursesLead,
};

export default function Page() {
  return <Home lang="ru" section="courses" />;
}
