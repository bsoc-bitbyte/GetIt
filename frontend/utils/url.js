export function extractPath(urlString) {
  try {
    const url = new URL(urlString);
    return url.pathname;
  } catch (error) {
    console.error("Invalid URL:", error);
    return null;
  }
}
