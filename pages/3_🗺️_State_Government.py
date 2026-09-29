import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from data.states  import STATE_DATA, STATE_ECONOMICS, NCRB_CRIME, NCRB_SOURCE, NCRB_NOTE, myneta_search
from helpers import setup_page, render_footer, src, note, fmt_amt, party_color, render_winner_card

setup_page("State Government")

@st.cache_data
def load_winners_data():
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "winners.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

WINNERS_DATA = load_winners_data()

state_mode = st.sidebar.radio(
    "**View**",
    [
        "🏆  Winner Profiles",
        "👔  Chief Minister Profile",
        "🗺️  State Overview",
        "⚖️  Compare Two States",
    ],
)
selected_state = st.sidebar.selectbox("**Select State**", sorted(STATE_DATA.keys()))

state_info = STATE_DATA[selected_state]
econ_data  = STATE_ECONOMICS.get(selected_state, {})
crime_data = NCRB_CRIME.get(selected_state, {})

# ── Winner Profiles ───────────────────────────────────────
if state_mode == "🏆  Winner Profiles":
    st.title(f"🏆 {selected_state} — Elected Winner Profiles")
    st.caption(
        "Asset declarations, liabilities, criminal records, and income tax "
        "data as self-declared in EC affidavits. Source: ADR/MyNeta + ECI.")

    state_winners_data = WINNERS_DATA.get(selected_state)

    if not state_winners_data:
        st.markdown("---")
        st.markdown(note(
            "Winner data for this state has not been fetched yet. "
            "Run fetch_winners.py first to collect data from MyNeta. "
            "Steps: open Command Prompt → navigate to your folder → "
            "type: python fetch_winners.py", "unavail"),
            unsafe_allow_html=True)
        st.markdown(f"**Alternatively, browse winners directly:**")
        st.markdown(
            f"[👉 Open {selected_state} Winners on MyNeta ↗]"
            f"({state_info['myneta_url']})")
        st.markdown(src("https://myneta.info","ADR/MyNeta"),
            unsafe_allow_html=True)
    else:
        winners   = state_winners_data["winners"]
        elec_year = state_winners_data["election_year"]

        st.markdown(
            f"**Election Year:** {elec_year}  |  "
            f"**Total Winners:** {len(winners)}  |  "
            f"**Source:** ADR/MyNeta + ECI Affidavit Archive")
        st.markdown(note(
            "All data is self-declared by candidates in EC affidavits. "
            "ADR/MyNeta reproduces ECI data without modification. "
            "For complete official affidavit, use the link on each profile. "
            "As per ADR policy, this display is for non-commercial "
            "public interest use only.", "note"),
            unsafe_allow_html=True)
        st.markdown(
            f"📎 Sources: "
            f'<a href="{state_winners_data["source"]}" target="_blank">ADR/MyNeta ↗</a>'
            ' | <a href="https://affidavit.eci.gov.in/" target="_blank">ECI Affidavit Archive ↗</a>',
            unsafe_allow_html=True)
        st.markdown("---")

        # ── Filter / search bar ───────────────────────────
        col_s, col_f, col_sort = st.columns([2,1,1])
        with col_s:
            search = st.text_input(
                "🔍 Search by name or constituency", "")
        with col_f:
            parties = sorted(set(
                w.get("party","") for w in winners if w.get("party")))
            party_f = st.selectbox(
                "Filter by Party", ["All"] + parties)
        with col_sort:
            sort_by = st.selectbox(
                "Sort by",
                ["Default","Assets ↓","Assets ↑",
                 "Liabilities ↓","Criminal Cases ↓"])

        # Apply filters
        filtered = winners
        if search:
            s = search.lower()
            filtered = [w for w in filtered
                        if s in w.get("name","").lower()
                        or s in w.get("constituency","").lower()]
        if party_f != "All":
            filtered = [w for w in filtered
                        if w.get("party","") == party_f]
        if sort_by == "Assets ↓":
            filtered = sorted(filtered,
                key=lambda w: w.get("total_assets_cr") or 0, reverse=True)
        elif sort_by == "Assets ↑":
            filtered = sorted(filtered,
                key=lambda w: w.get("total_assets_cr") or 0)
        elif sort_by == "Liabilities ↓":
            filtered = sorted(filtered,
                key=lambda w: w.get("total_liabilities_cr") or 0,
                reverse=True)
        elif sort_by == "Criminal Cases ↓":
            filtered = sorted(filtered,
                key=lambda w: len(w.get("criminal_cases",[])),
                reverse=True)

        st.markdown(
            f"Showing **{len(filtered)}** of {len(winners)} winners")

        if not filtered:
            st.info("No winners match the current filter.")
        else:
            for w in filtered:
                a = w.get('total_assets_cr')
                label = (
                    f"{w.get('name','—')}  |  "
                    f"{w.get('party','—')}  |  "
                    f"{w.get('constituency','—')}  |  "
                    f"Assets: {fmt_amt(a)}"
                    if a else
                    f"{w.get('name','—')}  |  {w.get('constituency','—')}"
                )
                with st.expander(label, expanded=False):
                    render_winner_card(w)

# ── CM Profile ────────────────────────────────────────────
elif state_mode == "👔  Chief Minister Profile":
    st.title(f"👔 {selected_state} — Chief Minister Profiles")
    st.caption(
        f"Capital: {state_info['capital']}  |  "
        f"Region: {state_info['region']}")
    st.markdown(src(state_info["source_cm"],
        "Wikipedia CM List + ECI Records"), unsafe_allow_html=True)

    cms = state_info["chief_ministers"]
    cm  = st.selectbox(
        "Select Chief Minister",
        cms, format_func=lambda c:
            f"{c['name']} ({c['start']}–{c['end']}) — {c['party']}")

    st.markdown("---")
    c1,c2,c3 = st.columns([2,1,1])
    with c1:
        pcolor = party_color(cm["party"])
        initials = "".join(p[0].upper() for p in cm["name"].split()[:2])
        st.markdown(
            f'<div style="display:inline-flex;align-items:center;gap:16px;">'
            f'<div style="width:70px;height:70px;border-radius:50%;'
            f'background:{pcolor};display:flex;align-items:center;'
            f'justify-content:center;font-size:24px;font-weight:700;'
            f'color:white;">{initials}</div>'
            f'<div><h2 style="margin:0">{cm["name"]}</h2>'
            f'<p style="margin:0;color:#aaa;">{cm["party"]} &nbsp;|&nbsp; '
            f'{cm["start"]}–{cm["end"]} ({cm["end"]-cm["start"]} yr)</p></div>'
            f'</div>', unsafe_allow_html=True)
    with c2:
        st.markdown("**🔍 Asset Declaration**")
        st.markdown(
            f"[Search {cm['name']} on MyNeta ↗]"
            f"({myneta_search(cm['name'])})")
    with c3:
        st.markdown("**📄 Official Affidavit**")
        st.markdown("[ECI Affidavit Portal ↗](https://affidavit.eci.gov.in/)")

    st.markdown(note(
        f"Personal asset and criminal declaration data for {cm['name']} "
        "is available directly from the EC affidavit portal and ADR/MyNeta "
        "— click the links above to view live, officially filed data. "
        "We link directly to ensure you always see the most current and "
        "accurate figures.", "avail"), unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('<div class="section-title">State Economic Performance</div>',
                unsafe_allow_html=True)
    st.markdown(src(
        "https://rbi.org.in/Scripts/AnnualPublications.aspx?"
        "head=State+Finances+%3a+A+Study+of+Budgets",
        "RBI State Finances Report"), unsafe_allow_html=True)
    st.markdown(note(
        "State economic data published by RBI at approximately 4–5 year "
        "intervals aligned with reporting cycles (2005, 2010, 2015, 2019, "
        "2022). Gaps between points reflect source availability.",
        "note"), unsafe_allow_html=True)

    if econ_data:
        tenure_yrs = list(range(cm["start"], cm["end"]+1))
        def ft(d): return {yr:v for yr,v in d.items() if yr in tenure_yrs}
        gsdp  = ft(econ_data.get("gsdp_lakh_cr",{}))
        bud   = ft(econ_data.get("state_budget_cr",{}))
        fd    = ft(econ_data.get("fiscal_deficit_pct",{}))
        debt  = ft(econ_data.get("debt_gdp_pct",{}))
        crime = ft(crime_data)

        tabs = st.tabs(["📈 GSDP","💰 Budget","🏛️ Fiscal Deficit",
                        "💳 Debt","🚨 Crime Rate"])
        for tab, data_d, y_label, title_sfx, color, benchmark in [
            (tabs[0], gsdp,  "GSDP (₹ Lakh Cr)", "GSDP at Current Prices","#22c55e", None),
            (tabs[1], bud,   "Budget (₹ Cr)",     "State Budget Size",      "#3b82f6", None),
            (tabs[2], fd,    "Fiscal Deficit %",   "Fiscal Deficit % GSDP", "#a855f7", 3.0),
            (tabs[3], debt,  "Debt % GSDP",        "Outstanding Debt",      "#ef4444", None),
            (tabs[4], crime, "Crimes/Lakh Pop",    "IPC Crimes per Lakh",   "#f97316", None),
        ]:
            with tab:
                if data_d:
                    df = pd.DataFrame({
                        "Year": list(data_d.keys()),
                        y_label: list(data_d.values()),
                    })
                    fig = px.bar(df, x="Year", y=y_label,
                        title=f"{selected_state} — {title_sfx}",
                        color=y_label,
                        color_continuous_scale="Blues")
                    if benchmark:
                        fig.add_hline(y=benchmark, line_dash="dash",
                            line_color="orange",
                            annotation_text=f"{benchmark}% Benchmark")
                    fig.update_layout(plot_bgcolor="#0e1117",
                        paper_bgcolor="#0e1117",font_color="white")
                    st.plotly_chart(fig, use_container_width=True)
                    if tab == tabs[4]:
                        st.markdown(note(NCRB_NOTE,"note"),
                            unsafe_allow_html=True)
                        st.markdown(src(NCRB_SOURCE,"NCRB"),
                            unsafe_allow_html=True)
                else:
                    st.markdown(note(
                        f"Data not available for {cm['name']}'s tenure "
                        f"({cm['start']}–{cm['end']}) in this dataset. "
                        "Access directly from source.",
                        "unavail"), unsafe_allow_html=True)
    else:
        st.markdown(note(
            f"Economic data for {selected_state} not in dataset. "
            "Access from RBI State Finances Report.", "unavail"),
            unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### All Chief Ministers")
    cm_df = pd.DataFrame([{
        "Name": c["name"], "Party": c["party"],
        "From": c["start"], "To": c["end"],
        "Duration (Yrs)": c["end"]-c["start"],
    } for c in cms])
    st.dataframe(cm_df, use_container_width=True, hide_index=True)
    st.markdown(src(state_info["source_cm"],"Wikipedia + ECI"),
        unsafe_allow_html=True)

# ── State Overview ────────────────────────────────────────
elif state_mode == "🗺️  State Overview":
    st.title(f"🗺️ {selected_state} — State Overview")
    st.caption(
        f"Capital: {state_info['capital']}  |  "
        f"Region: {state_info['region']}")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Political History")
        cms = state_info["chief_ministers"]
        party_counts = {}
        for c in cms:
            party_counts[c["party"]] = \
                party_counts.get(c["party"],0) + (c["end"]-c["start"])
        df_party = pd.DataFrame({
            "Party": list(party_counts.keys()),
            "Years in Power": list(party_counts.values()),
        })
        fig_p = px.pie(df_party, names="Party", values="Years in Power",
            title="Years in Power by Party", hole=0.4,
            color_discrete_sequence=px.colors.qualitative.Set3)
        fig_p.update_layout(plot_bgcolor="#0e1117",
            paper_bgcolor="#0e1117",font_color="white")
        st.plotly_chart(fig_p, use_container_width=True)
        st.markdown(src(state_info["source_cm"],"Wikipedia + ECI"),
            unsafe_allow_html=True)

    with col2:
        st.markdown("### Economic Snapshot")
        if econ_data and econ_data.get("gsdp_lakh_cr"):
            gsdp = econ_data["gsdp_lakh_cr"]
            yrs  = sorted(gsdp.keys())
            if len(yrs)>=2:
                growth = ((gsdp[yrs[-1]]-gsdp[yrs[0]])/gsdp[yrs[0]]*100)
                st.metric(f"GSDP {yrs[0]}",  f"₹{gsdp[yrs[0]]:.2f} L Cr")
                st.metric(f"GSDP {yrs[-1]}", f"₹{gsdp[yrs[-1]]:.2f} L Cr",
                    delta=f"{growth:+.1f}% growth over period")
            df_g = pd.DataFrame({
                "Year": list(gsdp.keys()),
                "GSDP (₹ L Cr)": list(gsdp.values()),
            })
            fig_g = px.line(df_g, x="Year", y="GSDP (₹ L Cr)",
                title="GSDP Trend", markers=True,
                color_discrete_sequence=["#22c55e"])
            fig_g.update_layout(plot_bgcolor="#0e1117",
                paper_bgcolor="#0e1117",font_color="white")
            st.plotly_chart(fig_g, use_container_width=True)
            st.markdown(src(
                "https://rbi.org.in/Scripts/AnnualPublications.aspx?"
                "head=State+Finances+%3a+A+Study+of+Budgets",
                "RBI State Finances"), unsafe_allow_html=True)
        else:
            st.markdown(note(
                f"GSDP data for {selected_state} not in dataset.",
                "unavail"), unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🔍 Browse All MLAs & Candidates on MyNeta")
    st.markdown(note(
        "Asset declarations, criminal records, and education qualifications "
        "for all MLAs and candidates are available on the MyNeta portal — "
        "sourced directly from EC affidavits.", "avail"),
        unsafe_allow_html=True)
    st.markdown(
        f"**[👉 Open {selected_state} on MyNeta ↗]"
        f"({state_info['myneta_url']})**")
    st.markdown(src("https://myneta.info","ADR/MyNeta — ADR Election Watch"),
        unsafe_allow_html=True)

# ── Compare States ────────────────────────────────────────
else:
    st.title("⚖️ Compare Two States")
    all_states = sorted(STATE_DATA.keys())
    cs1,cs2 = st.columns(2)
    with cs1: s1 = st.selectbox("State 1", all_states, index=0)
    with cs2: s2 = st.selectbox("State 2", all_states,
        index=min(5,len(all_states)-1))
    if s1==s2:
        st.warning("Please select two different states.")
        st.stop()

    e1 = STATE_ECONOMICS.get(s1,{})
    e2 = STATE_ECONOMICS.get(s2,{})
    st.markdown("---")

    st.markdown('<div class="section-title">GSDP Comparison</div>',
                unsafe_allow_html=True)
    st.markdown(src(
        "https://rbi.org.in/Scripts/AnnualPublications.aspx?"
        "head=State+Finances+%3a+A+Study+of+Budgets",
        "RBI State Finances"), unsafe_allow_html=True)
    fig_g = go.Figure()
    for state,econ,color in [(s1,e1,"#3b82f6"),(s2,e2,"#f97316")]:
        gsdp = econ.get("gsdp_lakh_cr",{})
        if gsdp:
            fig_g.add_trace(go.Scatter(
                x=list(gsdp.keys()), y=list(gsdp.values()),
                name=state,mode="lines+markers",
                line=dict(color=color,width=2)))
    fig_g.update_layout(title="GSDP at Current Prices (₹ Lakh Crore)",
        plot_bgcolor="#0e1117",paper_bgcolor="#0e1117",font_color="white")
    st.plotly_chart(fig_g, use_container_width=True)

    st.markdown('<div class="section-title">Fiscal Deficit Comparison</div>',
                unsafe_allow_html=True)
    fig_fd = go.Figure()
    for state,econ,color in [(s1,e1,"#3b82f6"),(s2,e2,"#f97316")]:
        fd = econ.get("fiscal_deficit_pct",{})
        if fd:
            fig_fd.add_trace(go.Scatter(
                x=list(fd.keys()), y=list(fd.values()),
                name=state,mode="lines+markers",
                line=dict(color=color,width=2)))
    fig_fd.add_hline(y=3.0,line_dash="dash",
        line_color="gray",annotation_text="3% Benchmark")
    fig_fd.update_layout(title="Fiscal Deficit as % of GSDP",
        plot_bgcolor="#0e1117",paper_bgcolor="#0e1117",font_color="white")
    st.plotly_chart(fig_fd, use_container_width=True)

    if NCRB_CRIME.get(s1) and NCRB_CRIME.get(s2):
        st.markdown('<div class="section-title">Crime Rate Comparison</div>',
                    unsafe_allow_html=True)
        st.markdown(src(NCRB_SOURCE,"NCRB — Crime in India"),
            unsafe_allow_html=True)
        fig_c = go.Figure()
        for state,color in [(s1,"#3b82f6"),(s2,"#f97316")]:
            cr = NCRB_CRIME.get(state,{})
            if cr:
                fig_c.add_trace(go.Scatter(
                    x=list(cr.keys()),y=list(cr.values()),
                    name=state,mode="lines+markers",
                    line=dict(color=color,width=2)))
        fig_c.update_layout(
            title="IPC Cognisable Crimes per Lakh Population",
            plot_bgcolor="#0e1117",paper_bgcolor="#0e1117",
            font_color="white")
        st.plotly_chart(fig_c, use_container_width=True)
        st.markdown(note(NCRB_NOTE,"note"), unsafe_allow_html=True)

    st.markdown('<div class="section-title">Political Landscape</div>',
                unsafe_allow_html=True)
    pc1,pc2 = st.columns(2)
    for col,state in [(pc1,s1),(pc2,s2)]:
        with col:
            st.markdown(f"**{state}**")
            cms = STATE_DATA[state]["chief_ministers"]
            party_counts = {}
            for c in cms:
                party_counts[c["party"]] = \
                    party_counts.get(c["party"],0) + (c["end"]-c["start"])
            df_pp = pd.DataFrame({
                "Party": list(party_counts.keys()),
                "Years": list(party_counts.values()),
            })
            fig_pp = px.pie(df_pp, names="Party", values="Years",
                hole=0.4,
                color_discrete_sequence=px.colors.qualitative.Set3)
            fig_pp.update_layout(plot_bgcolor="#0e1117",
                paper_bgcolor="#0e1117",font_color="white",
                showlegend=True,height=300)
            st.plotly_chart(fig_pp, use_container_width=True)

    st.markdown(note(
        "Data availability varies by state. Economic data reflects RBI "
        "State Finances publication cycles. Gaps reflect source "
        "availability, not omission.", "note"), unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────

render_footer()
