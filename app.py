"""
VHQ GROWTHLINE — app.py
Phase 1 · Core Matrix
Modules: AI Script Engine · PV Dashboard · 6-Month Blueprint · Settings
"""

import streamlit as st
from datetime import date

# ═══════════════════════════════════════════════════════════════
# PAGE CONFIG
# ═══════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="VHQ · GrowthLine",
    page_icon="◈",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ═══════════════════════════════════════════════════════════════
# DESIGN SYSTEM
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Orbitron:wght@700;900&family=IBM+Plex+Mono:wght@400;500&display=swap');

html, body, [class*="css"] {
  font-family: 'Space Grotesk', sans-serif;
  background: #04040A;
  color: #E8E6F0;
  -webkit-font-smoothing: antialiased;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 0.9rem 5rem 0.9rem; max-width: 700px; margin: auto; }

/* ── Animations ── */
@keyframes neonPulse {
  0%,100% {
    text-shadow: 0 0 6px #fff, 0 0 20px #34d399, 0 0 40px #059669,
      0 0 80px #059669, 0 2px 0 #064e3b, 0 4px 0 #022c22,
      0 6px 10px rgba(0,0,0,0.7);
  }
  50% {
    text-shadow: 0 0 10px #fff, 0 0 30px #6ee7b7, 0 0 60px #34d399,
      0 0 100px #059669, 0 2px 0 #064e3b, 0 4px 0 #022c22,
      0 6px 16px rgba(0,0,0,0.8);
  }
}
@keyframes scanH {
  0%   { transform: translateX(-100%); }
  100% { transform: translateX(100vw); }
}
@keyframes fadeUp {
  from { opacity:0; transform:translateY(14px); }
  to   { opacity:1; transform:translateY(0); }
}
@keyframes fadeDown {
  from { opacity:0; transform:translateY(-14px); }
  to   { opacity:1; transform:translateY(0); }
}
@keyframes glowGreen {
  0%,100% { box-shadow: 0 0 8px rgba(52,211,153,0.3), inset 0 0 6px rgba(52,211,153,0.04); }
  50%     { box-shadow: 0 0 20px rgba(52,211,153,0.45), inset 0 0 10px rgba(52,211,153,0.07); }
}
@keyframes shimmer {
  0%  { background-position: -200% center; }
  100%{ background-position:  200% center; }
}
@keyframes pop {
  0%  { transform:scale(0.85); opacity:0; }
  60% { transform:scale(1.06); }
  100%{ transform:scale(1);    opacity:1; }
}
@keyframes progressFill {
  from { width: 0; }
}

/* ── Header ── */
.gl-header {
  position: relative; text-align: center;
  padding: 2.6rem 1rem 1.9rem; overflow: hidden;
  animation: fadeDown 0.7s ease both;
}
.gl-header::before {
  content:''; position:absolute; top:0; left:0; right:0; height:2px;
  background: linear-gradient(90deg,transparent,rgba(52,211,153,0.7),transparent);
  animation: scanH 5s linear infinite;
}
.gl-header::after {
  content:''; position:absolute; bottom:0; left:8%; right:8%; height:1px;
  background: linear-gradient(90deg,transparent,rgba(5,150,105,0.5),transparent);
}
.gl-eyebrow {
  font-family:'IBM Plex Mono',monospace; font-size:0.62rem;
  letter-spacing:0.28em; text-transform:uppercase;
  color:rgba(52,211,153,0.6); margin-bottom:0.75rem;
  animation: fadeDown 0.6s ease 0.1s both;
}
.gl-logo {
  font-family:'Orbitron',monospace; font-weight:900;
  font-size:clamp(1.5rem,5.5vw,2.3rem); letter-spacing:0.08em;
  color:#fff; line-height:1.15; user-select:none;
  animation: neonPulse 3.5s ease-in-out infinite, fadeDown 0.7s ease 0.15s both;
}
.gl-tagline {
  font-family:'IBM Plex Mono',monospace; font-size:0.68rem;
  color:rgba(52,211,153,0.5); letter-spacing:0.07em; margin-top:0.6rem;
  animation: fadeDown 0.7s ease 0.3s both;
}
.gl-badge {
  display:inline-block; background:rgba(5,150,105,0.14);
  border:1px solid rgba(52,211,153,0.3); color:#34d399;
  font-family:'IBM Plex Mono',monospace; font-size:0.6rem;
  letter-spacing:0.14em; padding:0.2rem 0.8rem; border-radius:20px;
  margin-top:0.65rem; animation: pop 0.5s ease 0.5s both;
}

/* ── Glass cards ── */
.gc {
  background: rgba(255,255,255,0.025);
  backdrop-filter: blur(18px); -webkit-backdrop-filter:blur(18px);
  border: 1px solid rgba(255,255,255,0.06);
  border-radius: 18px; padding: 1.6rem 1.4rem;
  margin-bottom: 1rem; position: relative; overflow: hidden;
  animation: glowGreen 4s ease-in-out infinite, fadeUp 0.45s ease both;
}
.gc::before {
  content:''; position:absolute; top:0; left:12%; right:12%; height:1px;
  background:linear-gradient(90deg,transparent,rgba(52,211,153,0.3),transparent);
}
.gc-label {
  font-family:'IBM Plex Mono',monospace; font-size:0.6rem;
  letter-spacing:0.18em; text-transform:uppercase;
  color:rgba(5,150,105,0.85); margin-bottom:0.9rem;
}

/* ── Inputs ── */
.stTextInput>div>div>input,
.stTextArea>div>div>textarea,
.stSelectbox>div>div,
.stNumberInput>div>div>input {
  background:rgba(255,255,255,0.035) !important;
  border:1px solid rgba(52,211,153,0.25) !important;
  border-radius:10px !important; color:#E8E6F0 !important;
  font-family:'Space Grotesk',sans-serif !important; font-size:0.9rem !important;
  transition: border-color 0.2s ease, box-shadow 0.2s ease !important;
}
.stTextInput>div>div>input:focus,
.stTextArea>div>div>textarea:focus {
  border-color:#34d399 !important;
  box-shadow:0 0 0 3px rgba(52,211,153,0.14) !important;
}
label { color:rgba(52,211,153,0.7) !important; font-size:0.79rem !important; font-weight:500 !important; letter-spacing:0.03em !important; }

/* ── Buttons ── */
.stButton>button[kind="primary"] {
  width:100%;
  background:linear-gradient(135deg,#059669 0%,#34d399 50%,#059669 100%) !important;
  background-size:200% auto !important; color:#000 !important;
  border:none !important; border-radius:12px !important;
  font-family:'Space Grotesk',sans-serif !important;
  font-weight:700 !important; font-size:0.93rem !important;
  padding:0.72rem 1.2rem !important; letter-spacing:0.04em !important;
  box-shadow:0 4px 20px rgba(5,150,105,0.35) !important;
  transition:background-position 0.4s ease, transform 0.15s ease, box-shadow 0.2s ease !important;
}
.stButton>button[kind="primary"]:hover {
  background-position:right center !important;
  transform:translateY(-1px) !important;
  box-shadow:0 6px 28px rgba(52,211,153,0.45) !important;
}
.stButton>button[kind="secondary"] {
  width:100%; background:rgba(255,255,255,0.03) !important;
  color:rgba(52,211,153,0.8) !important;
  border:1px solid rgba(52,211,153,0.25) !important;
  border-radius:12px !important;
  font-family:'Space Grotesk',sans-serif !important; font-size:0.87rem !important;
  transition:border-color 0.2s,background 0.2s !important;
}
.stButton>button[kind="secondary"]:hover {
  border-color:rgba(52,211,153,0.5) !important;
  background:rgba(52,211,153,0.07) !important;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
  background:rgba(255,255,255,0.02) !important;
  border:1px solid rgba(52,211,153,0.18) !important;
  border-radius:13px !important; padding:5px !important; gap:4px !important;
  margin-bottom:1rem !important;
}
.stTabs [data-baseweb="tab"] {
  background:transparent !important; border-radius:9px !important;
  color:rgba(52,211,153,0.45) !important;
  font-family:'Space Grotesk',sans-serif !important;
  font-weight:600 !important; font-size:0.84rem !important;
  padding:0.48rem 0.7rem !important; border:none !important;
  transition:all 0.2s ease !important;
}
.stTabs [aria-selected="true"] {
  background:linear-gradient(135deg,#059669,#34d399) !important;
  color:#000 !important; font-weight:700 !important;
  box-shadow:0 2px 14px rgba(5,150,105,0.4) !important;
}
.stTabs [data-baseweb="tab-border"] { display:none !important; }
.stTabs [data-baseweb="tab-panel"]  { padding-top:0.2rem !important; }

/* ── Section label ── */
.sl {
  font-family:'IBM Plex Mono',monospace; font-size:0.6rem;
  letter-spacing:0.2em; text-transform:uppercase;
  color:rgba(5,150,105,0.75); margin:1.6rem 0 0.6rem;
}

/* ── Progress bar ── */
.pv-bar-wrap {
  background:rgba(255,255,255,0.05); border-radius:20px;
  height:14px; overflow:hidden; margin:0.6rem 0;
  border:1px solid rgba(52,211,153,0.15);
}
.pv-bar-fill {
  height:100%; border-radius:20px;
  background:linear-gradient(90deg,#059669,#34d399,#6ee7b7);
  background-size:200% auto;
  animation: progressFill 1.2s ease both, shimmer 2.5s linear infinite;
  transition: width 0.8s ease;
}
.pv-legend {
  display:flex; justify-content:space-between;
  font-family:'IBM Plex Mono',monospace; font-size:0.65rem;
  color:rgba(52,211,153,0.5); margin-top:0.3rem;
}

/* ── Metric chips ── */
.metric-row { display:flex; gap:0.5rem; margin-bottom:0.6rem; flex-wrap:wrap; }
.metric-chip {
  flex:1; min-width:90px;
  background:rgba(5,150,105,0.08);
  border:1px solid rgba(52,211,153,0.18);
  border-radius:12px; padding:0.8rem 0.6rem; text-align:center;
}
.metric-val {
  font-family:'Orbitron',monospace; font-size:1.3rem;
  font-weight:700; color:#34d399; line-height:1;
}
.metric-lbl {
  font-family:'IBM Plex Mono',monospace; font-size:0.58rem;
  letter-spacing:0.09em; text-transform:uppercase;
  color:rgba(52,211,153,0.45); margin-top:0.25rem; line-height:1.3;
}

/* ── Script output box ── */
.script-box {
  background:rgba(5,150,105,0.06);
  border:1px solid rgba(52,211,153,0.25);
  border-radius:14px; padding:1.2rem 1.1rem;
  font-size:0.9rem; line-height:1.75; color:#E8E6F0;
  white-space:pre-wrap; margin-top:0.6rem;
  animation: fadeUp 0.4s ease both;
}

/* ── Blueprint accordion ── */
.bp-month {
  background:rgba(255,255,255,0.025);
  border:1px solid rgba(52,211,153,0.15);
  border-radius:14px; padding:1.1rem 1.2rem;
  margin-bottom:0.7rem; animation: fadeUp 0.4s ease both;
}
.bp-month-title {
  font-family:'Orbitron',monospace; font-size:0.82rem;
  font-weight:700; color:#34d399; letter-spacing:0.06em;
  margin-bottom:0.6rem;
}
.bp-tag {
  display:inline-block; font-family:'IBM Plex Mono',monospace;
  font-size:0.6rem; letter-spacing:0.1em; text-transform:uppercase;
  background:rgba(5,150,105,0.14); color:#34d399;
  border:1px solid rgba(52,211,153,0.25);
  padding:0.15rem 0.6rem; border-radius:10px; margin-bottom:0.7rem;
}

/* ── Banners ── */
.b-success {
  background:rgba(34,197,94,0.07); border:1px solid rgba(34,197,94,0.28);
  border-radius:11px; padding:0.75rem 1rem; font-size:0.83rem;
  color:#86efac; margin:0.5rem 0; animation:fadeUp 0.25s ease both;
}
.b-warn {
  background:rgba(251,191,36,0.07); border:1px solid rgba(251,191,36,0.28);
  border-radius:11px; padding:0.75rem 1rem; font-size:0.83rem;
  color:#fde68a; margin:0.5rem 0; animation:fadeUp 0.25s ease both;
}

/* ── Shimmer divider ── */
.sdiv {
  height:1px; margin:1.3rem 0;
  background:linear-gradient(90deg,transparent,rgba(52,211,153,0.35) 50%,transparent);
  background-size:200% auto; animation:shimmer 3s linear infinite;
}

/* ── Footer ── */
.gl-footer {
  text-align:center; font-family:'IBM Plex Mono',monospace;
  font-size:0.58rem; letter-spacing:0.12em;
  color:rgba(5,150,105,0.3); margin-top:3rem; padding-top:1rem;
  border-top:1px solid rgba(5,150,105,0.08);
}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# SESSION STATE
# ═══════════════════════════════════════════════════════════════
_defaults = {
    "plans_shown":    0,
    "webinars":       0,
    "month_pv":       0,
    "total_pv":       0,
    "generated_script": "",
    # Blueprint checkboxes: dict of {task_id: bool}
    "checks": {},
}
for k, v in _defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# ═══════════════════════════════════════════════════════════════
# SCRIPT LIBRARY
# ═══════════════════════════════════════════════════════════════
SCRIPTS: dict[tuple, str] = {

    # ── College Student ─────────────────────────────────────
    ("🎓 College Student", "📞 Invite to Zoom Meeting"):
"""Hey [Name] 👋

I've been exploring something genuinely interesting lately — an income stream a lot of students are using to cover expenses without affecting studies.

Takes about 20 minutes on a Zoom call to explain properly. Would you be open to hearing it this week — say Tuesday or Thursday evening?

No pressure at all. If it fits your situation, great. If not, no worries. 🙂""",

    ("🎓 College Student", "📦 Product Recommendation"):
"""Hey [Name]! 

I've been using Vestige's health and wellness products for a few months and the difference has been noticeable — especially [specific product e.g. spirulina / protein supplement].

Given you're in [exams / gym / sports], thought you might find them useful. They're reasonably priced and good quality.

Want me to share more details or the product catalogue? 📋""",

    ("🎓 College Student", "🚀 Explaining the Business Income Plan"):
"""Hey [Name],

Quick question — are you open to earning on the side while still in college?

I'm part of a network with Vestige (it's a legitimate FMCG health brand — been around 20+ years in India). The model is performance-based, no fixed timings, and suits students well.

I can share how it works in a short call. No obligation to join — just worth knowing about. Interested?""",

    # ── Corporate Employee ───────────────────────────────────
    ("💼 Corporate Employee", "📞 Invite to Zoom Meeting"):
"""Hi [Name],

Hope work is going well! I know how hectic schedules get.

I've been building a secondary income stream on the side over the past few months — doesn't interfere with the job at all, mostly weekends and evenings. 

Would you have 20 minutes this Saturday for a quick Zoom? I think it might be relevant to where you are right now. Let me know what time works. 🙌""",

    ("💼 Corporate Employee", "📦 Product Recommendation"):
"""Hey [Name]!

You mentioned being tired / stressed lately — I wanted to share something that's helped me: Vestige's wellness range (they have supplements, immunity products, and personal care that are actually good quality).

Not a sales pitch — just sharing something that works for me. Happy to send you the details or order link if you want to check it out. 🟢""",

    ("💼 Corporate Employee", "🚀 Explaining the Business Income Plan"):
"""Hi [Name],

Direct question — are you happy with only one source of income?

I'm working with Vestige as a part-time distributor. It's a performance-based model — no salary, but no fixed hours either. Fits well alongside a job.

I can walk you through how the income structure works in 15–20 minutes. If it doesn't make sense for your situation, that's totally fine. Worth a look though — interested?""",

    # ── Housewife ────────────────────────────────────────────
    ("🏠 Housewife", "📞 Invite to Zoom Meeting"):
"""Hi [Name] 😊

I wanted to share something I started recently that fits really well around home life — flexible timings, no office, and good earning potential with consistency.

It's an online business model with Vestige — I can explain everything on a quick call at whatever time suits you. Even 20 minutes is enough to get the full picture. 

When works for you this week?""",

    ("🏠 Housewife", "📦 Product Recommendation"):
"""Hi [Name]!

I've been using Vestige's home care and health products for a while now and genuinely find them good — especially [aloe vera gel / multivitamins / home cleaner].

Quality is solid and they're available for home delivery. Thought of you because you care about these things too! 

Want me to share the catalogue? No obligation at all. 🌿""",

    ("🏠 Housewife", "🚀 Explaining the Business Income Plan"):
"""Hi [Name],

Quick thought — have you ever considered building your own income from home, fully on your schedule?

I'm working with Vestige as a distributor. It suits home life really well — you work when you have time, there's no target pressure, and the earnings are genuinely performance-linked.

I can explain the model in about 15 minutes whenever you're free. Would you like to know more? 😊""",

    # ── Small Business Owner ─────────────────────────────────
    ("🏪 Small Business Owner", "📞 Invite to Zoom Meeting"):
"""Hi [Name],

You've built something of your own — which means you already understand how business works better than most.

I'm exploring a model with Vestige that creates recurring income through a product distribution network. Given your background, I think you'd evaluate it clearly and quickly.

20-minute Zoom this week? I'll walk you through the full picture — numbers included. Let me know a time. 📊""",

    ("🏪 Small Business Owner", "📦 Product Recommendation"):
"""Hi [Name]!

Have you looked at Vestige's product range? High-quality FMCG — health, wellness, home care.

Given your setup [shop / customers], there's also a straightforward way to stock and recommend them with a margin. Thought it might be worth knowing about as a product line addition.

Interested in seeing the catalogue or the distributor margin structure?""",

    ("🏪 Small Business Owner", "🚀 Explaining the Business Income Plan"):
"""Hi [Name],

Straight to the point — Vestige's distributor model is one of the more transparent ones in network marketing, with clear PV-based payouts and a legitimate product range.

As a business owner you'd probably assess this in 10 minutes. I'd rather show you the actual numbers than pitch you.

Can we do a quick call this week? You tell me if it's worth your time after.""",
}

# ═══════════════════════════════════════════════════════════════
# BLUEPRINT DATA
# ═══════════════════════════════════════════════════════════════
BLUEPRINT = [
    {
        "phase": "Month 1–2",
        "title": "Core Learning & Self-Use Activation",
        "tag": "Foundation Phase",
        "goal": "Hit consistent 100 PV/month personal use. Learn products deeply.",
        "tasks": [
            "Complete Vestige product training videos (official channel)",
            "Order your first personal-use product bundle (target: 100 PV)",
            "Open WhatsApp Business account with a clear professional bio",
            "List 30 people you know — family, friends, classmates, colleagues",
            "Attend 2 company webinars / team Zoom sessions this month",
            "Use the AI Script Engine to practice 5 conversations (no selling — just sharing)",
            "Track every conversation in your PV Dashboard",
            "Identify 3 people genuinely interested — note them separately",
        ],
    },
    {
        "phase": "Month 3–4",
        "title": "Duplication Phase — Building Your Frontline",
        "tag": "Growth Phase",
        "goal": "Onboard 3–6 active frontline distributors. Reach 500–1500 PV.",
        "tasks": [
            "Use AI Script Engine daily — personalise for each lead type",
            "Show the business plan to at least 1 person per day",
            "Onboard your first active frontline distributor",
            "Help your frontline place their first product order",
            "Attend every team training — bring a new member each time",
            "Hit 300 PV this month (personal + first frontline combined)",
            "Celebrate first downline's success publicly in team group",
            "Review your list — identify 3 more warm leads to approach",
        ],
    },
    {
        "phase": "Month 5–6",
        "title": "Bronze Director Push",
        "tag": "Leadership Phase",
        "goal": "Cumulative 5500 PV (or Fast Start 4500 PV). Unlock Bronze Director.",
        "tasks": [
            "Total team PV: target 1500–2500 this month",
            "Support each frontline to onboard their first recruit",
            "Run a team product education session (you lead it)",
            "Track every team member's PV weekly — flag who needs support",
            "Cross 4500 cumulative PV — Fast Start Bronze qualifier",
            "Submit Bronze Director application with your sponsor/upline",
            "Plan your post-Bronze duplication strategy for Silver Director",
            "Document your 6-month journey — share with your downline as proof",
        ],
    },
]

# ═══════════════════════════════════════════════════════════════
# HEADER
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<div class="gl-header">
  <div class="gl-eyebrow">◈ AI-Copilot for Network Distributors</div>
  <div class="gl-logo">VHQ · GROWTHLINE</div>
  <div class="gl-tagline">Your Structured Path from Level 0 → Bronze Director</div>
  <div class="gl-badge">PHASE 1 · CORE MATRIX · VESTIGE EDITION</div>
</div>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# MAIN NAVIGATION
# ═══════════════════════════════════════════════════════════════
tabs = st.tabs(["🎯  Script Engine", "📈  PV Dashboard", "🎓  6-Month Blueprint", "⚙  Settings"])


# ═══════════════════════════════════════════════════════════════
# TAB 1 — AI SCRIPT ENGINE
# ═══════════════════════════════════════════════════════════════
with tabs[0]:
    st.markdown('<div class="sl">◈ &nbsp; AI Lead Script Generator</div>', unsafe_allow_html=True)
    st.markdown('<div class="gc"><div class="gc-label">— Script Inputs —</div>', unsafe_allow_html=True)

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
    lead_name = st.text_input("Lead's First Name (optional)", placeholder="e.g. Rohit", key="lead_name")

    generate = st.button("◈  Generate Script", type="primary", use_container_width=True, key="gen_btn")
    st.markdown('</div>', unsafe_allow_html=True)

    if generate:
        key = (lead_type, objective)
        script = SCRIPTS.get(key, "Script not found for this combination.")
        if lead_name.strip():
            script = script.replace("[Name]", lead_name.strip())
        st.session_state.generated_script = script

    if st.session_state.generated_script:
        st.markdown('<div class="sl">◈ &nbsp; Your Script</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="script-box">{st.session_state.generated_script}</div>', unsafe_allow_html=True)

        # Copy via code block (native 1-tap copy on mobile)
        st.caption("Tap the copy icon below to copy to clipboard ↓")
        st.code(st.session_state.generated_script, language=None)

        st.markdown('<div class="b-success">✓ Script ready. Personalise it naturally before sending — authenticity converts better than any script.</div>', unsafe_allow_html=True)

    st.markdown('<div class="b-warn">💡 Tip: The best conversations start with genuine curiosity about the other person. Use this script as a guide, not a monologue.</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# TAB 2 — PV DASHBOARD
# ═══════════════════════════════════════════════════════════════
with tabs[1]:
    st.markdown('<div class="sl">◈ &nbsp; Daily Activity Tracker</div>', unsafe_allow_html=True)

    # ── Activity counters ──────────────────────────────────
    st.markdown('<div class="gc"><div class="gc-label">— Today\'s Activity —</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("＋", key="pp", type="secondary", use_container_width=True):
            st.session_state.plans_shown += 1
        if st.button("－", key="pm", type="secondary", use_container_width=True):
            st.session_state.plans_shown = max(0, st.session_state.plans_shown - 1)
    with col2:
        if st.button("＋", key="wp", type="secondary", use_container_width=True):
            st.session_state.webinars += 1
        if st.button("－", key="wm", type="secondary", use_container_width=True):
            st.session_state.webinars = max(0, st.session_state.webinars - 1)
    with col3:
        month_pv_input = st.number_input(
            "Month PV", min_value=0, max_value=9999,
            value=st.session_state.month_pv, step=50, key="mpv_input",
            label_visibility="visible",
        )
        st.session_state.month_pv = month_pv_input

    st.markdown(f"""
    <div class="metric-row">
      <div class="metric-chip">
        <div class="metric-val">{st.session_state.plans_shown}</div>
        <div class="metric-lbl">Plans<br>Shown Today</div>
      </div>
      <div class="metric-chip">
        <div class="metric-val">{st.session_state.webinars}</div>
        <div class="metric-lbl">Webinars<br>Attended</div>
      </div>
      <div class="metric-chip">
        <div class="metric-val">{st.session_state.month_pv}</div>
        <div class="metric-lbl">Month PV<br>This Month</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Cumulative PV & Bronze Director progress ───────────
    st.markdown('<div class="sl">◈ &nbsp; Bronze Director Progress</div>', unsafe_allow_html=True)
    st.markdown('<div class="gc"><div class="gc-label">— PV Milestone Tracker —</div>', unsafe_allow_html=True)

    total_pv_input = st.number_input(
        "Cumulative Total PV (all time)", min_value=0, max_value=99999,
        value=st.session_state.total_pv, step=100, key="tpv_input",
    )
    st.session_state.total_pv = total_pv_input

    FAST_START = 4500
    STANDARD   = 5500
    pct_fast   = min(100, round(total_pv_input / FAST_START * 100, 1))
    pct_std    = min(100, round(total_pv_input / STANDARD  * 100, 1))

    st.markdown(f"""
    <div style="margin-top:0.3rem">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:0.2rem">
        <span style="font-family:'IBM Plex Mono',monospace;font-size:0.65rem;color:rgba(52,211,153,0.7)">
          ⚡ Fast Start Bronze (4500 PV)
        </span>
        <span style="font-family:'Orbitron',monospace;font-size:0.75rem;color:#34d399">{pct_fast}%</span>
      </div>
      <div class="pv-bar-wrap">
        <div class="pv-bar-fill" style="width:{pct_fast}%"></div>
      </div>
      <div class="pv-legend"><span>{total_pv_input} PV achieved</span><span>4500 PV target</span></div>

      <div style="display:flex;justify-content:space-between;align-items:center;margin:1rem 0 0.2rem">
        <span style="font-family:'IBM Plex Mono',monospace;font-size:0.65rem;color:rgba(52,211,153,0.7)">
          ◈ Standard Bronze (5500 PV)
        </span>
        <span style="font-family:'Orbitron',monospace;font-size:0.75rem;color:#34d399">{pct_std}%</span>
      </div>
      <div class="pv-bar-wrap">
        <div class="pv-bar-fill" style="width:{pct_std}%"></div>
      </div>
      <div class="pv-legend"><span>{total_pv_input} PV achieved</span><span>5500 PV target</span></div>
    </div>
    """, unsafe_allow_html=True)

    if total_pv_input >= STANDARD:
        st.markdown('<div class="b-success">🏆 Bronze Director target achieved! Submit your qualifier to your upline.</div>', unsafe_allow_html=True)
    elif total_pv_input >= FAST_START:
        st.markdown('<div class="b-success">⚡ Fast Start Bronze qualifier hit! 900 PV away from Standard Bronze.</div>', unsafe_allow_html=True)
    elif total_pv_input >= 2000:
        st.markdown(f'<div class="b-warn">📈 Good progress — {FAST_START - total_pv_input} PV to Fast Start Bronze. Keep building your team\'s volume.</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="b-warn">🎯 Focus on Month 1–2 tasks. Build your personal 100 PV base first. {FAST_START - total_pv_input} PV to go.</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ── Daily best practices ───────────────────────────────
    st.markdown('<div class="sl">◈ &nbsp; Non-Negotiable Daily Actions</div>', unsafe_allow_html=True)
    st.markdown('<div class="gc"><div class="gc-label">— Daily Operating Rhythm —</div>', unsafe_allow_html=True)

    daily_tasks = [
        "Share value content on WhatsApp Status (products / team wins)",
        "Send 2–3 personalised follow-up messages (use Script Engine)",
        "Read or listen to 15 min of personal development",
        "Check in with one downline member — support their activity",
        "Log today's plans shown and webinars in the dashboard",
    ]
    for i, task in enumerate(daily_tasks):
        ck_key = f"daily_{i}"
        if ck_key not in st.session_state.checks:
            st.session_state.checks[ck_key] = False
        st.session_state.checks[ck_key] = st.checkbox(task, value=st.session_state.checks[ck_key], key=f"ck_daily_{i}")

    done = sum(1 for i in range(len(daily_tasks)) if st.session_state.checks.get(f"daily_{i}", False))
    if done == len(daily_tasks):
        st.markdown('<div class="b-success">✅ Perfect day! All 5 daily actions complete.</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="b-warn">{done}/{len(daily_tasks)} actions done today. Consistency is the only strategy.</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# TAB 3 — 6-MONTH BLUEPRINT
# ═══════════════════════════════════════════════════════════════
with tabs[2]:
    st.markdown('<div class="sl">◈ &nbsp; 6-Month Blueprint Engine</div>', unsafe_allow_html=True)

    for phase_idx, phase in enumerate(BLUEPRINT):
        st.markdown(f"""
        <div class="bp-month">
          <div class="bp-month-title">◈ {phase['phase']} — {phase['title']}</div>
          <div class="bp-tag">{phase['tag']}</div>
          <div style="font-size:0.83rem;color:rgba(52,211,153,0.65);margin-bottom:0.8rem;
            font-family:'IBM Plex Mono',monospace;font-size:0.68rem;line-height:1.5">
            🎯 Goal: {phase['goal']}
          </div>
        </div>
        """, unsafe_allow_html=True)

        completed = 0
        for task_idx, task in enumerate(phase["tasks"]):
            ck_key = f"bp_{phase_idx}_{task_idx}"
            if ck_key not in st.session_state.checks:
                st.session_state.checks[ck_key] = False
            val = st.checkbox(task, value=st.session_state.checks[ck_key], key=f"cb_{ck_key}")
            st.session_state.checks[ck_key] = val
            if val:
                completed += 1

        total = len(phase["tasks"])
        pct   = round(completed / total * 100) if total else 0
        st.markdown(f"""
        <div style="margin:0.5rem 0 1.2rem">
          <div class="pv-bar-wrap">
            <div class="pv-bar-fill" style="width:{pct}%"></div>
          </div>
          <div class="pv-legend">
            <span>{completed}/{total} tasks</span>
            <span>{pct}% complete</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

        if pct == 100:
            st.markdown(f'<div class="b-success">✅ {phase["phase"]} complete! Move to the next phase.</div>', unsafe_allow_html=True)

        st.markdown('<div class="sdiv"></div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="gc" style="text-align:center">
      <div class="gc-label">— Blueprint Reminder —</div>
      <div style="font-size:0.85rem;color:rgba(52,211,153,0.55);line-height:1.75">
        Consistency over intensity.<br>
        One genuine conversation per day beats 10 rushed pitches.<br>
        This is a business — treat it like one.
      </div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# TAB 4 — SETTINGS
# ═══════════════════════════════════════════════════════════════
with tabs[3]:
    st.markdown('<div class="sl">◈ &nbsp; Settings</div>', unsafe_allow_html=True)
    st.markdown('<div class="gc"><div class="gc-label">— App Configuration —</div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="font-family:'IBM Plex Mono',monospace;font-size:0.72rem;
      color:rgba(52,211,153,0.4);letter-spacing:0.06em;line-height:2.1">
      ◈ &nbsp; Supabase Auth &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Phase 2 (coming next)<br>
      ◈ &nbsp; User Profile &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Phase 2<br>
      ◈ &nbsp; AI Script Engine &nbsp;&nbsp; Backend API — Phase 3<br>
      ◈ &nbsp; Razorpay / Paywall &nbsp; Phase 4<br>
      ◈ &nbsp; Notification Suite &nbsp; Phase 4
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="sl">◈ &nbsp; Reset Session Data</div>', unsafe_allow_html=True)
    if st.button("⚠ Reset All Trackers", type="secondary", use_container_width=True, key="reset_btn"):
        for k in ["plans_shown", "webinars", "month_pv", "total_pv", "generated_script", "checks"]:
            del st.session_state[k]
        st.rerun()

    st.markdown('<div class="b-warn">⚠ Reset clears all session data including blueprint progress. This cannot be undone until Supabase persistence is added in Phase 2.</div>', unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<div class="gl-footer">
  VHQ · GROWTHLINE &nbsp;·&nbsp; PHASE 1 CORE MATRIX
  &nbsp;·&nbsp; VESTIGE EDITION &nbsp;·&nbsp; 2025
</div>
""", unsafe_allow_html=True)
