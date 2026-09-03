import type { NextConfig } from "next";

/** Сайт живёт на GitHub Pages по адресу /agentquests, отсюда basePath. */
const repo = "/agentquests";

const nextConfig: NextConfig = {
  output: "export",
  basePath: process.env.NODE_ENV === "production" ? repo : "",
  trailingSlash: true,
  images: { unoptimized: true },
};

export default nextConfig;
