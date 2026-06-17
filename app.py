"""
VHQ GROWTHLINE — Vestige Edition
Phase 1 · Core Matrix (Brand Overhaul + Product Consulting Engine)
Deep Blue corporate theme · Teal accents · Gold highlights
"""

import streamlit as st

# ═══════════════════════════════════════════════════════════════
# PAGE CONFIG
# ═══════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="VHQ GrowthLine · Vestige Edition",
    page_icon="◈",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ═══════════════════════════════════════════════════════════════
# DESIGN SYSTEM — VESTIGE CORPORATE BRAND
# Deep Blue #0F172A · Teal #0D9488 · Gold #CA8A04 · White #F1F5F9
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Orbitron:wght@700;900&family=IBM+Plex+Mono:wght@400;500&display=swap');

/* ── Base ── */
html, body, [class*="css"] {
  font-family: 'Inter', sans-serif;
  background: linear-gradient(145deg, #0A0F1E 0%, #0F172A 50%, #0C1526 100%);
  color: #E2E8F0;
  -webkit-font-smoothing: antialiased;
  min-height: 100vh;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container {
  padding: 0 0.9rem 5rem 0.9rem;
  max-width: 720px; margin: auto;
}

/* ── Animations ── */
@keyframes corporatePulse {
  0%,100% {
    text-shadow:
      0 0 8px rgba(13,148,136,0.6),
      0 0 24px rgba(13,148,136,0.35),
      0 3px 0 rgba(7,89,82,0.8),
      0 5px 0 rgba(4,55,51,0.6),
      0 8px 16px rgba(0,0,0,0.6);
  }
  50% {
    text-shadow:
      0 0 12px rgba(45,212,191,0.7),
      0 0 36px rgba(13,148,136,0.45),
      0 3px 0 rgba(7,89,82,0.9),
      0 5px 0 rgba(4,55,51,0.7),
      0 8px 20px rgba(0,0,0,0.7);
  }
}
@keyframes scanH {
  0%   { transform: translateX(-100%); }
  100% { transform: translateX(100vw); }
}
@keyframes fadeUp {
  from { opacity:0; transform:translateY(12px); }
  to   { opacity:1; transform:translateY(0); }
}
@keyframes fadeDown {
  from { opacity:0; transform:translateY(-12px); }
  to   { opacity:1; transform:translateY(0); }
}
@keyframes glowTeal {
  0%,100% { box-shadow: 0 1px 3px rgba(0,0,0,0.4), 0 0 0 1px rgba(13,148,136,0.15); }
  50%     { box-shadow: 0 4px 16px rgba(0,0,0,0.5), 0 0 0 1px rgba(13,148,136,0.3); }
}
@keyframes shimmer {
  0%  { background-position: -200% center; }
  100%{ background-position:  200% center; }
}
@keyframes barFill { from { width:0; } }
@keyframes pop {
  0%  { transform:scale(0.85); opacity:0; }
  65% { transform:scale(1.04); }
  100%{ transform:scale(1);    opacity:1; }
}

/* ══════════════════════════════════════
   CORPORATE HEADER
══════════════════════════════════════ */
.vhq-header {
  position: relative; text-align: center;
  padding: 3rem 1rem 2.2rem; overflow: hidden;
  animation: fadeDown 0.65s ease both;
  border-bottom: 1px solid rgba(13,148,136,0.2);
  margin-bottom: 0.5rem;
}
.vhq-header::before {
  content:''; position:absolute; top:0; left:0; right:0; height:2px;
  background: linear-gradient(90deg,transparent,rgba(45,212,191,0.6),transparent);
  animation: scanH 5s linear infinite;
}
.vhq-eyebrow {
  font-family:'IBM Plex Mono',monospace; font-size:0.6rem;
  letter-spacing:0.28em; text-transform:uppercase;
  color:rgba(45,212,191,0.6); margin-bottom:0.7rem;
}
.vhq-logo {
  font-family:'Orbitron',monospace; font-weight:900;
  font-size:clamp(1.35rem,5vw,2.1rem); letter-spacing:0.07em;
  color:#F1F5F9; line-height:1.2; user-select:none;
  animation: corporatePulse 4s ease-in-out infinite;
}
.vhq-sub {
  font-family:'IBM Plex Mono',monospace; font-size:0.65rem;
  color:rgba(203,213,225,0.5); letter-spacing:0.1em;
  margin-top:0.15rem;
}
.vhq-tagline {
  font-size:0.8rem; color:rgba(148,163,184,0.65);
  margin-top:0.6rem; line-height:1.5;
}
.vhq-badges { margin-top:0.8rem; display:flex; gap:0.5rem; justify-content:center; flex-wrap:wrap; }
.vhq-badge {
  display:inline-block; font-family:'IBM Plex Mono',monospace;
  font-size:0.58rem; letter-spacing:0.12em; text-transform:uppercase;
  padding:0.2rem 0.75rem; border-radius:20px;
  animation: pop 0.5s ease 0.4s both;
}
.badge-teal  { background:rgba(13,148,136,0.15); border:1px solid rgba(13,148,136,0.35); color:#2DD4BF; }
.badge-gold  { background:rgba(202,138,4,0.12);  border:1px solid rgba(202,138,4,0.35);  color:#FCD34D; }
.badge-slate { background:rgba(71,85,105,0.2);   border:1px solid rgba(71,85,105,0.4);   color:#94A3B8; }

/* ══════════════════════════════════════
   GLASS CARDS
══════════════════════════════════════ */
.gc {
  background: rgba(15,23,42,0.6);
  backdrop-filter: blur(20px); -webkit-backdrop-filter:blur(20px);
  border: 1px solid rgba(51,65,85,0.5);
  border-radius: 16px; padding:1.6rem 1.4rem;
  margin-bottom:1rem; position:relative; overflow:hidden;
  animation: glowTeal 5s ease-in-out infinite, fadeUp 0.4s ease both;
}
.gc::before {
  content:''; position:absolute; top:0; left:10%; right:10%; height:1px;
  background:linear-gradient(90deg,transparent,rgba(13,148,136,0.4),transparent);
}
.gc-label {
  font-family:'IBM Plex Mono',monospace; font-size:0.58rem;
  letter-spacing:0.18em; text-transform:uppercase;
  color:rgba(13,148,136,0.8); margin-bottom:0.9rem;
}

/* gold-border variant for active metric cards */
.gc-gold {
  background:rgba(15,23,42,0.65);
  backdrop-filter:blur(20px); -webkit-backdrop-filter:blur(20px);
  border:1px solid rgba(202,138,4,0.35);
  border-radius:16px; padding:1.4rem 1.3rem;
  margin-bottom:1rem; position:relative; overflow:hidden;
  box-shadow:0 0 20px rgba(202,138,4,0.08);
}
.gc-gold::before {
  content:''; position:absolute; top:0; left:10%; right:10%; height:1px;
  background:linear-gradient(90deg,transparent,rgba(202,138,4,0.45),transparent);
}

/* ══════════════════════════════════════
   INPUTS
══════════════════════════════════════ */
.stTextInput>div>div>input,
.stTextArea>div>div>textarea,
.stSelectbox>div>div,
.stNumberInput>div>div>input {
  background:rgba(30,41,59,0.7) !important;
  border:1px solid rgba(51,65,85,0.7) !important;
  border-radius:10px !important; color:#E2E8F0 !important;
  font-family:'Inter',sans-serif !important; font-size:0.9rem !important;
  transition:border-color 0.2s ease, box-shadow 0.2s ease !important;
}
.stTextInput>div>div>input:focus,
.stTextArea>div>div>textarea:focus,
.stNumberInput>div>div>input:focus {
  border-color:#0D9488 !important;
  box-shadow:0 0 0 3px rgba(13,148,136,0.18) !important;
}
label {
  color:rgba(148,163,184,0.85) !important;
  font-size:0.78rem !important; font-weight:500 !important;
  letter-spacing:0.02em !important;
}

/* ══════════════════════════════════════
   BUTTONS
══════════════════════════════════════ */
.stButton>button[kind="primary"] {
  width:100%;
  background:linear-gradient(135deg,#0D9488 0%,#14B8A6 50%,#0D9488 100%) !important;
  background-size:200% auto !important; color:#fff !important;
  border:none !important; border-radius:10px !important;
  font-family:'Inter',sans-serif !important; font-weight:700 !important;
  font-size:0.9rem !important; padding:0.7rem 1.1rem !important;
  letter-spacing:0.03em !important;
  box-shadow:0 4px 18px rgba(13,148,136,0.3) !important;
  transition:background-position 0.4s ease,transform 0.15s ease,box-shadow 0.2s ease !important;
}
.stButton>button[kind="primary"]:hover {
  background-position:right center !important;
  transform:translateY(-1px) !important;
  box-shadow:0 6px 24px rgba(13,148,136,0.45) !important;
}
.stButton>button[kind="secondary"] {
  width:100%; background:rgba(30,41,59,0.6) !important;
  color:rgba(148,163,184,0.85) !important;
  border:1px solid rgba(51,65,85,0.6) !important;
  border-radius:10px !important; font-family:'Inter',sans-serif !important;
  font-size:0.85rem !important;
  transition:border-color 0.2s,background 0.2s !important;
}
.stButton>button[kind="secondary"]:hover {
  border-color:rgba(13,148,136,0.5) !important;
  background:rgba(13,148,136,0.08) !important;
}

/* ══════════════════════════════════════
   TABS
══════════════════════════════════════ */
.stTabs [data-baseweb="tab-list"] {
  background:rgba(15,23,42,0.7) !important;
  border:1px solid rgba(51,65,85,0.5) !important;
  border-radius:12px !important; padding:5px !important;
  gap:3px !important; margin-bottom:1rem !important;
}
.stTabs [data-baseweb="tab"] {
  background:transparent !important; border-radius:8px !important;
  color:rgba(148,163,184,0.6) !important;
  font-family:'Inter',sans-serif !important;
  font-weight:600 !important; font-size:0.8rem !important;
  padding:0.45rem 0.6rem !important; border:none !important;
  transition:all 0.2s ease !important;
}
.stTabs [aria-selected="true"] {
  background:linear-gradient(135deg,#0F766E,#0D9488) !important;
  color:#fff !important;
  box-shadow:0 2px 12px rgba(13,148,136,0.35) !important;
}
.stTabs [data-baseweb="tab-border"] { display:none !important; }
.stTabs [data-baseweb="tab-panel"]  { padding-top:0.2rem !important; }

/* ══════════════════════════════════════
   SECTION LABEL
══════════════════════════════════════ */
.sl {
  font-family:'IBM Plex Mono',monospace; font-size:0.58rem;
  letter-spacing:0.2em; text-transform:uppercase;
  color:rgba(13,148,136,0.7); margin:1.6rem 0 0.65rem;
}

/* ══════════════════════════════════════
   METRIC BLOCKS (clean horizontal)
══════════════════════════════════════ */
.metric-row { display:flex; gap:0.5rem; margin:0.5rem 0; }
.metric-block {
  flex:1; background:rgba(30,41,59,0.6);
  border:1px solid rgba(51,65,85,0.5);
  border-radius:12px; padding:0.9rem 0.6rem; text-align:center;
}
.metric-block-gold {
  flex:1; background:rgba(30,41,59,0.6);
  border:1px solid rgba(202,138,4,0.3);
  border-radius:12px; padding:0.9rem 0.6rem; text-align:center;
}
.metric-val {
  font-family:'Orbitron',monospace; font-size:1.4rem;
  font-weight:700; color:#2DD4BF; line-height:1;
}
.metric-val-gold {
  font-family:'Orbitron',monospace; font-size:1.4rem;
  font-weight:700; color:#FCD34D; line-height:1;
}
.metric-lbl {
  font-family:'IBM Plex Mono',monospace; font-size:0.55rem;
  letter-spacing:0.08em; text-transform:uppercase;
  color:rgba(148,163,184,0.5); margin-top:0.3rem; line-height:1.3;
}

/* ══════════════════════════════════════
   PROGRESS BARS
══════════════════════════════════════ */
.pv-bar-wrap {
  background:rgba(30,41,59,0.7); border-radius:20px; height:12px;
  overflow:hidden; border:1px solid rgba(51,65,85,0.4);
}
.pv-bar-teal {
  height:100%; border-radius:20px;
  background:linear-gradient(90deg,#0F766E,#0D9488,#2DD4BF);
  background-size:200% auto;
  animation: barFill 1.2s ease both, shimmer 3s linear infinite;
}
.pv-bar-gold {
  height:100%; border-radius:20px;
  background:linear-gradient(90deg,#92400E,#CA8A04,#FCD34D);
  background-size:200% auto;
  animation: barFill 1.4s ease both, shimmer 3s linear infinite;
}
.pv-legend {
  display:flex; justify-content:space-between;
  font-family:'IBM Plex Mono',monospace; font-size:0.6rem;
  color:rgba(100,116,139,0.8); margin-top:0.3rem;
}

/* ══════════════════════════════════════
   SCRIPT & PRODUCT CARDS
══════════════════════════════════════ */
.script-box {
  background:rgba(15,23,42,0.8);
  border:1px solid rgba(13,148,136,0.3);
  border-radius:12px; padding:1.2rem 1.1rem;
  font-size:0.88rem; line-height:1.8; color:#CBD5E1;
  white-space:pre-wrap; animation:fadeUp 0.4s ease both;
}
.product-card {
  background:rgba(15,23,42,0.8);
  border:1px solid rgba(202,138,4,0.3);
  border-radius:14px; padding:1.4rem 1.3rem;
  margin-top:0.8rem; animation:fadeUp 0.4s ease both;
  position:relative; overflow:hidden;
}
.product-card::before {
  content:''; position:absolute; top:0; left:8%; right:8%; height:1px;
  background:linear-gradient(90deg,transparent,rgba(202,138,4,0.4),transparent);
}
.product-card-title {
  font-family:'IBM Plex Mono',monospace; font-size:0.6rem;
  letter-spacing:0.15em; text-transform:uppercase;
  color:rgba(202,138,4,0.85); margin-bottom:0.9rem;
}
.product-name {
  font-weight:700; font-size:0.95rem; color:#F1F5F9; margin-bottom:0.2rem;
}
.product-detail {
  font-size:0.8rem; color:rgba(148,163,184,0.7); line-height:1.6;
}
.pv-tag {
  display:inline-block; background:rgba(202,138,4,0.12);
  border:1px solid rgba(202,138,4,0.3); color:#FCD34D;
  font-family:'IBM Plex Mono',monospace; font-size:0.62rem;
  letter-spacing:0.1em; padding:0.2rem 0.7rem; border-radius:8px;
  margin:0.6rem 0;
}
.disclaimer-box {
  background:rgba(30,41,59,0.5); border:1px solid rgba(71,85,105,0.4);
  border-radius:8px; padding:0.6rem 0.8rem; margin-top:0.8rem;
  font-size:0.72rem; color:rgba(100,116,139,0.9); line-height:1.5;
}

/* ══════════════════════════════════════
   BLUEPRINT
══════════════════════════════════════ */
.bp-phase {
  background:rgba(15,23,42,0.6);
  border:1px solid rgba(51,65,85,0.45);
  border-radius:14px; padding:1.2rem 1.3rem;
  margin-bottom:0.8rem; animation:fadeUp 0.4s ease both;
}
.bp-phase-header {
  font-family:'Orbitron',monospace; font-size:0.78rem;
  font-weight:700; color:#2DD4BF; letter-spacing:0.05em;
  margin-bottom:0.4rem;
}
.bp-tag {
  display:inline-block; font-family:'IBM Plex Mono',monospace;
  font-size:0.58rem; letter-spacing:0.1em; text-transform:uppercase;
  background:rgba(13,148,136,0.12); color:#2DD4BF;
  border:1px solid rgba(13,148,136,0.28);
  padding:0.15rem 0.6rem; border-radius:8px; margin-bottom:0.7rem;
}
.bp-goal {
  font-size:0.78rem; color:rgba(148,163,184,0.65);
  font-family:'IBM Plex Mono',monospace; font-size:0.65rem;
  line-height:1.5; margin-bottom:0.7rem;
}

/* ══════════════════════════════════════
   BANNERS
══════════════════════════════════════ */
.b-success {
  background:rgba(6,78,59,0.2); border:1px solid rgba(16,185,129,0.3);
  border-radius:10px; padding:0.75rem 1rem;
  font-size:0.82rem; color:#6EE7B7; margin:0.5rem 0;
  animation:fadeUp 0.25s ease both;
}
.b-warn {
  background:rgba(120,53,15,0.2); border:1px solid rgba(245,158,11,0.3);
  border-radius:10px; padding:0.75rem 1rem;
  font-size:0.82rem; color:#FDE68A; margin:0.5rem 0;
  animation:fadeUp 0.25s ease both;
}
.b-info {
  background:rgba(15,23,42,0.7); border:1px solid rgba(51,65,85,0.5);
  border-radius:10px; padding:0.75rem 1rem;
  font-size:0.82rem; color:rgba(148,163,184,0.8); margin:0.5rem 0;
}

/* ══════════════════════════════════════
   DIVIDER & FOOTER
══════════════════════════════════════ */
.sdiv {
  height:1px; margin:1.2rem 0;
  background:linear-gradient(90deg,transparent,rgba(13,148,136,0.3) 50%,transparent);
}
.vhq-footer {
  text-align:center; font-family:'IBM Plex Mono',monospace;
  font-size:0.56rem; letter-spacing:0.12em;
  color:rgba(51,65,85,0.8); margin-top:3rem; padding-top:1rem;
  border-top:1px solid rgba(30,41,59,0.8);
}
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# SESSION STATE
# ═══════════════════════════════════════════════════════════════
_defaults = {
    "plans_shown":        0,
    "webinars":           0,
    "month_pv":           0,
    "total_pv":           0,
    "generated_script":   "",
    "product_card":       None,
    "checks":             {},
}
for k, v in _defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v


# ═══════════════════════════════════════════════════════════════
# SCRIPT LIBRARY
# ═══════════════════════════════════════════════════════════════
SCRIPTS: dict[tuple, str] = {
    ("🎓 College Student", "📞 Invite to Zoom Meeting"):
"""Hey [Name] 👋

Hope you're doing well! I've been exploring something that a lot of students are using to build a side income — doesn't need much time and fits around college life.

Takes about 20 minutes over a Zoom call to explain properly.

Would you be open to a quick chat this week — say Tuesday or Thursday evening? No pressure at all. 🙂""",

    ("🎓 College Student", "📦 Product Recommendation"):
"""Hey [Name]!

I've been using Vestige's health supplements for a few months and noticed a genuine difference — especially in energy and focus during exams.

Given your schedule, thought you might find them useful. Quality is solid and the pricing is reasonable.

Want me to share the product details or catalogue? 📋""",

    ("🎓 College Student", "🚀 Explaining the Business Income Plan"):
"""Hey [Name],

Quick question — are you open to building a part-time income while still in college?

I'm part of a network with Vestige — it's a legitimate health and wellness brand, 20+ years in India. The model is performance-based, fully flexible.

I can explain how it works in about 15 minutes over a call. No obligation at all. Interested?""",

    ("💼 Corporate Employee", "📞 Invite to Zoom Meeting"):
"""Hi [Name],

I know how full work schedules can get — so I'll be brief.

I've been building a secondary income on the side for a few months now. Mostly evenings and weekends — no conflict with the job at all.

Would you have 20 minutes this Saturday for a quick Zoom? I think it's worth your time. Let me know what works. 🙌""",

    ("💼 Corporate Employee", "📦 Product Recommendation"):
"""Hey [Name]!

You mentioned feeling tired / stressed lately — I've been using Vestige's wellness range and it's made a noticeable difference (better energy, clearer focus).

Not a pitch — just sharing something that works for me. Happy to send the product link if you want to check it out. 🟢""",

    ("💼 Corporate Employee", "🚀 Explaining the Business Income Plan"):
"""Hi [Name],

Straight question — are you comfortable relying on only one income source?

I'm working with Vestige as a part-time distributor. It's performance-based, no fixed hours, fits well alongside a job.

I can walk you through the income structure in 15 minutes. If it doesn't suit your situation, no problem. Worth knowing about though — interested?""",

    ("🏠 Housewife", "📞 Invite to Zoom Meeting"):
"""Hi [Name] 😊

I started something recently that works really well around home life — fully flexible timings, no office, and genuine earning potential.

It's an online business with Vestige. I can explain everything in about 20 minutes at whatever time suits you.

When would work for you this week?""",

    ("🏠 Housewife", "📦 Product Recommendation"):
"""Hi [Name]!

I've been using Vestige's home care and wellness products and genuinely find them good — quality is consistent and they deliver to home.

Thought of you because you always prioritise good products for the family! Want me to share the catalogue? 🌿""",

    ("🏠 Housewife", "🚀 Explaining the Business Income Plan"):
"""Hi [Name],

Have you ever thought about building your own income from home, fully on your own schedule?

I'm working with Vestige as a distributor. No target pressure, you work when you have time, and the earnings are genuinely performance-linked.

I can explain how it works in 15 minutes whenever you're free. Would you like to hear more? 😊""",

    ("🏪 Small Business Owner", "📞 Invite to Zoom Meeting"):
"""Hi [Name],

You already understand business better than most — so I'll be direct.

I'm building a distribution network with Vestige. Given your background, you'd evaluate it quickly and clearly.

20-minute Zoom this week? I'll show you the numbers, not just the concept. What time works? 📊""",

    ("🏪 Small Business Owner", "📦 Product Recommendation"):
"""Hi [Name]!

Have you looked at Vestige's FMCG range? Health, wellness, personal and home care — quality products with consistent demand.

Given your setup, there's also a clear distributor margin structure that could work as a product-line addition.

Interested in seeing the catalogue or the numbers?""",

    ("🏪 Small Business Owner", "🚀 Explaining the Business Income Plan"):
"""Hi [Name],

Vestige's distributor model is one of the more transparent ones in the network marketing space — clear PV-based payouts, genuine products, 20+ years in the market.

As a business owner you'd assess this in 10 minutes. I'd rather show you the actual numbers than pitch you.

Quick call this week?""",
}


# ═══════════════════════════════════════════════════════════════
# PRODUCT CONSULTING DATABASE
# ═══════════════════════════════════════════════════════════════
PRODUCT_DB: dict[str, dict] = {
    "💇 Hair Fall & Skin Health": {
        "bundle": [
            {"name": "Vestige Hair, Skin & Nails",   "pv": 40,  "detail": "Biotin + collagen support for hair strength and skin elasticity."},
            {"name": "Vestige Neem Capsules",          "pv": 22,  "detail": "Natural blood purifier supporting skin health and acne reduction."},
            {"name": "Vestige Aloe Vera Juice",        "pv": 28,  "detail": "Internal hydration and gut-skin axis support."},
        ],
        "whatsapp_script": """Hi [Name] 😊

I came across a Vestige supplement bundle that's specifically designed for hair fall and skin concerns — wanted to share it with you.

The combination is:
✅ Hair, Skin & Nails — biotin + collagen for hair strength
✅ Neem Capsules — natural blood purifier (really helps with skin clarity)
✅ Aloe Vera Juice — internal hydration support

These work better as a bundle because they address the root causes together rather than just the visible symptoms.

Would you like me to share the full product details or place an order for you? The products are home-delivered. 🙏""",
    },

    "💪 Immunity & General Wellness": {
        "bundle": [
            {"name": "Vestige Spirulina",             "pv": 35,  "detail": "Complete protein + micronutrients. Strong daily immunity base."},
            {"name": "Vestige Flax Oil Capsules",     "pv": 30,  "detail": "Omega-3 support for inflammation and cardiovascular health."},
            {"name": "Vestige Wheat Grass Powder",    "pv": 25,  "detail": "Alkalising greens blend for energy and detox support."},
        ],
        "whatsapp_script": """Hi [Name],

For overall immunity and daily wellness, there's a Vestige bundle I'd genuinely recommend based on what I've seen work:

✅ Spirulina — complete plant protein + micronutrients (great daily base)
✅ Flax Oil Capsules — Omega-3s for reducing inflammation
✅ Wheat Grass Powder — alkalising, energy-boosting greens

Together these cover the basics of nutrition that most Indian diets miss, especially for people with hectic schedules.

Happy to share more details or arrange a home delivery. Let me know! 🙂""",
    },

    "🦴 Joint & Bone Pain (Arthritis)": {
        "bundle": [
            {"name": "Vestige Glucosamine",           "pv": 45,  "detail": "Cartilage repair and joint mobility support."},
            {"name": "Vestige Calcium",               "pv": 28,  "detail": "Bone density and strength maintenance."},
            {"name": "Vestige Flax Oil Capsules",     "pv": 30,  "detail": "Anti-inflammatory Omega-3s to reduce joint pain."},
        ],
        "whatsapp_script": """Hi [Name],

For joint pain and bone health concerns, here's what I'd suggest looking at from Vestige:

✅ Glucosamine — specifically supports cartilage repair and joint mobility
✅ Calcium Supplement — for bone density (especially important as we age)
✅ Flax Oil Capsules — natural Omega-3s which reduce joint inflammation

These three together address the pain, the underlying joint wear, and the inflammation that makes it worse.

These aren't a replacement for medical treatment — but as nutritional support, they're solid. Want me to share more details? 🙏""",
    },

    "🩸 Blood Sugar / Glucose Management": {
        "bundle": [
            {"name": "Vestige Stevia",                "pv": 20,  "detail": "Natural zero-calorie sweetener, safe for blood sugar management."},
            {"name": "Vestige Neem Capsules",          "pv": 22,  "detail": "Supports healthy blood glucose levels naturally."},
            {"name": "Vestige Spirulina",             "pv": 35,  "detail": "Supports metabolic health and reduces blood sugar spikes."},
        ],
        "whatsapp_script": """Hi [Name],

For blood sugar management, here's a Vestige wellness bundle worth knowing about:

✅ Stevia — natural sweetener with zero glycaemic impact (great sugar substitute)
✅ Neem Capsules — traditionally used to support healthy glucose levels
✅ Spirulina — shown in studies to support metabolic health and reduce blood sugar spikes

This is nutritional support — not a replacement for prescribed medication. But used consistently alongside a healthy lifestyle, many people find real benefit.

Shall I share the full product information? 😊""",
    },

    "❤️ Heart & Cardiovascular Care": {
        "bundle": [
            {"name": "Vestige Flax Oil Capsules",     "pv": 30,  "detail": "Omega-3s for cholesterol management and heart protection."},
            {"name": "Vestige Garlic Capsules",       "pv": 22,  "detail": "Natural blood pressure support and circulation improvement."},
            {"name": "Vestige Spirulina",             "pv": 35,  "detail": "Antioxidant-rich superfood that supports cardiovascular health."},
        ],
        "whatsapp_script": """Hi [Name],

For heart and cardiovascular care, here's a Vestige supplement bundle I'd recommend:

✅ Flax Oil Capsules — Omega-3s for healthy cholesterol and heart protection
✅ Garlic Capsules — natural circulation support and blood pressure management
✅ Spirulina — powerful antioxidant that protects against oxidative stress

These are nutritional supplements, not a substitute for cardiac medication or medical advice. But as daily preventive support, they're well-regarded.

Want me to send more details or arrange home delivery? 🙏""",
    },
}


# ═══════════════════════════════════════════════════════════════
# BLUEPRINT DATA
# ═══════════════════════════════════════════════════════════════
BLUEPRINT = [
    {
        "phase": "Month 1–2",
        "title": "Core Learning & Self-Use Activation",
        "tag": "Foundation Phase",
        "goal": "Hit 100 PV/month personal use. Learn products deeply. Build your contact list.",
        "tasks": [
            "Complete Vestige product training (official YouTube channel)",
            "Place your first personal-use product bundle — target 100 PV",
            "Set up WhatsApp Business with a clear professional bio and profile",
            "List 30 people you know — family, friends, classmates, colleagues",
            "Attend 2 company webinars or team Zoom sessions this month",
            "Use the Script Engine to practise 5 conversation openers",
            "Identify 3 genuinely interested people from your initial conversations",
            "Log every conversation in the PV Dashboard daily",
        ],
    },
    {
        "phase": "Month 3–4",
        "title": "Duplication Phase — Building Your Frontline",
        "tag": "Growth Phase",
        "goal": "Onboard 3–6 active frontline distributors. Reach 500–1500 cumulative PV.",
        "tasks": [
            "Use the Script Engine daily — personalise for each lead type",
            "Show the business plan to at least one new person per day",
            "Onboard your first active frontline distributor",
            "Help your frontline place their first product order",
            "Attend every team training — bring a new member each time",
            "Hit 300 PV this month (personal + frontline combined)",
            "Celebrate your first downline's first order in your team group",
            "Identify 3 more warm leads from your original list",
        ],
    },
    {
        "phase": "Month 5–6",
        "title": "Bronze Director Leadership Push",
        "tag": "Leadership Phase",
        "goal": "Cumulative 5500 PV (or Fast Start 4500 PV). Unlock Bronze Director.",
        "tasks": [
            "Target team PV of 1500–2500 this month",
            "Support each frontline to onboard their first recruit",
            "Lead a team product education session yourself",
            "Track every team member's PV weekly — support anyone falling behind",
            "Cross 4500 cumulative PV — Fast Start Bronze qualifier milestone",
            "Coordinate Bronze Director application with your sponsor / upline",
            "Plan your post-Bronze strategy toward Silver Director",
            "Document your 6-month journey — share as proof of system with your downline",
        ],
    },
]


# ═══════════════════════════════════════════════════════════════
# HEADER
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<div class="vhq-header">
  <div class="vhq-eyebrow">◈ Official AI Copilot · Network Distribution Platform</div>
  <div class="vhq-logo">VHQ · GROWTHLINE</div>
  <div class="vhq-sub">VESTIGE EDITION</div>
  <div class="vhq-tagline">Structured path from Level 0 to Bronze Director — powered by AI</div>
  <div class="vhq-badges">
    <span class="vhq-badge badge-teal">Phase 1 · Core Matrix</span>
    <span class="vhq-badge badge-gold">Vestige Edition</span>
    <span class="vhq-badge badge-slate">Built for Distributors</span>
  </div>
</div>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# NAVIGATION TABS
# ═══════════════════════════════════════════════════════════════
tabs = st.tabs(["🎯 Script Engine", "📦 Product Finder", "📈 PV Dashboard", "🎓 Blueprint", "⚙ Settings"])


# ═══════════════════════════════════════════════════════════════
# TAB 1 — AI SCRIPT ENGINE
# ═══════════════════════════════════════════════════════════════
with tabs[0]:
    st.markdown('<div class="sl">◈ &nbsp; AI Lead Script Generator</div>', unsafe_allow_html=True)
    st.markdown('<div class="gc"><div class="gc-label">— Conversation Script Inputs —</div>', unsafe_allow_html=True)

    lead_type = st.selectbox(
        "Lead Type",
        ["🎓 College Student", "💼 Corporate Employee", "🏠 Housewife", "🏪 Small Business Owner"],
        key="lead_type",
    )
    objective = st.selectbox(
        "Objective",
        ["📞 Invite to Zoom Meeting", "📦 Product Recommendation", "🚀 Explaining the Business Income Plan"],
        key="objective",
    )
    lead_name = st.text_input("Lead's First Name (optional)", placeholder="e.g. Priya", key="lead_name")
    gen_btn   = st.button("◈  Generate Script", type="primary", use_container_width=True, key="gen_btn")
    st.markdown('</div>', unsafe_allow_html=True)

    if gen_btn:
        raw = SCRIPTS.get((lead_type, objective), "")
        if lead_name.strip():
            raw = raw.replace("[Name]", lead_name.strip())
        st.session_state.generated_script = raw

    if st.session_state.generated_script:
        st.markdown('<div class="sl">◈ &nbsp; Your Script</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="script-box">{st.session_state.generated_script}</div>', unsafe_allow_html=True)
        st.caption("Tap the copy icon ↓ for 1-tap clipboard copy")
        st.code(st.session_state.generated_script, language=None)
        st.markdown('<div class="b-success">✓ Script ready. Add a personal touch before sending — authenticity always converts better than any script.</div>', unsafe_allow_html=True)

    st.markdown('<div class="b-info">💡 Use these scripts as conversation starters, not sales monologues. Lead with genuine interest in the other person first.</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# TAB 2 — VESTIGE PRODUCT CONSULTING ENGINE
# ═══════════════════════════════════════════════════════════════
with tabs[1]:
    st.markdown('<div class="sl">◈ &nbsp; Vestige Product Solution Finder</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="b-info">
      Select a customer's health concern below to instantly see the right Vestige supplement bundle,
      the PV value it generates, and a ready-made WhatsApp message you can share.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="gc"><div class="gc-label">— Customer Health Concern —</div>', unsafe_allow_html=True)

    concern = st.selectbox(
        "Health Concern",
        list(PRODUCT_DB.keys()),
        key="concern",
    )
    cust_name = st.text_input("Customer's Name (optional)", placeholder="e.g. Rahul ji", key="cust_name")
    find_btn  = st.button("◈  Find Product Solution", type="primary", use_container_width=True, key="find_btn")
    st.markdown('</div>', unsafe_allow_html=True)

    if find_btn:
        st.session_state.product_card = PRODUCT_DB[concern]
        st.session_state.product_concern = concern

    if st.session_state.get("product_card"):
        card    = st.session_state.product_card
        concern_label = st.session_state.get("product_concern", "")
        bundle  = card["bundle"]
        total_pv = sum(p["pv"] for p in bundle)
        ws_msg  = card["whatsapp_script"]
        if cust_name.strip():
            ws_msg = ws_msg.replace("[Name]", cust_name.strip())

        # ── Product bundle card ────────────────────────────
        st.markdown('<div class="sl">◈ &nbsp; Recommended Bundle</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="product-card"><div class="product-card-title">— Solution for {concern_label} —</div>', unsafe_allow_html=True)

        for prod in bundle:
            st.markdown(f"""
            <div style="margin-bottom:0.9rem;padding-bottom:0.9rem;border-bottom:1px solid rgba(51,65,85,0.3)">
              <div class="product-name">◈ &nbsp;{prod['name']}</div>
              <div class="product-detail">{prod['detail']}</div>
              <div style="margin-top:0.3rem;font-family:'IBM Plex Mono',monospace;font-size:0.65rem;color:rgba(13,148,136,0.8)">
                PV: {prod['pv']}
              </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style="display:flex;align-items:center;justify-content:space-between;margin-top:0.3rem">
          <div class="pv-tag">◈ &nbsp; Bundle PV: {total_pv} PV</div>
          <div style="font-size:0.75rem;color:rgba(148,163,184,0.55)">
            {len(bundle)} products
          </div>
        </div>
        <div class="disclaimer-box">
          ⚠ These are dietary supplement suggestions only — not medical advice.
          Always advise customers to consult their doctor before starting any supplement,
          especially if they are on prescription medication.
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # ── WhatsApp message ───────────────────────────────
        st.markdown('<div class="sl">◈ &nbsp; Ready-Made WhatsApp Message</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="script-box">{ws_msg}</div>', unsafe_allow_html=True)
        st.caption("Tap the copy icon ↓ to copy the message")
        st.code(ws_msg, language=None)
        st.markdown(f'<div class="b-success">✓ Bundle generates <strong>{total_pv} PV</strong> when ordered. Keep recommending consistently to build your monthly volume.</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# TAB 3 — PV DASHBOARD
# ═══════════════════════════════════════════════════════════════
with tabs[2]:
    st.markdown('<div class="sl">◈ &nbsp; Daily Activity Tracker</div>', unsafe_allow_html=True)

    # ── Activity inputs — clean number_input row ───────────
    st.markdown('<div class="gc"><div class="gc-label">— Today\'s Activity Inputs —</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        plans_val = st.number_input(
            "Plans Shown Today",
            min_value=0, max_value=99,
            value=st.session_state.plans_shown,
            step=1, key="plans_input",
        )
        st.session_state.plans_shown = plans_val
    with col2:
        web_val = st.number_input(
            "Webinars Attended",
            min_value=0, max_value=99,
            value=st.session_state.webinars,
            step=1, key="web_input",
        )
        st.session_state.webinars = web_val

    month_val = st.number_input(
        "This Month's PV (personal + direct team)",
        min_value=0, max_value=9999,
        value=st.session_state.month_pv,
        step=50, key="month_input",
    )
    st.session_state.month_pv = month_val
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Metric display ─────────────────────────────────────
    st.markdown(f"""
    <div class="metric-row">
      <div class="metric-block">
        <div class="metric-val">{st.session_state.plans_shown}</div>
        <div class="metric-lbl">Plans<br>Shown Today</div>
      </div>
      <div class="metric-block">
        <div class="metric-val">{st.session_state.webinars}</div>
        <div class="metric-lbl">Webinars<br>Attended</div>
      </div>
      <div class="metric-block-gold">
        <div class="metric-val-gold">{st.session_state.month_pv}</div>
        <div class="metric-lbl">Month<br>PV</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Bronze Director progress ───────────────────────────
    st.markdown('<div class="sl">◈ &nbsp; Bronze Director Progress Tracker</div>', unsafe_allow_html=True)
    st.markdown('<div class="gc-gold"><div class="gc-label">— Cumulative PV Milestones —</div>', unsafe_allow_html=True)

    total_val = st.number_input(
        "Total Cumulative PV (all-time)",
        min_value=0, max_value=99999,
        value=st.session_state.total_pv,
        step=100, key="total_input",
    )
    st.session_state.total_pv = total_val

    FAST = 4500
    STD  = 5500
    pf   = min(100, round(total_val / FAST * 100, 1))
    ps   = min(100, round(total_val / STD  * 100, 1))

    st.markdown(f"""
    <div style="margin-top:0.5rem">
      <div style="display:flex;justify-content:space-between;margin-bottom:0.25rem">
        <span style="font-family:'IBM Plex Mono',monospace;font-size:0.62rem;color:rgba(13,148,136,0.75)">
          ⚡ Fast Start Bronze — 4500 PV
        </span>
        <span style="font-family:'Orbitron',monospace;font-size:0.72rem;color:#2DD4BF">{pf}%</span>
      </div>
      <div class="pv-bar-wrap"><div class="pv-bar-teal" style="width:{pf}%"></div></div>
      <div class="pv-legend"><span>{total_val:,} PV</span><span>4,500 PV</span></div>

      <div style="display:flex;justify-content:space-between;margin:1rem 0 0.25rem">
        <span style="font-family:'IBM Plex Mono',monospace;font-size:0.62rem;color:rgba(202,138,4,0.8)">
          ◈ Standard Bronze — 5500 PV
        </span>
        <span style="font-family:'Orbitron',monospace;font-size:0.72rem;color:#FCD34D">{ps}%</span>
      </div>
      <div class="pv-bar-wrap"><div class="pv-bar-gold" style="width:{ps}%"></div></div>
      <div class="pv-legend"><span>{total_val:,} PV</span><span>5,500 PV</span></div>
    </div>
    """, unsafe_allow_html=True)

    if total_val >= STD:
        st.markdown('<div class="b-success">🏆 Bronze Director achieved! Contact your upline to submit your qualifier immediately.</div>', unsafe_allow_html=True)
    elif total_val >= FAST:
        st.markdown(f'<div class="b-success">⚡ Fast Start Bronze qualified! {STD - total_val} PV to Standard Bronze.</div>', unsafe_allow_html=True)
    elif total_val >= 2000:
        st.markdown(f'<div class="b-warn">📈 On track — {FAST - total_val} PV to Fast Start Bronze. Keep driving team volume.</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="b-warn">🎯 Build your personal base first. Focus on Month 1–2 tasks. {FAST - total_val} PV to go.</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ── Daily actions checklist ────────────────────────────
    st.markdown('<div class="sl">◈ &nbsp; Non-Negotiable Daily Actions</div>', unsafe_allow_html=True)
    st.markdown('<div class="gc"><div class="gc-label">— Daily Operating Rhythm —</div>', unsafe_allow_html=True)

    daily = [
        "Share value content on WhatsApp Status (products or team wins)",
        "Send 2–3 personalised follow-up messages using the Script Engine",
    "Read or listen to 15 minutes of personal development",
        "Check in with one downline member — offer support",
        "Log today's plans shown and webinars in the tracker above",
    ]
    done = 0
    for i, task in enumerate(daily):
        ck = f"daily_{i}"
        if ck not in st.session_state.checks:
            st.session_state.checks[ck] = False
        val = st.checkbox(task, value=st.session_state.checks[ck], key=f"cb_daily_{i}")
        st.session_state.checks[ck] = val
        if val: done += 1

    if done == len(daily):
        st.markdown('<div class="b-success">✅ All 5 daily actions complete. Excellent consistency.</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="b-warn">{done}/{len(daily)} actions complete today. Consistency builds the business.</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# TAB 4 — 6-MONTH BLUEPRINT
# ═══════════════════════════════════════════════════════════════
with tabs[3]:
    st.markdown('<div class="sl">◈ &nbsp; 6-Month Blueprint Engine</div>', unsafe_allow_html=True)

    for pidx, phase in enumerate(BLUEPRINT):
        st.markdown(f"""
        <div class="bp-phase">
          <div class="bp-phase-header">◈ &nbsp;{phase['phase']} — {phase['title']}</div>
          <div class="bp-tag">{phase['tag']}</div>
          <div class="bp-goal">🎯 Goal: {phase['goal']}</div>
        </div>
        """, unsafe_allow_html=True)

        done_p = 0
        for tidx, task in enumerate(phase["tasks"]):
            ck = f"bp_{pidx}_{tidx}"
            if ck not in st.session_state.checks:
                st.session_state.checks[ck] = False
            val = st.checkbox(task, value=st.session_state.checks[ck], key=f"cb_bp_{pidx}_{tidx}")
            st.session_state.checks[ck] = val
            if val: done_p += 1

        total_t = len(phase["tasks"])
        pct_p   = round(done_p / total_t * 100) if total_t else 0
        bar_cls = "pv-bar-gold" if pct_p == 100 else "pv-bar-teal"

        st.markdown(f"""
        <div style="margin:0.6rem 0 1.4rem">
          <div class="pv-bar-wrap">
            <div class="{bar_cls}" style="width:{pct_p}%"></div>
          </div>
          <div class="pv-legend">
            <span>{done_p}/{total_t} tasks</span>
            <span>{pct_p}% complete</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

        if pct_p == 100:
            st.markdown(f'<div class="b-success">✅ {phase["phase"]} complete. Advance to the next phase.</div>', unsafe_allow_html=True)

        st.markdown('<div class="sdiv"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="gc" style="text-align:center">
      <div class="gc-label">— Core Principle —</div>
      <div style="font-size:0.85rem;color:rgba(148,163,184,0.55);line-height:1.8">
        Consistency over intensity.<br>
        One genuine conversation daily beats ten rushed pitches.<br>
        Build a business — treat it like one.
      </div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# TAB 5 — SETTINGS
# ═══════════════════════════════════════════════════════════════
with tabs[4]:
    st.markdown('<div class="sl">◈ &nbsp; Settings</div>', unsafe_allow_html=True)
    st.markdown('<div class="gc"><div class="gc-label">— Platform Roadmap —</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family:'IBM Plex Mono',monospace;font-size:0.7rem;
      color:rgba(100,116,139,0.8);letter-spacing:0.05em;line-height:2.2">
      ✅ &nbsp; Script Engine &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Phase 1 · Live<br>
      ✅ &nbsp; Product Finder &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Phase 1 · Live<br>
      ✅ &nbsp; PV Dashboard &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Phase 1 · Live<br>
      ✅ &nbsp; 6-Month Blueprint &nbsp;&nbsp;&nbsp; Phase 1 · Live<br>
      ◈ &nbsp;&nbsp; Supabase Auth &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Phase 2 · Next<br>
      ◈ &nbsp;&nbsp; Persistent Data &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Phase 2 · Next<br>
      ◈ &nbsp;&nbsp; AI Script Engine &nbsp;&nbsp;&nbsp;&nbsp; Phase 3 · Planned<br>
      ◈ &nbsp;&nbsp; Razorpay Paywall &nbsp;&nbsp;&nbsp;&nbsp; Phase 4 · Planned
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="sl">◈ &nbsp; Session Management</div>', unsafe_allow_html=True)
    if st.button("⚠  Reset All Session Trackers", type="secondary", use_container_width=True, key="reset_btn"):
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.rerun()
    st.markdown('<div class="b-warn">⚠ Reset clears all progress and tracker data for this session. Persistent saving requires Supabase (Phase 2).</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<div class="vhq-footer">
  VHQ · GROWTHLINE &nbsp;·&nbsp; VESTIGE EDITION &nbsp;·&nbsp; PHASE 1 CORE MATRIX &nbsp;·&nbsp; 2025<br>
  Product recommendations are for informational purposes only — not medical advice.
</div>
""", unsafe_allow_html=True)
