"""Rebuild the one-page public portfolio with Chromium (Python Playwright)."""
from pathlib import Path
import re
from playwright.sync_api import sync_playwright

root = Path(__file__).resolve().parents[1]
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1200, "height": 630})
    page.goto((root / "docs/portfolio-brief.html").as_uri())
    pdf = page.pdf(path=str(root / "assets/engineering-portfolio.pdf"), format="A4", print_background=True, prefer_css_page_size=True)
    assert len(re.findall(rb"/Type /Page\b", pdf)) == 1, "Portfolio must remain one page"
    assert b"GreenContract" not in pdf, "Private predecessor must not be linked"
    page.goto((root / "docs/assets/social-preview.svg").as_uri())
    page.locator("svg").screenshot(path=str(root / "docs/assets/social-preview.png"))
    browser.close()
print("Portfolio PDF and source preview rebuilt; one-page/private-link checks passed.")
