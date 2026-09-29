import streamlit as st
import pandas as pd
import plotly.express as px
import json
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from data.states  import STATE_DATA
from helpers import setup_page, render_footer, src, note, fmt_amt, render_winner_card, party_color

setup_page("Lok Sabha")

@st.cache_data
def load_lok_sabha_data():
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "lok_sabha.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

LOK_SABHA_DATA = load_lok_sabha_data()

ls_mode = st.sidebar.radio(
    "**View**",
    ["👤  Browse by State", "📊  National Overview", "📈  Analytics / Correlations"],
)

st.title("🗳️ Lok Sabha 2024 — Elected MPs")
st.caption(
    "All 543 elected Members of Parliament — asset declarations, "
    "liabilities, criminal records as per EC affidavits via ADR/MyNeta.")

all_mps = [mp for mps in LOK_SABHA_DATA.values() for mp in mps] if LOK_SABHA_DATA else []

if ls_mode == "👤  Browse by State":
    # National summary stats at the top
    if all_mps:
        total_mps   = len(all_mps)
        with_crime  = sum(1 for m in all_mps if m.get("criminal_cases"))
        crorepati   = sum(1 for m in all_mps
                         if m.get("total_assets_cr") and m["total_assets_cr"] >= 1.0)
        avg_assets  = (sum(m["total_assets_cr"] for m in all_mps
                          if m.get("total_assets_cr")) / total_mps
                      if total_mps else 0)

        st.markdown("### 🇮🇳 National Summary — Lok Sabha 2024")
        n1,n2,n3,n4 = st.columns(4)
        n1.metric("Total MPs",            f"{total_mps}")
        n2.metric("With Criminal Cases",  f"{with_crime} ({int(with_crime/total_mps*100)}%)")
        n3.metric("Crorepati MPs",        f"{crorepati} ({int(crorepati/total_mps*100)}%)")
        n4.metric("Avg Declared Assets",  fmt_amt(avg_assets))
        st.markdown(note(
            "Summary computed from self-declared EC affidavit data. "
            "Figures reflect declarations filed at time of election, "
            "not current values.", "note"), unsafe_allow_html=True)
        st.markdown(
            "📎 Sources: [ADR/MyNeta Lok Sabha 2024](https://myneta.info/LokSabha2024/) | "
            "[ECI Affidavit Archive](https://affidavit.eci.gov.in/)",
            unsafe_allow_html=True)
        st.markdown("---")

    # State selector
    ls_states = sorted(LOK_SABHA_DATA.keys()) if LOK_SABHA_DATA else sorted(STATE_DATA.keys())
    ls_state  = st.selectbox("Select State to View MPs", ls_states)

    if not LOK_SABHA_DATA:
        st.markdown("---")
        st.markdown(note(
            "Lok Sabha MP data has not been fetched yet. "
            "Run fetch_lok_sabha.py first — it fetches all 543 MPs automatically.",
            "unavail"), unsafe_allow_html=True)
    else:
        state_mps = LOK_SABHA_DATA.get(ls_state, [])
        if not state_mps:
            st.markdown(note(f"No MP data found for {ls_state}.", "unavail"), unsafe_allow_html=True)
        else:
            s_crime    = sum(1 for m in state_mps if m.get("criminal_cases"))
            s_cropati  = sum(1 for m in state_mps if m.get("total_assets_cr") and m["total_assets_cr"] >= 1.0)
            s_avg      = (sum(m["total_assets_cr"] for m in state_mps if m.get("total_assets_cr")) / len(state_mps) if state_mps else 0)

            st.markdown(f"### {ls_state} — {len(state_mps)} MPs elected")
            s1,s2,s3,s4 = st.columns(4)
            s1.metric("Total MPs",           f"{len(state_mps)}")
            s2.metric("With Criminal Cases", f"{s_crime}")
            s3.metric("Crorepati MPs",       f"{s_cropati}")
            s4.metric("Avg Assets",          fmt_amt(s_avg))
            st.markdown("---")

            # Filters
            fc1, fc2, fc3 = st.columns([2,1,1])
            with fc1:
                search_ls = st.text_input("🔍 Search MP name or constituency", "")
            with fc2:
                parties_ls = sorted(set(m.get("party","") for m in state_mps if m.get("party")))
                party_ls   = st.selectbox("Filter by Party", ["All"]+parties_ls)
            with fc3:
                sort_ls = st.selectbox("Sort by", ["Default","Assets ↓","Assets ↑","Criminal Cases ↓"])

            filtered_ls = state_mps
            if search_ls:
                s = search_ls.lower()
                filtered_ls = [m for m in filtered_ls if s in m.get("name","").lower() or s in m.get("constituency","").lower()]
            if party_ls != "All":
                filtered_ls = [m for m in filtered_ls if m.get("party","") == party_ls]
            if sort_ls == "Assets ↓":
                filtered_ls = sorted(filtered_ls, key=lambda m: m.get("total_assets_cr") or 0, reverse=True)
            elif sort_ls == "Assets ↑":
                filtered_ls = sorted(filtered_ls, key=lambda m: m.get("total_assets_cr") or 0)
            elif sort_ls == "Criminal Cases ↓":
                filtered_ls = sorted(filtered_ls, key=lambda m: len(m.get("criminal_cases",[])), reverse=True)

            st.markdown(f"Showing **{len(filtered_ls)}** of {len(state_mps)} MPs")
            if not filtered_ls:
                st.info("No MPs match current filter.")
            else:
                for mp in filtered_ls:
                    a = mp.get('total_assets_cr')
                    label = (
                        f"{mp.get('name','—')}  |  {mp.get('party','—')}  |  {mp.get('constituency','—')}  |  "
                        f"Assets: {fmt_amt(a)}" if a else f"{mp.get('name','—')}  |  {mp.get('constituency','—')}"
                    )
                    with st.expander(label, expanded=False):
                        render_winner_card(mp)

elif ls_mode == "📊  National Overview":
    st.markdown("### 🏢 Party-Level Analysis")
    if not all_mps:
        st.warning("Data not loaded.")
    else:
        party_stats = {}
        for mp in all_mps:
            p = mp.get("party", "Independent/Others")
            if p not in party_stats:
                party_stats[p] = {"count": 0, "total_assets": 0.0, "total_crimes": 0}
            
            party_stats[p]["count"] += 1
            party_stats[p]["total_assets"] += (mp.get("total_assets_cr") or 0.0)
            party_stats[p]["total_crimes"] += len(mp.get("criminal_cases") or [])

        # Flatten to list for dataframe
        df_party = pd.DataFrame([
            {
                "Party": k,
                "MPs": v["count"],
                "Total Assets (₹ Cr)": v["total_assets"],
                "Total Criminal Cases": v["total_crimes"],
                "Avg Assets (₹ Cr)": v["total_assets"] / v["count"] if v["count"] > 0 else 0,
                "Avg Cases per MP": v["total_crimes"] / v["count"] if v["count"] > 0 else 0
            }
            for k, v in party_stats.items()
        ]).sort_values("MPs", ascending=False)

        # Plotly chart for Top 10 parties by Wealth
        top_wealth = df_party.sort_values("Total Assets (₹ Cr)", ascending=False).head(10)
        fig = px.bar(top_wealth, x="Party", y="Total Assets (₹ Cr)", title="Top 10 Parties by Total Declared Wealth (₹ Cr)", 
                     color="Party", color_discrete_map={row["Party"]: party_color(row["Party"]) for _, row in top_wealth.iterrows()})
        fig.update_layout(plot_bgcolor="#0e1117", paper_bgcolor="#0e1117", font_color="white", showlegend=False)
        st.plotly_chart(fig, use_container_width=True)
        
        # Plotly chart for Top 10 parties by MP Count
        top_mps = df_party.head(10)
        fig2 = px.bar(top_mps, x="Party", y="MPs", title="Top 10 Parties by Number of MPs",
                     color="Party", color_discrete_map={row["Party"]: party_color(row["Party"]) for _, row in top_mps.iterrows()})
        fig2.update_layout(plot_bgcolor="#0e1117", paper_bgcolor="#0e1117", font_color="white", showlegend=False)
        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("#### Full Party Breakdown")
        st.dataframe(df_party.set_index("Party"), use_container_width=True)

elif ls_mode == "📈  Analytics / Correlations":
    st.markdown("### 📈 Analytics & Correlations")
    if not all_mps:
        st.warning("Data not loaded.")
    else:
        df_scatter = pd.DataFrame([
            {
                "Name": mp.get("name", "Unknown"),
                "Party": mp.get("party", "Independent"),
                "Constituency": mp.get("constituency", "Unknown"),
                "Assets (₹ Cr)": mp.get("total_assets_cr") or 0.0,
                "Criminal Cases": len(mp.get("criminal_cases") or [])
            }
            for mp in all_mps
        ])

        st.markdown("#### Wealth vs. Criminal Cases")
        st.markdown(note("Each dot represents one Member of Parliament. Hover to see details.", "note"), unsafe_allow_html=True)
        
        fig = px.scatter(df_scatter, x="Assets (₹ Cr)", y="Criminal Cases", 
                         color="Party", hover_name="Name", hover_data=["Party", "Constituency"],
                         title="Correlation: Declared Assets vs. Criminal Cases",
                         color_discrete_map={p: party_color(p) for p in df_scatter["Party"].unique()})
        
        # Use a log scale for assets since they vary wildly
        fig.update_xaxes(type="log", title="Assets (₹ Cr) [Log Scale]")
        fig.update_layout(plot_bgcolor="#0e1117", paper_bgcolor="#0e1117", font_color="white")
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Adding a quick statistical summary
        st.markdown("#### Insight Summary")
        top_criminal = df_scatter.sort_values("Criminal Cases", ascending=False).iloc[0]
        top_wealth = df_scatter.sort_values("Assets (₹ Cr)", ascending=False).iloc[0]
        
        c1, c2 = st.columns(2)
        c1.info(f"**Highest Criminal Cases:** {top_criminal['Name']} ({top_criminal['Party']}) - {top_criminal['Criminal Cases']} cases")
        c2.success(f"**Highest Declared Wealth:** {top_wealth['Name']} ({top_wealth['Party']}) - ₹{top_wealth['Assets (₹ Cr)']:,.2f} Cr")

render_footer()
