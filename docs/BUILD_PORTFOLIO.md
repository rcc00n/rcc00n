# Rebuild the public portfolio

Use Python 3.12, `playwright==1.55.0`, and its Chromium browser:

```sh
python -m pip install playwright==1.55.0
python -m playwright install chromium
python scripts/build_portfolio.py
```

The editable source is `docs/portfolio-brief.html`; the SVG source preview is
`docs/assets/social-preview.svg`. The script writes the PDF and preview PNG,
checks the PDF stays one page, and rejects links to the private predecessor.
Review all linked public default-branch files before publishing. This is a
selected-work brief, not an employment-history CV or a declaration of team
ownership. Do not invent dates, metrics, roles or availability.
