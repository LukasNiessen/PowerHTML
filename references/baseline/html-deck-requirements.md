# HTML Deck Requirements

## Required Features

- Self-contained HTML when requested: inline `<style>`, inline `<script>`, data URLs for local images.
- Slide sections as viewport-sized elements.
- Keyboard controls:
  - forward: `ArrowRight`, `ArrowDown`, `PageDown`, `Space`
  - back: `ArrowLeft`, `ArrowUp`, `PageUp`
  - jump: `Home`, `End`
- URL hash support: `#1`, `#2`, etc.
- Static fallback: readable if JavaScript fails.

## Recommended Structure

```html
<main id="deck">
  <section class="slide">...</section>
  <section class="slide">...</section>
</main>
<script>
  // keyboard + hash navigation
</script>
```

## CSS Requirements

- Use `height: 100vh` and `scroll-snap-align: start` for slide feel.
- Use responsive clamps for font sizes.
- Avoid viewport-width font scaling that creates extreme text sizes.
- Define safe areas with padding.
- Use `overflow: hidden` on slides when presenting.
- Use media queries for mobile fallback.

## Asset Rules

- Use real local assets when provided.
- Embed with base64 data URLs for portability.
- Keep alt text concise.
- Do not rely on external CDNs unless the user explicitly accepts network dependency.

## Common Failure Modes

- Body scroll instead of deck scroll.
- Smooth scrolling when the user wants slide jumps.
- Text too low and clipped on projectors.
- Images linked by local path instead of embedded.
- Too many competing colors.
- A deck that looks like a website instead of a presentation.
