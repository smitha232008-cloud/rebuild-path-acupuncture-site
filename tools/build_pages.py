"""Builds the public pages for The Rebuild Path website. Edit text here, then run: python3 tools/build_pages.py"""
import os
from pathlib import Path

# The FAQ stays off the live site until Amber approves it (Nov 16, 2026). Build a preview with FAQ_LIVE=1.
FAQ_LIVE = os.environ.get("FAQ_LIVE") == "1"

OUT = Path(__file__).resolve().parent.parent / "public"

PHONE = "(928) 316 6511"
TEL = "tel:+19283166511"
SMS = "sms:+19283166511"
ADDRESS = "2700 S Woodlands Village Blvd<br>Ste 300 PMB 212<br>Flagstaff, AZ 86001"
EMAIL_EDU = "therebuildpath@gmail.com"
EMAIL_ACU = "therebuildpathacu@gmail.com"
SKOOL = "https://www.skool.com/the-rebuild-path-6648/about"
SKOOL_CLASSROOM = "https://www.skool.com/the-rebuild-path-6648/classroom"
DISCOVERY = "https://calendly.com/ambersmith2008/discovery"
SITE = "https://therebuildpath.org"
INSTAGRAM = "https://www.instagram.com/therebuildpath/"
FACEBOOK = "https://www.facebook.com/profile.php?id=61582631524025"

NAV = [("index.html", "Home"), ("acupuncture.html", "Acupuncture"), ("education.html", "Education")] + ([("faq.html", "FAQ")] if FAQ_LIVE else []) + [("about.html", "Meet Amber"), ("contact.html", "Contact")]
FAQ_FOOT = '<p><a href="faq.html">FAQ</a></p>' if FAQ_LIVE else ""
FAQ_ACU_LINK = ' Have questions? See the <a href="faq.html#acupuncture">acupuncture FAQ</a>.' if FAQ_LIVE else ""
FAQ_EDU_LINK = '<p class="fine" style="margin-top:14px">Questions? See the <a href="faq.html#education">education FAQ</a>.</p>' if FAQ_LIVE else ""

# Upcoming events. Each card hides itself in the browser once "ends" has passed.
EVENTS = [
    dict(
        title="Acupressure for Seasonal Stress",
        kind="Online workshop",
        month="Nov", day="19", weekday="Thursday",
        ends="2026-11-20T01:15:00Z",
        meta=["5:30 pm Arizona time", "45 minutes", "Live online"],
        text="Learn five acupressure points and a simple breathing practice you can use anywhere, any time stress builds. Take home guide included.",
        price="$15",
        link="https://square.link/u/eWQnmE1y",
        cta="Reserve your spot",
        pages=["index.html", "acupuncture.html", "education.html"],
    ),
]

# Ongoing offers with no date. Always shown after the dated events.
ONGOING = [
    dict(
        title="Goals Workshop",
        kind="In the Skool classroom",
        text="Work through the Goals workshop at your own pace in The Rebuild Path classroom on Skool, with the community there for support.",
        link=SKOOL_CLASSROOM,
        cta="Open the classroom",
        pages=["index.html", "education.html"],
    ),
    dict(
        title="Free 15 minute discovery call",
        kind="Online",
        text="Not sure where to start? Book a short, no pressure call with Amber to talk through what you are working on and which next step fits.",
        link=DISCOVERY,
        cta="Book a discovery call",
        pages=["index.html", "education.html"],
    ),
]

SCHEMA = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Organization","name":"The Rebuild Path",
"description":"Education, CPR training and acupressure coaching in Flagstaff, Arizona, with Amber Smith, L.Ac.",
"logo":"images/logo.jpg","telephone":"+1-928-316-6511","email":"{EMAIL_EDU}",
"areaServed":"Flagstaff, Arizona","sameAs":["{INSTAGRAM}","{FACEBOOK}","{SKOOL}"],
"founder":{{"@type":"Person","name":"Amber Smith","honorificSuffix":"L.Ac."}}}}
</script>"""

LEAF = '<symbol id="leaf" viewBox="0 0 40 80"><path d="M20 2 C35 18 39 46 20 78 C1 46 5 18 20 2 Z"/><path d="M20 8 V76 M20 26 L29 18 M20 26 L11 18 M20 40 L31 31 M20 40 L9 31 M20 54 L30 46 M20 54 L10 46" stroke="rgba(0,0,0,.25)" stroke-width="1.4" fill="none"/></symbol>'
MAPLE = '<symbol id="maple" viewBox="0 0 100 100"><path d="M50 4 L58 26 L72 18 L68 40 L90 34 L80 50 L96 60 L72 64 L76 80 L56 70 L53 96 L47 96 L44 70 L24 80 L28 64 L4 60 L20 50 L10 34 L32 40 L28 18 L42 26 Z"/><path d="M50 30 V94 M50 58 L72 46 M50 58 L28 46 M50 46 L62 30 M50 46 L38 30" stroke="rgba(0,0,0,.22)" stroke-width="1.6" fill="none"/></symbol>'
SPRITE = f'<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>{LEAF}{MAPLE}</defs></svg>'

LEAVES = """<svg class="leafs" viewBox="0 0 300 240" aria-hidden="true">
  <use href="#maple" x="170" y="10" width="100" height="100" fill="#A4502A" transform="rotate(18 220 60)"/>
  <use href="#leaf" x="112" y="22" width="34" height="68" fill="#C8963E" transform="rotate(-38 129 56)"/>
  <use href="#maple" x="222" y="104" width="64" height="64" fill="#D9893A" transform="rotate(-22 254 136)"/>
  <use href="#leaf" x="186" y="126" width="30" height="60" fill="#5F7A4E" transform="rotate(48 201 156)"/>
  <use href="#leaf" x="256" y="14" width="26" height="52" fill="#E2BC72" transform="rotate(30 269 40)"/>
  <use href="#maple" x="132" y="104" width="44" height="44" fill="#8A6A2E" transform="rotate(30 154 126)"/>
</svg>"""

ICON = {
    "hand": '<svg viewBox="0 0 24 24" fill="none" stroke="#2C4F3B" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M8 13V5.5a1.5 1.5 0 0 1 3 0V12M11 11V4.5a1.5 1.5 0 0 1 3 0V12M14 11.5V6a1.5 1.5 0 0 1 3 0v7c0 4.5-2.5 8-6.5 8-2.4 0-3.9-1.1-5.3-3.2L3.4 14a1.5 1.5 0 0 1 2.4-1.8L8 15"/></svg>',
    "breath": '<svg viewBox="0 0 24 24" fill="none" stroke="#2C4F3B" stroke-width="1.6" stroke-linecap="round"><path d="M3 8h11a3 3 0 1 0-3-3M3 12h15a3 3 0 1 1-3 3M3 16h8"/></svg>',
    "move": '<svg viewBox="0 0 24 24" fill="none" stroke="#2C4F3B" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="13" cy="4" r="2"/><path d="M9 21l2.5-6.5L14 17v4M7 10l4-2 3 2 3 1M11.5 14.5L10 9"/></svg>',
    "heart": '<svg viewBox="0 0 24 24" fill="none" stroke="#2C4F3B" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20s-7.5-4.6-7.5-10A4.3 4.3 0 0 1 12 7.4 4.3 4.3 0 0 1 19.5 10c0 5.4-7.5 10-7.5 10z"/><path d="M7 12h3l1.5-2.5 2 4.5 1.5-2h2"/></svg>',
    "group": '<svg viewBox="0 0 24 24" fill="none" stroke="#2C4F3B" stroke-width="1.6" stroke-linecap="round"><circle cx="8" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M2.5 20c.6-3.4 2.8-5.5 5.5-5.5s4.9 2.1 5.5 5.5M14 15c2.9-.6 6 .9 7 5"/></svg>',
    "book": '<svg viewBox="0 0 24 24" fill="none" stroke="#2C4F3B" stroke-width="1.6" stroke-linejoin="round"><path d="M4 5.5C6.5 4 9.5 4 12 6c2.5-2 5.5-2 8-.5V19c-2.5-1.5-5.5-1.5-8 .5-2.5-2-5.5-2-8-.5z"/><path d="M12 6v13.5"/></svg>',
}


def event_cards(file):
    items = [e for e in EVENTS if file in e["pages"]]
    out = []
    for e in items:
        meta = "".join(f"<span>{m}</span>" for m in e["meta"])
        out.append(f"""<article class="event" data-ends="{e['ends']}">
  <div class="date"><small>{e['weekday']}</small><b>{e['day']}</b><span>{e['month']} 2026</span></div>
  <div><p class="tag">{e['kind']}</p><h3>{e['title']}</h3><div class="meta">{meta}</div><p>{e['text']}</p></div>
  <div><div class="price">{e['price']}</div><a class="btn" href="{e['link']}">{e['cta']}</a></div>
</article>""")
    ongoing = "".join(f"""<article class="event ongoing">
  <div class="date"><small>Anytime</small><b>{GOAL if o['link'] == SKOOL_CLASSROOM else CALL}</b><span>{o['kind']}</span></div>
  <div><p class="tag">{o['kind']}</p><h3>{o['title']}</h3><p>{o['text']}</p></div>
  <div><a class="btn ghost" href="{o['link']}">{o['cta']}</a></div>
</article>""" for o in ONGOING if file in o["pages"])
    return f"""<div class="events" data-events>{''.join(out)}
<p class="empty" data-empty hidden>New dates are on the way. Follow along on <a href="{INSTAGRAM}">Instagram</a> or <a href="{FACEBOOK}">Facebook</a>, or join the <a href="{SKOOL}">Skool community</a> to hear first.</p>
{ongoing}
</div>"""


GOAL = '<svg viewBox="0 0 24 24" width="34" height="34" fill="none" stroke="#E2BC72" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5" fill="#E2BC72"/></svg>'
CALL = '<svg viewBox="0 0 24 24" width="34" height="34" fill="none" stroke="#E2BC72" stroke-width="1.6" stroke-linejoin="round"><rect x="3" y="6" width="13" height="12" rx="2"/><path d="M16 10l5-3v10l-5-3z"/></svg>'

SCRIPT = """<script>
(function(){
  var now=Date.now();
  document.querySelectorAll('[data-events]').forEach(function(box){
    var left=0;
    box.querySelectorAll('.event[data-ends]').forEach(function(ev){
      if(Date.parse(ev.getAttribute('data-ends'))<now){ev.remove();}else{left++;}
    });
    if(!left){var e=box.querySelector('[data-empty]'); if(e) e.hidden=false;}
  });
  document.querySelectorAll('section[data-ends]').forEach(function(sec){if(Date.parse(sec.getAttribute('data-ends'))<now) sec.remove();});
  var b=document.querySelector('.menu-btn'), n=document.querySelector('nav.main');
  if(b&&n){b.addEventListener('click',function(){var o=n.classList.toggle('open');b.setAttribute('aria-expanded',o);});}
})();
</script>"""


def page(file, title, desc, body, schema=False):
    links = "".join(
        f'<a href="{href}"{" class=\"on\" aria-current=\"page\"" if href == file else ""}>{name}</a>' for href, name in NAV)
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="google-site-verification" content="A9I97ulmOd-KFU6-9-u8Sgs333k6SVJPT_6PX_2Ohlo">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="images/amber-smith-acupuncturist.jpg">
<meta name="theme-color" content="#152A1E">
<link rel="icon" href="images/logo.jpg">
<link rel="preload" href="fonts/CormorantGaramond-700.ttf" as="font" type="font/ttf" crossorigin>
<link rel="stylesheet" href="styles.css">
{SCHEMA if schema else ""}
</head>
<body>
{SPRITE}
<header class="site">
  <div class="bar">
    <a class="brand" href="index.html"><img src="images/logo.jpg" alt="" width="44" height="44"><span><b>THE REBUILD PATH</b><small>Flagstaff, Arizona</small></span></a>
    <button class="menu-btn" aria-expanded="false" aria-controls="mainnav">Menu</button>
    <nav class="main" id="mainnav" aria-label="Main">{links}</nav>
    <a class="btn gold small" href="{SKOOL}">Join the community</a>
  </div>
</header>
<main>
{body}
</main>
<div class="rule"></div>
<footer class="site">
  <div class="wrap foot">
    <div>
      <a class="brand" href="index.html"><img src="images/logo.jpg" alt="" width="44" height="44"><span><b>THE REBUILD PATH</b><small>Rebuild Mind. Rebuild Body. Rebuild Spirit.</small></span></a>
      <p>Empowering you to reclaim your own choices in health and lifestyle.</p>
    </div>
    <div><h4>Explore</h4><p><a href="acupuncture.html">Acupuncture</a></p><p><a href="education.html">Education</a></p>{FAQ_FOOT}<p><a href="about.html">Meet Amber</a></p><p><a href="contact.html">Contact</a></p></div>
    <div><h4>Connect</h4><p><a href="{SKOOL}">Skool community</a></p><p><a href="{DISCOVERY}">Discovery call</a></p><p><a href="{INSTAGRAM}">Instagram</a></p><p><a href="{FACEBOOK}">Facebook</a></p></div>
    <div><h4>Contact</h4><p class="lbl">Mailing address</p><p>{ADDRESS}</p><p>Online, by appointment only</p><p><a href="{TEL}">Call {PHONE}</a></p><p><a href="{SMS}">Text {PHONE}</a></p><p><a href="mailto:{EMAIL_EDU}">{EMAIL_EDU}</a></p><p><a href="mailto:{EMAIL_ACU}">{EMAIL_ACU}</a></p></div>
  </div>
  <div class="wrap copy"><span>© 2026 The Rebuild Path LLC and The Rebuild Path Acupuncture LLC</span><span>Flagstaff, Arizona</span></div>
</footer>
{SCRIPT}
</body>
</html>
"""
    # Cloudflare serves pages without ".html", so link to the short addresses (no redirect hop).
    import re
    html = html.replace('href="index.html"', 'href="/"')
    html = re.sub(r'href="([a-z]+)\.html(#[a-z]+)?"', lambda m: f'href="/{m.group(1)}{m.group(2) or ""}"', html)
    html = html.replace(f'{SITE}/thanks.html', f'{SITE}/thanks')
    (OUT / file).write_text(html)


EDU_ART = """<svg viewBox="0 0 600 400" role="img" aria-label="Illustration of a heart with a heartbeat line, a book and a leaf">
  <defs><linearGradient id="eg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#F4E9D2"/><stop offset="1" stop-color="#FBF5E9"/></linearGradient></defs>
  <rect width="600" height="400" fill="url(#eg)"/>
  <circle cx="300" cy="200" r="150" fill="none" stroke="#E5D6B4" stroke-width="2"/>
  <circle cx="300" cy="200" r="118" fill="#1F3A2B"/>
  <path d="M300 268 C 250 236 214 206 214 168 A 42 42 0 0 1 300 150 A 42 42 0 0 1 386 168 C 386 206 350 236 300 268 Z" fill="#A4502A"/>
  <path d="M150 204 H 236 L 256 170 L 282 236 L 306 150 L 330 222 L 346 204 H 450" fill="none" stroke="#E2BC72" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
  <use href="#maple" x="440" y="70" width="70" height="70" fill="#D9893A" transform="rotate(18 475 105)"/>
  <use href="#leaf" x="96" y="250" width="34" height="68" fill="#5F7A4E" transform="rotate(-40 113 284)"/>
  <use href="#leaf" x="470" y="262" width="28" height="56" fill="#C8963E" transform="rotate(36 484 290)"/>
</svg>"""

PEAKS_ART = """<svg viewBox="0 0 600 400" role="img" aria-label="Illustration of mountain peaks, pine trees and a winding path at sunrise">
  <defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F4E9D2"/><stop offset="1" stop-color="#F7D9A8"/></linearGradient></defs>
  <rect width="600" height="400" fill="url(#sky)"/>
  <circle cx="300" cy="190" r="70" fill="#E2BC72" opacity=".75"/>
  <path d="M0 250 L 110 170 L 170 205 L 260 120 L 330 175 L 380 140 L 470 205 L 540 160 L 600 200 V 400 H 0 Z" fill="#5F7A4E" opacity=".55"/>
  <path d="M0 290 C 120 250 220 270 300 255 C 400 238 500 250 600 235 V 400 H 0 Z" fill="#2C4F3B"/>
  <path d="M0 330 C 140 305 260 320 360 300 C 450 284 530 300 600 290 V 400 H 0 Z" fill="#1F3A2B"/>
  <path d="M300 400 C 360 370 250 345 300 318 C 340 296 290 280 305 262" fill="none" stroke="#C8963E" stroke-width="10" stroke-linecap="round" opacity=".9"/>
  <g fill="#152A1E">
    <path d="M70 330 L 92 262 L 114 330 Z"/><path d="M80 300 L 92 250 L 104 300 Z"/>
    <path d="M120 322 L 138 268 L 156 322 Z"/>
    <path d="M470 320 L 494 248 L 518 320 Z"/><path d="M482 290 L 494 238 L 506 290 Z"/>
    <path d="M520 316 L 538 266 L 556 316 Z"/>
  </g>
  <use href="#maple" x="40" y="40" width="56" height="56" fill="#A4502A" transform="rotate(-16 68 68)"/>
  <use href="#leaf" x="520" y="50" width="26" height="52" fill="#D9893A" transform="rotate(30 533 76)"/>
</svg>"""

# ---------------- Home ----------------
TRAIL_SVG = """<svg class="line" viewBox="0 0 1000 1200" preserveAspectRatio="none" aria-hidden="true">
  <path d="M500 0 C 500 120, 120 160, 140 330 S 880 470, 860 640 S 120 800, 150 960 S 500 1100, 500 1200" fill="none" stroke="#C8963E" stroke-width="2.5" stroke-dasharray="2 10" stroke-linecap="round" vector-effect="non-scaling-stroke"/>
</svg>"""

page("index.html",
     "The Rebuild Path | Acupressure, CPR and Education in Flagstaff, AZ",
     "The Rebuild Path empowers you to reclaim your own choices in health and lifestyle, with acupressure education, CPR training and community support from Amber Smith, L.Ac., in Flagstaff, Arizona.",
     f"""
<section class="hero dark photo" style="--bg:url(images/01-home-hero-forest-path.webp)">
  {LEAVES}
  <div class="wrap">
    <div>
      <p class="eyebrow">The Rebuild Path</p>
      <h1>Your health. Your choices. <em>Your path.</em></h1>
      <p class="lead">Education, practical tools and a community that help you understand your body and make choices that fit your life.</p>
      <div class="actions"><a class="btn gold arrow" href="#upcoming">See what's coming up</a><a class="btn ghost" href="{SKOOL}">Join the community</a></div>
    </div>
    <div class="arch">
      <div class="frame"><img src="images/amber-smith-acupuncturist.jpg" alt="Amber Smith, L.Ac." width="640" height="800"></div>
      <div class="cap"><b>Amber Smith, L.Ac.</b>Paramedic, CPR instructor<br>and licensed acupuncturist</div>
    </div>
  </div>
</section>
<div class="rule"></div>

<section class="vision cream">
  <div class="wrap">
    <p class="eyebrow">Our vision</p>
    <blockquote>Empowering individuals to reclaim their own choices in health and lifestyle.</blockquote>
    <p class="lead narrow" style="margin:0 auto">Too often, people are told what to do about their health without being shown how their own body works. The Rebuild Path starts from the other side: when you understand your body, you can choose what fits your life. Every class, consultation and conversation here is built to put that choice back in your hands.</p>
    <figure class="wide"><img src="images/02-home-journey-meadow.webp" alt="Open meadow footpath through grasses toward distant mountains" width="1672" height="941" loading="lazy"><figcaption>Become your own wayfinder.</figcaption></figure>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="center"><p class="eyebrow">Find your way</p><h2>Three ways to start</h2></div>
    <div class="trail">
      {TRAIL_SVG}
      <div class="stop">
        <div class="pic"><img src="images/09-acupuncture-care-ambience.webp" alt="Neutral treatment room with linens and warm natural light" width="1000" height="1250" loading="lazy" style="object-position:center 62%"></div>
        <div class="txt"><span class="marker">1</span><p class="tag">The Rebuild Path Acupuncture</p><h3>Acupuncture and Acupressure</h3><p>Learn what acupuncture and acupressure are, and how Traditional Chinese Medicine looks at the whole person, not just the symptom.</p><a class="more" href="acupuncture.html">Explore acupuncture</a></div>
      </div>
      <div class="stop flip">
        <div class="pic"><img src="images/07-education-learning-journal.webp" alt="Open blank journal, fountain pen, tea, and botanical shadows" width="1000" height="1250" loading="lazy" style="object-position:center 60%"></div>
        <div class="txt"><span class="marker">2</span><p class="tag">The Rebuild Path Education</p><h3>Education and CPR</h3><p>American Heart Association CPR and first aid taught by a paramedic, plus online one on one consultations and workshops.</p><a class="more" href="education.html">Explore education</a></div>
      </div>
      <div class="stop">
        <div class="pic"><img src="images/06-personal-growth-overlook.webp" alt="Person viewed from behind looking over a mountain valley" width="1000" height="1250" loading="lazy" style="object-position:center 35%"></div>
        <div class="txt"><span class="marker">3</span><p class="tag">Community</p><h3>Support along the way</h3><p>Join The Rebuild Path on Skool for guided workbooks, conversation and encouragement from people on the same path.</p><a class="more" href="{SKOOL}">Join on Skool</a></div>
      </div>
    </div>
  </div>
</section>

<section class="parch" id="upcoming">
  <div class="wrap">
    <div class="center" style="margin-bottom:40px"><p class="eyebrow">Upcoming</p><h2>Classes, workshops and ways to start</h2></div>
    {event_cards("index.html")}
  </div>
</section>

<section class="community dark photo" style="--bg:url(images/03-journey-forest-trail.webp)">
  {LEAVES.replace('class="leafs"', 'class="leafs" style="left:auto;right:-30px;top:auto;bottom:-30px"')}
  <div class="wrap">
    <div><p class="eyebrow">Community</p><h2>You don't have to rebuild alone.</h2><p class="lead">The Rebuild Path community on Skool is a place for questions, encouragement and the guided workbooks that go with you between classes.</p></div>
    <div class="actions" style="justify-content:flex-start"><a class="btn gold arrow" href="{SKOOL}">Join on Skool</a><a class="btn ghost" href="{INSTAGRAM}">Instagram</a><a class="btn ghost" href="{FACEBOOK}">Facebook</a></div>
  </div>
</section>
""", schema=True)

# ---------------- Acupuncture ----------------
page("acupuncture.html",
     "The Rebuild Path Acupuncture | Acupuncture and Acupressure | Flagstaff, AZ",
     "What acupuncture and acupressure are, with Amber Smith, L.Ac., licensed acupuncturist in Flagstaff, Arizona. Join the online Acupressure for Seasonal Stress workshop.",
     f"""
<section class="page-head dark photo" style="--bg:url(images/10-acupuncture-services-ambience.webp)">
  {LEAVES}
  <div class="wrap">
    <p class="eyebrow">The Rebuild Path Acupuncture</p>
    <h1>Acupuncture and Acupressure</h1>
    <p class="lead">Traditional Chinese Medicine with Amber Smith, L.Ac., licensed acupuncturist and NCBAHM Certified Diplomate in Acupuncture.</p>
  </div>
</section>
<div class="rule"></div>

<section>
  <div class="wrap split">
    <div class="media"><img src="images/needles.jpg" alt="Sterile single use acupuncture needles on a tray" width="1200" height="800" loading="lazy"></div>
    <div>
      <p class="eyebrow">What is acupuncture?</p>
      <h2>Fine needles, specific points, time to rest</h2>
      <p>Acupuncture is one of the oldest parts of Traditional Chinese Medicine. Fine, sterile, single use needles, about the width of a hair, are placed at specific points on the body and left in while you rest.</p>
      <p>Most people feel a mild, dull heaviness or a gentle warmth around the needle, then settle in. The points follow a system developed and refined over more than two thousand years, and Traditional Chinese Medicine looks at the whole person, not just the symptom that brought you in.</p>
      <div class="note">The Rebuild Path is currently online. In person acupuncture visits will return when a new treatment space opens. Follow along on <a href="{INSTAGRAM}">Instagram</a> or <a href="{FACEBOOK}">Facebook</a> to hear first.</div>
    </div>
  </div>
</section>

<section class="cream">
  <div class="wrap split rev">
    <div class="media tall"><img src="images/04-wayfinder-compass-in-hands.webp" alt="Hands holding an antique brass compass against olive fabric" width="1000" height="1250" loading="lazy"></div>
    <div>
      <p class="eyebrow">What is acupressure?</p>
      <h2>The same points, in your own hands</h2>
      <p>Acupressure uses the same points as acupuncture, with steady, comfortable pressure from your fingertips instead of needles. Because you can do it yourself, almost anywhere, it is one of the simplest ways to bring Traditional Chinese Medicine into your daily life.</p>
      <ul class="ticks">
        <li>No needles and no equipment</li>
        <li>Takes a few minutes, at home, at work or before bed</li>
        <li>Pairs well with slow breathing and gentle movement</li>
      </ul>
      <p>Want personal guidance? Amber offers <a href="education.html#consultations">online one on one consultations</a>.{FAQ_ACU_LINK}</p>
    </div>
  </div>
</section>

<section class="parch" id="workshop" data-ends="2026-11-20T01:15:00Z">
  <div class="wrap">
    <div class="center" style="margin-bottom:40px"><p class="eyebrow">Online workshop</p><h2>Acupressure for Seasonal Stress</h2></div>
    <div class="feature">
      <div class="fimg"><img src="images/acupressure-kd27.jpg" alt="Illustration of the Shu Mansion acupressure point below the collarbone" width="1400" height="467" loading="lazy"></div>
      <div class="fbody">
        <p class="lead" style="margin-bottom:14px">45 minutes to ground yourself, using nothing but your own hands.</p>
        <ul class="ticks">
          <li>What acupressure is and how to use it for self care</li>
          <li>A simple grounding sequence of acupressure points</li>
          <li>Where each point is, its traditional uses, and how to apply comfortable pressure</li>
          <li>A brief guided grounding meditation</li>
          <li>A take home guide with every point and the full sequence</li>
        </ul>
        <p class="fine">No experience needed. Your class link is emailed after you register. For education purposes only.</p>
      </div>
    </div>
    <div style="margin-top:28px">{event_cards("acupuncture.html")}</div>
  </div>
</section>
""")

# ---------------- Education ----------------
page("education.html",
     "The Rebuild Path Education | CPR Classes and Consultations | Flagstaff, AZ",
     "American Heart Association CPR and first aid classes taught by a paramedic, online acupressure consultations and workshops from The Rebuild Path in Flagstaff, Arizona.",
     f"""
<section class="page-head dark photo" style="--bg:url(images/08-education-workbook-resources.webp)">
  {LEAVES}
  <div class="wrap">
    <p class="eyebrow">The Rebuild Path Education</p>
    <h1>Learn skills you can carry with you</h1>
    <p class="lead">CPR and first aid, one on one consultations, workshops and a community, so you can take care of yourself and the people around you.</p>
  </div>
</section>
<div class="rule"></div>

<section id="consultations">
  <div class="wrap split">
    <div>
      <p class="eyebrow">Online consultations</p>
      <h2>One on one: reconnect with your body</h2>
      <p>A private online session on how acupressure, meditation and movement can help you reconnect with your body. You learn points and practices you can use on your own, at your own pace, and leave with a plan that fits your day.</p>
      <ul class="ticks"><li>45 minutes, online</li><li>Coaching and education only, no hands on treatment</li><li>Start with a free 15 minute discovery call</li></ul>
      <div class="actions"><a class="btn" href="{DISCOVERY}">Book a free discovery call</a><a class="btn ghost" href="{SMS}">Text to schedule a consultation</a></div>
      {FAQ_EDU_LINK}
    </div>
    <div class="cards" style="grid-template-columns:1fr;margin-top:0">
      <div class="card"><div class="ico">{ICON['hand']}</div><h3>Acupressure</h3><p>Points you can find and press yourself, any time you need them.</p></div>
      <div class="card"><div class="ico">{ICON['breath']}</div><h3>Meditation</h3><p>Simple breathing and grounding practices to settle your mind.</p></div>
      <div class="card"><div class="ico">{ICON['move']}</div><h3>Movement</h3><p>Gentle movement to help you notice and reconnect with your body.</p></div>
    </div>
  </div>
</section>

<section class="parch" id="classes">
  <div class="wrap">
    <div class="center" style="margin-bottom:40px"><p class="eyebrow">Upcoming</p><h2>Classes and educational opportunities</h2></div>
    {event_cards("education.html")}
  </div>
</section>

<section class="cream" id="cpr">
  <div class="wrap">
    <div class="center narrow" style="margin:0 auto"><p class="eyebrow">CPR and first aid</p><h2>Taught by a paramedic</h2><p class="lead">American Heart Association courses from someone who has used these skills in the field. Classes come to your workplace, team or group.</p></div>
    <div class="cards">
      <div class="card"><div class="ico">{ICON['heart']}</div><p class="tag">Healthcare</p><h3>BLS Provider</h3><p>Basic Life Support for healthcare workers and students. Hybrid: the AHA online course, then an in person skills session.</p></div>
      <div class="card"><div class="ico">{ICON['group']}</div><p class="tag">Workplace</p><h3>Heartsaver CPR and AED</h3><p>CPR and AED skills for workplaces, coaches, caregivers and anyone who wants to be ready.</p></div>
      <div class="card"><div class="ico">{ICON['book']}</div><p class="tag">Workplace</p><h3>Heartsaver First Aid, CPR and AED</h3><p>First aid plus CPR and AED in one course, for workplaces that need both.</p></div>
    </div>
    <div class="center" style="margin-top:36px">
      <p>Public class dates are posted above as they are scheduled. To book a private class for your group, call or text <a href="{TEL}">{PHONE}</a>.</p>
      <div class="actions"><a class="btn" href="{SMS}">Text to book a group class</a></div>
    </div>
  </div>
</section>

<section class="community dark photo" style="--bg:url(images/05-wayfinder-journal-and-compass.webp)">
  {LEAVES.replace('class="leafs"', 'class="leafs" style="left:auto;right:-30px;top:auto;bottom:-30px"')}
  <div class="wrap">
    <div><p class="eyebrow">Community support</p><h2>Keep learning between classes.</h2><p class="lead">Guided workbooks, questions and encouragement live in The Rebuild Path community on Skool.</p></div>
    <div class="actions" style="justify-content:flex-start"><a class="btn gold arrow" href="{SKOOL}">Join on Skool</a><a class="btn ghost" href="{SKOOL_CLASSROOM}">Open the classroom</a></div>
  </div>
</section>
""")

# ---------------- About ----------------
page("about.html",
     "Meet Amber Smith, L.Ac. | Founder of The Rebuild Path, Flagstaff, AZ",
     "Amber Smith, L.Ac., founder of The Rebuild Path, is a licensed acupuncturist, paramedic and CPR instructor in Flagstaff, Arizona.",
     f"""
<section class="page-head dark photo light" style="--bg:url(images/11-summit-trail-sunrise.webp)">
  {LEAVES}
  <div class="wrap"><p class="eyebrow">About</p><h1>Meet Amber</h1><p class="lead">Founder of The Rebuild Path.</p></div>
</section>
<div class="rule"></div>
<section>
  <div class="wrap about">
    <aside>
      <img class="photo" src="images/amber-smith-acupuncturist.jpg" alt="Amber Smith, L.Ac." width="640" height="800">
      <div class="cred">
        <img src="images/ncbahm-certified-diplomate.png" alt="NCBAHM Certified Diplomate in Acupuncture" width="96" height="96">
        <ul><li>Licensed Acupuncturist, Arizona</li><li>NCBAHM Certified Diplomate in Acupuncture</li><li>Master of Acupuncture</li><li>Degree in molecular and cellular biology</li><li>Paramedic and CPR instructor</li></ul>
      </div>
    </aside>
    <div>
      <p class="lead">I'm Amber Smith, founder of The Rebuild Path and a licensed acupuncturist practicing Traditional Chinese Medicine.</p>
      <p>Across all my work, one question keeps guiding me: what can help this person move forward from where they are right now?</p>
      <p>That question has taken me from emergency care as a paramedic to teaching CPR, practicing acupuncture, and creating guided workbooks for personal reflection. My training in molecular and cellular biology and my years in emergency medicine shape the curiosity and attention I bring to everything I teach.</p>
      <p>I enjoy making complicated things understandable. That starts with listening to what you're experiencing, how it affects your day, and what you'd like to be able to do or feel differently.</p>
      <p>What I love most is building a relationship over time: learning what matters to you, noticing changes together, and adjusting along the way. My goal is to help you understand your body and feel confident taking an active role in your own well being.</p>
      <div class="actions"><a class="btn" href="{DISCOVERY}">Book a free discovery call</a><a class="btn ghost" href="{SKOOL}">Join the community</a></div>
    </div>
  </div>
</section>
""")

# ---------------- Two part series page (framework) ----------------
# Nov 23, 2026 (Amber): no use of the word inflammation. Title: What Is Your Body Trying to Tell You?
# Topic: how Traditional Chinese Medicine understands the disease process and how its fundamentals help.
# Stage "prelaunch": sneak peek only, no dates, prices or payment buttons.
# Stage "registration": full descriptions, prices and Square buttons. Switch only when every
# field in INFLAMMATION_PARTS is filled in and Amber approves.
# The page is built only with INFLAMMATION_LIVE=1 until Amber approves it (Nov 23, 2026).
INFLAMMATION_LIVE = os.environ.get("SERIES_LIVE") == "1"
INFLAMMATION_STAGE = os.environ.get("SERIES_STAGE", "prelaunch")
INFLAMMATION_IMAGE = "images/series-meditation.webp"  # Amber's promo image of a meditating woman; not supplied yet
INFLAMMATION_PARTS = [
    dict(part="Part 1", title=None, date=None, time=None, length=None, price=None, link=None, text=None),
    dict(part="Part 2", title=None, date=None, time=None, length=None, price=None, link=None, text=None),
]
INFL_THEMES = [
    ("Physical health", "Explore how Traditional Chinese Medicine interprets patterns involving:", "body",
     ["Internal Heat and Cold", "Qi stagnation", "Blood stasis", "Dampness and fluid metabolism", "Digestive discomfort", "Pain, tension and swelling"]),
    ("Mental well being", "Explore traditional connections between internal imbalances and:", "mind",
     ["Mental fatigue", "Difficulty concentrating", "Restlessness", "Sleep disturbances", "Repetitive thinking", "Mental clarity"]),
    ("Emotional well being", "Explore how Traditional Chinese Medicine traditionally understands the relationship between Qi movement and:", "heart",
     ["Anger and frustration", "Emotional tension", "Anxiety and restlessness"]),
]
INFL_ICON = {
    "body": '<svg viewBox="0 0 24 24" fill="none" stroke="#2C4F3B" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="4.5" r="2"/><path d="M12 7v7M8 10l4-1.5 4 1.5M9.5 21l2.5-7 2.5 7"/></svg>',
    "mind": '<svg viewBox="0 0 24 24" fill="none" stroke="#2C4F3B" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M9 20v-3a6 6 0 1 1 6 0v3"/><path d="M9.5 9.5a2.5 2.5 0 0 1 5 0c0 1.5-2.5 2-2.5 3.5M12 15.5v.01"/></svg>',
    "heart": '<svg viewBox="0 0 24 24" fill="none" stroke="#2C4F3B" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20s-7.5-4.6-7.5-10A4.3 4.3 0 0 1 12 7.4 4.3 4.3 0 0 1 19.5 10c0 5.4-7.5 10-7.5 10z"/></svg>',
}

def infl_hero_media():
    if (OUT / INFLAMMATION_IMAGE).exists():
        return f'<div class="infl-photo"><img src="{INFLAMMATION_IMAGE}" alt="A woman sitting in a forest with one hand on her chest and one on her belly, listening to her body" loading="eager" style="object-position:center 18%"></div>'
    # Until Amber's image arrives: a quiet decorative panel, never a stand in photo.
    return """<div class="infl-photo art" aria-hidden="true"><svg viewBox="0 0 400 500">
  <defs><radialGradient id="ig" cx="50%" cy="42%" r="55%"><stop offset="0" stop-color="#D9893A" stop-opacity=".55"/><stop offset=".45" stop-color="#C8963E" stop-opacity=".18"/><stop offset="1" stop-color="#1F3A2B" stop-opacity="0"/></radialGradient></defs>
  <rect width="400" height="500" fill="#1F3A2B"/>
  <circle cx="200" cy="210" r="190" fill="url(#ig)"/>
  <circle cx="200" cy="210" r="70" fill="none" stroke="#E2BC72" stroke-opacity=".55" stroke-width="1.5"/>
  <circle cx="200" cy="210" r="110" fill="none" stroke="#E2BC72" stroke-opacity=".32" stroke-width="1.2"/>
  <circle cx="200" cy="210" r="150" fill="none" stroke="#E2BC72" stroke-opacity=".18" stroke-width="1"/>
  <use href="#maple" x="268" y="330" width="80" height="80" fill="#A4502A" transform="rotate(18 308 370)"/>
  <use href="#leaf" x="70" y="340" width="34" height="68" fill="#C8963E" transform="rotate(-36 87 374)"/>
  <use href="#leaf" x="150" y="400" width="26" height="52" fill="#5F7A4E" transform="rotate(40 163 426)"/>
</svg></div>"""

def infl_registration():
    parts = INFLAMMATION_PARTS
    missing = [p["part"] for p in parts if not all(p[k] for k in ("title", "date", "time", "length", "price", "link", "text"))]
    if missing:
        raise SystemExit("Series registration stage needs every field filled for: " + ", ".join(missing))
    cards = "".join(f"""<article class="infl-part"><p class="tag">{p['part']}</p><h3>{p['title']}</h3>
  <div class="meta"><span>{p['date']}</span><span>{p['time']}</span><span>{p['length']}</span><span>Live online</span></div>
  <p>{p['text']}</p><div class="infl-buy"><span class="price">{p['price']}</span><a class="btn" href="{p['link']}">Register for {p['part']}</a></div></article>""" for p in parts)
    return f"""<section class="parch" id="register"><div class="wrap">
  <div class="center" style="margin-bottom:40px"><p class="eyebrow">Registration is open</p><h2>The two part series</h2></div>
  <div class="infl-parts">{cards}</div>
  <p class="fine center" style="margin-top:22px">For education purposes only. Your class link is emailed after you register.</p>
</div></section>"""

def infl_prelaunch():
    return f"""<section class="parch" id="register"><div class="wrap narrow center">
  <p class="eyebrow">Coming soon</p>
  <h2>A two part educational experience</h2>
  <p class="lead">More information and registration details will be available shortly.</p>
  <p>Want to hear first? Follow along on <a href="{INSTAGRAM}">Instagram</a> or <a href="{FACEBOOK}">Facebook</a>, or join <a href="{SKOOL}">The Rebuild Path community on Skool</a>.</p>
  <p class="fine" style="margin-top:18px">For education purposes only.</p>
</div></section>"""

if INFLAMMATION_LIVE:
    themes = "".join(f"""<article class="infl-theme {key}"><div class="ico">{INFL_ICON[key]}</div><h3>{name}</h3><p>{intro}</p><ul class="ticks">{''.join(f'<li>{i}</li>' for i in items)}</ul></article>""" for name, intro, key, items in INFL_THEMES)
    page("your-body.html",
         "What Is Your Body Trying to Tell You? | A Two Part Series | The Rebuild Path",
         "An upcoming two part educational series from The Rebuild Path on how Traditional Chinese Medicine understands the physical, mental and emotional connections in the body, and how its fundamentals can help you.",
         f"""
<section class="infl-hero dark">
  {LEAVES}
  <div class="wrap">
    <div>
      <p class="eyebrow">Become Your Own Wayfinder</p>
      <h1>What Is Your Body Trying to Tell You?</h1>
      <p class="lead">Understanding the physical, mental and emotional connections through Traditional Chinese Medicine.</p>
      <p class="infl-flag">Coming soon: a two part educational series</p>
    </div>
    {infl_hero_media()}
  </div>
</section>
<div class="rule"></div>

<section class="cream">
  <div class="wrap narrow infl-intro">
    <p class="lead">When something feels off, we often focus on the symptom in front of us: the pain, the tension, the restless night.</p>
    <p class="infl-q">But what about the symptoms that aren't as visible?</p>
    <p>Digestive disturbances, difficulty sleeping, mental fog, muscle tension and emotional changes can sometimes accompany ongoing physical discomfort or illness.</p>
    <p>Traditional Chinese Medicine offers a unique framework for understanding how these patterns develop throughout the body, rather than examining symptoms in isolation. Its fundamentals give you a way to read what your body is telling you.</p>
    <p>Join The Rebuild Path for an upcoming two part educational series exploring these connections and learning practical ways to support your well being.</p>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="center" style="margin-bottom:44px"><p class="eyebrow">What we will explore</p><h2>Three connected themes</h2></div>
    <div class="infl-themes">{themes}</div>
  </div>
</section>

{infl_registration() if INFLAMMATION_STAGE == "registration" else infl_prelaunch()}
""")

# ---------------- FAQ ----------------
FAQ_ACU = [
    ("What is acupuncture?", "Acupuncture is one of the oldest parts of Traditional Chinese Medicine. Fine, sterile, single use needles are placed at specific points on the body and left in while you rest."),
    ("Does acupuncture hurt?", "The needles are solid and about the width of a hair. Most people feel a mild, dull heaviness or a gentle warmth around the needle, then settle in. Speak up any time something feels uncomfortable and it will be adjusted."),
    ("Are the needles reused?", "No. Every needle is sterile, used once, and then disposed of safely."),
    ("What is the difference between acupuncture and acupressure?", "They use the same points. Acupuncture uses fine needles placed by a licensed acupuncturist. Acupressure uses steady, comfortable pressure from your fingertips, so you can do it yourself, almost anywhere."),
    ("Can I use acupressure during pregnancy?", "Some points are traditionally avoided during pregnancy, such as Joining Valley (LI 4) on the hand. If you are pregnant, let Amber know so she can suggest alternative points."),
    ("Can I book an in person acupuncture visit?", "The Rebuild Path is online right now. In person acupuncture visits will return when a new treatment space opens. In the meantime, online workshops and consultations teach acupressure you can use at home."),
    ("Does acupuncture replace my doctor?", "No. Acupuncture and acupressure work alongside the care you already receive. Keep seeing your doctor and other providers."),
    ("Who is the acupuncturist?", "Amber Smith, L.Ac., a licensed acupuncturist in Arizona and an NCBAHM Certified Diplomate in Acupuncture, with a Master of Acupuncture and years of experience as a paramedic."),
]
FAQ_EDU = [
    ("What happens in a one on one consultation?", "A 45 minute online session on how acupressure, meditation and movement can help you reconnect with your body. You learn points and practices you can use on your own. It is coaching and education only, with no hands on treatment."),
    ("How do I get started?", f'Book a <a href="{DISCOVERY}">free 15 minute discovery call</a>. You talk through what you are working on, and together you decide whether a consultation, a workshop or the community is the right next step.'),
    ("Where do consultations and workshops happen?", "Online, by video call. Your link is sent to you before your session or workshop."),
    ("How do I join an online workshop?", "Reserve your spot with the payment link on the workshop card. Your class link and joining instructions are emailed to you before the workshop."),
    ("What is a hybrid CPR class?", "You complete the American Heart Association online course first, then attend an in person skills session with Amber. The online course is purchased directly from the American Heart Association."),
    ("Which CPR class do I need?", "BLS Provider is for healthcare workers and students. Heartsaver courses are for workplaces, coaches, caregivers and the community. If your job requires a certification, ask your employer which course they accept."),
    ("Can you teach a class for our group?", f'Yes. Classes can come to your workplace, team or group. Call or text <a href="{TEL}">{PHONE}</a> to plan a date.'),
    ("How long is a CPR certification good for?", "American Heart Association course completion cards are valid for two years."),
    ("What is The Rebuild Path community?", f'An online community on Skool with guided workbooks, the Goals workshop in the <a href="{SKOOL_CLASSROOM}">classroom</a>, and conversation and support between classes.'),
]
def faq_list(items):
    return "".join(f'<details class="qa"><summary>{q}</summary><div class="ans"><p>{a}</p></div></details>' for q, a in items)

if FAQ_LIVE:
  page("faq.html",
     "Frequently Asked Questions | Acupuncture and Education | The Rebuild Path",
     "Answers to common questions about acupuncture, acupressure, online consultations, workshops and CPR classes with The Rebuild Path in Flagstaff, Arizona.",
     f"""
<section class="page-head dark photo" style="--bg:url(images/03-journey-forest-trail.webp)">
  {LEAVES}
  <div class="wrap"><p class="eyebrow">FAQ</p><h1>Questions and answers</h1><p class="lead">Everything in one place, for acupuncture and for education.</p></div>
</section>
<div class="rule"></div>
<div class="faq-tabs"><div class="wrap"><a href="#acupuncture">Acupuncture</a><a href="#education">Education</a></div></div>
<section id="acupuncture" class="faq-sec">
  <div class="wrap narrow">
    <p class="eyebrow">The Rebuild Path Acupuncture</p><h2>Acupuncture and Acupressure</h2>
    {faq_list(FAQ_ACU)}
  </div>
</section>
<section id="education" class="faq-sec cream">
  <div class="wrap narrow">
    <p class="eyebrow">The Rebuild Path Education</p><h2>Consultations, workshops and CPR</h2>
    {faq_list(FAQ_EDU)}
    <p class="center" style="margin-top:36px">Still have a question? <a href="contact.html">Send a message</a> or <a href="{DISCOVERY}">book a free discovery call</a>.</p>
  </div>
</section>
""")

# ---------------- Contact ----------------
page("contact.html",
     "Contact The Rebuild Path | Flagstaff, AZ",
     "Send The Rebuild Path a general inquiry, book a free 15 minute discovery call, or call or text (928) 316 6511.",
     f"""
<section class="page-head dark photo" style="--bg:url(images/05-wayfinder-journal-and-compass.webp)">
  {LEAVES}
  <div class="wrap"><p class="eyebrow">Contact</p><h1>Send a message</h1><p class="lead">Questions about classes, consultations or the community? Reach out and Amber will get back to you.</p></div>
</section>
<div class="rule"></div>
<section>
  <div class="wrap contact-grid">
    <form class="form" id="inquiry" action="https://formsubmit.co/{EMAIL_EDU}" method="POST" data-ajax="https://formsubmit.co/ajax/{EMAIL_EDU}">
      <input type="hidden" name="_subject" value="New inquiry from The Rebuild Path website">
      <input type="hidden" name="_next" value="{SITE}/thanks.html">
      <input type="hidden" name="_template" value="table">
      <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
      <label>Name<input type="text" name="name" required autocomplete="name"></label>
      <label>Email<input type="email" name="email" required autocomplete="email"></label>
      <label>Your inquiry<textarea name="message" rows="7" required></textarea></label>
      <p class="fine">Please do not include health information in this form.</p>
      <button class="btn" type="submit">Send message</button>
      <p class="form-status" role="status" aria-live="polite" hidden></p>
    </form>
    <div class="form-done" id="inquiry-done" hidden tabindex="-1">
      <h2>Thank you, your message was sent.</h2>
      <p>Amber will reply by email. If it is urgent, call or text <a href="{TEL}">{PHONE}</a>.</p>
    </div>
    <aside class="contact-side">
      <div class="card"><h3>Free discovery call</h3><p>A short, no pressure call to talk through where you are and what you are looking for.</p><p style="margin-top:14px"><a class="btn gold small" href="{DISCOVERY}">Book a discovery call</a></p></div>
      <div class="card"><h3>Call or text</h3><p><a href="{TEL}">{PHONE}</a></p><p class="fine" style="margin-top:8px">Online, by appointment only.</p></div>
      <div class="card"><h3>Email</h3><p>General and education: <a href="mailto:{EMAIL_EDU}">{EMAIL_EDU}</a></p><p>Acupuncture: <a href="mailto:{EMAIL_ACU}">{EMAIL_ACU}</a></p></div>
      <div class="card"><h3>Mailing address</h3><p>{ADDRESS}</p></div>
    </aside>
  </div>
</section>
<script>
(function(){{
  var f=document.getElementById('inquiry'); if(!f||!window.fetch) return;
  var st=f.querySelector('.form-status'), btn=f.querySelector('button[type=submit]'), done=document.getElementById('inquiry-done');
  f.addEventListener('submit',function(e){{
    e.preventDefault();
    if(f._honey&&f._honey.value) return;
    btn.disabled=true; btn.textContent='Sending, one moment';
    st.hidden=false; st.className='form-status'; st.textContent='Sending your message. This can take up to 30 seconds.';
    var data={{}}; new FormData(f).forEach(function(v,k){{data[k]=v;}});
    var ctl=window.AbortController?new AbortController():null; var t=setTimeout(function(){{if(ctl)ctl.abort();}},45000);
    fetch(f.getAttribute('data-ajax'),{{method:'POST',headers:{{'Content-Type':'application/json','Accept':'application/json'}},body:JSON.stringify(data),signal:ctl?ctl.signal:undefined}})
      .then(function(r){{return r.json().catch(function(){{return {{}};}}).then(function(j){{return {{ok:r.ok,j:j}};}});}})
      .then(function(res){{
        clearTimeout(t);
        if(res.ok&&String(res.j.success)!=='false'){{f.hidden=true; done.hidden=false; done.focus();}}
        else{{throw new Error(res.j.message||'not sent');}}
      }})
      .catch(function(){{
        clearTimeout(t); btn.disabled=false; btn.textContent='Send message';
        st.className='form-status error'; st.innerHTML='Sorry, your message did not go through. Please try again, or email <a href="mailto:{EMAIL_EDU}">{EMAIL_EDU}</a> or text <a href="{SMS}">{PHONE}</a>.';
      }});
  }});
}})();
</script>
""")

page("thanks.html",
     "Thank You | The Rebuild Path",
     "Thank you for reaching out to The Rebuild Path.",
     f"""
<section class="page-head dark photo" style="--bg:url(images/02-home-journey-meadow.webp)">
  {LEAVES}
  <div class="wrap"><p class="eyebrow">Message sent</p><h1>Thank you for reaching out.</h1><p class="lead">Your message is on its way. Amber will reply by email.</p>
  <div class="actions"><a class="btn gold" href="index.html">Back to home</a><a class="btn ghost" href="{SKOOL}">Join the community</a></div></div>
</section>
""")

# Old addresses forward to the new pages
for old, new in [("treatment.html", "acupuncture.html"), ("visits.html", "education.html")]:
    (OUT / old).write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex"><link rel="canonical" href="{new}"><meta http-equiv="refresh" content="0; url={new}"><title>The Rebuild Path</title></head><body><p><a href="{new}">Continue to The Rebuild Path</a></p></body></html>\n')

print("built")
