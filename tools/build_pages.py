from pathlib import Path
OUT = Path(__file__).resolve().parent.parent / "public"
BOOK = "https://app.acuityscheduling.com/schedule.php?owner=39409020&amp;calendarID=14435236"
TEL = "tel:+19284449411"

NAV = [("index.html", "Home"), ("treatment.html", "Treatment"), ("about.html", "Meet Amber"), ("visits.html", "Visits"), ("contact.html", "Contact")]

SCHEMA = """<script type="application/ld+json">
{"@context":"https://schema.org","@type":"MedicalBusiness","name":"The Rebuild Path Acupuncture",
"description":"Acupuncture and Traditional Chinese Medicine with Amber Smith, L.Ac., at Barefoot Sage Center in downtown Flagstaff.",
"image":"images/amber-smith-acupuncturist.jpg","telephone":"+1-928-444-9411","email":"therebuildpathacu@gmail.com",
"address":{"@type":"PostalAddress","streetAddress":"14 E Birch Ave","addressLocality":"Flagstaff","addressRegion":"AZ","postalCode":"86001","addressCountry":"US"},
"openingHoursSpecification":[
{"@type":"OpeningHoursSpecification","dayOfWeek":"Wednesday","opens":"10:00","closes":"19:00"},
{"@type":"OpeningHoursSpecification","dayOfWeek":["Thursday","Friday","Saturday"],"opens":"10:00","closes":"20:00"},
{"@type":"OpeningHoursSpecification","dayOfWeek":"Sunday","opens":"10:00","closes":"17:00"}],
"medicalSpecialty":"Acupuncture","founder":{"@type":"Person","name":"Amber Smith","honorificSuffix":"L.Ac."}}
</script>"""


def page(file, title, desc, body, schema=False):
    links = "".join(
        f'<a href="{href}"{" class=\"on\" aria-current=\"page\"" if href == file else ""}>{name}</a>' for href, name in NAV)
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="images/amber-smith-acupuncturist.jpg">
<link rel="icon" href="images/logo.jpg">
<link rel="stylesheet" href="styles.css">
{SCHEMA if schema else ""}
</head>
<body>
<header class="site">
  <div class="bar">
    <a class="brand" href="index.html"><img src="images/logo.jpg" alt="" width="44" height="44"><span><b>The Rebuild Path</b><small>Acupuncture</small></span></a>
    <nav aria-label="Main">{links}</nav>
    <a class="btn small" href="{BOOK}">Book</a>
  </div>
</header>
<main>
{body}
</main>
<section class="band">
  <div class="wrap band-in">
    <div><h2>Ready to begin?</h2><p>Book online in a minute, or call the Center and we will find a time that works.</p></div>
    <div class="actions"><a class="btn light" href="{BOOK}">Book online</a><a class="btn outline-light" href="{TEL}">Call (928) 444 9411</a></div>
  </div>
</section>
<footer class="site">
  <div class="wrap foot">
    <div><b>The Rebuild Path Acupuncture</b><br>Amber Smith, L.Ac.<br>at Barefoot Sage Center</div>
    <div>14 E Birch Ave<br>Flagstaff, AZ 86001<br><a href="{TEL}">(928) 444 9411</a></div>
    <div>Wed 10 am to 7 pm<br>Thu to Sat 10 am to 8 pm<br>Sun 10 am to 5 pm</div>
    <div class="fine">© 2026 The Rebuild Path Acupuncture LLC<br>NCBAHM Certified Diplomate in Acupuncture<br><a href="mailto:therebuildpathacu@gmail.com">therebuildpathacu@gmail.com</a></div>
  </div>
</footer>
</body>
</html>
"""
    (OUT / file).write_text(html)


SYMPTOMS = ["Back pain", "Neck and shoulder pain", "Foot pain", "Joint pain", "Headaches", "Sleep issues",
            "Stress and overwhelm", "Muscle tension", "Digestive discomfort", "Menstrual discomfort", "Recovery after injury"]
chips = "".join(f"<li>{s}</li>" for s in SYMPTOMS)

# Home
page("index.html",
     "Acupuncture in Flagstaff, AZ | Amber Smith, L.Ac. | The Rebuild Path Acupuncture",
     "Acupuncture and Traditional Chinese Medicine in downtown Flagstaff with Amber Smith, L.Ac., at Barefoot Sage Center. Back pain, neck pain, headaches, sleep issues, stress and more. Call (928) 444 9411.",
     f"""
<section class="hero">
  <div class="wrap hero-in">
    <div class="hero-text">
      <p class="eyebrow">Downtown Flagstaff · Barefoot Sage Center</p>
      <h1>Acupuncture in Flagstaff</h1>
      <p class="lead">Acupuncture is one branch of Traditional Chinese Medicine, a complete system of care that looks at the whole person and how every part of your life connects.</p>
      <p>Amber Smith, L.Ac. holds a Master of Acupuncture and a degree in molecular and cellular biology, and brings about twelve years in emergency medicine to this work. If you are ready to take a step in a new direction for your health, this is a good place to start.</p>
      <div class="actions"><a class="btn" href="{BOOK}">Book online</a><a class="btn outline" href="{TEL}">Call (928) 444 9411</a></div>
    </div>
    <figure class="portrait"><img src="images/amber-smith-acupuncturist.jpg" alt="Amber Smith, licensed acupuncturist in Flagstaff" width="640" height="800"></figure>
  </div>
</section>
<section>
  <div class="wrap center">
    <p class="eyebrow">How we can help</p>
    <h2>What people come in for</h2>
    <ul class="chips">{chips}</ul>
  </div>
</section>
<section class="soft">
  <div class="wrap">
    <div class="tiles">
      <a class="tile" href="treatment.html"><img src="images/needles.jpg" alt="Sterile single use acupuncture needles on a tray" width="1200" height="800" loading="lazy"><div class="tile-body"><span class="num">01</span><h3>What a treatment is</h3><p>Fine needles, a quiet room, and time to rest. Here is what to expect.</p><span class="more">Learn more</span></div></a>
      <a class="tile" href="about.html"><img class="top" src="images/amber-smith-acupuncturist.jpg" alt="Amber Smith, L.Ac." width="640" height="800" loading="lazy"><div class="tile-body"><span class="num">02</span><h3>Meet Amber</h3><p>Paramedic, CPR instructor and licensed acupuncturist practicing Traditional Chinese Medicine.</p><span class="more">Read her story</span></div></a>
      <a class="tile" href="visits.html"><img src="images/cupping.jpg" alt="Glass cupping cups on folded linen" width="1200" height="800" loading="lazy"><div class="tile-body"><span class="num">03</span><h3>Visits</h3><p>Initial and return visits, plus couples acupuncture for two.</p><span class="more">See visits</span></div></a>
    </div>
  </div>
</section>
""", schema=True)

# Treatment
page("treatment.html",
     "What an Acupuncture Treatment Is | The Rebuild Path Acupuncture, Flagstaff",
     "What to expect from acupuncture in Flagstaff with Amber Smith, L.Ac.: fine single use needles, deep relaxation, and care built around you.",
     f"""
<section class="page-head"><div class="wrap"><p class="eyebrow">Treatment</p><h1>What a treatment is</h1></div></section>
<section>
  <div class="wrap split">
    <figure class="pic"><img src="images/needles.jpg" alt="Sterile single use acupuncture needles on a tray" width="1200" height="800"></figure>
    <div class="prose">
    <p class="lead">Fine, single use needles are placed at specific points and left in while you rest.</p>
    <p>Each needle is solid and about the width of a hair. Most people feel a mild, dull heaviness or a gentle warmth around the needle, then settle in. Some people fall asleep, and others drift into deep relaxation. Both are part of the treatment.</p>
    <p>The points follow a system developed and refined over more than two thousand years. Which points to use, how deep, and how many is the clinical judgment Amber trained for, and it changes from visit to visit as you do.</p>
    </div>
  </div>
</section>
<section class="soft">
  <div class="wrap split rev">
    <div>
      <h2>Other modalities</h2>
      <p>These may be used when indicated. Not every modality is used in every visit.</p>
      <ul class="chips left"><li>Electroacupuncture</li><li>Cupping</li><li>Gua sha</li><li>Hot and cold stone</li><li>Red light therapy</li><li>Ear seeds</li></ul>
    </div>
    <figure class="pic"><img src="images/cupping.jpg" alt="Glass cupping cups on folded linen" width="1200" height="800" loading="lazy"></figure>
  </div>
</section>
<section>
  <div class="wrap narrow">
    <h2>Before your first visit</h2>
    <div class="steps">
      <div><span class="num">1</span><p>Book online or call the Center.</p></div>
      <div><span class="num">2</span><p>Arrive 30 minutes early to complete your new patient paperwork.</p></div>
      <div><span class="num">3</span><p>Wear loose, comfortable clothing that rolls up easily above the knees and elbows.</p></div>
    </div>
  </div>
</section>
<section class="soft">
  <div class="wrap center"><h2>People come in for</h2><ul class="chips">{chips}</ul></div>
</section>
""")

# About
page("about.html",
     "Meet Amber Smith, L.Ac. | Acupuncturist in Flagstaff, AZ",
     "Amber Smith, L.Ac., founder of The Rebuild Path, is a licensed acupuncturist practicing Traditional Chinese Medicine at Barefoot Sage Center in Flagstaff.",
     """
<section class="page-head"><div class="wrap"><p class="eyebrow">About</p><h1>Meet Amber</h1></div></section>
<section>
  <div class="wrap about">
    <aside>
      <img class="photo" src="images/amber-smith-acupuncturist.jpg" alt="Amber Smith, L.Ac." width="640" height="800">
      <div class="cred">
        <img src="images/ncbahm-certified-diplomate.png" alt="NCBAHM Certified Diplomate in Acupuncture" width="96" height="96">
        <ul><li>Licensed Acupuncturist, Arizona</li><li>NCBAHM Certified Diplomate in Acupuncture</li><li>Master of Acupuncture</li><li>Degree in molecular and cellular biology</li><li>Paramedic and CPR instructor</li></ul>
      </div>
    </aside>
    <div class="prose">
      <p class="lead">I'm Amber Smith, founder of The Rebuild Path and a licensed acupuncturist practicing Traditional Chinese Medicine at Barefoot Sage Center.</p>
      <p>Across all my work, one question keeps guiding me: what can help this person move forward from where they are right now?</p>
      <p>That question has taken me from emergency care as a paramedic to teaching CPR, practicing acupuncture, and creating guided workbooks for personal reflection. My training in molecular and cellular biology and my years in emergency medicine shape the curiosity and attention I bring to every treatment.</p>
      <p>I enjoy making complicated things understandable. In acupuncture, that starts with listening to what you're experiencing, how it affects your day, and what you'd like to be able to do or feel differently.</p>
      <p>What I love most is building a relationship over time: learning what matters to you, noticing changes together, and adjusting care along the way. My goal is to help you understand your body and feel confident taking an active role in your own well-being.</p>
    </div>
  </div>
</section>
""")

# Visits
VISITS = [
    ("Initial Visit", "90 minutes", "A full history, a real conversation, then your first treatment, built around what your body needs that day. Please arrive 30 minutes early to complete your new patient paperwork."),
    ("Return Visit", "60 minutes", "A short check in on how you have felt since your last treatment and what has shifted, then the session is adjusted to match."),
    ("Couples Acupuncture, Initial Visit", "150 minutes for two", "Experience acupuncture with someone you love, treated side by side in the same room by one practitioner. Book this visit when either of you is new to the practice. Each person completes their own paperwork here, so please arrive 1 hour early. If something comes up that you would rather discuss privately, just say so."),
    ("Couples Acupuncture, Return Visit", "75 minutes for two", "Together, for two returning patients. A short check in for each person, then treatment adjusted to what each of you needs that day."),
]
cards = "".join(f'<article class="visit"><p class="len">{l}</p><h3>{n}</h3><p>{d}</p><a class="link" href="{BOOK}">Book this visit</a></article>' for n, l, d in VISITS)
page("visits.html",
     "Acupuncture Visits | Initial, Return and Couples | Flagstaff, AZ",
     "Acupuncture visits in Flagstaff with Amber Smith, L.Ac.: Initial Visit, Return Visit, and couples acupuncture. Book online or call (928) 444 9411.",
     f"""
<section class="page-head"><div class="wrap"><p class="eyebrow">Visits</p><h1>Choose your visit</h1></div></section>
<section>
  <div class="wrap">
    <div class="visits">{cards}</div>
    <div class="policy">
      <p>Please give at least 24 hours notice to cancel or reschedule.</p>
      <p>Not sure which visit is yours? Call <a href="{TEL}">(928) 444 9411</a>.</p>
    </div>
  </div>
</section>
""")

# Contact
page("contact.html",
     "Contact and Hours | The Rebuild Path Acupuncture at Barefoot Sage Center, Flagstaff",
     "Find The Rebuild Path Acupuncture at Barefoot Sage Center, 14 E Birch Ave, downtown Flagstaff. Hours, phone and booking.",
     f"""
<section class="page-head"><div class="wrap"><p class="eyebrow">Contact</p><h1>Find us</h1></div></section>
<section>
  <div class="wrap contact">
    <div>
      <h2>Barefoot Sage Center</h2>
      <p>14 E Birch Ave<br>Flagstaff, AZ 86001</p>
      <p class="muted">Downtown, one block off Route 66.</p>
      <p><a href="{TEL}">(928) 444 9411</a><br><a href="mailto:therebuildpathacu@gmail.com">therebuildpathacu@gmail.com</a></p>
      <p class="muted">Payment at your visit. No card needed to book.</p>
      <h2 class="mt">Hours</h2>
      <table class="hours">
        <tr><td>Wednesday</td><td>10 am to 7 pm</td></tr>
        <tr><td>Thursday to Saturday</td><td>10 am to 8 pm</td></tr>
        <tr><td>Sunday</td><td>10 am to 5 pm</td></tr>
        <tr><td>Monday and Tuesday</td><td>Closed</td></tr>
      </table>
      <p class="muted">Appointments outside these hours may be available on request.</p>
    </div>
    <div class="map"><iframe title="Map to Barefoot Sage Center" src="https://maps.google.com/maps?q=14%20E%20Birch%20Ave%2C%20Flagstaff%2C%20AZ%2086001&amp;z=16&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
  </div>
</section>
""")
print("built")
