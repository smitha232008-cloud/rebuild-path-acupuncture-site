# CLAUDE.md: rebuild-path-acupuncture-site

Public website for The Rebuild Path Acupuncture (Amber Smith, L.Ac.) at Barefoot Sage Center, 14 E Birch Ave, Flagstaff, AZ 86001.

* This repository is PUBLIC. Never add books, financial records, patient information, passwords, intake forms, or anything from rebuild-path-books or rebuild_path_operations.
* One page, public/index.html, plain HTML and CSS, no build step. Cloudflare Workers serves the public folder (wrangler.jsonc), deployed by "npx wrangler deploy" on every push to main. Only files in public/ are on the website.
* Brand: warm browns and gold on cream, serif type, Amber's logo. No hyphens or dashes in site copy.
* Booking: https://app.acuityscheduling.com/schedule.php?owner=39409020&calendarID=14435236 or call (928) 444 9411. No payments or health questions on the site.
* Copy rules: no promises of results; symptoms only, never diagnoses; no Tuina for now; never "myofascial release" or "lymphatic drainage".
* Hours shown are Barefoot Sage Center's published hours.
* Live address: https://rebuildpathacupuncture.therebuildpathacu.workers.dev
