#!/usr/bin/env python
"""Create a starter Power HTML deck.

The generated file is intentionally small. Treat it as a starting point and
customize the visual system to the user prompt.
"""

from __future__ import annotations

import argparse
import html
from pathlib import Path


BASE_CSS = r"""
:root { --bg:#050506; --ink:#f7f8fb; --muted:#a8afbb; --accent:#32f5b2; }
* { box-sizing:border-box; }
html, body { margin:0; height:100%; background:var(--bg); color:var(--ink); font-family:Segoe UI, system-ui, sans-serif; }
body { overflow:hidden; }
main { height:100vh; overflow-y:scroll; scroll-snap-type:y mandatory; scrollbar-width:none; }
main::-webkit-scrollbar { display:none; }
.slide { position:relative; height:100vh; padding:72px 104px; scroll-snap-align:start; overflow:hidden; background:var(--bg); }
.kicker { color:var(--accent); font-weight:800; text-transform:uppercase; font-size:20px; margin:0 0 22px; }
h1 { margin:0; font-size:clamp(64px, 7vw, 112px); line-height:.95; letter-spacing:0; }
p, li { font-size:clamp(24px, 2vw, 34px); line-height:1.2; color:var(--muted); }
.accent { position:absolute; left:104px; bottom:56px; width:380px; height:6px; background:var(--accent); }
"""

NAV_JS = r"""
(() => {
  const deck = document.getElementById("deck");
  const slides = [...document.querySelectorAll(".slide")];
  let index = 0;
  const currentIndex = () => {
    const y = deck.scrollTop;
    let best = 0, bestDistance = Infinity;
    slides.forEach((slide, i) => {
      const dist = Math.abs(slide.offsetTop - y);
      if (dist < bestDistance) { best = i; bestDistance = dist; }
    });
    return best;
  };
  const go = (next) => {
    index = Math.max(0, Math.min(slides.length - 1, next));
    deck.scrollTo({ top: slides[index].offsetTop, behavior: "auto" });
  };
  const fromHash = () => {
    const parsed = Number.parseInt(location.hash.replace("#", ""), 10);
    if (Number.isFinite(parsed)) go(parsed - 1);
  };
  addEventListener("keydown", (event) => {
    const forward = ["ArrowRight", "ArrowDown", "PageDown", " "];
    const back = ["ArrowLeft", "ArrowUp", "PageUp"];
    if (![...forward, ...back, "Home", "End"].includes(event.key)) return;
    event.preventDefault();
    index = currentIndex();
    if (forward.includes(event.key)) go(index + 1);
    if (back.includes(event.key)) go(index - 1);
    if (event.key === "Home") go(0);
    if (event.key === "End") go(slides.length - 1);
  });
  addEventListener("hashchange", fromHash);
  requestAnimationFrame(fromHash);
})();
"""


def read_customization(cwd: Path) -> str:
    custom = cwd / ".power-html" / "power-html.md"
    return custom.read_text(encoding="utf-8") if custom.exists() else ""


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a starter self-contained Power HTML deck.")
    parser.add_argument("output", type=Path)
    parser.add_argument("--title", default="Power HTML Deck")
    parser.add_argument("--cwd", type=Path, default=Path.cwd())
    args = parser.parse_args()

    customization = read_customization(args.cwd)
    customization_comment = f"\n<!-- Customization loaded:\n{html.escape(customization)}\n-->\n" if customization else ""

    doc = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(args.title)}</title>
  <style>{BASE_CSS}</style>
</head>
<body>{customization_comment}
  <main id="deck">
    <section class="slide"><p class="kicker">Start</p><h1>{html.escape(args.title)}</h1><div class="accent"></div></section>
    <section class="slide"><p class="kicker">Principle</p><h1>One slide, one job.</h1><div class="accent"></div></section>
  </main>
  <script>{NAV_JS}</script>
</body>
</html>
"""
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(doc, encoding="utf-8")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
