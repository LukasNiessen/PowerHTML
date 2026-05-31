# QA Checklist

Run the checks that are practical for the environment.

## Static Checks

- File exists and is non-empty.
- Slide count matches the narrative.
- CSS and JS are inline.
- No unresolved placeholders like `TODO`, `lorem`, `undefined`, or broken asset names.
- Data URL count matches expected embedded assets.
- Keyboard handler includes forward/back/Home/End.
- Hash jumps work in code.

## Visual Checks

- Render representative screenshots:
  - cover / opener
  - agenda
  - densest text slide
  - most visual slide
  - final slide
- Check for:
  - clipped titles
  - overlapping text
  - tiny body text
  - missing images
  - low contrast
  - accidental scrollbars
  - wrong final slide

## Browser Command Pattern

Use a headless browser if available:

```powershell
msedge.exe --headless --disable-gpu --window-size=1920,1080 --screenshot=out.png file:///C:/path/deck.html#3
```

Use separate browser profile directories for parallel screenshots.

## Final Response

Include:

- HTML path.
- Screenshot paths if created.
- Slide count.
- Navigation support.
- Known limitations.
