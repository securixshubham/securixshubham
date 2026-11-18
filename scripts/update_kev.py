#!/usr/bin/env python3
"""Build a compact SVG panel from the official CISA Known Exploited Vulnerabilities catalog."""
import json
import urllib.request
from datetime import datetime, timezone
from xml.sax.saxutils import escape
from pathlib import Path

URL = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"
OUT = Path("assets/kev-feed.svg")

def fetch():
    req = urllib.request.Request(URL, headers={"User-Agent": "SECURIX-GitHub-Profile/1.0"})
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)

def svg_text(x, y, text, size=14, color="#b8ffd0", weight="normal"):
    return f'<text x="{x}" y="{y}" font-family="monospace" font-size="{size}" font-weight="{weight}" fill="{color}">{escape(str(text))}</text>'

def main():
    data = fetch()
    items = sorted(data.get("vulnerabilities", []),
                   key=lambda v: v.get("dateAdded", ""), reverse=True)[:7]
    width, height = 1000, 360
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" rx="16" fill="#050b08" stroke="#20c878" stroke-width="2"/>',
        svg_text(28, 42, "SECURIX // CISA KNOWN EXPLOITED VULNERABILITIES", 20, "#65ff9b", "bold"),
        svg_text(28, 70, f"Catalog version: {data.get('catalogVersion','n/a')}  |  Total entries: {data.get('count','n/a')}", 13, "#9adbb2"),
        svg_text(28, 94, f"Catalog released: {data.get('dateReleased','n/a')}", 12, "#78a98a"),
        '<line x1="28" y1="110" x2="972" y2="110" stroke="#176b43"/>'
    ]
    y = 145
    for v in items:
        cve = v.get("cveID", "CVE unavailable")
        vendor = v.get("vendorProject", "")
        product = v.get("product", "")
        date = v.get("dateAdded", "")
        label = f"{cve}  |  {vendor} {product}".strip()
        if len(label) > 92:
            label = label[:89] + "..."
        parts.append(svg_text(30, y, label, 14, "#c7ffd9", "bold"))
        parts.append(svg_text(52, y+20, f"Added: {date}  |  Ransomware use: {v.get('knownRansomwareCampaignUse','Unknown')}", 11, "#83bd98"))
        y += 48
    parts += [
        '<line x1="28" y1="330" x2="972" y2="330" stroke="#176b43"/>',
        svg_text(28, 350, "Source: CISA KEV catalog | Exploited-vulnerability tracking, NOT a live attack feed", 11, "#70b58b"),
        '</svg>'
    ]
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(f"Wrote {OUT} from CISA catalog version {data.get('catalogVersion')}")

if __name__ == "__main__":
    main()
