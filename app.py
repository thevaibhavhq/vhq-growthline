"""
VHQ GROWTHLINE — Vestige Edition
Phase 1 · Core Matrix · Full Enterprise Upgrade
Dual Language EN/HI · Supplement Finder · Live Search · Age/Severity System
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
# SESSION STATE
# ═══════════════════════════════════════════════════════════════
_defaults = {
    "lang":               "en",
    "plans_shown":        0,
    "webinars":           0,
    "month_pv":           0,
    "total_pv":           0,
    "generated_script":   "",
    "supp_result":        None,
    "supp_concern":       "",
    "checks":             {},
}
for k, v in _defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

L = st.session_state.lang   # "en" or "hi"

# ═══════════════════════════════════════════════════════════════
# TRANSLATION DICTIONARY
# ═══════════════════════════════════════════════════════════════
T = {
    # Nav
    "nav_script":   {"en": "🎯 Script Engine",      "hi": "🎯 स्क्रिप्ट इंजन"},
    "nav_supp":     {"en": "📦 Supplement Finder",   "hi": "📦 सप्लीमेंट खोजें"},
    "nav_pv":       {"en": "📈 PV Dashboard",        "hi": "📈 PV डैशबोर्ड"},
    "nav_bp":       {"en": "🎓 Blueprint",           "hi": "🎓 ब्लूप्रिंट"},
    "nav_set":      {"en": "⚙ Settings",             "hi": "⚙ सेटिंग्स"},
    # Header
    "tagline":      {"en": "Structured path from Level 0 to Bronze Director — powered by AI",
                     "hi": "स्तर 0 से ब्रॉन्ज़ डायरेक्टर तक — AI द्वारा संचालित"},
    # Script engine
    "lead_type_lbl":  {"en": "Lead Type",            "hi": "लीड का प्रकार"},
    "objective_lbl":  {"en": "Objective",             "hi": "उद्देश्य"},
    "name_lbl":       {"en": "Lead's First Name (optional)", "hi": "लीड का नाम (वैकल्पिक)"},
    "gen_btn":        {"en": "◈  Generate Script",    "hi": "◈  स्क्रिप्ट बनाएं"},
    "your_script":    {"en": "Your Script",           "hi": "आपकी स्क्रिप्ट"},
    "copy_tip":       {"en": "Tap the copy icon ↓ for 1-tap clipboard copy",
                       "hi": "नीचे कॉपी आइकन दबाएं ↓"},
    "script_ready":   {"en": "✓ Script ready. Add a personal touch — authenticity converts better than any script.",
                       "hi": "✓ स्क्रिप्ट तैयार है। भेजने से पहले थोड़ा व्यक्तिगत बनाएं।"},
    "script_tip":     {"en": "💡 Use these as conversation starters, not monologues. Lead with genuine interest in the person.",
                       "hi": "💡 इसे बातचीत शुरू करने के लिए उपयोग करें, भाषण की तरह नहीं।"},
    # Supplement finder
    "supp_title":     {"en": "Vestige Supplement Finder", "hi": "वेस्टीज सप्लीमेंट खोजें"},
    "search_lbl":     {"en": "Search health concern or supplement name", "hi": "स्वास्थ्य समस्या या सप्लीमेंट खोजें"},
    "search_ph":      {"en": "e.g. hair fall, immunity, knee pain, diabetes, acne…",
                       "hi": "जैसे बाल झड़ना, रोग प्रतिरोधक, घुटने का दर्द, मधुमेह…"},
    "or_browse":      {"en": "— or browse by category —",  "hi": "— या श्रेणी से चुनें —"},
    "cat_lbl":        {"en": "Category",             "hi": "श्रेणी"},
    "concern_lbl":    {"en": "Health / Beauty Concern", "hi": "स्वास्थ्य / सौंदर्य समस्या"},
    "age_lbl":        {"en": "Customer's Age",       "hi": "ग्राहक की आयु"},
    "severity_lbl":   {"en": "Severity Level",       "hi": "समस्या की गंभीरता"},
    "sev_mild":       {"en": "Mild",                 "hi": "हल्का"},
    "sev_mod":        {"en": "Moderate",             "hi": "मध्यम"},
    "sev_sev":        {"en": "Severe",               "hi": "गंभीर"},
    "cust_name_lbl":  {"en": "Customer Name (optional)", "hi": "ग्राहक का नाम (वैकल्पिक)"},
    "find_btn":       {"en": "◈  Find Supplement Bundle", "hi": "◈  सप्लीमेंट खोजें"},
    "rec_bundle":     {"en": "Recommended Bundle",   "hi": "अनुशंसित सप्लीमेंट"},
    "wa_msg":         {"en": "Ready-Made WhatsApp Message", "hi": "WhatsApp संदेश"},
    "pv_lbl":         {"en": "Bundle PV",            "hi": "बंडल PV"},
    "usage_lbl":      {"en": "General Usage Guidance", "hi": "सामान्य उपयोग निर्देश"},
    "disc_supp":      {"en": "⚠ These are dietary supplement suggestions — not medical advice. Always advise customers to consult their doctor, especially for existing conditions or medication.",
                       "hi": "⚠ ये केवल आहार पूरक सुझाव हैं — चिकित्सीय सलाह नहीं। ग्राहकों को हमेशा डॉक्टर से परामर्श लेने की सलाह दें।"},
    "age_warn":       {"en": "⚠ Customer is under 12 years old. Do NOT recommend supplements without explicit medical supervision. Consult a paediatrician.",
                       "hi": "⚠ ग्राहक 12 वर्ष से कम है। डॉक्टर की निगरानी के बिना सप्लीमेंट न दें। बाल रोग विशेषज्ञ से सलाह लें।"},
    "no_results":     {"en": "No matches found. Try different keywords or browse by category.",
                       "hi": "कोई परिणाम नहीं मिला। अलग शब्द आज़माएं या श्रेणी से चुनें।"},
    # PV Dashboard
    "pv_dash_title":  {"en": "Daily Activity Tracker", "hi": "दैनिक गतिविधि ट्रैकर"},
    "plans_lbl":      {"en": "Plans Shown Today",    "hi": "आज प्लान दिखाए"},
    "webinar_lbl":    {"en": "Webinars Attended",    "hi": "वेबिनार उपस्थिति"},
    "month_pv_lbl":   {"en": "This Month's PV",      "hi": "इस माह का PV"},
    "total_pv_lbl":   {"en": "Total Cumulative PV",  "hi": "कुल संचित PV"},
    "bronze_title":   {"en": "Bronze Director Progress", "hi": "ब्रॉन्ज़ डायरेक्टर प्रगति"},
    "fast_start":     {"en": "⚡ Fast Start Bronze — 4500 PV", "hi": "⚡ फास्ट स्टार्ट ब्रॉन्ज़ — 4500 PV"},
    "std_bronze":     {"en": "◈ Standard Bronze — 5500 PV",   "hi": "◈ स्टैंडर्ड ब्रॉन्ज़ — 5500 PV"},
    "daily_title":    {"en": "Non-Negotiable Daily Actions", "hi": "अनिवार्य दैनिक कार्य"},
    "daily_tasks": {
        "en": [
            "Share value content on WhatsApp Status (supplements or team wins)",
            "Send 2–3 personalised follow-up messages using the Script Engine",
            "Read or listen to 15 minutes of personal development",
            "Check in with one downline member — offer support",
            "Log today's plans shown and webinars in the tracker above",
        ],
        "hi": [
            "WhatsApp Status पर उपयोगी सामग्री शेयर करें (सप्लीमेंट या टीम की सफलता)",
            "स्क्रिप्ट इंजन का उपयोग करके 2–3 व्यक्तिगत फॉलो-अप संदेश भेजें",
            "15 मिनट व्यक्तिगत विकास पढ़ें या सुनें",
            "एक डाउनलाइन सदस्य से बात करें — सहयोग दें",
            "आज के प्लान और वेबिनार ऊपर ट्रैकर में दर्ज करें",
        ],
    },
    "all_done":       {"en": "✅ All 5 daily actions complete. Excellent consistency.",
                       "hi": "✅ पाँचों दैनिक कार्य पूर्ण। उत्कृष्ट निरंतरता।"},
    "partial_done":   {"en": "daily actions complete today. Consistency builds the business.",
                       "hi": "दैनिक कार्य पूर्ण। निरंतरता ही व्यापार बनाती है।"},
    # Blueprint
    "bp_title":       {"en": "6-Month Blueprint Engine", "hi": "6-माह ब्लूप्रिंट इंजन"},
    "bp_principle":   {"en": "Consistency over intensity. One genuine conversation daily beats ten rushed pitches. Build a business — treat it like one.",
                       "hi": "निरंतरता तीव्रता से बड़ी है। एक सच्ची बातचीत दस जल्दबाज़ी में की गई बातों से बेहतर है।"},
    "bp_complete":    {"en": "complete. Advance to the next phase.", "hi": "पूर्ण। अगले चरण पर जाएं।"},
    "tasks_lbl":      {"en": "tasks",  "hi": "कार्य"},
    "complete_lbl":   {"en": "complete", "hi": "पूर्ण"},
    # Settings
    "lang_toggle":    {"en": "Interface Language", "hi": "भाषा चुनें"},
    "reset_btn":      {"en": "⚠  Reset All Session Trackers", "hi": "⚠  सभी डेटा रीसेट करें"},
    "reset_warn":     {"en": "⚠ Reset clears all progress and tracker data for this session.",
                       "hi": "⚠ रीसेट करने पर इस सत्र का सभी डेटा हट जाएगा।"},
    # Bronze status messages
    "b_qualified":    {"en": "🏆 Bronze Director achieved! Contact your upline to submit your qualifier immediately.",
                       "hi": "🏆 ब्रॉन्ज़ डायरेक्टर योग्यता प्राप्त! अपने अपलाइन से तुरंत संपर्क करें।"},
    "b_fast":         {"en": "⚡ Fast Start Bronze qualified!",
                       "hi": "⚡ फास्ट स्टार्ट ब्रॉन्ज़ योग्यता प्राप्त!"},
    "b_progress":     {"en": "📈 On track —",       "hi": "📈 प्रगति जारी —"},
    "b_start":        {"en": "🎯 Build your personal base first.",
                       "hi": "🎯 पहले अपना व्यक्तिगत आधार बनाएं।"},
    "pv_to_go":       {"en": "PV to Fast Start Bronze.", "hi": "PV फास्ट स्टार्ट ब्रॉन्ज़ तक।"},
}

def t(key):
    """Return translated string for current language."""
    return T.get(key, {}).get(L, T.get(key, {}).get("en", key))

# ═══════════════════════════════════════════════════════════════
# SUPPLEMENT DATABASE
# ═══════════════════════════════════════════════════════════════
# Structure: search_tags (list, both EN and HI), category, concern EN, concern HI,
# bundle: [{name, name_hi, pv, detail_en, detail_hi, usage_en, usage_hi}]
# wa_script_en, wa_script_hi

SUPP_DB = [
    # ── HEALTH SUPPLEMENTS ────────────────────────────────────
    {
        "category_en": "Health Supplements",
        "category_hi": "स्वास्थ्य सप्लीमेंट",
        "concern_en": "Hair Fall & Skin Health",
        "concern_hi": "बाल झड़ना और त्वचा स्वास्थ्य",
        "tags": ["hair fall", "hair loss", "skin", "acne", "glow", "बाल झड़ना", "त्वचा", "कील-मुंहासे", "चमक", "बाल"],
        "bundle": [
            {"name": "Vestige Hair, Skin & Nails",
             "name_hi": "वेस्टीज हेयर, स्किन एंड नेल्स",
             "pv": 40,
             "detail_en": "Biotin + collagen complex for hair strength and skin elasticity.",
             "detail_hi": "बायोटिन + कोलेजन कॉम्प्लेक्स — बालों की मजबूती और त्वचा की लोच के लिए।",
             "usage_en": "1 capsule after breakfast with water",
             "usage_hi": "1 कैप्सूल नाश्ते के बाद पानी के साथ"},
            {"name": "Vestige Neem Capsules",
             "name_hi": "वेस्टीज नीम कैप्सूल",
             "pv": 22,
             "detail_en": "Natural blood purifier supporting skin clarity.",
             "detail_hi": "प्राकृतिक रक्त शोधक — त्वचा की स्पष्टता के लिए।",
             "usage_en": "1 capsule after meals with warm water",
             "usage_hi": "1 कैप्सूल खाने के बाद गर्म पानी के साथ"},
            {"name": "Vestige Aloe Vera Juice",
             "name_hi": "वेस्टीज एलो वेरा जूस",
             "pv": 28,
             "detail_en": "Internal hydration and gut-skin axis support.",
             "detail_hi": "आंतरिक जलयोजन और आंत-त्वचा स्वास्थ्य के लिए।",
             "usage_en": "30 ml on an empty stomach with water",
             "usage_hi": "30 मिली खाली पेट पानी के साथ"},
        ],
        "wa_en": """Hi [Name] 😊

I wanted to share a Vestige supplement bundle specifically designed for hair and skin concerns:

✅ Hair, Skin & Nails — biotin + collagen for hair strength
✅ Neem Capsules — natural blood purifier for skin clarity
✅ Aloe Vera Juice — internal hydration support

These work better together as they address the root causes, not just visible symptoms.

Would you like full product details or a home delivery? 🙏""",
        "wa_hi": """नमस्ते [Name] जी 😊

मैं आपके साथ वेस्टीज का एक सप्लीमेंट बंडल शेयर करना चाहता/चाहती हूँ जो बाल और त्वचा की समस्याओं के लिए विशेष रूप से उपयोगी है:

✅ हेयर, स्किन एंड नेल्स — बायोटिन + कोलेजन बालों की मजबूती के लिए
✅ नीम कैप्सूल — प्राकृतिक रक्त शोधक, त्वचा की चमक के लिए
✅ एलो वेरा जूस — आंतरिक जलयोजन सहायता

ये मिलकर बेहतर काम करते हैं क्योंकि ये मूल कारणों को संबोधित करते हैं।

क्या आप पूरी जानकारी या होम डिलीवरी चाहेंगे? 🙏""",
    },

    {
        "category_en": "Health Supplements",
        "category_hi": "स्वास्थ्य सप्लीमेंट",
        "concern_en": "Immunity & General Wellness",
        "concern_hi": "रोग प्रतिरोधक शक्ति और सामान्य स्वास्थ्य",
        "tags": ["immunity", "energy", "wellness", "fatigue", "weak", "रोग प्रतिरोधक", "थकान", "कमज़ोरी", "ऊर्जा", "स्वास्थ्य"],
        "bundle": [
            {"name": "Vestige Spirulina",
             "name_hi": "वेस्टीज स्पाइरुलिना",
             "pv": 35,
             "detail_en": "Complete plant protein + micronutrients. Strong daily immunity base.",
             "detail_hi": "संपूर्ण पौधा प्रोटीन + सूक्ष्म पोषक तत्व। दैनिक प्रतिरोधक आधार।",
             "usage_en": "2 tablets after meals with water",
             "usage_hi": "2 गोलियाँ खाने के बाद पानी के साथ"},
            {"name": "Vestige Flax Oil Capsules",
             "name_hi": "वेस्टीज फ्लैक्स ऑयल कैप्सूल",
             "pv": 30,
             "detail_en": "Omega-3 support for inflammation and overall wellness.",
             "detail_hi": "ओमेगा-3 — सूजन कम करने और समग्र स्वास्थ्य के लिए।",
             "usage_en": "1 capsule after meals with water",
             "usage_hi": "1 कैप्सूल खाने के बाद पानी के साथ"},
            {"name": "Vestige Wheat Grass Powder",
             "name_hi": "वेस्टीज व्हीट ग्रास पाउडर",
             "pv": 25,
             "detail_en": "Alkalising greens blend for energy and detox.",
             "detail_hi": "ऊर्जा और विषहरण के लिए क्षारीय हरा मिश्रण।",
             "usage_en": "1 tsp mixed in water on an empty stomach",
             "usage_hi": "1 चम्मच पानी में मिलाकर खाली पेट"},
        ],
        "wa_en": """Hi [Name],

For daily immunity and energy support, here's a Vestige bundle I'd genuinely recommend:

✅ Spirulina — complete plant protein + micronutrients
✅ Flax Oil Capsules — Omega-3s to reduce inflammation
✅ Wheat Grass Powder — alkalising, energy-boosting greens

Together these cover nutritional gaps that most busy lifestyles create.

Happy to share more or arrange home delivery. 🙂""",
        "wa_hi": """नमस्ते [Name] जी,

दैनिक रोग प्रतिरोधक शक्ति और ऊर्जा के लिए, मैं यह वेस्टीज बंडल सुझाना चाहूँगा/चाहूँगी:

✅ स्पाइरुलिना — संपूर्ण पौधा प्रोटीन + सूक्ष्म पोषक तत्व
✅ फ्लैक्स ऑयल कैप्सूल — सूजन कम करने के लिए ओमेगा-3
✅ व्हीट ग्रास पाउडर — ऊर्जावर्धक हरा पाउडर

ये मिलकर व्यस्त जीवनशैली में पोषण की कमी पूरी करते हैं।

अधिक जानकारी या होम डिलीवरी के लिए बताएं। 🙂""",
    },

    {
        "category_en": "Health Supplements",
        "category_hi": "स्वास्थ्य सप्लीमेंट",
        "concern_en": "Joint & Bone Pain",
        "concern_hi": "जोड़ों और हड्डियों का दर्द",
        "tags": ["joint", "knee", "bone", "arthritis", "pain", "जोड़", "घुटना", "हड्डी", "गठिया", "दर्द", "जोड़ों का दर्द"],
        "bundle": [
            {"name": "Vestige Glucosamine",
             "name_hi": "वेस्टीज ग्लूकोसामीन",
             "pv": 45,
             "detail_en": "Cartilage repair and joint mobility support.",
             "detail_hi": "उपास्थि की मरम्मत और जोड़ों की गतिशीलता के लिए।",
             "usage_en": "1 capsule after meals with water",
             "usage_hi": "1 कैप्सूल खाने के बाद पानी के साथ"},
            {"name": "Vestige Calcium",
             "name_hi": "वेस्टीज कैल्शियम",
             "pv": 28,
             "detail_en": "Bone density and strength maintenance.",
             "detail_hi": "हड्डी घनत्व और मजबूती के लिए।",
             "usage_en": "1 tablet after meals with warm milk or water",
             "usage_hi": "1 गोली खाने के बाद गर्म दूध या पानी के साथ"},
            {"name": "Vestige Flax Oil Capsules",
             "name_hi": "वेस्टीज फ्लैक्स ऑयल कैप्सूल",
             "pv": 30,
             "detail_en": "Natural Omega-3s to reduce joint inflammation.",
             "detail_hi": "जोड़ों की सूजन कम करने के लिए प्राकृतिक ओमेगा-3।",
             "usage_en": "1 capsule after meals with water",
             "usage_hi": "1 कैप्सूल खाने के बाद पानी के साथ"},
        ],
        "wa_en": """Hi [Name],

For joint pain and bone health, here's a Vestige supplement bundle worth looking at:

✅ Glucosamine — cartilage repair and joint mobility
✅ Calcium — bone density and strength
✅ Flax Oil Capsules — natural Omega-3s to reduce inflammation

These address the pain, joint wear, and inflammation together.

These are nutritional supplements — not a replacement for medical treatment. Would you like more details? 🙏""",
        "wa_hi": """नमस्ते [Name] जी,

जोड़ों के दर्द और हड्डियों के स्वास्थ्य के लिए यह वेस्टीज बंडल देखें:

✅ ग्लूकोसामीन — उपास्थि की मरम्मत और जोड़ों की गतिशीलता
✅ कैल्शियम — हड्डी घनत्व और मजबूती
✅ फ्लैक्स ऑयल कैप्सूल — सूजन कम करने के लिए ओमेगा-3

ये तीनों मिलकर दर्द, जोड़ों के घिसाव और सूजन को एक साथ संबोधित करते हैं।

ये पोषण सप्लीमेंट हैं — चिकित्सा उपचार का विकल्प नहीं। क्या आप अधिक जानकारी चाहते हैं? 🙏""",
    },

    {
        "category_en": "Health Supplements",
        "category_hi": "स्वास्थ्य सप्लीमेंट",
        "concern_en": "Blood Sugar Management",
        "concern_hi": "रक्त शर्करा प्रबंधन",
        "tags": ["blood sugar", "diabetes", "glucose", "sugar", "मधुमेह", "रक्त शर्करा", "शुगर", "ग्लूकोज"],
        "bundle": [
            {"name": "Vestige Stevia",
             "name_hi": "वेस्टीज स्टीविया",
             "pv": 20,
             "detail_en": "Natural zero-calorie sweetener, safe for blood sugar management.",
             "detail_hi": "प्राकृतिक शून्य-कैलोरी मिठास — रक्त शर्करा प्रबंधन के लिए सुरक्षित।",
             "usage_en": "Use as needed in place of sugar in food or drinks",
             "usage_hi": "चाय, खाने में चीनी की जगह आवश्यकतानुसार उपयोग करें"},
            {"name": "Vestige Neem Capsules",
             "name_hi": "वेस्टीज नीम कैप्सूल",
             "pv": 22,
             "detail_en": "Traditionally used to support healthy glucose levels.",
             "detail_hi": "स्वस्थ ग्लूकोज स्तर के समर्थन के लिए पारंपरिक उपयोग।",
             "usage_en": "1 capsule after meals with warm water",
             "usage_hi": "1 कैप्सूल खाने के बाद गर्म पानी के साथ"},
            {"name": "Vestige Spirulina",
             "name_hi": "वेस्टीज स्पाइरुलिना",
             "pv": 35,
             "detail_en": "Supports metabolic health alongside a balanced diet.",
             "detail_hi": "संतुलित आहार के साथ चयापचय स्वास्थ्य का समर्थन।",
             "usage_en": "2 tablets after meals with water",
             "usage_hi": "2 गोलियाँ खाने के बाद पानी के साथ"},
        ],
        "wa_en": """Hi [Name],

For blood sugar management support, here's a Vestige wellness bundle:

✅ Stevia — natural sweetener with zero glycaemic impact (great sugar substitute)
✅ Neem Capsules — traditionally supports healthy glucose levels
✅ Spirulina — supports metabolic health alongside a balanced diet

Important: these are nutritional supplements — not a substitute for prescribed medication. Please consult your doctor.

Would you like more information? 😊""",
        "wa_hi": """नमस्ते [Name] जी,

रक्त शर्करा प्रबंधन के लिए यह वेस्टीज वेलनेस बंडल:

✅ स्टीविया — शून्य ग्लाइसेमिक प्रभाव वाला प्राकृतिक मिठास (चीनी का विकल्प)
✅ नीम कैप्सूल — पारंपरिक रूप से ग्लूकोज स्तर का समर्थन करता है
✅ स्पाइरुलिना — संतुलित आहार के साथ चयापचय स्वास्थ्य

महत्वपूर्ण: ये पोषण सप्लीमेंट हैं — दवाइयों का विकल्प नहीं। कृपया डॉक्टर से परामर्श लें।

क्या आप अधिक जानकारी चाहते हैं? 😊""",
    },

    {
        "category_en": "Health Supplements",
        "category_hi": "स्वास्थ्य सप्लीमेंट",
        "concern_en": "Heart & Cardiovascular Care",
        "concern_hi": "हृदय और हृदय-रोग सुरक्षा",
        "tags": ["heart", "cholesterol", "blood pressure", "cardiovascular", "bp", "हृदय", "कोलेस्ट्रॉल", "रक्तचाप", "बीपी"],
        "bundle": [
            {"name": "Vestige Flax Oil Capsules",
             "name_hi": "वेस्टीज फ्लैक्स ऑयल कैप्सूल",
             "pv": 30,
             "detail_en": "Omega-3s for cholesterol management and heart protection.",
             "detail_hi": "कोलेस्ट्रॉल प्रबंधन और हृदय सुरक्षा के लिए ओमेगा-3।",
             "usage_en": "1 capsule after meals with water",
             "usage_hi": "1 कैप्सूल खाने के बाद पानी के साथ"},
            {"name": "Vestige Garlic Capsules",
             "name_hi": "वेस्टीज लहसुन कैप्सूल",
             "pv": 22,
             "detail_en": "Natural blood purifier supporting skin clarity.",
             "detail_hi": "प्राकृतिक रक्त शोधक — त्वचा की स्पष्टता के लिए।",
             "usage_en": "1 capsule after meals with warm water",
             "usage_hi": "1 कैप्सूल खाने के बाद गर्म पानी के साथ"},
            {"name": "Vestige Aloe Vera Juice",
             "name_hi": "वेस्टीज एलो वेरा जूस",
             "pv": 28,
             "detail_en": "Internal hydration and gut-skin axis support.",
             "detail_hi": "आंतरिक जलयोजन और आंत-त्वचा स्वास्थ्य के लिए।",
             "usage_en": "30 ml on an empty stomach with water",
             "usage_hi": "30 मिली खाली पेट पानी के साथ"},
        ],
        "wa_en": """Hi [Name] 😊

I wanted to share a Vestige supplement bundle specifically designed for hair and skin concerns:

✅ Hair, Skin & Nails — biotin + collagen for hair strength
✅ Neem Capsules — natural blood purifier for skin clarity
✅ Aloe Vera Juice — internal hydration support

These work better together as they address the root causes, not just visible symptoms.

Would you like full product details or a home delivery? 🙏""",
        "wa_hi": """नमस्ते [Name] जी 😊

मैं आपके साथ वेस्टीज का एक सप्लीमेंट बंडल शेयर करना चाहता/चाहती हूँ जो बाल और त्वचा की समस्याओं के लिए विशेष रूप से उपयोगी है:

✅ हेयर, स्किन एंड नेल्स — बायोटिन + कोलेजन बालों की मजबूती के लिए
✅ नीम कैप्सूल — प्राकृतिक रक्त शोधक, त्वचा की चमक के लिए
✅ एलो वेरा जूस — आंतरिक जलयोजन सहायता

ये मिलकर बेहतर काम करते हैं क्योंकि ये मूल कारणों को संबोधित करते हैं।

क्या आप पूरी जानकारी या होम डिलीवरी चाहेंगे? 🙏""",
    },

    {
        "category_en": "Health Supplements",
        "category_hi": "स्वास्थ्य सप्लीमेंट",
        "concern_en": "Immunity & General Wellness",
        "concern_hi": "रोग प्रतिरोधक शक्ति और सामान्य स्वास्थ्य",
        "tags": ["immunity", "energy", "wellness", "fatigue", "weak", "रोग प्रतिरोधक", "थकान", "कमज़ोरी", "ऊर्जा", "स्वास्थ्य"],
        "bundle": [
            {"name": "Vestige Spirulina",
             "name_hi": "वेस्टीज स्पाइरुलिना",
             "pv": 35,
             "detail_en": "Complete plant protein + micronutrients. Strong daily immunity base.",
             "detail_hi": "संपूर्ण पौधा प्रोटीन + सूक्ष्म पोषक तत्व। दैनिक प्रतिरोधक आधार।",
             "usage_en": "2 tablets after meals with water",
             "usage_hi": "2 गोलियाँ खाने के बाद पानी के साथ"},
            {"name": "Vestige Flax Oil Capsules",
             "name_hi": "वेस्टीज फ्लैक्स ऑयल कैप्सूल",
             "pv": 30,
             "detail_en": "Omega-3 support for inflammation and overall wellness.",
             "detail_hi": "ओमेगा-3 — सूजन कम करने और समग्र स्वास्थ्य के लिए।",
             "usage_en": "1 capsule after meals with water",
             "usage_hi": "1 कैप्सूल खाने के बाद पानी के साथ"},
            {"name": "Vestige Wheat Grass Powder",
             "name_hi": "वेस्टीज व्हीट ग्रास पाउडर",
             "pv": 25,
             "detail_en": "Alkalising greens blend for energy and detox.",
             "detail_hi": "ऊर्जा और विषहरण के लिए क्षारीय हरा मिश्रण।",
             "usage_en": "1 tsp mixed in water on an empty stomach",
             "usage_hi": "1 चम्मच पानी में मिलाकर खाली पेट"},
        ],
        "wa_en": """Hi [Name],

For daily immunity and energy support, here's a Vestige bundle I'd genuinely recommend:

✅ Spirulina — complete plant protein + micronutrients
✅ Flax Oil Capsules — Omega-3s to reduce inflammation
✅ Wheat Grass Powder — alkalising, energy-boosting greens

Together these cover nutritional gaps that most busy lifestyles create.

Happy to share more or arrange home delivery. 🙂""",
        "wa_hi": """नमस्ते [Name] जी,

दैनिक रोग प्रतिरोधक शक्ति और ऊर्जा के लिए, मैं यह वेस्टीज बंडल सुझाना चाहूँगा/चाहूँगी:

✅ स्पाइरुलिना — संपूर्ण पौधा प्रोटीन + सूक्ष्म पोषक तत्व
✅ फ्लैक्स ऑयल कैप्सूल — सूजन कम करने के लिए ओमेगा-3
✅ व्हीट ग्रास पाउडर — ऊर्जावर्धक हरा पाउडर

ये मिलकर व्यस्त जीवनशैली में पोषण की कमी पूरी करते हैं।

अधिक जानकारी या होम डिलीवरी के लिए बताएं। 🙂""",
    },

    {
        "category_en": "Health Supplements",
        "category_hi": "स्वास्थ्य सप्लीमेंट",
        "concern_en": "Joint & Bone Pain",
        "concern_hi": "जोड़ों और हड्डियों का दर्द",
        "tags": ["joint", "knee", "bone", "arthritis", "pain", "जोड़", "घुटना", "हड्डी", "गठिया", "दर्द", "जोड़ों का दर्द"],
        "bundle": [
            {"name": "Vestige Glucosamine",
             "name_hi": "वेस्टीज ग्लूकोसामीन",
             "pv": 45,
             "detail_en": "Cartilage repair and joint mobility support.",
             "detail_hi": "उपास्थि की मरम्मत और जोड़ों की गतिशीलता के लिए।",
             "usage_en": "1 capsule after meals with water",
             "usage_hi": "1 कैप्सूल खाने के बाद पानी के साथ"},
            {"name": "Vestige Calcium",
             "name_hi": "वेस्टीज कैल्शियम",
             "pv": 28,
             "detail_en": "Bone density and strength maintenance.",
             "detail_hi": "हड्डी घनत्व और मजबूती के लिए।",
             "usage_en": "1 tablet after meals with warm milk or water",
             "usage_hi": "1 गोली खाने के बाद गर्म दूध या पानी के साथ"},
            {"name": "Vestige Flax Oil Capsules",
             "name_hi": "वेस्टीज फ्लैक्स ऑयल कैप्सूल",
             "pv": 30,
             "detail_en": "Natural Omega-3s to reduce joint inflammation.",
             "detail_hi": "जोड़ों की सूजन कम करने के लिए प्राकृतिक ओमेगा-3।",
             "usage_en": "1 capsule after meals with water",
             "usage_hi": "1 कैप्सूल खाने के बाद पानी के साथ"},
        ],
        "wa_en": """Hi [Name],

For joint pain and bone health, here's a Vestige supplement bundle worth looking at:

✅ Glucosamine — cartilage repair and joint mobility
✅ Calcium — bone density and strength
✅ Flax Oil Capsules — natural Omega-3s to reduce inflammation

These address the pain, joint wear, and inflammation together.

These are nutritional supplements — not a replacement for medical treatment. Would you like more details? 🙏""",
        "wa_hi": """नमस्ते [Name] जी,

जोड़ों के दर्द और हड्डियों के स्वास्थ्य के लिए यह वेस्टीज बंडल देखें:

✅ ग्लूकोसामीन — उपास्थि की मरम्मत और जोड़ों की गतिशीलता
✅ कैल्शियम — हड्डी घनत्व और मजबूती
✅ फ्लैक्स ऑयल कैप्सूल — सूजन कम करने के लिए ओमेगा-3

ये तीनों मिलकर दर्द, जोड़ों के घिसाव और सूजन को एक साथ संबोधित करते हैं।

ये पोषण सप्लीमेंट हैं — चिकित्सा उपचार का विकल्प नहीं। क्या आप अधिक जानकारी चाहते हैं? 🙏""",
    },

    {
        "category_en": "Health Supplements",
        "category_hi": "स्वास्थ्य सप्लीमेंट",
        "concern_en": "Blood Sugar Management",
        "concern_hi": "रक्त शर्करा प्रबंधन",
        "tags": ["blood sugar", "diabetes", "glucose", "sugar", "मधुमेह", "रक्त शर्करा", "शुगर", "ग्लूकोज"],
        "bundle": [
            {"name": "Vestige Stevia",
             "name_hi": "वेस्टीज स्टीविया",
             "pv": 20,
             "detail_en": "Natural zero-calorie sweetener, safe for blood sugar management.",
             "detail_hi": "प्राकृतिक शून्य-कैलोरी मिठास — रक्त शर्करा प्रबंधन के लिए सुरक्षित।",
             "usage_en": "Use as needed in place of sugar in food or drinks",
             "usage_hi": "चाय, खाने में चीनी की जगह आवश्यकतानुसार उपयोग करें"},
            {"name": "Vestige Neem Capsules",
             "name_hi": "वेस्टीज नीम कैप्सूल",
             "pv": 22,
             "detail_en": "Traditionally used to support healthy glucose levels.",
             "detail_hi": "स्वस्थ ग्लूकोज स्तर के समर्थन के लिए पारंपरिक उपयोग।",
             "usage_en": "1 capsule after meals with warm water",
             "usage_hi": "1 कैप्सूल खाने के बाद गर्म पानी के साथ"},
            {"name": "Vestige Spirulina",
             "name_hi": "वेस्टीज स्पाइरुलिना",
             "pv": 35,
             "detail_en": "Supports metabolic health alongside a balanced diet.",
             "detail_hi": "संतुलित आहार के साथ चयापचय स्वास्थ्य का समर्थन।",
             "usage_en": "2 tablets after meals with water",
             "usage_hi": "2 गोलियाँ खाने के बाद पानी के साथ"},
        ],
        "wa_en": """Hi [Name],

For blood sugar management support, here's a Vestige wellness bundle:

✅ Stevia — natural sweetener with zero glycaemic impact (great sugar substitute)
✅ Neem Capsules — traditionally supports healthy glucose levels
✅ Spirulina — supports metabolic health alongside a balanced diet

Important: these are nutritional supplements — not a substitute for prescribed medication. Please consult your doctor.

Would you like more information? 😊""",
        "wa_hi": """नमस्ते [Name] जी,

रक्त शर्करा प्रबंधन के लिए यह वेस्टीज वेलनेस बंडल:

✅ स्टीविया — शून्य ग्लाइसेमिक प्रभाव वाला प्राकृतिक मिठास (चीनी का विकल्प)
✅ नीम कैप्सूल — पारंपरिक रूप से ग्लूकोज स्तर का समर्थन करता है
✅ स्पाइरुलिना — संतुलित आहार के साथ चयापचय स्वास्थ्य

महत्वपूर्ण: ये पोषण सप्लीमेंट हैं — दवाइयों का विकल्प नहीं। कृपया डॉक्टर से परामर्श लें।

क्या आप अधिक जानकारी चाहते हैं? 😊""",
    },

    {
        "category_en": "Health Supplements",
        "category_hi": "स्वास्थ्य सप्लीमेंट",
        "concern_en": "Heart & Cardiovascular Care",
        "concern_hi": "हृदय और हृदय-रोग सुरक्षा",
        "tags": ["heart", "cholesterol", "blood pressure", "cardiovascular", "bp", "हृदय", "कोलेस्ट्रॉल", "रक्तचाप", "बीपी"],
        "bundle": [
            {"name": "Vestige Flax Oil Capsules",
             "name_hi": "वेस्टीज फ्लैक्स ऑयल कैप्सूल",
             "pv": 30,
             "detail_en": "Omega-3s for cholesterol management and heart protection.",
             "detail_hi": "कोलेस्ट्रॉल प्रबंधन और हृदय सुरक्षा के लिए ओमेगा-3।",
             "usage_en": "1 capsule after meals with water",
             "usage_hi": "1 कैप्सूल खाने के बाद पानी के साथ"},
            {"name": "Vestige Garlic Capsules",
             "name_hi": "वेस्टीज लहसुन कैप्सूल",
             "pv": 22,
             "detail_en": "Natural circulation support and blood pressure management.",
             "detail_hi": "प्राकृतिक रक्त संचार सहायता और रक्तचाप प्रबंधन।",
             "usage_en": "1 capsule after meals with water",
             "usage_hi": "1 कैप्सूल खाने के बाद पानी के साथ"},
            {"name": "Vestige Spirulina",
             "name_hi": "वेस्टीज स्पाइरुलिना",
             "pv": 35,
             "detail_en": "Antioxidant-rich superfood supporting cardiovascular health.",
             "detail_hi": "एंटीऑक्सीडेंट युक्त सुपरफूड — हृदय स्वास्थ्य के लिए।",
             "usage_en": "2 tablets after meals with water",
             "usage_hi": "2 गोलियाँ खाने के बाद पानी के साथ"},
        ],
        "wa_en": """Hi [Name],

For heart and cardiovascular wellness support:

✅ Flax Oil Capsules — Omega-3s for healthy cholesterol and heart protection
✅ Garlic Capsules — natural circulation and blood pressure support
✅ Spirulina — powerful antioxidant for cardiovascular health

Important: these are nutritional supplements — not a substitute for cardiac medication or medical advice.

Would you like more details or home delivery? 🙏""",
        "wa_hi": """नमस्ते [Name] जी,

हृदय स्वास्थ्य और हृदय-रोग सुरक्षा के लिए:

✅ फ्लैक्स ऑयल कैप्सूल — स्वस्थ कोलेस्ट्रॉल और हृदय सुरक्षा के लिए ओमेगा-3
✅ लहसुन कैप्सूल — प्राकृतिक रक्त संचार और रक्तचाप सहायता
✅ स्पाइरुलिना — हृदय स्वास्थ्य के लिए शक्तिशाली एंटीऑक्सीडेंट

महत्वपूर्ण: ये पोषण सप्लीमेंट हैं — हृदय की दवाओं या चिकित्सीय सलाह का विकल्प नहीं।

क्या आप अधिक जानकारी चाहते हैं? 🙏""",
    },

    # ── SKIN CARE ─────────────────────────────────────────────
    {
        "category_en": "Premium Skin Care",
        "category_hi": "प्रीमियम त्वचा देखभाल",
        "concern_en": "Acne & Oily Skin",
        "concern_hi": "कील-मुंहासे और तैलीय त्वचा",
        "tags": ["acne", "pimple", "oily skin", "breakout", "कील-मुंहासे", "मुंहासे", "तैलीय त्वचा", "पिंपल"],
        "bundle": [
            {"name": "Vestige Neem Face Wash",
             "name_hi": "वेस्टीज नीम फेस वॉश",
             "pv": 18,
             "detail_en": "Antibacterial neem formula for deep pore cleansing.",
             "detail_hi": "गहरी सफाई के लिए जीवाणुरोधी नीम फार्मूला।",
             "usage_en": "Twice daily — morning and before bed",
             "usage_hi": "दिन में दो बार — सुबह और सोने से पहले"},
            {"name": "Vestige Neem Capsules",
             "name_hi": "वेस्टीज नीम कैप्सूल",
             "pv": 22,
             "detail_en": "Internal blood purifier to address acne from within.",
             "detail_hi": "अंदर से मुंहासों को ठीक करने के लिए आंतरिक रक्त शोधक।",
             "usage_en": "1 capsule after meals with warm water",
             "usage_hi": "1 कैप्सूल खाने के बाद गर्म पानी के साथ"},
            {"name": "Vestige Aloe Vera Gel",
             "name_hi": "वेस्टीज एलो वेरा जेल",
             "pv": 20,
             "detail_en": "Soothing topical application to calm inflamed skin.",
             "detail_hi": "सूजन वाली त्वचा को शांत करने के लिए सामयिक अनुप्रयोग।",
             "usage_en": "Apply thinly on affected areas after cleansing",
             "usage_hi": "सफाई के बाद प्रभावित क्षेत्रों पर हल्के से लगाएं"},
        ],
        "wa_en": """Hi [Name] 😊

For acne and oily skin concerns, here's a Vestige combination that works from the inside out:

✅ Neem Face Wash — deep antibacterial cleansing
✅ Neem Capsules — internal blood purifier (addresses root cause)
✅ Aloe Vera Gel — soothes and calms inflamed skin

The inside-out approach works better than topical products alone.

Would you like home delivery? 🌿""",
        "wa_hi": """नमस्ते [Name] जी 😊

कील-मुंहासे और तैलीय त्वचा के लिए यह वेस्टीज संयोजन अंदर और बाहर दोनों से काम करता है:

✅ नीम फेस वॉश — गहरी जीवाणुरोधी सफाई
✅ नीम कैप्सूल — आंतरिक रक्त शोधक (मूल कारण को संबोधित करता है)
✅ एलो वेरा जेल — सूजन वाली त्वचा को शांत करता है

यह अंदर-बाहर दोनों से काम करने वाला दृष्टिकोण केवल बाहरी उत्पादों से बेहतर है।

क्या आप होम डिलीवरी चाहते हैं? 🌿""",
    },

    {
        "category_en": "Premium Skin Care",
        "category_hi": "प्रीमियम त्वचा देखभाल",
        "concern_en": "Dry Skin & Moisturisation",
        "concern_hi": "रूखी त्वचा और नमी",
        "tags": ["dry skin", "moisturiser", "dryness", "rash", "रूखी त्वचा", "नमी", "खुरदरी त्वचा", "सूखापन"],
        "bundle": [
            {"name": "Vestige Aloe Vera Gel",
             "name_hi": "वेस्टीज एलो वेरा जेल",
             "pv": 20,
             "detail_en": "Deep hydration and skin barrier repair.",
             "detail_hi": "गहरी जलयोजन और त्वचा अवरोधक मरम्मत।",
             "usage_en": "Apply on face and body after bathing",
             "usage_hi": "नहाने के बाद चेहरे और शरीर पर लगाएं"},
            {"name": "Vestige Aloe Vera Juice",
             "name_hi": "वेस्टीज एलो वेरा जूस",
             "pv": 28,
             "detail_en": "Internal skin hydration from within.",
             "detail_hi": "अंदर से त्वचा को नमी देता है।",
             "usage_en": "30 ml on empty stomach with water",
             "usage_hi": "30 मिली खाली पेट पानी के साथ"},
            {"name": "Vestige Flax Oil Capsules",
             "name_hi": "वेस्टीज फ्लैक्स ऑयल कैप्सूल",
             "pv": 30,
             "detail_en": "Essential fatty acids for skin moisture retention.",
             "detail_hi": "त्वचा की नमी बनाए रखने के लिए आवश्यक वसा अम्ल।",
             "usage_en": "1 capsule after meals with water",
             "usage_hi": "1 कैप्सूल खाने के बाद पानी के साथ"},
        ],
        "wa_en": """Hi [Name]!

For dry skin, this Vestige combination works from inside and outside:

✅ Aloe Vera Gel — topical hydration and skin barrier repair
✅ Aloe Vera Juice — internal hydration support
✅ Flax Oil Capsules — essential fatty acids to retain skin moisture

Want me to arrange home delivery? 🌿""",
        "wa_hi": """नमस्ते [Name] जी!

रूखी त्वचा के लिए यह वेस्टीज संयोजन अंदर और बाहर दोनों से काम करता है:

✅ एलो वेरा जेल — बाहरी जलयोजन और त्वचा अवरोधक मरम्मत
✅ एलो वेरा जूस — आंतरिक जलयोजन सहायता
✅ फ्लैक्स ऑयल कैप्सूल — त्वचा की नमी बनाए रखने के लिए

होम डिलीवरी चाहेंगे? 🌿""",
    },

    # ── PERSONAL CARE & BEAUTY ────────────────────────────────
    {
        "category_en": "Personal Care & Beauty",
        "category_hi": "व्यक्तिगत देखभाल और सौंदर्य",
        "concern_en": "Oral Hygiene & Teeth Care",
        "concern_hi": "मुँह की स्वच्छता और दाँतों की देखभाल",
        "tags": ["teeth", "oral", "toothpaste", "gum", "breath", "दाँत", "मुँह", "टूथपेस्ट", "मसूड़े", "सांस"],
        "bundle": [
            {"name": "Vestige Toothpaste (Neem + Clove)",
             "name_hi": "वेस्टीज टूथपेस्ट (नीम + लौंग)",
             "pv": 15,
             "detail_en": "Antibacterial neem and clove formula for oral health.",
             "detail_hi": "मुँह के स्वास्थ्य के लिए जीवाणुरोधी नीम और लौंग फार्मूला।",
             "usage_en": "Twice daily after meals",
             "usage_hi": "खाने के बाद दिन में दो बार"},
            {"name": "Vestige Calcium",
             "name_hi": "वेस्टीज कैल्शियम",
             "pv": 28,
             "detail_en": "Calcium supplementation for strong teeth and bone density.",
             "detail_hi": "मजबूत दाँतों और हड्डी घनत्व के लिए कैल्शियम।",
             "usage_en": "1 tablet after meals with warm milk or water",
             "usage_hi": "1 गोली खाने के बाद गर्म दूध या पानी के साथ"},
        ],
        "wa_en": """Hi [Name]!

For oral hygiene and strong teeth, here's what Vestige offers:

✅ Neem + Clove Toothpaste — antibacterial protection and fresh breath
✅ Calcium Supplement — strong teeth from within

Simple, effective, and great quality. Would you like the details? 😊""",
        "wa_hi": """नमस्ते [Name] जी!

मुँह की स्वच्छता और मजबूत दाँतों के लिए वेस्टीज:

✅ नीम + लौंग टूथपेस्ट — जीवाणुरोधी सुरक्षा और ताज़ी सांस
✅ कैल्शियम सप्लीमेंट — अंदर से मजबूत दाँत

सरल, प्रभावी और बेहतरीन गुणवत्ता। क्या आप जानकारी चाहेंगे? 😊""",
    },

    # ── AGRI CARE ─────────────────────────────────────────────
    {
        "category_en": "Agri Care",
        "category_hi": "कृषि देखभाल",
        "concern_en": "Crop Growth & Soil Health",
        "concern_hi": "फसल वृद्धि और मिट्टी स्वास्थ्य",
        "tags": ["crop", "soil", "fertilizer", "farming", "plant", "फसल", "मिट्टी", "खाद", "खेती", "कृषि", "पौधा"],
        "bundle": [
            {"name": "Vestige Power Booster",
             "name_hi": "वेस्टीज पावर बूस्टर",
             "pv": 30,
             "detail_en": "Concentrated organic plant growth stimulant.",
             "detail_hi": "केंद्रित जैविक पौधा वृद्धि उत्तेजक।",
             "usage_en": "Mix as per product label directions before spraying on crops",
             "usage_hi": "उत्पाद लेबल निर्देश के अनुसार मिलाएं और फसल पर छिड़कें"},
            {"name": "Vestige Terminate",
             "name_hi": "वेस्टीज टर्मिनेट",
             "pv": 35,
             "detail_en": "Natural bio-pesticide for crop protection.",
             "detail_hi": "फसल सुरक्षा के लिए प्राकृतिक जैव-कीटनाशक।",
             "usage_en": "Dilute and spray per product label instructions",
             "usage_hi": "उत्पाद लेबल निर्देश के अनुसार पतला करके छिड़कें"},
        ],
        "wa_en": """Hi [Name],

For crop growth and soil health, Vestige's Agri Care range is worth knowing about:

✅ Power Booster — organic plant growth stimulant
✅ Terminate — natural bio-pesticide for crop protection

These are popular among farmers who want effective and natural crop care alternatives.

Would you like more details or a demo? 🌾""",
        "wa_hi": """नमस्ते [Name] जी,

फसल वृद्धि और मिट्टी स्वास्थ्य के लिए वेस्टीज एग्री केयर रेंज जानने लायक है:

✅ पावर बूस्टर — जैविक पौधा वृद्धि उत्तेजक
✅ टर्मिनेट — फसल सुरक्षा के लिए प्राकृतिक जैव-कीटनाशक

ये उन किसानों में लोकप्रिय हैं जो प्रभावी और प्राकृतिक फसल देखभाल चाहते हैं।

क्या आप अधिक जानकारी या डेमो चाहेंगे? 🌾""",
    },
]

# Build category lists
CAT_EN = sorted(set(s["category_en"] for s in SUPP_DB))
CAT_HI = sorted(set(s["category_hi"] for s in SUPP_DB))


def search_supplements(query: str) -> list:
    """Return matching supplement entries for a search query."""
    q = query.strip().lower()
    if not q:
        return []
return [s for s in SUPP_DB if any(q in tag.lower() for tag in s["tags"])]


def get_by_category_concern(cat_en: str, concern_en: str) -> dict | None:
    for s in SUPP_DB:
        if s["category_en"] == cat_en and s["concern_en"] == concern_en:
            return s
    return None


# ═══════════════════════════════════════════════════════════════
# SCRIPT LIBRARY
# ═══════════════════════════════════════════════════════════════
SCRIPTS = {
    ("🎓 College Student", "📞 Invite to Zoom Meeting"):
"""Hey [Name] 👋

Hope you're doing well! I've been exploring a side income that a lot of students are using — doesn't need much time and fits around college life completely.

Takes about 20 minutes on a Zoom call to explain properly.

Would you be open to a chat this week — say Tuesday or Thursday evening? No pressure at all. 🙂""",

    ("🎓 College Student", "📦 Supplement Recommendation"):
"""Hey [Name]!

I've been using Vestige's health supplements for a few months and noticed a genuine difference — especially in energy and focus during studies.

Given your schedule, thought you might find them useful. Quality is solid and the pricing is fair.

Want me to share the product details? 📋""",

    ("🎓 College Student", "🚀 Explaining the Business Income Plan"):
"""Hey [Name],

Quick question — are you open to building a part-time income while still in college?

I'm part of a network with Vestige — a legitimate health and wellness brand, 20+ years in India. The model is performance-based, fully flexible.

I can explain how it works in about 15 minutes. No obligation. Interested?""",

    ("💼 Corporate Employee", "📞 Invite to Zoom Meeting"):
"""Hi [Name],

I know how full schedules can get — so I'll be brief.

I've been building a secondary income on the side for a few months now. Mostly evenings and weekends — no conflict with my job at all.

Would you have 20 minutes this Saturday for a quick Zoom? I think it's worth your time. 🙌""",

    ("💼 Corporate Employee", "📦 Supplement Recommendation"):
"""Hey [Name]!

You mentioned feeling tired lately — I've been using Vestige's wellness supplements and the difference in energy has been real.

Not a pitch — just sharing something that works for me. Happy to send the product details if you want. 🟢""",

    ("💼 Corporate Employee", "🚀 Explaining the Business Income Plan"):
"""Hi [Name],

Straight question — are you comfortable with only one income source?

I'm working with Vestige as a part-time distributor. Performance-based, no fixed hours, fits alongside a job.

I can walk you through the income structure in 15 minutes. Worth knowing about — interested?""",

    ("🏠 Housewife", "📞 Invite to Zoom Meeting"):
"""Hi [Name] 😊

I started something recently that works really well around home life — flexible timing, no office, genuine earning potential.

It's with Vestige. I can explain in about 20 minutes at whatever time suits you.

When works for you this week?""",

    ("🏠 Housewife", "📦 Supplement Recommendation"):
"""Hi [Name]!

I've been using Vestige's wellness supplements and home care products and genuinely find them good quality with consistent results.

Thought of you because you always prioritise the best for your family! Want me to share the catalogue? 🌿""",

    ("🏠 Housewife", "🚀 Explaining the Business Income Plan"):
"""Hi [Name],

Have you ever thought about building your own income from home, fully on your schedule?

I'm with Vestige as a distributor. No pressure, flexible hours, performance-linked earnings.

I can explain in 15 minutes whenever you're free. Would you like to hear more? 😊""",

    ("🏪 Small Business Owner", "📞 Invite to Zoom Meeting"):
"""Hi [Name],

You already understand business better than most — so I'll be direct.

I'm building a distribution network with Vestige. Given your background, you'd assess it quickly.

20-minute Zoom this week? I'll show you numbers, not just concepts. 📊""",

    ("🏪 Small Business Owner", "📦 Supplement Recommendation"):
"""Hi [Name]!

Have you looked at Vestige's supplement and wellness range? Solid quality, consistent demand, home delivery.

Given your setup, there's also a clear distributor margin structure worth knowing about.

Interested in seeing the numbers?""",

    ("🏪 Small Business Owner", "🚀 Explaining the Business Income Plan"):
"""Hi [Name],

Vestige's distributor model is one of the more transparent ones in the space — clear PV-based payouts, genuine products, 20+ years in India.

As a business owner you'd assess this in 10 minutes. I'd rather show you actual numbers than pitch you.

Quick call this week?""",
}

# ═══════════════════════════════════════════════════════════════
# BLUEPRINT DATA
# ═══════════════════════════════════════════════════════════════
BLUEPRINT = [
    {
        "phase_en": "Month 1–2", "phase_hi": "माह 1–2",
        "title_en": "Core Learning & Self-Use Activation",
        "title_hi": "मूल शिक्षा और स्व-उपयोग सक्रियण",
        "tag_en": "Foundation Phase", "tag_hi": "आधार चरण",
        "goal_en": "Hit 100 PV/month personal use. Learn supplements deeply. Build contact list.",
        "goal_hi": "100 PV/माह व्यक्तिगत उपयोग। सप्लीमेंट को गहराई से जानें। संपर्क सूची बनाएं।",
        "tasks_en": [
            "Complete Vestige supplement training (official YouTube channel)",
            "Place your first personal-use supplement bundle — target 100 PV",
            "Set up WhatsApp Business with clear professional bio and profile photo",
            "List 30 people you know — family, friends, classmates, colleagues",
            "Attend 2 company webinars or team Zoom sessions this month",
            "Use the Script Engine to practise 5 conversation openers",
            "Identify 3 genuinely interested people from initial conversations",
            "Log every conversation in the PV Dashboard daily",
        ],
        "tasks_hi": [
            "वेस्टीज सप्लीमेंट प्रशिक्षण पूरा करें (आधिकारिक YouTube चैनल)",
            "पहला व्यक्तिगत सप्लीमेंट बंडल ऑर्डर करें — लक्ष्य 100 PV",
            "स्पष्ट व्यावसायिक बायो और प्रोफाइल फोटो के साथ WhatsApp Business सेटअप करें",
            "अपने 30 परिचितों की सूची बनाएं — परिवार, मित्र, सहपाठी, सहकर्मी",
            "इस माह 2 कंपनी वेबिनार या टीम ज़ूम सत्र में भाग लें",
            "स्क्रिप्ट इंजन से 5 बातचीत के अभ्यास करें",
            "प्रारंभिक बातचीत से 3 वास्तव में इच्छुक लोगों की पहचान करें",
            "PV डैशबोर्ड में हर बातचीत दैनिक दर्ज करें",
        ],
    },
    {
        "phase_en": "Month 3–4", "phase_hi": "माह 3–4",
        "title_en": "Duplication Phase — Building Your Frontline",
        "title_hi": "द्विगुणन चरण — अपनी फ्रंटलाइन बनाएं",
        "tag_en": "Growth Phase", "tag_hi": "विकास चरण",
        "goal_en": "Onboard 3–6 active frontline distributors. Reach 500–1500 cumulative PV.",
        "goal_hi": "3–6 सक्रिय फ्रंटलाइन वितरकों को जोड़ें। 500–1500 संचित PV तक पहुँचें।",
        "tasks_en": [
            "Use the Script Engine daily — personalise for each lead type",
            "Show the business plan to at least one new person per day",
            "Onboard your first active frontline distributor",
            "Help your frontline place their first supplement order",
            "Attend every team training — bring a new member each time",
            "Hit 300 PV this month (personal + frontline combined)",
            "Celebrate your first downline's first order in your team group",
            "Identify 3 more warm leads from your original list",
        ],
        "tasks_hi": [
            "प्रतिदिन स्क्रिप्ट इंजन का उपयोग करें — हर लीड के लिए व्यक्तिगत बनाएं",
            "प्रतिदिन कम से कम एक नए व्यक्ति को बिज़नेस प्लान दिखाएं",
            "पहले सक्रिय फ्रंटलाइन वितरक को जोड़ें",
            "अपने फ्रंटलाइन का पहला सप्लीमेंट ऑर्डर में मदद करें",
            "हर टीम प्रशिक्षण में भाग लें — हर बार एक नया सदस्य लाएं",
            "इस माह 300 PV प्राप्त करें (व्यक्तिगत + फ्रंटलाइन मिलाकर)",
            "टीम ग्रुप में पहली डाउनलाइन की सफलता का जश्न मनाएं",
            "मूल सूची से 3 और इच्छुक लोगों की पहचान करें",
        ],
    },
    {
        "phase_en": "Month 5–6", "phase_hi": "माह 5–6",
        "title_en": "Bronze Director Leadership Push",
        "title_hi": "ब्रॉन्ज़ डायरेक्टर नेतृत्व लक्ष्य",
        "tag_en": "Leadership Phase", "tag_hi": "नेतृत्व चरण",
        "goal_en": "Cumulative 5500 PV (or Fast Start 4500 PV). Unlock Bronze Director.",
        "goal_hi": "संचित 5500 PV (या फास्ट स्टार्ट 4500 PV)। ब्रॉन्ज़ डायरेक्टर प्राप्त करें।",
        "tasks_en": [
            "Target team PV of 1500–2500 this month",
            "Support each frontline to onboard their first recruit",
            "Lead a team supplement education session yourself",
            "Track every team member's PV weekly — support anyone falling behind",
            "Cross 4500 cumulative PV — Fast Start Bronze qualifier milestone",
            "Coordinate Bronze Director application with your sponsor / upline",
            "Plan your post-Bronze strategy toward Silver Director",
            "Document your 6-month journey — share as proof with your downline",
        ],
        "tasks_hi": [
            "इस माह 1500–2500 टीम PV का लक्ष्य रखें",
            "हर फ्रंटलाइन को उनका पहला सदस्य जोड़ने में सहायता करें",
            "स्वयं एक टीम सप्लीमेंट शिक्षा सत्र का नेतृत्व करें",
            "हर सप्ताह हर टीम सदस्य का PV ट्रैक करें — जो पीछे हो उन्हें सहायता दें",
            "4500 संचित PV पार करें — फास्ट स्टार्ट ब्रॉन्ज़ मील का पत्थर",
            "अपने प्रायोजक/अपलाइन के साथ ब्रॉन्ज़ डायरेक्टर आवेदन समन्वित करें",
            "सिल्वर डायरेक्टर की ओर ब्रॉन्ज़ के बाद की रणनीति बनाएं",
            "अपनी 6-माह यात्रा दर्ज करें — डाउनलाइन के साथ प्रमाण के रूप में साझा करें",
        ],
    },
]

# ═══════════════════════════════════════════════════════════════
# CSS DESIGN SYSTEM
# ═══════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Orbitron:wght@700;900&family=IBM+Plex+Mono:wght@400;500&family=Noto+Sans+Devanagari:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
  font-family: 'Inter', 'Noto Sans Devanagari', sans-serif;
  background: linear-gradient(145deg, #0A0F1E 0%, #0F172A 55%, #0C1526 100%);
  color: #E2E8F0; -webkit-font-smoothing: antialiased; min-height: 100vh;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 0.9rem 5rem 0.9rem; max-width: 720px; margin: auto; }

@keyframes corpPulse {
  0%,100% { text-shadow: 0 0 8px rgba(13,148,136,0.6), 0 0 24px rgba(13,148,136,0.3),
    0 3px 0 rgba(7,89,82,0.8), 0 5px 0 rgba(4,55,51,0.6), 0 8px 16px rgba(0,0,0,0.6); }
  50%     { text-shadow: 0 0 14px rgba(45,212,191,0.7), 0 0 40px rgba(13,148,136,0.4),
    0 3px 0 rgba(7,89,82,0.9), 0 5px 0 rgba(4,55,51,0.7), 0 8px 22px rgba(0,0,0,0.7); }
}
@keyframes scanH { 0%{transform:translateX(-100%)} 100%{transform:translateX(100vw)} }
@keyframes fadeUp { from{opacity:0;transform:translateY(12px)} to{opacity:1;transform:translateY(0)} }
@keyframes fadeDown { from{opacity:0;transform:translateY(-12px)} to{opacity:1;transform:translateY(0)} }
@keyframes glowTeal {
  0%,100% { box-shadow:0 1px 3px rgba(0,0,0,0.4),0 0 0 1px rgba(13,148,136,0.12); }
  50%     { box-shadow:0 4px 16px rgba(0,0,0,0.5),0 0 0 1px rgba(13,148,136,0.28); }
}
@keyframes shimmer { 0%{background-position:-200% center} 100%{background-position:200% center} }
@keyframes barFill { from{width:0} }
@keyframes pop { 0%{transform:scale(0.85);opacity:0} 65%{transform:scale(1.04)} 100%{transform:scale(1);opacity:1} }

/* Header */
.vhq-header {
  position:relative; text-align:center; padding:2.8rem 1rem 2rem;
  overflow:hidden; animation:fadeDown 0.65s ease both;
  border-bottom:1px solid rgba(13,148,136,0.18); margin-bottom:0.5rem;
}
.vhq-header::before {
  content:''; position:absolute; top:0; left:0; right:0; height:2px;
  background:linear-gradient(90deg,transparent,rgba(45,212,191,0.55),transparent);
  animation:scanH 5s linear infinite;
}
.vhq-eyebrow {
  font-family:'IBM Plex Mono',monospace; font-size:0.6rem;
  letter-spacing:0.25em; text-transform:uppercase; color:rgba(45,212,191,0.55);
  margin-bottom:0.65rem; animation:fadeDown 0.6s ease 0.1s both;
}
.vhq-logo {
  font-family:'Orbitron',monospace; font-weight:900;
  font-size:clamp(1.3rem,4.8vw,2rem); letter-spacing:0.07em;
  color:#F1F5F9; line-height:1.2; user-select:none;
  animation:corpPulse 4s ease-in-out infinite, fadeDown 0.7s ease 0.15s both;
}
.vhq-sub {
  font-family:'IBM Plex Mono',monospace; font-size:0.63rem;
  color:rgba(203,213,225,0.45); letter-spacing:0.1em; margin-top:0.15rem;
}
.vhq-tagline { font-size:0.78rem; color:rgba(148,163,184,0.6); margin-top:0.55rem; line-height:1.5; }
.vhq-badges { margin-top:0.75rem; display:flex; gap:0.45rem; justify-content:center; flex-wrap:wrap; }
.vhq-badge {
  display:inline-block; font-family:'IBM Plex Mono',monospace;
  font-size:0.57rem; letter-spacing:0.12em; text-transform:uppercase;
  padding:0.2rem 0.7rem; border-radius:20px; animation:pop 0.5s ease 0.4s both;
}
.badge-teal  { background:rgba(13,148,136,0.14); border:1px solid rgba(13,148,136,0.32); color:#2DD4BF; }
.badge-gold  { background:rgba(202,138,4,0.11);  border:1px solid rgba(202,138,4,0.32);  color:#FCD34D; }
.badge-slate { background:rgba(71,85,105,0.18);  border:1px solid rgba(71,85,105,0.38);  color:#94A3B8; }

/* Glass cards */
.gc {
  background:rgba(15,23,42,0.6); backdrop-filter:blur(20px);
  -webkit-backdrop-filter:blur(20px); border:1px solid rgba(51,65,85,0.45);
  border-radius:16px; padding:1.5rem 1.3rem; margin-bottom:1rem;
  position:relative; overflow:hidden;
  animation:glowTeal 5s ease-in-out infinite, fadeUp 0.4s ease both;
}
.gc::before {
  content:''; position:absolute; top:0; left:10%; right:10%; height:1px;
  background:linear-gradient(90deg,transparent,rgba(13,148,136,0.35),transparent);
}
.gc-label {
  font-family:'IBM Plex Mono',monospace; font-size:0.58rem;
  letter-spacing:0.18em; text-transform:uppercase; color:rgba(13,148,136,0.78);
  margin-bottom:0.85rem;
}
.gc-gold {
  background:rgba(15,23,42,0.65); backdrop-filter:blur(20px);
  -webkit-backdrop-filter:blur(20px); border:1px solid rgba(202,138,4,0.32);
  border-radius:16px; padding:1.4rem 1.3rem; margin-bottom:1rem;
  position:relative; overflow:hidden; box-shadow:0 0 18px rgba(202,138,4,0.07);
}
.gc-gold::before {
  content:''; position:absolute; top:0; left:10%; right:10%; height:1px;
  background:linear-gradient(90deg,transparent,rgba(202,138,4,0.4),transparent);
}

/* Inputs */
.stTextInput>div>div>input,
.stTextArea>div>div>textarea,
.stSelectbox>div>div,
.stNumberInput>div>div>input,
.stSlider>div>div { 
  background:rgba(30,41,59,0.7) !important;
  border:1px solid rgba(51,65,85,0.65) !important; border-radius:10px !important;
  color:#E2E8F0 !important; font-family:'Inter','Noto Sans Devanagari',sans-serif !important;
  font-size:0.9rem !important; transition:border-color 0.2s ease,box-shadow 0.2s ease !important;
}
.stTextInput>div>div>input:focus, .stTextArea>div>div>textarea:focus,
.stNumberInput>div>div>input:focus {
  border-color:#0D9488 !important; box-shadow:0 0 0 3px rgba(13,148,136,0.17) !important;
}
label { color:rgba(148,163,184,0.85) !important; font-size:0.78rem !important;
  font-weight:500 !important; letter-spacing:0.02em !important; }

/* Buttons */
.stButton>button[kind="primary"] {
  width:100%;
  background:linear-gradient(135deg,#0D9488 0%,#14B8A6 50%,#0D9488 100%) !important;
  background-size:200% auto !important; color:#fff !important; border:none !important;
  border-radius:10px !important; font-family:'Inter',sans-serif !important;
  font-weight:700 !important; font-size:0.9rem !important; padding:0.7rem 1.1rem !important;
  letter-spacing:0.03em !important; box-shadow:0 4px 18px rgba(13,148,136,0.3) !important;
  transition:background-position 0.4s ease,transform 0.15s ease,box-shadow 0.2s ease !important;
}
.stButton>button[kind="primary"]:hover {
  background-position:right center !important; transform:translateY(-1px) !important;
  box-shadow:0 6px 24px rgba(13,148,136,0.45) !important;
}
.stButton>button[kind="secondary"] {
  width:100%; background:rgba(30,41,59,0.6) !important;
  color:rgba(148,163,184,0.85) !important; border:1px solid rgba(51,65,85,0.6) !important;
  border-radius:10px !important; font-family:'Inter',sans-serif !important;
  font-size:0.85rem !important; transition:border-color 0.2s,background 0.2s !important;
}
.stButton>button[kind="secondary"]:hover {
  border-color:rgba(13,148,136,0.5) !important; background:rgba(13,148,136,0.08) !important;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
  background:rgba(15,23,42,0.7) !important; border:1px solid rgba(51,65,85,0.45) !important;
  border-radius:12px !important; padding:5px !important; gap:3px !important; margin-bottom:1rem !important;
}
.stTabs [data-baseweb="tab"] {
  background:transparent !important; border-radius:8px !important;
  color:rgba(148,163,184,0.55) !important; font-family:'Inter','Noto Sans Devanagari',sans-serif !important;
  font-weight:600 !important; font-size:0.78rem !important;
  padding:0.42rem 0.55rem !important; border:none !important; transition:all 0.2s ease !important;
}
.stTabs [aria-selected="true"] {
  background:linear-gradient(135deg,#0F766E,#0D9488) !important; color:#fff !important;
  box-shadow:0 2px 12px rgba(13,148,136,0.35) !important;
}
.stTabs [data-baseweb="tab-border"] { display:none !important; }
.stTabs [data-baseweb="tab-panel"]  { padding-top:0.2rem !important; }

/* Section label */
.sl {
  font-family:'IBM Plex Mono',monospace; font-size:0.58rem; letter-spacing:0.2em;
  text-transform:uppercase; color:rgba(13,148,136,0.7); margin:1.5rem 0 0.6rem;
}

/* Metric blocks */
.metric-row { display:flex; gap:0.45rem; margin:0.5rem 0; }
.metric-block {
  flex:1; background:rgba(30,41,59,0.6); border:1px solid rgba(51,65,85,0.5);
  border-radius:12px; padding:0.85rem 0.5rem; text-align:center;
}
.metric-block-gold {
  flex:1; background:rgba(30,41,59,0.6); border:1px solid rgba(202,138,4,0.28);
  border-radius:12px; padding:0.85rem 0.5rem; text-align:center;
}
.metric-val { font-family:'Orbitron',monospace; font-size:1.3rem; font-weight:700; color:#2DD4BF; line-height:1; }
.metric-val-gold { font-family:'Orbitron',monospace; font-size:1.3rem; font-weight:700; color:#FCD34D; line-height:1; }
.metric-lbl { font-family:'IBM Plex Mono',monospace; font-size:0.54rem; letter-spacing:0.08em;
  text-transform:uppercase; color:rgba(148,163,184,0.5); margin-top:0.28rem; line-height:1.3; }

/* Progress bars */
.pv-bar-wrap { background:rgba(30,41,59,0.7); border-radius:20px; height:11px;
  overflow:hidden; border:1px solid rgba(51,65,85,0.4); }
.pv-bar-teal { height:100%; border-radius:20px;
  background:linear-gradient(90deg,#0F766E,#0D9488,#2DD4BF); background-size:200% auto;
  animation:barFill 1.2s ease both, shimmer 3s linear infinite; }
.pv-bar-gold { height:100%; border-radius:20px;
  background:linear-gradient(90deg,#92400E,#CA8A04,#FCD34D); background-size:200% auto;
  animation:barFill 1.4s ease both, shimmer 3s linear infinite; }
.pv-legend { display:flex; justify-content:space-between; font-family:'IBM Plex Mono',monospace;
  font-size:0.59rem; color:rgba(100,116,139,0.8); margin-top:0.28rem; }

/* Script & product cards */
.script-box {
  background:rgba(15,23,42,0.8); border:1px solid rgba(13,148,136,0.28); border-radius:12px;
  padding:1.15rem 1.05rem; font-size:0.88rem; line-height:1.8; color:#CBD5E1;
  white-space:pre-wrap; animation:fadeUp 0.4s ease both;
  font-family:'Inter','Noto Sans Devanagari',sans-serif;
}
.product-card {
  background:rgba(15,23,42,0.8); border:1px solid rgba(202,138,4,0.28);
  border-radius:14px; padding:1.3rem 1.2rem; margin-top:0.7rem;
  animation:fadeUp 0.4s ease both; position:relative; overflow:hidden;
}
.product-card::before {
  content:''; position:absolute; top:0; left:8%; right:8%; height:1px;
  background:linear-gradient(90deg,transparent,rgba(202,138,4,0.38),transparent);
}
.product-card-title {
  font-family:'IBM Plex Mono',monospace; font-size:0.58rem; letter-spacing:0.15em;
  text-transform:uppercase; color:rgba(202,138,4,0.82); margin-bottom:0.85rem;
}
.product-name { font-weight:700; font-size:0.93rem; color:#F1F5F9; margin-bottom:0.18rem; }
.product-detail { font-size:0.78rem; color:rgba(148,163,184,0.68); line-height:1.55; }
.usage-line { font-family:'IBM Plex Mono',monospace; font-size:0.63rem;
  color:rgba(13,148,136,0.85); margin-top:0.22rem; }
.pv-tag {
  display:inline-block; background:rgba(202,138,4,0.11); border:1px solid rgba(202,138,4,0.28);
  color:#FCD34D; font-family:'IBM Plex Mono',monospace; font-size:0.6rem; letter-spacing:0.1em;
  padding:0.18rem 0.65rem; border-radius:8px; margin:0.55rem 0;
}
.disclaimer-box {
  background:rgba(30,41,59,0.5); border:1px solid rgba(71,85,105,0.4); border-radius:8px;
  padding:0.6rem 0.8rem; margin-top:0.7rem; font-size:0.7rem;
  color:rgba(100,116,139,0.9); line-height:1.55;
  font-family:'Inter','Noto Sans Devanagari',sans-serif;
}

/* Severity pills */
.severity-mild { background:rgba(34,197,94,0.1); border:1px solid rgba(34,197,94,0.28);
  color:#86EFAC; border-radius:8px; padding:0.18rem 0.6rem;
  font-family:'IBM Plex Mono',monospace; font-size:0.62rem; display:inline-block; }
.severity-mod  { background:rgba(251,146,60,0.1); border:1px solid rgba(251,146,60,0.28);
  color:#FED7AA; border-radius:8px; padding:0.18rem 0.6rem;
  font-family:'IBM Plex Mono',monospace; font-size:0.62rem; display:inline-block; }
.severity-sev  { background:rgba(239,68,68,0.1); border:1px solid rgba(239,68,68,0.28);
  color:#FCA5A5; border-radius:8px; padding:0.18rem 0.6rem;
  font-family:'IBM Plex Mono',monospace; font-size:0.62rem; display:inline-block; }

/* Blueprint */
.bp-phase { background:rgba(15,23,42,0.6); border:1px solid rgba(51,65,85,0.42);
  border-radius:14px; padding:1.1rem 1.2rem; margin-bottom:0.7rem; animation:fadeUp 0.4s ease both; }
.bp-phase-header { font-family:'Orbitron',monospace; font-size:0.76rem; font-weight:700;
  color:#2DD4BF; letter-spacing:0.05em; margin-bottom:0.35rem; }
.bp-tag { display:inline-block; font-family:'IBM Plex Mono',monospace; font-size:0.56rem;
  letter-spacing:0.1em; text-transform:uppercase; background:rgba(13,148,136,0.11); color:#2DD4BF;
  border:1px solid rgba(13,148,136,0.26); padding:0.14rem 0.55rem; border-radius:8px; margin-bottom:0.65rem; }
.bp-goal { font-size:0.68rem; color:rgba(148,163,184,0.6);
  font-family:'IBM Plex Mono','Noto Sans Devanagari',monospace; line-height:1.5; margin-bottom:0.65rem; }

/* Banners */
.b-success { background:rgba(6,78,59,0.2); border:1px solid rgba(16,185,129,0.28);
  border-radius:10px; padding:0.72rem 0.95rem; font-size:0.81rem; color:#6EE7B7;
  margin:0.45rem 0; animation:fadeUp 0.25s ease both;
  font-family:'Inter','Noto Sans Devanagari',sans-serif; }
.b-warn { background:rgba(120,53,15,0.2); border:1px solid rgba(245,158,11,0.28);
  border-radius:10px; padding:0.72rem 0.95rem; font-size:0.81rem; color:#FDE68A;
  margin:0.45rem 0; animation:fadeUp 0.25s ease both;
  font-family:'Inter','Noto Sans Devanagari',sans-serif; }
.b-danger { background:rgba(127,29,29,0.25); border:1px solid rgba(239,68,68,0.35);
  border-radius:10px; padding:0.72rem 0.95rem; font-size:0.81rem; color:#FCA5A5;
  margin:0.45rem 0; animation:fadeUp 0.25s ease both;
  font-family:'Inter','Noto Sans Devanagari',sans-serif; }
.b-info { background:rgba(15,23,42,0.7); border:1px solid rgba(51,65,85,0.5);
  border-radius:10px; padding:0.72rem 0.95rem; font-size:0.81rem;
  color:rgba(148,163,184,0.8); margin:0.45rem 0;
  font-family:'Inter','Noto Sans Devanagari',sans-serif; }

.sdiv { height:1px; margin:1.2rem 0;
  background:linear-gradient(90deg,transparent,rgba(13,148,136,0.28) 50%,transparent); }
.vhq-footer { text-align:center; font-family:'IBM Plex Mono',monospace; font-size:0.56rem;
  letter-spacing:0.1em; color:rgba(51,65,85,0.75); margin-top:3rem; padding-top:1rem;
  border-top:1px solid rgba(30,41,59,0.8); }
</style>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# HEADER
# ═══════════════════════════════════════════════════════════════
st.markdown(f"""
<div class="vhq-header">
  <div class="vhq-eyebrow">◈ Official AI Copilot · Network Distribution Platform</div>
  <div class="vhq-logo">VHQ · GROWTHLINE</div>
  <div class="vhq-sub">VESTIGE EDITION</div>
  <div class="vhq-tagline">{t("tagline")}</div>
  <div class="vhq-badges">
    <span class="vhq-badge badge-teal">Phase 1 · Core Matrix</span>
    <span class="vhq-badge badge-gold">Vestige Edition</span>
    <span class="vhq-badge badge-slate">{"EN / हिंदी" if L == "en" else "हिंदी / EN"}</span>
  </div>
</div>
""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# NAVIGATION
# ═══════════════════════════════════════════════════════════════
tabs = st.tabs([
    t("nav_script"), t("nav_supp"), t("nav_pv"), t("nav_bp"), t("nav_set")
])


# ═══════════════════════════════════════════════════════════════
# TAB 1 — SCRIPT ENGINE
# ═══════════════════════════════════════════════════════════════
with tabs[0]:
    st.markdown(f'<div class="sl">◈ &nbsp; {t("nav_script")}</div>', unsafe_allow_html=True)
    st.markdown('<div class="gc"><div class="gc-label">— Script Inputs —</div>', unsafe_allow_html=True)

    lead_type = st.selectbox(t("lead_type_lbl"),
        ["🎓 College Student", "💼 Corporate Employee", "🏠 Housewife", "🏪 Small Business Owner"],
        key="lead_type")
    objective = st.selectbox(t("objective_lbl"),
        ["📞 Invite to Zoom Meeting", "📦 Supplement Recommendation", "🚀 Explaining the Business Income Plan"],
        key="objective")
    lead_name = st.text_input(t("name_lbl"), placeholder="e.g. Priya / प्रिया", key="lead_name")
    gen_btn = st.button(t("gen_btn"), type="primary", use_container_width=True, key="gen_btn")
    st.markdown('</div>', unsafe_allow_html=True)

    if gen_btn:
        raw = SCRIPTS.get((lead_type, objective), "")
        if lead_name.strip():
            raw = raw.replace("[Name]", lead_name.strip())
        st.session_state.generated_script = raw

    if st.session_state.generated_script:
        st.markdown(f'<div class="sl">◈ &nbsp; {t("your_script")}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="script-box">{st.session_state.generated_script}</div>', unsafe_allow_html=True)
        st.caption(t("copy_tip"))
        st.code(st.session_state.generated_script, language=None)
        st.markdown(f'<div class="b-success">{t("script_ready")}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="b-info">{t("script_tip")}</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# TAB 2 — SUPPLEMENT FINDER
# ═══════════════════════════════════════════════════════════════
with tabs[1]:
    st.markdown(f'<div class="sl">◈ &nbsp; {t("supp_title")}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="b-info">{"Select a customer health concern to get the right Vestige supplement bundle, PV value, and a ready WhatsApp message." if L=="en" else "ग्राहक की स्वास्थ्य समस्या चुनें और सही सप्लीमेंट बंडल, PV मूल्य और WhatsApp संदेश तुरंत पाएं।"}</div>', unsafe_allow_html=True)

    # ── Live search ─────────────────────────────────────────
    st.markdown('<div class="gc"><div class="gc-label">— Live Search —</div>', unsafe_allow_html=True)
    search_q = st.text_input(t("search_lbl"), placeholder=t("search_ph"), key="supp_search")
    st.markdown('</div>', unsafe_allow_html=True)

    search_results = []
    if search_q.strip():
        search_results = search_supplements(search_q)

    # ── Browse by category ───────────────────────────────────
    st.markdown(f'<div style="text-align:center;font-family:\'IBM Plex Mono\',monospace;font-size:0.6rem;color:rgba(100,116,139,0.6);margin:0.4rem 0">{t("or_browse")}</div>', unsafe_allow_html=True)
    st.markdown('<div class="gc"><div class="gc-label">— Browse by Category —</div>', unsafe_allow_html=True)

    cat_options = CAT_EN if L == "en" else CAT_HI
    cat_map = dict(zip(CAT_HI, CAT_EN)) if L == "hi" else {c: c for c in CAT_EN}

    sel_cat_display = st.selectbox(t("cat_lbl"), cat_options, key="sel_cat")
    sel_cat_en = cat_map.get(sel_cat_display, sel_cat_display)

    cat_concerns = [s for s in SUPP_DB if s["category_en"] == sel_cat_en]
    concern_options = [s["concern_en"] if L == "en" else s["concern_hi"] for s in cat_concerns]
    concern_en_map = {(s["concern_en"] if L == "en" else s["concern_hi"]): s["concern_en"] for s in cat_concerns}

    sel_concern_display = st.selectbox(t("concern_lbl"), concern_options, key="sel_concern")
    sel_concern_en = concern_en_map.get(sel_concern_display, sel_concern_display)

    st.markdown('</div>', unsafe_allow_html=True)

    # ── Age + Severity ───────────────────────────────────────
    st.markdown('<div class="gc"><div class="gc-label">— Customer Profile —</div>', unsafe_allow_html=True)
    col_a, col_b = st.columns(2)
    with col_a:
        cust_age = st.number_input(t("age_lbl"), min_value=1, max_value=100, value=30, step=1, key="cust_age")
    with col_b:
        sev_options = [f"{t('sev_mild')}", f"{t('sev_mod')}", f"{t('sev_sev')}"]
        severity = st.selectbox(t("severity_lbl"), sev_options, key="severity")

    cust_name_inp = st.text_input(t("cust_name_lbl"), placeholder="e.g. Rahul ji / राहुल जी", key="cust_name")
    find_btn = st.button(t("find_btn"), type="primary", use_container_width=True, key="find_btn")
    st.markdown('</div>', unsafe_allow_html=True)

    # ── Under-12 safety gate ─────────────────────────────────
    if cust_age < 12:
        st.markdown(f'<div class="b-danger">{t("age_warn")}</div>', unsafe_allow_html=True)

    # ── Resolve which entry to show ──────────────────────────
    if find_btn and cust_age >= 12:
        # Priority: search results > browse selection
        if search_results:
            entry = search_results[0]
        else:
            entry = get_by_category_concern(sel_cat_en, sel_concern_en)
        st.session_state.supp_result = entry
        st.session_state.supp_concern = sel_concern_display

    # ── Show search matches list if multiple ─────────────────
    if search_q.strip() and search_results and not find_btn:
        st.markdown(f'<div class="b-success">{"Found" if L=="en" else "मिला:"} {len(search_results)} {"result(s). Hit Find button to view." if L=="en" else "परिणाम। खोज बटन दबाएं।"}</div>', unsafe_allow_html=True)
        for r in search_results:
            lbl = r["concern_en"] if L == "en" else r["concern_hi"]
            cat = r["category_en"] if L == "en" else r["category_hi"]
            st.markdown(f'<div style="font-size:0.8rem;color:rgba(45,212,191,0.75);margin:0.2rem 0">◈ {cat} → {lbl}</div>', unsafe_allow_html=True)
    elif search_q.strip() and not search_results:
        st.markdown(f'<div class="b-warn">{t("no_results")}</div>', unsafe_allow_html=True)

    # ── Output card ──────────────────────────────────────────
    if st.session_state.supp_result and cust_age >= 12:
        entry = st.session_state.supp_result
        bundle = entry["bundle"]
        total_pv = sum(p["pv"] for p in bundle)
        concern_label = entry["concern_en"] if L == "en" else entry["concern_hi"]

        # Severity label
        sev_class = "severity-mild"
        if t("sev_mod") in severity:   sev_class = "severity-mod"
        if t("sev_sev") in severity:   sev_class = "severity-sev"

        wa_script = entry["wa_en"] if L == "en" else entry["wa_hi"]
        if cust_name_inp.strip():
            wa_script = wa_script.replace("[Name]", cust_name_inp.strip())
            wa_script = wa_script.replace("[नाम]", cust_name_inp.strip())

        # ── Bundle card ──────────────────────────────────────
        st.markdown(f'<div class="sl">◈ &nbsp; {t("rec_bundle")}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="product-card"><div class="product-card-title">— {concern_label} · <span class="{sev_class}">{severity}</span> · {"Age" if L=="en" else "आयु"} {cust_age} —</div>', unsafe_allow_html=True)

        for prod in bundle:
            name_disp = prod["name"] if L == "en" else prod["name_hi"]
            detail    = prod["detail_en"] if L == "en" else prod["detail_hi"]
            usage     = prod["usage_en"] if L == "en" else prod["usage_hi"]
            st.markdown(f"""
            <div style="margin-bottom:0.9rem;padding-bottom:0.9rem;border-bottom:1px solid rgba(51,65,85,0.3)">
              <div class="product-name">◈ &nbsp;{name_disp}</div>
              <div class="product-detail">{detail}</div>
              <div class="usage-line">{'⏱ Usage:' if L=='en' else '⏱ उपयोग:'} {usage}</div>
              <div style="font-family:'IBM Plex Mono',monospace;font-size:0.62rem;color:rgba(13,148,136,0.75);margin-top:0.18rem">PV: {prod['pv']}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style="display:flex;align-items:center;justify-content:space-between;margin-top:0.2rem">
          <div class="pv-tag">◈ &nbsp; {t("pv_lbl")}: {total_pv} PV</div>
          <div style="font-size:0.73rem;color:rgba(148,163,184,0.5)">{len(bundle)} {"supplements" if L=="en" else "सप्लीमेंट"}</div>
        </div>
        <div class="disclaimer-box">{t("disc_supp")}</div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # ── WhatsApp message ─────────────────────────────────
        st.markdown(f'<div class="sl">◈ &nbsp; {t("wa_msg")}</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="script-box">{wa_script}</div>', unsafe_allow_html=True)
        st.caption(t("copy_tip"))
        st.code(wa_script, language=None)
        st.markdown(f'<div class="b-success">{"✓ Bundle generates" if L=="en" else "✓ बंडल उत्पन्न करता है"} <strong>{total_pv} PV</strong> {"when ordered." if L=="en" else "जब ऑर्डर किया जाता है।"}</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# TAB 3 — PV DASHBOARD
# ═══════════════════════════════════════════════════════════════
with tabs[2]:
    st.markdown(f'<div class="sl">◈ &nbsp; {t("pv_dash_title")}</div>', unsafe_allow_html=True)
    st.markdown('<div class="gc"><div class="gc-label">— Activity Inputs —</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        pv = st.number_input(t("plans_lbl"), min_value=0, max_value=99,
            value=st.session_state.plans_shown, step=1, key="plans_input")
        st.session_state.plans_shown = pv
    with col2:
        wv = st.number_input(t("webinar_lbl"), min_value=0, max_value=99,
            value=st.session_state.webinars, step=1, key="web_input")
        st.session_state.webinars = wv

    mv = st.number_input(t("month_pv_lbl"), min_value=0, max_value=9999,
        value=st.session_state.month_pv, step=50, key="month_input")
    st.session_state.month_pv = mv
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="metric-row">
      <div class="metric-block">
        <div class="metric-val">{st.session_state.plans_shown}</div>
        <div class="metric-lbl">{"Plans Shown" if L=="en" else "प्लान दिखाए"}</div>
      </div>
      <div class="metric-block">
        <div class="metric-val">{st.session_state.webinars}</div>
        <div class="metric-lbl">{"Webinars" if L=="en" else "वेबिनार"}</div>
      </div>
      <div class="metric-block-gold">
        <div class="metric-val-gold">{st.session_state.month_pv}</div>
        <div class="metric-lbl">{"Month PV" if L=="en" else "माह PV"}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f'<div class="sl">◈ &nbsp; {t("bronze_title")}</div>', unsafe_allow_html=True)
    st.markdown('<div class="gc-gold"><div class="gc-label">— Milestone Tracker —</div>', unsafe_allow_html=True)

    tv = st.number_input(t("total_pv_lbl"), min_value=0, max_value=99999,
        value=st.session_state.total_pv, step=100, key="total_input")
    st.session_state.total_pv = tv

    FAST = 4500; STD = 5500
    pf = min(100, round(tv / FAST * 100, 1))
    ps = min(100, round(tv / STD  * 100, 1))

    st.markdown(f"""
    <div style="margin-top:0.4rem">
      <div style="display:flex;justify-content:space-between;margin-bottom:0.22rem">
        <span style="font-family:'IBM Plex Mono',monospace;font-size:0.6rem;color:rgba(13,148,136,0.72)">{t("fast_start")}</span>
        <span style="font-family:'Orbitron',monospace;font-size:0.7rem;color:#2DD4BF">{pf}%</span>
      </div>
      <div class="pv-bar-wrap"><div class="pv-bar-teal" style="width:{pf}%"></div></div>
      <div class="pv-legend"><span>{tv:,} PV</span><span>4,500 PV</span></div>
      <div style="display:flex;justify-content:space-between;margin:0.9rem 0 0.22rem">
        <span style="font-family:'IBM Plex Mono',monospace;font-size:0.6rem;color:rgba(202,138,4,0.78)">{t("std_bronze")}</span>
        <span style="font-family:'Orbitron',monospace;font-size:0.7rem;color:#FCD34D">{ps}%</span>
      </div>
      <div class="pv-bar-wrap"><div class="pv-bar-gold" style="width:{ps}%"></div></div>
      <div class="pv-legend"><span>{tv:,} PV</span><span>5,500 PV</span></div>
    </div>
    """, unsafe_allow_html=True)

    if tv >= STD:
        st.markdown(f'<div class="b-success">{t("b_qualified")}</div>', unsafe_allow_html=True)
    elif tv >= FAST:
        st.markdown(f'<div class="b-success">{t("b_fast")} {STD - tv} PV {"to Standard Bronze." if L=="en" else "स्टैंडर्ड ब्रॉन्ज़ तक।"}</div>', unsafe_allow_html=True)
    elif tv >= 2000:
        st.markdown(f'<div class="b-warn">{t("b_progress")} {FAST - tv} {t("pv_to_go")}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="b-warn">{t("b_start")} {FAST - tv} {t("pv_to_go")}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f'<div class="sl">◈ &nbsp; {t("daily_title")}</div>', unsafe_allow_html=True)
    st.markdown('<div class="gc"><div class="gc-label">— Daily Operating Rhythm —</div>', unsafe_allow_html=True)

    daily_list = t("daily_tasks")
    done = 0
    for i, task in enumerate(daily_list):
        ck = f"daily_{i}"
        if ck not in st.session_state.checks: st.session_state.checks[ck] = False
        val = st.checkbox(task, value=st.session_state.checks[ck], key=f"cb_daily_{i}")
        st.session_state.checks[ck] = val
        if val: done += 1

    if done == len(daily_list):
        st.markdown(f'<div class="b-success">{t("all_done")}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="b-warn">{done}/{len(daily_list)} {t("partial_done")}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# TAB 4 — 6-MONTH BLUEPRINT
# ═══════════════════════════════════════════════════════════════
with tabs[3]:
    st.markdown(f'<div class="sl">◈ &nbsp; {t("bp_title")}</div>', unsafe_allow_html=True)

    for pidx, phase in enumerate(BLUEPRINT):
        ph  = phase["phase_en"]  if L == "en" else phase["phase_hi"]
        ttl = phase["title_en"]  if L == "en" else phase["title_hi"]
        tag = phase["tag_en"]    if L == "en" else phase["tag_hi"]
        gl  = phase["goal_en"]   if L == "en" else phase["goal_hi"]
        tasks = phase["tasks_en"] if L == "en" else phase["tasks_hi"]

        st.markdown(f"""
        <div class="bp-phase">
          <div class="bp-phase-header">◈ &nbsp;{ph} — {ttl}</div>
          <div class="bp-tag">{tag}</div>
          <div class="bp-goal">🎯 {"Goal" if L=="en" else "लक्ष्य"}: {gl}</div>
        </div>
        """, unsafe_allow_html=True)

        done_p = 0
        for tidx, task in enumerate(tasks):
            ck = f"bp_{pidx}_{tidx}"
            if ck not in st.session_state.checks: st.session_state.checks[ck] = False
            val = st.checkbox(task, value=st.session_state.checks[ck], key=f"cb_bp_{pidx}_{tidx}")
            st.session_state.checks[ck] = val
            if val: done_p += 1

        total_t = len(tasks)
        pct_p   = round(done_p / total_t * 100) if total_t else 0
        bar_cls = "pv-bar-gold" if pct_p == 100 else "pv-bar-teal"

        st.markdown(f"""
        <div style="margin:0.5rem 0 1.3rem">
          <div class="pv-bar-wrap"><div class="{bar_cls}" style="width:{pct_p}%"></div></div>
          <div class="pv-legend">
            <span>{done_p}/{total_t} {t("tasks_lbl")}</span>
            <span>{pct_p}% {t("complete_lbl")}</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

        if pct_p == 100:
            st.markdown(f'<div class="b-success">✅ {ph} {t("bp_complete")}</div>', unsafe_allow_html=True)
        st.markdown('<div class="sdiv"></div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="gc" style="text-align:center">
      <div class="gc-label">— {"Core Principle" if L=="en" else "मूल सिद्धांत"} —</div>
      <div style="font-size:0.83rem;color:rgba(148,163,184,0.5);line-height:1.8;
        font-family:'Inter','Noto Sans Devanagari',sans-serif">
        {t("bp_principle")}
      </div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# TAB 5 — SETTINGS
# ═══════════════════════════════════════════════════════════════
with tabs[4]:
    st.markdown(f'<div class="sl">◈ &nbsp; {t("nav_set")}</div>', unsafe_allow_html=True)
    st.markdown('<div class="gc"><div class="gc-label">— Language / भाषा —</div>', unsafe_allow_html=True)

    lang_choice = st.radio(
        t("lang_toggle"),
        ["🇬🇧 English", "🇮🇳 हिंदी"],
        index=0 if L == "en" else 1,
        horizontal=True,
        key="lang_radio",
    )
    if st.button("◈  Apply Language" if L == "en" else "◈  भाषा लागू करें", type="primary", use_container_width=True, key="lang_apply"):
        st.session_state.lang = "en" if "English" in lang_choice else "hi"
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="gc"><div class="gc-label">— Platform Roadmap —</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="font-family:'IBM Plex Mono',monospace;font-size:0.68rem;
      color:rgba(100,116,139,0.8);letter-spacing:0.04em;line-height:2.2">
      ✅ &nbsp; Script Engine &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Phase 1 · Live<br>
      ✅ &nbsp; Supplement Finder &nbsp;&nbsp;&nbsp;&nbsp; Phase 1 · Live<br>
      ✅ &nbsp; PV Dashboard &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Phase 1 · Live<br>
      ✅ &nbsp; 6-Month Blueprint &nbsp;&nbsp;&nbsp;&nbsp; Phase 1 · Live<br>
      ✅ &nbsp; EN / हिंदी Language &nbsp;&nbsp; Phase 1 · Live<br>
      ◈ &nbsp;&nbsp; Supabase Auth &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Phase 2 · Next<br>
      ◈ &nbsp;&nbsp; Persistent Data &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Phase 2 · Next<br>
      ◈ &nbsp;&nbsp; AI Script Engine &nbsp;&nbsp;&nbsp;&nbsp; Phase 3 · Planned<br>
      ◈ &nbsp;&nbsp; Razorpay Paywall &nbsp;&nbsp;&nbsp;&nbsp; Phase 4 · Planned
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="sdiv"></div>', unsafe_allow_html=True)
    if st.button(t("reset_btn"), type="secondary", use_container_width=True, key="reset_btn"):
        lang_save = st.session_state.lang
        for k in list(st.session_state.keys()):
            del st.session_state[k]
        st.session_state.lang = lang_save
        st.rerun()
    st.markdown(f'<div class="b-warn">{t("reset_warn")}</div>', unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════════
st.markdown(f"""
<div class="vhq-footer">
  VHQ · GROWTHLINE &nbsp;·&nbsp; VESTIGE EDITION &nbsp;·&nbsp; PHASE 1 &nbsp;·&nbsp; 2025<br>
  {"Supplement recommendations are for informational purposes only — not medical advice." if L=="en" else "सप्लीमेंट सुझाव केवल जानकारी के लिए हैं — चिकित्सीय सलाह नहीं।"}
</div>
""", unsafe_allow_html=True)
