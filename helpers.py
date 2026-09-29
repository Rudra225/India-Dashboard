import streamlit as st
import pandas as pd
import requests
import json
from datetime import datetime

def build_html_table(df):
    html = '<div style="overflow-x:auto; margin-bottom: 20px;"><table style="width:100%; border-collapse: collapse; font-family: sans-serif; font-size: 14px; text-align: left;">'
    
    # Headers
    html += '<thead><tr style="border-bottom: 2px solid #555;">'
    for col in df.columns:
        html += f'<th style="padding: 8px; font-weight: 600;">{col}</th>'
    html += '</tr></thead><tbody>'
    
    # Rows
    for i, row in df.iterrows():
        bg = "rgba(0,0,0,0.05)" if i % 2 == 0 else "transparent"
        html += f'<tr style="background-color: {bg}; border-bottom: 1px solid #444;">'
        for val in row:
            val_str = str(val).replace('\n', '<br>')
            html += f'<td style="padding: 8px; vertical-align: top;">{val_str}</td>'
        html += '</tr>'
        
    html += '</tbody></table></div>'
    return html

def fmt_cell(amount, detail):
    a = fmt_amt(amount)
    if not detail: return a
    return detail if a == "—" else f"**{a}**<br><span style='font-size:0.9em;color:#666;'>{detail}</span>"

def setup_page(title):
    st.set_page_config(
        page_title=f"{title} | India Governance & Economic Dashboard",
        page_icon="🇮🇳", layout="wide",
        initial_sidebar_state="expanded",
    )
    st.markdown('''
    <style>
    .source-tag{font-size:11px;color:#aaa;font-style:italic;border-left:3px solid #f97316;
      padding-left:8px;margin:4px 0 10px 0;line-height:1.6;}
    .note-box{background:#1c1c2e;border-left:4px solid #f0c040;padding:10px 14px;
      border-radius:4px;font-size:13px;color:#ccc;margin:8px 0;}
    .avail-box{background:#0f2027;border-left:4px solid #22c55e;padding:10px 14px;
      border-radius:4px;font-size:13px;color:#ccc;margin:8px 0;}
    .unavail-box{background:#1a0a00;border-left:4px solid #ef4444;padding:10px 14px;
      border-radius:4px;font-size:13px;color:#ccc;margin:8px 0;}
    .section-title{font-size:18px;font-weight:700;color:#f97316;
      border-bottom:1px solid #333;padding-bottom:6px;margin:16px 0 10px 0;}
    .winner-card{background:#111827;border:1px solid #1f2937;border-radius:12px;
      padding:20px;margin-bottom:16px;}
    .built-by{font-size:12px;color:#888;text-align:right;padding:4px 8px;}
    </style>
    ''', unsafe_allow_html=True)
    
    st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg", width=55)
    st.sidebar.title("🇮🇳 India Governance")
    st.sidebar.caption("Political accountability & economic transparency since 1947")
    st.sidebar.markdown("---")

def render_footer():
    st.sidebar.markdown("---")
    st.sidebar.markdown("**📚 Verified Data Sources**")
    st.sidebar.markdown('''
    - [indiabudget.gov.in](https://www.indiabudget.gov.in)
    - [cag.gov.in](https://cag.gov.in/en/audit-report)
    - [rbi.org.in](https://rbi.org.in/Scripts/AnnualPublications.aspx?head=State+Finances+%3a+A+Study+of+Budgets)
    - [data.worldbank.org](https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG?locations=IN)
    - [fred.stlouisfed.org](https://fred.stlouisfed.org/series/AEXINUS)
    - [affidavitarchive.nic.in](https://affidavit.eci.gov.in/)
    - [myneta.info](https://myneta.info)
    - [ncrb.gov.in](https://ncrb.gov.in)
    - [mospi.gov.in](https://mospi.gov.in/consumer-price-index)
    ''')
    st.sidebar.markdown("---")
    st.sidebar.markdown('<div style="font-size:11px;color:#888;">🛠️ Built by <b>Sudarshan Singh Rathore</b></div>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown('''
    <div style="text-align:center;color:#555;font-size:11px;line-height:1.8;">
    India Governance &amp; Economic Dashboard &nbsp;|&nbsp;
    All data from verified official and independent sources.<br>
    indiabudget.gov.in &nbsp;·&nbsp; CAG &nbsp;·&nbsp; RBI &nbsp;·&nbsp;
    MoSPI &nbsp;·&nbsp; ECI &nbsp;·&nbsp; ADR/MyNeta &nbsp;·&nbsp;
    World Bank &nbsp;·&nbsp; FRED &nbsp;·&nbsp; DPIIT &nbsp;·&nbsp; NCRB<br>
    <i>Built for academic and public-interest transparency. Not affiliated with
    any political party or government body.</i><br>
    <i>Winner data: self-declared EC affidavits via ADR/MyNeta —
    non-commercial use as per ADR policy.</i><br><br>
    <b style="color:#777;">Built by Sudarshan Singh Rathore</b>
    &nbsp;·&nbsp; <span style="color:#555;">© 2025 All rights reserved.</span>
    </div>''', unsafe_allow_html=True)

def src(url, label="Source"):
    return f'<div class="source-tag">📎 {label}: <a href="{url}" target="_blank">{url}</a></div>'

def note(text, kind="note"):
    css  = {"note":"note-box","avail":"avail-box","unavail":"unavail-box"}
    icon = {"note":"ℹ️","avail":"✅","unavail":"⚠️"}
    return f'<div class="{css[kind]}">{icon[kind]} {text}</div>'

def fmt_amt(cr):
    """Format a crore value into human-readable Indian units."""
    if cr is None: return "—"
    if cr == 0:    return "Nil"
    rupees = cr * 10_000_000
    if rupees < 1000:
        return f"₹{rupees:,.0f}"
    if rupees < 100_000:
        return f"₹{rupees:,.0f}"
    if rupees < 10_000_000:
        lakhs = rupees / 100_000
        return f"₹{lakhs:.2f} Lakh"
    return f"₹{cr:.2f} Cr"

def party_color(party):
    p = (party or "").upper()
    if "BJP"  in p: return "#f97316"
    if "INC"  in p or "CONGRESS" in p: return "#3b82f6"
    if "AAP"  in p: return "#22c55e"
    if "TMC"  in p: return "#06b6d4"
    if "CPI"  in p or "CPM" in p: return "#ef4444"
    if "SP"   in p: return "#e11d48"
    if "BSP"  in p: return "#7c3aed"
    if "DMK"  in p: return "#0ea5e9"
    if "YSRCP"in p or "YSR" in p: return "#eab308"
    if "BJD"  in p: return "#10b981"
    if "TRS"  in p or "BRS" in p: return "#f59e0b"
    if "JMM"  in p: return "#84cc16"
    if "NCP"  in p: return "#6366f1"
    if "SHS"  in p or "SHIV" in p: return "#f43f5e"
    return "#64748b"


@st.cache_data(ttl=86400, show_spinner=False)
def fetch_photo(photo_url):
    try:
        resp = requests.get(photo_url, headers={"Referer": "https://myneta.info/", "User-Agent": "Mozilla/5.0"}, timeout=5)
        if resp.status_code == 200 and len(resp.content) > 1000:
            return resp.content
    except Exception:
        pass
    return None
# WINNER CARD RENDERER
# ════════════════════════════════════════════════════════════════
def render_winner_card(w):
    party      = w.get("party","")
    name       = w.get("name","Unknown")
    const      = w.get("constituency","")
    age        = w.get("age")
    edu        = w.get("education","")
    profession = w.get("profession","")
    photo_url  = w.get("photo_url")
    total_a    = w.get("total_assets_cr")
    total_l    = w.get("total_liabilities_cr")
    crimes     = w.get("criminal_cases",[])
    income_tax = w.get("income_tax",[])
    movable    = w.get("movable_assets",[])
    immovable  = w.get("immovable_assets",[])
    liab_det   = w.get("liabilities_detail",[])
    tier2      = w.get("tier2_available", False)
    aff_url    = w.get("affidavit_url","https://myneta.info")
    pcolor     = party_color(party)

    # ── Photo / Avatar + Header ───────────────────────────────
    c_photo, c_info = st.columns([1, 4])
    with c_photo:
        if photo_url:
            img_data = fetch_photo(photo_url)
            if img_data:
                st.image(img_data, width=95)
            else:
                initials = "".join(p[0].upper() for p in name.split()[:2])
                st.markdown(
                    f'<div style="width:90px;height:90px;border-radius:50%;background:{pcolor};'
                    f'display:flex;align-items:center;justify-content:center;'
                    f'font-size:26px;font-weight:700;color:white;">{initials}</div>',
                    unsafe_allow_html=True)
        else:
            initials = "".join(p[0].upper() for p in name.split()[:2])
            st.markdown(
                f'<div style="width:90px;height:90px;border-radius:50%;background:{pcolor};'
                f'display:flex;align-items:center;justify-content:center;'
                f'font-size:26px;font-weight:700;color:white;">{initials}</div>',
                unsafe_allow_html=True)

    with c_info:
        st.markdown(f"### {name}")
        meta = []
        if party:      meta.append(f"`{party}`")
        if const:      meta.append(f"`{const}`")
        if age:        meta.append(f"`Age {age}`")
        if edu:        meta.append(f"`{edu}`")
        if profession: meta.append(f"`{profession}`")
        st.markdown("  ".join(meta))

        if crimes:
            st.markdown(
                f'<span style="background:#ef4444;color:white;padding:2px 10px;'
                f'border-radius:10px;font-size:12px;font-weight:600;">'
                f'⚖️ {len(crimes)} Criminal Case(s) Declared</span>',
                unsafe_allow_html=True)
        else:
            st.markdown(
                f'<span style="background:#22c55e;color:white;padding:2px 10px;'
                f'border-radius:10px;font-size:12px;font-weight:600;">'
                f'✅ No Criminal Cases Declared</span>',
                unsafe_allow_html=True)

    st.markdown("")

    # ── Top metrics ───────────────────────────────────────────
    m1, m2, m3 = st.columns(3)
    m1.metric("Total Declared Assets",      fmt_amt(total_a))
    m2.metric("Total Declared Liabilities", fmt_amt(total_l) if total_l else "Nil")
    net = (total_a or 0) - (total_l or 0)
    m3.metric("Net Worth (Self-Declared)",  fmt_amt(net) if total_a else "—")

    # ── Detail tabs ───────────────────────────────────────────
    t1, t2, t3, t4 = st.tabs(["💰 Assets", "📉 Liabilities", "⚖️ Criminal Cases", "🧾 Income Tax"])

    # Assets
    with t1:
        st.markdown(
            "📎 Sources: "
            f'<a href="{aff_url}" target="_blank">EC Affidavit (MyNeta) ↗</a>'
            ' | <a href="https://affidavit.eci.gov.in/" target="_blank">ECI Affidavit Archive ↗</a>',
            unsafe_allow_html=True)
        if tier2 and movable:
            st.markdown("**Movable Assets** *(cash, bank deposits, vehicles, bonds, jewellery)*")
            st.markdown(note(
                "Vehicle names, bank account details, and asset descriptions "
                "reproduced as declared in EC affidavit.", "note"), unsafe_allow_html=True)
            df_m = pd.DataFrame([{
                "Description / Item": i["description"],
                "Self":               fmt_cell(i.get("self"), i.get("self_detail")),
                "Spouse":             fmt_cell(i.get("spouse"), i.get("spouse_detail")),
                "Dep 1":              fmt_amt(i.get("dep1")),
                "Dep 2":              fmt_amt(i.get("dep2")),
                "Total":              fmt_amt(i.get("amount_cr")),
            } for i in movable])
            st.markdown(build_html_table(df_m), unsafe_allow_html=True)
            st.caption("ℹ️ Total includes Self + Spouse + HUF + Dependents as declared in EC affidavit.")
        else:
            st.markdown(note(
                "Detailed movable asset breakdown not parsed for this candidate. "
                "Total declared figure shown above is from summary page.",
                "unavail"), unsafe_allow_html=True)

        if tier2 and immovable:
            st.markdown("**Immovable Assets** *(land, buildings — with location)*")
            df_i = pd.DataFrame([{
                "Type":           i["description"],
                "Self":           fmt_cell(i.get("self"), i.get("self_detail")),
                "Spouse":         fmt_cell(i.get("spouse"), i.get("spouse_detail")),
                "Dep 1":          fmt_amt(i.get("dep1")),
                "Dep 2":          fmt_amt(i.get("dep2")),
                "Total":          fmt_amt(i.get("amount_cr")),
            } for i in immovable])
            st.markdown(build_html_table(df_i), unsafe_allow_html=True)

        st.markdown(
            f'<div class="note-box" style="margin-top:10px;">ℹ️ '
            f'For complete official affidavit including all asset details: '
            f'<a href="{aff_url}" target="_blank">View on MyNeta ↗</a> &nbsp;|&nbsp; '
            f'<a href="https://affidavit.eci.gov.in/" target="_blank">'
            f'ECI Affidavit Archive ↗</a></div>',
            unsafe_allow_html=True)

    # Liabilities
    with t2:
        st.markdown(
            "📎 Sources: "
            f'<a href="{aff_url}" target="_blank">EC Affidavit (MyNeta) ↗</a>'
            ' | <a href="https://affidavit.eci.gov.in/" target="_blank">ECI Affidavit Archive ↗</a>',
            unsafe_allow_html=True)
        if tier2 and liab_det:
            st.markdown("**Liabilities Breakdown** *(bank-wise / source-wise)*")
            st.markdown(note(
                "Bank names and loan sources reproduced as declared in EC affidavit.",
                "note"), unsafe_allow_html=True)
            df_l = pd.DataFrame([{
                "Loan Source / Bank": i["description"],
                "Self":               fmt_cell(i.get("self"), i.get("self_detail", "")),
                "Spouse":             fmt_cell(i.get("spouse"), i.get("spouse_detail", "")),
                "Dep 1":              fmt_cell(i.get("dep1"), i.get("dep1_detail", "")),
                "Dep 2":              fmt_cell(i.get("dep2"), i.get("dep2_detail", "")),
                "Total":              fmt_amt(i.get("amount_cr")),
            } for i in liab_det])
            st.markdown(build_html_table(df_l), unsafe_allow_html=True)
        elif not total_l or total_l == 0:
            st.markdown(note(
                "Nil liabilities declared in EC affidavit.", "avail"),
                unsafe_allow_html=True)
        else:
            st.markdown(note(
                "Detailed liability breakdown not parsed. "
                f"Total liabilities: {fmt_amt(total_l)}. "
                "Full breakdown at official affidavit link.",
                "unavail"), unsafe_allow_html=True)

        st.markdown(
            f'<div class="note-box">ℹ️ Full affidavit: '
            f'<a href="{aff_url}" target="_blank">View on MyNeta ↗</a></div>',
            unsafe_allow_html=True)

    # Criminal
    with t3:
        st.markdown(
            "📎 Sources: "
            f'<a href="{aff_url}" target="_blank">EC Affidavit (MyNeta) ↗</a>'
            ' | <a href="https://affidavit.eci.gov.in/" target="_blank">ECI Affidavit Archive ↗</a>',
            unsafe_allow_html=True)
        if crimes:
            st.markdown(note(
                "Criminal cases declared by the candidate in their EC affidavit. "
                "IPC sections and descriptions reproduced as filed.",
                "note"), unsafe_allow_html=True)
            df_c = pd.DataFrame([{
                "IPC / Section":  c.get("section","—"),
                "Description":    c.get("description","—"),
                "No. of Charges": c.get("count","—"),
            } for c in crimes])
            st.markdown(build_html_table(df_c), unsafe_allow_html=True)
            st.markdown(note(
                "⚠️ These are self-declared cases. Charges listed are not "
                "convictions. For full legal status refer to EC affidavit "
                "and respective court records.", "note"), unsafe_allow_html=True)
        else:
            st.markdown(note(
                "No criminal cases declared by this candidate in their EC affidavit.",
                "avail"), unsafe_allow_html=True)

        st.markdown(
            f'<div class="note-box">ℹ️ Verify: '
            f'<a href="{aff_url}" target="_blank">EC Affidavit on MyNeta ↗</a>'
            f'</div>', unsafe_allow_html=True)

    # Income Tax
    with t4:
        st.markdown(
            "📎 Sources: "
            f'<a href="{aff_url}" target="_blank">EC Affidavit (MyNeta) ↗</a>'
            ' | <a href="https://affidavit.eci.gov.in/" target="_blank">ECI Affidavit Archive ↗</a>',
            unsafe_allow_html=True)
        if income_tax:
            st.markdown("**Income Declared in IT Returns** *(as per EC affidavit filing)*")
            df_it = pd.DataFrame([{
                "Financial Year":   it["fy"],
                "Filed By":         it.get("relation","Self").title(),
                "Income Declared":  fmt_amt(it.get("amount_cr")),
            } for it in income_tax])
            st.markdown(build_html_table(df_it), unsafe_allow_html=True)
        else:
            st.markdown(note(
                "Income tax details could not be parsed from affidavit. "
                "Available at official affidavit link below.", "unavail"),
                unsafe_allow_html=True)

        st.markdown(
            f'<div class="note-box">ℹ️ Full affidavit: '
            f'<a href="{aff_url}" target="_blank">View on MyNeta ↗</a> '
            f'&nbsp;|&nbsp; For most accurate data always verify at: '
            f'<a href="https://myneta.info" target="_blank">myneta.info ↗</a>'
            f'</div>', unsafe_allow_html=True)

    # Bottom disclaimer
    st.markdown(note(
        "All data self-declared by candidate in EC affidavit. "
        "ADR/MyNeta does not modify ECI data. This display is for "
        "transparency and academic reference. "
        f'<a href="{aff_url}" target="_blank">'
        "Click here to view original affidavit ↗</a>",
        "note"), unsafe_allow_html=True)
    st.markdown("---")



