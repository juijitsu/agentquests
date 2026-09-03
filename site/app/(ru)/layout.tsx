import type { Metadata } from "next";
import Root from "@/app/_shared/Root";
import { dictFor } from "@/lib/i18n";

/* Корневых макетов два — по одному на язык: `<html lang>` может задать
   только корневой макет, а язык страницы обязан быть настоящим. Переход
   между ними перезагружает страницу, и для смены языка это как раз то,
   что нужно. */
const dict = dictFor("ru");

export const metadata: Metadata = {
  title: dict.siteTitle,
  description: dict.siteDescription,
};

export default function Layout({ children }: { children: React.ReactNode }) {
  return <Root lang="ru">{children}</Root>;
}
