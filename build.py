#!/usr/bin/env python3
"""Static site generator for cleargridstudios.com — no dependencies.

Edit PAGES/PRODUCTS below, run `python3 build.py`, commit the HTML.
"""
import html
from pathlib import Path

OUT = Path(__file__).parent
DOMAIN = "https://cleargridstudios.com"
GUMROAD = "https://cleargridstudios.gumroad.com"
ETSY = "https://www.etsy.com/shop/ClearGridStudiosCo"

PRODUCTS = [
    ("Ultimate Job Search Tracker", "9.99", f"{GUMROAD}/l/jobsearchtracker",
     "Applications, interviews, contacts, and offer comparison — with a dashboard that runs itself."),
    ("ATS Resume Template — Classic", "12.99", f"{GUMROAD}/l/atsresume",
     "The parse-tested single-column resume bundle: resume, cover letter, references, ATS guide."),
    ("All-in-One Wedding Planner", "19.99", f"{GUMROAD}/l/weddingplanner",
     "Checklist, budget, guest list, vendors, seating, and the day-of run sheet in one file."),
    ("Wedding Budget Tracker", "8.99", f"{GUMROAD}/l/weddingbudget",
     "18 benchmark categories, payment schedule with due-date alerts, auto dashboard."),
    ("Rental Property Deal Analyzer", "14.99", f"{GUMROAD}/l/dealanalyzer",
     "Cash flow, cap rate, cash-on-cash, DSCR, and a 3-deal comparison — before you offer."),
    ("Landlord Income & Expense Tracker", "16.99", f"{GUMROAD}/l/landlordtracker",
     "Schedule-E-aligned bookkeeping with a tax summary that reads straight onto the form."),
    ("ATS Resume Template — Modern", "12.99", f"{GUMROAD}/l/atsresumemodern",
     "The same parse-tested single-column bundle with a teal, contemporary look."),
    ("Freelancer Income & Expense Tracker", "16.99", f"{GUMROAD}/l/freelancertracker",
     "Schedule-C bookkeeping with quarterly estimated tax, mileage, and per-client income."),
    ("Short-Term Rental P&L Tracker", "16.99", f"{GUMROAD}/l/strtracker",
     "Occupancy, ADR and RevPAR computed from your bookings — monthly and per listing."),
    ("Job Offer Comparison & Salary Negotiation Calculator", "12.99", f"{GUMROAD}/l/offercompare",
     "Five offers ranked on total compensation — equity, match, benefits, commute, cost of living."),
    ("Interview Prep Kit", "10.99", f"{GUMROAD}/l/interviewprepkit",
     "A STAR story bank, a practiced-question log, and company research notes — with a readiness dashboard."),
    ("CapEx Reserve & Replacement Schedule", "12.99", f"{GUMROAD}/l/capexschedule",
     "Know what breaks next, and whether you've saved enough for it — due-now/due-soon flags and reserve coverage."),
    ("Salary Negotiation Tracker", "11.99", f"{GUMROAD}/l/salarynegotiation",
     "Market research, a target/walk-away range, a talking-points script, and a round-by-round negotiation log."),
    ("BRRRR Deal Calculator", "15.99", f"{GUMROAD}/l/brrrrcalculator",
     "All-in cost, ARV, refinance loan and cash-out, cash left in the deal, and the resulting cash-on-cash return."),
    ("Tenant Move-In/Move-Out & Deposit Tracker", "14.99", f"{GUMROAD}/l/tenanttracker",
     "Room-by-room condition at move-in and move-out, with the deposit refund — or amount owed — computed automatically."),
    ("Career Change Skills Gap Tracker", "11.99", f"{GUMROAD}/l/careerchangetracker",
     "Your skills matched by exact name against the target role's requirements — sorted into Have, must-fix, or nice-to-have."),
    ("New Job 90-Day Onboarding Planner", "8.99", f"{GUMROAD}/l/newjobonboarding",
     "30/60/90-day goals, a stakeholder map, a wins log, and a manager check-in log — for after you start."),
    ("Tenant Screening & Applicant Comparison Tracker", "13.99", f"{GUMROAD}/l/tenantscreening",
     "Income-to-rent ratio, credit/background/eviction status, and a 0-10 score that ranks every applicant per unit."),
    ("Fix-and-Flip Budget & Timeline Tracker", "15.99", f"{GUMROAD}/l/fixandfliptracker",
     "Renovation budget by category, contractor draws, holding costs, and ARV-vs-cost-basis profit/ROI at sale."),
    ("Job Search Networking & Referral Tracker", "10.99", f"{GUMROAD}/l/networkingtracker",
     "Outreach log with overdue follow-up flags, informational interviews, and referral requests — response rate included."),
]

CSS = """
:root{--ink:#1F2A44;--navy:#1F3A5F;--teal:#2E8B8B;--bg:#fafbfc;--soft:#eef3f4;--gray:#5b6472;--line:#e3e8ef}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:system-ui,-apple-system,'Segoe UI',sans-serif;color:var(--ink);background:var(--bg);line-height:1.65}
a{color:var(--teal)}
.wrap{max-width:880px;margin:0 auto;padding:0 20px}
header{background:#fff;border-bottom:1px solid var(--line)}
header .wrap{display:flex;align-items:center;justify-content:space-between;padding:14px 20px}
.logo{font-weight:800;font-size:1.15rem;color:var(--navy);text-decoration:none}
.logo span{color:var(--teal)}
nav a{margin-left:18px;font-size:.95rem;text-decoration:none;color:var(--gray)}
nav a:hover{color:var(--teal)}
.hero{padding:64px 0 40px;text-align:center}
.hero h1{font-size:2.3rem;line-height:1.15;color:var(--navy);margin-bottom:14px}
.hero p{font-size:1.15rem;color:var(--gray);max-width:640px;margin:0 auto 26px}
.btn{display:inline-block;background:var(--teal);color:#fff;font-weight:700;padding:12px 26px;border-radius:8px;text-decoration:none}
.btn.ghost{background:transparent;color:var(--teal);border:2px solid var(--teal);margin-left:10px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:18px;padding:30px 0 50px}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:22px;display:flex;flex-direction:column}
.card h3{color:var(--navy);font-size:1.05rem;margin-bottom:8px}
.card p{font-size:.92rem;color:var(--gray);flex:1}
.card .price{font-weight:800;color:var(--ink);margin:12px 0 10px}
.card a{font-weight:700;text-decoration:none}
article{background:#fff;border:1px solid var(--line);border-radius:12px;padding:40px;margin:36px 0}
article h1{color:var(--navy);font-size:1.9rem;line-height:1.2;margin-bottom:8px}
article .byline{color:var(--gray);font-size:.9rem;margin-bottom:24px}
article h2{color:var(--navy);font-size:1.3rem;margin:28px 0 10px}
article p,article li{margin-bottom:12px}
article ul,article ol{padding-left:24px}
article table{width:100%;border-collapse:collapse;margin:14px 0}
article th{background:var(--navy);color:#fff;text-align:left;padding:8px 12px;font-size:.9rem}
article td{border-bottom:1px solid var(--line);padding:8px 12px;font-size:.95rem}
.cta{background:var(--soft);border-radius:10px;padding:20px 22px;margin:26px 0}
.cta strong{color:var(--navy)}
footer{border-top:1px solid var(--line);padding:28px 0 40px;color:var(--gray);font-size:.88rem;text-align:center}
footer a{color:var(--gray)}
@media(max-width:600px){.hero h1{font-size:1.7rem}article{padding:26px 18px}nav a{margin-left:10px;font-size:.85rem}}
"""


def layout(slug, title, desc, body):
    canonical = DOMAIN + ("/" if slug == "index" else f"/{slug}.html")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{canonical}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<meta name="p:domain_verify" content="c6eddd83d54ee4cae3e0228343f279e9"/>
<link rel="stylesheet" href="style.css">
</head>
<body>
<header><div class="wrap">
<a class="logo" href="index.html">ClearGrid<span>Studios</span></a>
<nav>
<a href="index.html">Templates</a>
<a href="ats-resume-checklist.html">Resume Help</a>
<a href="wedding-budget-guide.html">Wedding</a>
<a href="rental-property-bookkeeping.html">Landlords</a>
<a href="about.html">About</a>
</nav>
</div></header>
<div class="wrap">
{body}
</div>
<footer><div class="wrap">
<p>© 2026 ClearGridStudios · Every cell checked before it ships.</p>
<p><a href="{GUMROAD}">Gumroad store</a> · <a href="{ETSY}">Etsy shop</a> · <a href="mailto:hello@cleargridstudios.com">hello@cleargridstudios.com</a> · <a href="about.html">About</a></p>
</div></footer>
</body>
</html>"""


def product_grid():
    cards = ""
    for name, price, url, blurb in PRODUCTS:
        cards += f"""<div class="card"><h3>{name}</h3><p>{blurb}</p>
<div class="price">${price}</div>
<a href="{url}">Get it on Gumroad →</a></div>\n"""
    return f'<div class="grid">{cards}</div>'


def cta(text, url, label):
    return f'<div class="cta"><strong>{text}</strong><br><a href="{url}">{label} →</a></div>'


PAGES = {}

PAGES["index"] = (
    "ClearGridStudios — Spreadsheets You Can Count On",
    "Job search trackers, wedding planners, landlord and freelancer bookkeeping, and ATS resume templates for Excel & Google Sheets. Every formula verified before release.",
    f"""
<div class="hero">
<h1>Spreadsheets with formulas you can <em>count on</em></h1>
<p>Job-search trackers, wedding planners, landlord and freelancer bookkeeping, and ATS-safe resume templates — built for Excel and Google Sheets, and mechanically tested before we sell them. No broken formulas, no decorative junk.</p>
<a class="btn" href="{GUMROAD}">Shop on Gumroad</a><a class="btn ghost" href="{ETSY}">Shop on Etsy</a>
</div>
<h2 style="color:var(--navy)">The catalog</h2>
{product_grid()}
"""
)

PAGES["ats-resume-checklist"] = (
    "Is Your Resume ATS-Friendly? A 10-Point Checklist (2026)",
    "Applicant tracking systems reject resumes for formatting, not qualifications. Run this free 10-point ATS checklist before your next application.",
    f"""
<article>
<h1>Is Your Resume ATS-Friendly? The 10-Point Checklist</h1>
<div class="byline">ClearGridStudios · Updated August 2026</div>
<p>Most mid-size and large employers run applications through an applicant tracking system (ATS) before a human sees them. The system extracts your text into a database; if the extraction garbles, your qualifications never get read. The frustrating part: rejections for <em>formatting</em> look identical to rejections for <em>fit</em>, so people keep polishing the wrong thing.</p>
<p>Run your resume against these ten checks. They're the same ones we test mechanically when we build resume templates.</p>
<h2>The checklist</h2>
<ol>
<li><strong>One column.</strong> Multi-column layouts scramble read order in many parsers — text from column two gets interleaved mid-sentence into column one.</li>
<li><strong>No tables.</strong> Even invisible layout tables. Parsers walk table cells in unpredictable order.</li>
<li><strong>No text boxes or graphics.</strong> Text inside a text box is often skipped entirely. Skill bars and icons read as nothing.</li>
<li><strong>Contact info in the body, not the header/footer.</strong> Several major systems don't parse header regions — that's a silent way to lose your phone number.</li>
<li><strong>Standard section names.</strong> "Professional Experience", "Education", "Skills". A clever heading like "Where I've Made an Impact" may not map to anything.</li>
<li><strong>Standard font.</strong> Calibri, Arial, Georgia. Downloaded display fonts can render as fallback glyphs after conversion.</li>
<li><strong>Consistent date format.</strong> "Mar 2021 – Present" on every role. Parsers compute your tenure; inconsistency breaks it.</li>
<li><strong>Real bullet characters.</strong> Use the word processor's list feature, not pasted symbols (➤, ✦) that can extract as junk bytes.</li>
<li><strong>Match the posting's exact keywords.</strong> "P&amp;L ownership" and "budget management" are different strings to a filter. Mirror their wording where it's true of you.</li>
<li><strong>Send the format they ask for.</strong> If the posting says PDF, send PDF; if .docx, send .docx. When unspecified, PDF preserves your formatting.</li>
</ol>
<h2>The quick self-test</h2>
<p>Select-all and copy your resume, then paste it into a plain text editor. What you see is roughly what an ATS sees. If lines interleave, sections vanish, or symbols turn to garbage — that's what the employer's database contains.</p>
{cta("Skip the formatting risk entirely: our ATS resume templates pass all ten checks mechanically — we verify zero tables, zero graphics, empty headers, and clean section extraction on every release. $12.99 with matching cover letter, references page, and setup guide.", GUMROAD + "/l/atsresume", "ATS Resume Template — Classic")}
</article>
"""
)

PAGES["wedding-budget-guide"] = (
    "Wedding Budget Breakdown: What Each Category Should Cost (2026)",
    "The percentage-based wedding budget: how to split your total across venue, catering, photography and 15 other categories — with a free tracking method.",
    f"""
<article>
<h1>The Percentage-Based Wedding Budget (and What Each Category Should Cost)</h1>
<div class="byline">ClearGridStudios · Updated August 2026</div>
<p>The fastest way to build a workable wedding budget isn't collecting quotes first — it's the reverse. Set the total you're genuinely willing to spend, split it across categories using typical percentages, and use those numbers as guardrails when you start talking to vendors. Quotes then have something to be compared <em>against</em>.</p>
<h2>Typical US wedding budget percentages</h2>
<table>
<tr><th>Category</th><th>Typical %</th><th>On a $40,000 budget</th></tr>
<tr><td>Venue</td><td>22%</td><td>$8,800</td></tr>
<tr><td>Catering</td><td>20%</td><td>$8,000</td></tr>
<tr><td>Photography</td><td>8%</td><td>$3,200</td></tr>
<tr><td>Flowers</td><td>7%</td><td>$2,800</td></tr>
<tr><td>Attire</td><td>6%</td><td>$2,400</td></tr>
<tr><td>Music/DJ</td><td>5%</td><td>$2,000</td></tr>
<tr><td>Honeymoon</td><td>5%</td><td>$2,000</td></tr>
<tr><td>Videography</td><td>4%</td><td>$1,600</td></tr>
<tr><td>Decor</td><td>4%</td><td>$1,600</td></tr>
<tr><td>Contingency</td><td>4%</td><td>$1,600</td></tr>
<tr><td>Rings</td><td>3%</td><td>$1,200</td></tr>
<tr><td>Everything else (stationery, cake, hair &amp; makeup, transport, favors, officiant)</td><td>12%</td><td>$4,800</td></tr>
</table>
<p>Two notes from watching real budgets fail: <strong>keep the contingency line</strong> (nearly every wedding needs 3–5% for things nobody predicted), and <strong>track payments, not just totals</strong> — wedding vendors bill in deposits and installments across a year, and the most common budget failure is simply losing track of what's already committed.</p>
<h2>The tracking method</h2>
<ol>
<li>One sheet with your categories, the suggested amount, your estimate, actual, and paid-so-far.</li>
<li>A payment schedule: one row per deposit or installment, with the due date. Review it weekly.</li>
<li>Compare actual vs. estimate per category monthly — overspending in one line means trimming another, immediately, not in April.</li>
</ol>
{cta("Our Wedding Budget Tracker does all of this automatically — type your total, get suggested amounts per category, and watch overdue payments flag themselves. $8.99, works in Excel and Google Sheets. Planning everything, not just money? The All-in-One Wedding Planner adds the checklist, guest list, seating chart, and day-of schedule for $19.99.", GUMROAD + "/l/weddingbudget", "Wedding Budget Tracker")}
</article>
"""
)

PAGES["job-application-tracker"] = (
    "How to Organize a Job Search: The Tracker System That Actually Gets Replies",
    "Stop losing applications in your inbox. The exact tracker system for applications, follow-ups, interviews and offers — and why follow-up timing wins.",
    f"""
<article>
<h1>How to Organize a Job Search (So Applications Stop Disappearing)</h1>
<div class="byline">ClearGridStudios · Updated August 2026</div>
<p>A serious job search generates more state than a person can hold in their head: 40–80 open applications, each at a different stage, each with its own contacts, deadlines, and follow-up clock. The people who seem "lucky" in their search are usually just the ones who didn't drop threads.</p>
<h2>Track these fields, ignore the rest</h2>
<ul>
<li><strong>Company, role, link, date applied</strong> — the identity of the thread.</li>
<li><strong>Status</strong> — Applied / Screening / Interviewing / Offer / Rejected / Ghosted. One word, updated the moment it changes.</li>
<li><strong>Next action + date</strong> — the single most important column. Every live application should have one. "Waiting" is not an action; "follow up on the 12th" is.</li>
<li><strong>Contact</strong> — recruiter or referrer name and where you talked (email, LinkedIn).</li>
<li><strong>Salary range</strong> — capture it when posted; you'll want it at offer time.</li>
</ul>
<h2>The two rules that produce replies</h2>
<p><strong>Follow up at 7 days, once.</strong> A short, specific nudge a week after applying measurably revives stalled applications, and one nudge is the polite maximum before an interview exists. This only happens reliably if something <em>tells</em> you it's day 7 — which is the whole argument for a tracker with conditional formatting over a notes app.</p>
<p><strong>Treat interviews as their own pipeline.</strong> Each round gets its own row: who you're meeting, what they care about, your prep notes, and whether the thank-you note went out. Walking into round 3 with your round 1 notes in front of you is an unreasonable advantage.</p>
<h2>Compare offers on total compensation</h2>
<p>Base salary is one line of five. Bonus, equity, benefits value, and time off move real compensation by 20–40%. When offers arrive, put them side by side and compute the total — never negotiate from memory.</p>
{cta("The Ultimate Job Search Tracker has all of this pre-built: 500 application rows with overdue follow-ups that highlight themselves, an interview pipeline, a networking tab, and a 3-offer comparison calculator. $9.99, Excel and Google Sheets.", GUMROAD + "/l/jobsearchtracker", "Ultimate Job Search Tracker")}
</article>
"""
)

PAGES["rental-property-bookkeeping"] = (
    "Rental Property Bookkeeping: Set Up Your Categories Like Schedule E",
    "The landlord bookkeeping mistake that costs hours every April — and the Schedule E category system that eliminates it. Plus the deal metrics that matter.",
    f"""
<article>
<h1>Rental Property Bookkeeping: Match Your Categories to Schedule E From Day One</h1>
<div class="byline">ClearGridStudios · Updated August 2026 · Record-keeping guidance, not tax advice</div>
<p>Most small landlords track expenses in categories that made sense in the moment — "Home Depot", "the plumber thing", "misc". Then April arrives, and IRS Schedule E wants those dollars sorted into <em>its</em> lines: advertising, auto and travel, cleaning and maintenance, insurance, mortgage interest, repairs, supplies, taxes, utilities, depreciation. The annual re-sorting of a year of receipts into a different taxonomy is where landlord weekends go to die.</p>
<p>The fix is embarrassingly simple: <strong>use Schedule E's categories as your bookkeeping categories.</strong> Every expense gets tagged with the line it will eventually land on, at entry time. Your year-end tax summary then computes itself — per property — and hands your preparer exactly what the form asks for.</p>
<h2>What to track, per property</h2>
<ul>
<li><strong>Rent ledger</strong> — every payment against every month, so late, short, and missing rent is visible the week it happens, not at year end.</li>
<li><strong>Expenses with Schedule E categories</strong> — plus a receipt checkbox; "do I have documentation for this?" is a question you want answered before an audit asks it.</li>
<li><strong>Security deposits</strong> — held, deducted, returned. Commingling deposit math with rent income is a classic small-landlord legal mistake.</li>
<li><strong>Per-property rollups</strong> — Schedule E is filed per property, so your books should sum that way natively.</li>
</ul>
<h2>Buying the next one? Run the numbers first</h2>
<p>Before bookkeeping there's the buy decision, and it has its own arithmetic: monthly cash flow after <em>all</em> costs (vacancy, maintenance, CapEx reserve, management — not just the mortgage), cap rate for comparing properties, cash-on-cash return on the money you actually put in, and DSCR (lenders typically want 1.2+). Deals die in the assumptions, not the math — but only if the math is actually computed.</p>
{cta("The Landlord Income & Expense Tracker is built around this exact system — every category matches a Schedule E line, and the tax summary computes per property automatically ($16.99). Evaluating a purchase? The Rental Property Deal Analyzer computes cash flow, cap rate, cash-on-cash and DSCR, and compares three deals side by side ($14.99).", GUMROAD + "/l/landlordtracker", "Landlord Income & Expense Tracker")}
</article>
"""
)

PAGES["about"] = (
    "About ClearGridStudios",
    "ClearGridStudios builds spreadsheets and templates whose formulas are computationally verified before release. Excel & Google Sheets.",
    f"""
<article>
<h1>About ClearGridStudios</h1>
<p>ClearGridStudios makes digital templates — spreadsheets for job searches, weddings, rental properties, and self-employed bookkeeping, plus ATS-safe resume templates — for Excel, Google Sheets, and Word.</p>
<h2>The one thing we do differently</h2>
<p>Every product is <strong>mechanically verified before it's listed</strong>. For spreadsheets, that means a test suite evaluates the actual workbook and checks every formula against independently computed results — totals, mortgage payments, tax-category rollups, seating counts. For resume templates, we verify the ATS-safety claims directly: zero tables, zero graphics, empty headers, sections that extract in order exactly the way a parser reads them. If a check fails, it doesn't ship.</p>
<p>We're honest about our process: products are designed with AI assistance and disclosed as such on every marketplace listing. The verification step is the point — claims you can test beat claims you have to trust.</p>
<h2>Where to buy</h2>
<p>Everything is available on <a href="{GUMROAD}">Gumroad</a> (instant download) and on <a href="{ETSY}">Etsy</a>. Something broken or confusing? Email <a href="mailto:hello@cleargridstudios.com">hello@cleargridstudios.com</a> or message us through either store — because these are instant digital downloads we can't offer returns, but we will make it right.</p>
</article>
"""
)


def build():
    (OUT / "style.css").write_text(CSS.strip() + "\n")
    urls = []
    for slug, (title, desc, body) in PAGES.items():
        (OUT / f"{slug}.html").write_text(layout(slug, title, desc, body))
        urls.append(DOMAIN + ("/" if slug == "index" else f"/{slug}.html"))
        print("built:", f"{slug}.html")
    (OUT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls)
        + "</urlset>\n")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
    (OUT / "CNAME").write_text("cleargridstudios.com\n")
    (OUT / "404.html").write_text(layout("404", "Page not found — ClearGridStudios",
        "Page not found.", '<div class="hero"><h1>Page not found</h1><p><a href="index.html">Back to the templates →</a></p></div>'))
    print("built: style.css sitemap.xml robots.txt CNAME 404.html")


if __name__ == "__main__":
    build()
