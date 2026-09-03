import type { NextConfig } from "next";

/** Сайт живёт на GitHub Pages по адресу /agentquests, отсюда basePath. */
const repo = "/agentquests";

const nextConfig: NextConfig = {
  output: "export",
  basePath: process.env.NODE_ENV === "production" ? repo : "",
  trailingSlash: true,
  images: { unoptimized: true },
  // Воркеру нужен абсолютный путь, а basePath на клиенте иначе не виден.
  env: { NEXT_PUBLIC_BASE_PATH: process.env.NODE_ENV === "production" ? repo : "" },
  // Корневых макетов два, и общего для них 404 из layout + not-found
  // не собрать. Этот флаг включает app/global-not-found.tsx.
  experimental: { globalNotFound: true },
};

export default nextConfig;
