# SECURIX GitHub Profile — Setup

## 1. Create the special profile repository
1. Open https://github.com/new
2. Set Repository name to your exact GitHub username (not `SECURIX`, unless that is your username).
3. Set visibility to **Public**.
4. Initialize with a README, then create the repository.
5. Replace its `README.md` with the `README.md` in this package.

GitHub only displays a profile README when the public repository name exactly matches the account username.

## 2. Upload this package
Upload these paths to the root of the profile repository:
- `README.md`
- `assets/matrix-rain.gif`
- `assets/kev-feed.svg`
- `scripts/update_kev.py`
- `.github/workflows/refresh-kev.yml`

The initial `assets/kev-feed.svg` is a placeholder. Run the workflow once after uploading to populate it from CISA's official catalog.

## 3. Enable the real CISA KEV updater
1. In the repository, open **Actions**.
2. If prompted, enable GitHub Actions.
3. Open **Refresh CISA KEV intelligence panel**.
4. Click **Run workflow**.
5. Wait for the run to complete. The workflow commits a refreshed `assets/kev-feed.svg`.
6. The workflow is scheduled daily at 06:17 UTC.

The CISA KEV catalog records vulnerabilities known to have been exploited. It is not a real-time feed of individual cyberattacks.

## 4. Replace placeholders
In `README.md`, replace every `YOUR_GITHUB_USERNAME`, repository placeholder, website placeholder, and social link with your actual public details. Remove any repository rows you do not use.

## 5. Important GitHub README limitation
GitHub profile READMEs render Markdown and images; they do not host arbitrary JavaScript, iframe dashboards, or continuously running browser animations. The Matrix GIF is a visual animation. The CISA panel updates when GitHub Actions runs. For interactive live attack maps, use the external dashboard links in the README.

## Data sources
- CISA KEV JSON: https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json
- CISA KEV catalog: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- Cloudflare Radar: https://radar.cloudflare.com/
- Check Point Threat Map: https://threatmap.checkpoint.com/
- Fortinet Threat Map: https://threatmap.fortiguard.com/

## Workflow permissions
The workflow needs repository `contents: write` permission to commit the generated SVG. If organization policy blocks this, enable the permission or update the panel manually.
