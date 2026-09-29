import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from data.leaders import ALL_LEADERS, PRIME_MINISTERS, FINANCE_MINISTERS
from data.budget  import UNION_BUDGET_DATA, SECTOR_BUDGET, get_budget_for_tenure, DISPLAY_AS_CRORE_BEFORE
from data.assets  import LEADER_ASSETS, PARTY_ASSETS
from data.economy import ECONOMY_DATA, get_economy_for_tenure, purchasing_power_of_100
from helpers import setup_page, render_footer, src, note, fmt_amt, party_color

setup_page("Union Government")

union_mode = st.sidebar.radio(
    "**View**",
    ["📊  Leader Analysis", "⚖️  Compare Leaders", "📅  Historical Timeline"],
)
if union_mode == "📊  Leader Analysis" or union_mode == "⚖️  Compare Leaders":
    role_filter = st.sidebar.radio(
        "**Filter by Role**",
        ["All Leaders", "Prime Ministers", "Finance Ministers"],
    )


def filtered_leaders():
    if role_filter == "Prime Ministers":   return PRIME_MINISTERS
    if role_filter == "Finance Ministers": return FINANCE_MINISTERS
    return ALL_LEADERS

# ── Leader Analysis ───────────────────────────────────────
if union_mode == "📊  Leader Analysis":
    st.title("🏛️ Union Government — Leader Analysis")
    st.caption("Tenure-wise political, budgetary, and macroeconomic profile.")

    leaders_dict = filtered_leaders()
    leader_key   = st.selectbox("Select Leader", list(leaders_dict.keys()))
    leader       = leaders_dict[leader_key]
    start_yr, end_yr = leader["start_year"], leader["end_year"]

    st.markdown("---")
    c1, c2, c3 = st.columns([2.5, 1, 1])
    with c1:
        st.markdown(f"## {leader['name']}")
        st.markdown(
            f"**Role:** {leader['role']}  |  **Party:** {leader['party']}")
        st.markdown(
            f"**Tenure:** {start_yr} – {end_yr}  ({end_yr-start_yr} year(s))")
        st.markdown(leader["summary"])
        st.markdown(src(leader["source"], "Official Record"), unsafe_allow_html=True)
    with c2:
        pwr = purchasing_power_of_100(start_yr, min(end_yr,2024))
        if pwr:
            st.metric(f"₹100 from {start_yr} buys", f"₹{pwr}",
                      delta=f"Purchasing Power by {min(end_yr,2024)}", delta_color="inverse")
    with c3:
        s = ECONOMY_DATA.get(start_yr,{})
        e = ECONOMY_DATA.get(min(end_yr,2024),{})
        if s.get("inr_usd") and e.get("inr_usd"):
            chg = e["inr_usd"] - s["inr_usd"]
            st.metric("INR/USD at tenure end", f"₹{e['inr_usd']}",
                      delta=f"{chg:+.2f} vs start", delta_color="inverse")

    st.markdown("---")
    tab1,tab2,tab3,tab4 = st.tabs(["💰 Budget","🏦 Assets","📈 Economy","📋 Summary"])

    with tab1:
        st.markdown('<div class="section-title">Union Budget — Allocation vs Expenditure</div>',
                    unsafe_allow_html=True)
        st.markdown(
            "📎 Sources: [IndiabudGet.gov.in](https://www.indiabudget.gov.in) | "
            "[CAG](https://cag.gov.in/en/audit-report)",
            unsafe_allow_html=True)
        bd    = get_budget_for_tenure(start_yr, end_yr)
        valid = {yr: v for yr, v in bd.items() if v.get("spent")}
        has_est = any(v.get("data_type")=="estimate_only" for v in valid.values())
        has_ver = any(v.get("data_type")=="verified"      for v in valid.values())
        if has_est and has_ver:
            st.markdown(note(
                "This tenure spans both verified data (1994 onwards, from "
                "CivicDataLab/Open Budgets India) and budget estimates only "
                "(pre-1994, from dataful.in/Ministry of Finance). "
                "Estimate-only rows are marked in the table below.",
                "note"), unsafe_allow_html=True)
        elif has_est:
            st.markdown(note(
                "Budget Estimates only — Actual expenditure data not available "
                "in verified digital form for this period. "
                "Figures are Budget Estimates as tabled in Parliament. "
                "Source: dataful.in (Ministry of Finance data).",
                "unavail"), unsafe_allow_html=True)

        if valid:
            df_b = pd.DataFrame([{
                "FY": f"{yr}-{str(yr+1)[2:]}",
                "Year": yr,
                "Allocated (₹ Cr)": v["allocated"] if v.get("allocated") else None,
                "Spent (₹ Cr)":     v["spent"]     if v.get("spent")     else None,
                "Fiscal Deficit % GDP": v.get("fiscal_deficit_gdp"),
                "Data Type": "✅ Verified" if v.get("data_type")=="verified" else "⚠️ Estimate Only",
            } for yr, v in valid.items()])
            ta  = df_b["Allocated (₹ Cr)"].sum(skipna=True)
            ts  = df_b["Spent (₹ Cr)"].sum(skipna=True)
            var = (ts-ta)/ta*100 if ta > 0 and ts > 0 else 0
            m1,m2,m3 = st.columns(3)
            m1.metric("Total Allocated (BE)", f"₹{ta/100000:.2f} L Cr" if ta > 100000 else f"₹{ta:,.0f} Cr")
            m2.metric("Total Spent (Actuals)", f"₹{ts/100000:.2f} L Cr" if ts > 100000 else f"₹{ts:,.0f} Cr" if ts > 0 else "Not available")
            m3.metric("Over/Under Spend", f"{var:+.1f}%" if var != 0 else "N/A",
                      delta_color="inverse" if var>0 else "normal")
            fig = go.Figure()
            fig.add_trace(go.Bar(name="Budget Estimate",
                x=df_b["Year"], y=df_b["Allocated (₹ Cr)"],
                marker_color="#3b82f6"))
            fig.add_trace(go.Bar(name="Actual Expenditure",
                x=df_b["Year"], y=df_b["Spent (₹ Cr)"],
                marker_color="#f97316"))
            fig.update_layout(yaxis_tickformat=',', barmode="group",
                title="Budget Estimate vs Actual Expenditure (₹ Crore)",
                plot_bgcolor="#0e1117", paper_bgcolor="#0e1117",
                font_color="white", legend=dict(orientation="h"))
            st.plotly_chart(fig, use_container_width=True)
            df_rd = df_b[df_b["Fiscal Deficit % GDP"].notna()]
            if len(df_rd):
                fig2 = px.line(df_rd, x="Year", y="Fiscal Deficit % GDP",
                    title="Revenue Deficit as % of GDP", markers=True,
                    color_discrete_sequence=["#ef4444"])
                fig2.add_hline(y=3.0, line_dash="dash",
                    line_color="orange", annotation_text="FRBM Target: 3%")
                fig2.update_layout(yaxis_tickformat=',', plot_bgcolor="#0e1117",
                    paper_bgcolor="#0e1117", font_color="white")
                st.plotly_chart(fig2, use_container_width=True)
            with st.expander("📋 Raw Budget Data"):
                st.dataframe(df_b.set_index("Year"), use_container_width=True)
        else:
            st.markdown(note(
                "Verified year-wise budget data for this tenure is not available "
                "in digitised form. Access original budget speech documents via "
                "indiabudget.gov.in archive.", "unavail"), unsafe_allow_html=True)

        if leader_key in SECTOR_BUDGET:
            st.markdown("### Key Sector Allocations (₹ Lakh Crore)")
            sd = SECTOR_BUDGET[leader_key]
            sectors = [k for k in sd if k != "source"]
            yrs = sorted({yr for s in sectors for yr in sd[s]})
            rows = [{"Sector":s,**{yr:sd[s].get(yr,"—") for yr in yrs}}
                    for s in sectors]
            st.dataframe(pd.DataFrame(rows).set_index("Sector"),
                         use_container_width=True)
            st.markdown(src(
                "https://www.indiabudget.gov.in", "Expenditure Budget Vol I"), unsafe_allow_html=True)

    with tab2:
        st.markdown('<div class="section-title">Declared Assets — EC Affidavit</div>',
                    unsafe_allow_html=True)
        st.markdown(
            "📎 Sources: [ECI Affidavit Archive](https://affidavit.eci.gov.in/) | "
            "[ADR/MyNeta](https://myneta.info)",
            unsafe_allow_html=True)
        ai = LEADER_ASSETS.get(leader_key)
        if ai:
            decls = {yr:v for yr,v in ai["declarations"].items()
                     if v.get("total") is not None}
            if decls:
                items = list(decls.items())
                df_a  = pd.DataFrame([{
                    "Election Year":   yr,
                    "Self (₹ Cr)":     v["self_assets"],
                    "Spouse (₹ Cr)":   v["spouse_assets"],
                    "Total (₹ Cr)":    v["total"],
                    "Liabilities":     v["liabilities"],
                } for yr,v in decls.items()])
                if len(items)>=2:
                    first,last = items[0][1]["total"],items[-1][1]["total"]
                    g    = ((last-first)/first*100) if first else 0
                    span = items[-1][0]-items[0][0]
                    cagr = ((last/first)**(1/span)-1)*100 if span>0 and first>0 else 0
                    m1,m2,m3 = st.columns(3)
                    m1.metric(f"Entry ({items[0][0]})", fmt_amt(first))
                    m2.metric(f"Exit  ({items[-1][0]})",fmt_amt(last))
                    m3.metric("Growth", f"{g:+.1f}%",
                              delta=f"CAGR ~{cagr:.1f}%/yr")
                fig = go.Figure()
                fig.add_trace(go.Bar(name="Self",
                    x=df_a["Election Year"], y=df_a["Self (₹ Cr)"],
                    marker_color="#3b82f6"))
                fig.add_trace(go.Bar(name="Spouse",
                    x=df_a["Election Year"], y=df_a["Spouse (₹ Cr)"],
                    marker_color="#8b5cf6"))
                fig.add_trace(go.Scatter(name="Total",
                    x=df_a["Election Year"], y=df_a["Total (₹ Cr)"],
                    mode="lines+markers",
                    line=dict(color="#f97316",width=3)))
                fig.update_layout(yaxis_tickformat=',', barmode="stack",
                    title="Declared Assets — EC Affidavit (₹ Crore)",
                    plot_bgcolor="#0e1117", paper_bgcolor="#0e1117",
                    font_color="white")
                st.plotly_chart(fig, use_container_width=True)
                st.markdown(note(ai["note"]), unsafe_allow_html=True)
                with st.expander("📋 Raw Asset Data"):
                    st.dataframe(df_a.set_index("Election Year"),
                                 use_container_width=True)
            else:
                st.markdown(note(
                    "EC affidavit system introduced from 1999. "
                    f"No declaration on record for this period. {ai['note']}",
                    "unavail"), unsafe_allow_html=True)
            st.markdown(src(ai["source"]), unsafe_allow_html=True)

            party = leader.get("party","")
            for pname,pdata in PARTY_ASSETS.items():
                if pname in party or party in pname:
                    st.markdown(f"---\n### Party Assets — {pname}")
                    df_p = pd.DataFrame({
                        "Year": pdata["years"],
                        "Assets (₹ Cr)": pdata["total_assets_cr"]})
                    fig_p = px.bar(df_p, x="Year", y="Assets (₹ Cr)",
                        title=f"{pname} — Declared Party Assets",
                        color="Assets (₹ Cr)",
                        color_continuous_scale="Oranges")
                    fig_p.update_layout(yaxis_tickformat=',', plot_bgcolor="#0e1117",
                        paper_bgcolor="#0e1117", font_color="white")
                    st.plotly_chart(fig_p, use_container_width=True)
                    st.markdown(note(pdata["note"]), unsafe_allow_html=True)
                    st.markdown(src(
                        "https://adrindia.org/research-and-report/political-party-watch",
                        "ADR India — Party Asset Analysis"), unsafe_allow_html=True)
                    break
        else:
            st.markdown(note(
                "EC affidavit system was not in place during this "
                "leader's tenure.", "unavail"), unsafe_allow_html=True)

    with tab3:
        st.markdown('<div class="section-title">Macroeconomic Indicators</div>',
                    unsafe_allow_html=True)
        st.markdown(
            "📎 Sources: [World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG?locations=IN) | "
            "[FRED (1950–2010)](https://fred.stlouisfed.org/series/FXRATEINA618NUPN) | "
            "[FRED INR/USD (2010–present)](https://fred.stlouisfed.org/series/AEXINUS) | "
            "[RBI](https://rbi.org.in)",
            unsafe_allow_html=True)
        eco = get_economy_for_tenure(start_yr, min(end_yr,2024))
        if eco:
            df_e = pd.DataFrame([{"Year":yr,**v} for yr,v in eco.items()])
            ind_map = {
                "INR/USD Exchange Rate":     "inr_usd",
                "CPI Inflation (%)":         "cpi_inflation",
                "GDP Growth (%)":            "gdp_growth",
                "Fiscal Deficit (% of GDP)": "fiscal_deficit_gdp",
                "FDI Inflows ($ Billion)":   "fdi_bn_usd",
            }
            chosen = st.selectbox("Select Indicator", list(ind_map.keys()))
            col_k  = ind_map[chosen]
            clr    = {"inr_usd":"#ef4444","cpi_inflation":"#f97316",
                      "gdp_growth":"#22c55e","fiscal_deficit_gdp":"#a855f7",
                      "fdi_bn_usd":"#3b82f6"}
            df_plot = df_e[df_e[col_k].notna()][["Year",col_k]]
            fig = px.line(df_plot, x="Year", y=col_k, markers=True,
                title=f"{chosen} — {leader['name']}'s Tenure",
                color_discrete_sequence=[clr.get(col_k,"#fff")])
            if col_k=="cpi_inflation":
                fig.add_hline(y=6.0,line_dash="dash",
                    line_color="red",annotation_text="RBI Upper: 6%")
                fig.add_hline(y=4.0,line_dash="dash",
                    line_color="green",annotation_text="RBI Target: 4%")
            if col_k=="fiscal_deficit_gdp":
                fig.add_hline(y=3.0,line_dash="dash",
                    line_color="orange",annotation_text="FRBM: 3%")
            if col_k=="gdp_growth":
                fig.add_hline(y=0.0,line_dash="dash",
                    line_color="red",annotation_text="Zero Growth")
            fig.update_layout(yaxis_tickformat=',', plot_bgcolor="#0e1117",
                paper_bgcolor="#0e1117",font_color="white")
            st.plotly_chart(fig, use_container_width=True)
            avgs = df_e[[c for c in df_e.columns if c!="Year"]].mean()
            st.markdown("#### Tenure Averages")
            a1,a2,a3,a4,a5 = st.columns(5)
            def sm(col,label,val,suf=""):
                col.metric(label,
                    f"{val:.1f}{suf}" if pd.notna(val) else "N/A")
            sm(a1,"Avg INR/USD",   avgs.get("inr_usd",float("nan")),        " ₹")
            sm(a2,"Avg Inflation", avgs.get("cpi_inflation",float("nan")),  "%")
            sm(a3,"Avg GDP Growth",avgs.get("gdp_growth",float("nan")),     "%")
            sm(a4,"Avg Fisc. Def.",avgs.get("fiscal_deficit_gdp",float("nan")),"%")
            sm(a5,"Avg FDI",       avgs.get("fdi_bn_usd",float("nan")),     " $Bn")
            with st.expander("📋 Full Economic Data"):
                st.dataframe(df_e.set_index("Year"),use_container_width=True)
        else:
            st.markdown(note(
                "Economic data not available for this period.",
                "unavail"), unsafe_allow_html=True)

    with tab4:
        st.markdown(f"## 📋 Tenure Report — {leader['name']} ({start_yr}–{end_yr})")
        bd    = get_budget_for_tenure(start_yr, end_yr)
        valid = {yr:v for yr,v in bd.items() if v.get("spent")}
        if valid:
            ta = sum(v["allocated"] for v in valid.values() if v.get("allocated"))
            ts = sum(v["spent"]     for v in valid.values() if v.get("spent"))
            st.markdown(f"- 💰 **Total Budget Allocated (BE):** ₹{ta:,.0f} Crore  (₹{ta/100000:.2f} Lakh Crore)")
            if ts > 0:
                st.markdown(f"- 💸 **Total Actually Spent (Actuals):** ₹{ts:,.0f} Crore  (₹{ts/100000:.2f} Lakh Crore)")
                st.markdown(f"- 📊 **Expenditure Variance:** {((ts-ta)/ta*100):+.1f}%")
            else:
                    st.markdown("- 💸 **Actual Expenditure:** Not available for this tenure period")
            st.markdown(
                "📎 Sources: [IndiabudGet.gov.in](https://www.indiabudget.gov.in) | "
                "[CAG](https://cag.gov.in/en/audit-report)",
                unsafe_allow_html=True)
        eco = get_economy_for_tenure(start_yr, min(end_yr,2024))
        if eco:
            df_e  = pd.DataFrame([{"Year":yr,**v} for yr,v in eco.items()])
            inr_v = df_e[df_e["inr_usd"].notna()]["inr_usd"]
            if len(inr_v)>=2:
                st.markdown(
                    f"- 💱 **INR/USD:** ₹{inr_v.iloc[0]} → ₹{inr_v.iloc[-1]}")
            for label,col,suf in [
                ("Avg GDP Growth","gdp_growth","%/yr"),
                ("Avg Inflation","cpi_inflation","%/yr"),
                ("Avg Fiscal Deficit","fiscal_deficit_gdp","% GDP"),
            ]:
                v = df_e[col].mean()
                if pd.notna(v):
                    st.markdown(f"- 📈 **{label}:** {v:.1f}{suf}")
            st.markdown(
                "📎 Sources: [World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG?locations=IN) | "
                "[FRED (1950–2010)](https://fred.stlouisfed.org/series/FXRATEINA618NUPN) | "
                "[FRED INR/USD (2010–present)](https://fred.stlouisfed.org/series/AEXINUS)",
                unsafe_allow_html=True)
        pwr = purchasing_power_of_100(start_yr, min(end_yr,2024))
        if pwr:
            st.markdown(
                f"- 📉 **Purchasing Power:** ₹100 from {start_yr} "
                f"buys ₹{pwr} worth of goods by {min(end_yr,2024)}")
            st.markdown(src("https://mospi.gov.in/consumer-price-index",
                "MoSPI — Consumer Price Index"), unsafe_allow_html=True)

# ── Compare ───────────────────────────────────────────────
elif union_mode == "⚖️  Compare Leaders":
    st.title("⚖️ Union Government — Compare Two Leaders")
    leaders_dict = filtered_leaders()
    keys = list(leaders_dict.keys())
    c1,c2 = st.columns(2)
    with c1: k1 = st.selectbox("Leader 1", keys, index=0)
    with c2: k2 = st.selectbox("Leader 2", keys, index=min(1,len(keys)-1))
    if k1==k2:
        st.warning("Please select two different leaders.")
        st.stop()
    l1,l2 = leaders_dict[k1],leaders_dict[k2]
    st.markdown("---")

    st.markdown('<div class="section-title">Economic Performance</div>',
                unsafe_allow_html=True)
    st.markdown(
        "📎 Sources: [World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG?locations=IN) | "
        "[RBI](https://rbi.org.in) | "
        "[MoSPI](https://mospi.gov.in/consumer-price-index)",
        unsafe_allow_html=True)
    eco_keys = {
        "GDP Growth (%)":        "gdp_growth",
        "CPI Inflation (%)":     "cpi_inflation",
        "Fiscal Deficit (%GDP)": "fiscal_deficit_gdp",
        "FDI Inflows ($Bn)":     "fdi_bn_usd",
    }
    def avg_eco(ldr):
        eco = get_economy_for_tenure(
            ldr["start_year"], min(ldr["end_year"],2024))
        out = {}
        for label,k in eco_keys.items():
            vals = [v[k] for v in eco.values() if v.get(k) is not None]
            out[label] = round(sum(vals)/len(vals),2) if vals else None
        return out
    a1,a2   = avg_eco(l1),avg_eco(l2)
    labels  = [k for k in eco_keys if a1.get(k) is not None and a2.get(k) is not None]
    fig = go.Figure()
    fig.add_trace(go.Bar(name=l1["name"], x=labels,
        y=[a1[k] for k in labels], marker_color="#3b82f6"))
    fig.add_trace(go.Bar(name=l2["name"], x=labels,
        y=[a2[k] for k in labels], marker_color="#f97316"))
    fig.update_layout(yaxis_tickformat=',', barmode="group",
        title="Tenure-Average Economic Indicators",
        plot_bgcolor="#0e1117",paper_bgcolor="#0e1117",font_color="white")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown('<div class="section-title">INR/USD Comparison</div>',
                unsafe_allow_html=True)
    st.markdown(
        "📎 Sources: [FRED (1950–2010)](https://fred.stlouisfed.org/series/FXRATEINA618NUPN) | "
        "[FRED INR/USD (2010–present)](https://fred.stlouisfed.org/series/AEXINUS)",
        unsafe_allow_html=True)
    fig_inr = go.Figure()
    for ldr,color in [(l1,"#3b82f6"),(l2,"#f97316")]:
        eco = get_economy_for_tenure(
            ldr["start_year"],min(ldr["end_year"],2024))
        pts = [(yr,v["inr_usd"]) for yr,v in eco.items() if v.get("inr_usd")]
        if pts:
            fig_inr.add_trace(go.Scatter(
                x=[p[0] for p in pts], y=[p[1] for p in pts],
                name=ldr["name"], mode="lines+markers",
                line=dict(color=color,width=2)))
    fig_inr.update_layout(yaxis_tickformat=',', title="INR per 1 USD by Tenure",
        xaxis_title="Year", yaxis_title="₹ per USD",
        plot_bgcolor="#0e1117",paper_bgcolor="#0e1117",font_color="white")
    st.plotly_chart(fig_inr, use_container_width=True)
    st.markdown(note(
        "Higher INR/USD = rupee depreciation. Currency movement is "
        "influenced by global factors (US Fed rates, oil prices) "
        "in addition to domestic policy."), unsafe_allow_html=True)

# ── Timeline ──────────────────────────────────────────────
else:
    st.title("📅 Historical Timeline — Union Government (1947–2024)")
    t1,t2,t3 = st.tabs(
        ["👔 Prime Ministers","💼 Finance Ministers","📊 Economy 1947–2024"])
    with t1:
        rows = []
        for k,v in PRIME_MINISTERS.items():
            eco  = get_economy_for_tenure(v["start_year"],min(v["end_year"],2024))
            gdps = [d["gdp_growth"] for d in eco.values()
                    if d.get("gdp_growth") is not None]
            rows.append({
                "Prime Minister": v["name"], "Party": v["party"],
                "From": v["start_year"], "To": v["end_year"],
                "Duration (Yrs)": v["end_year"]-v["start_year"],
                "Avg GDP Growth": f"{sum(gdps)/len(gdps):.1f}%" if gdps else "N/A",
            })
        st.dataframe(pd.DataFrame(rows),use_container_width=True,hide_index=True)
        st.markdown(src("https://en.wikipedia.org/wiki/List_of_prime_ministers_of_India",
            "PMO India"), unsafe_allow_html=True)
    with t2:
        rows = []
        for k,v in FINANCE_MINISTERS.items():
            rows.append({
                "Finance Minister": v["name"], "Party": v["party"],
                "From": v["start_year"], "To": v["end_year"],
                "Duration (Yrs)": v["end_year"]-v["start_year"],
                "Key Note": v["summary"][:70]+"...",
            })
        st.dataframe(pd.DataFrame(rows),use_container_width=True,hide_index=True)
        st.markdown(src("https://finmin.gov.in","Ministry of Finance"),
            unsafe_allow_html=True)
    with t3:
        st.markdown("### India Macroeconomic History — 1947 to 2024")
        ind_map2 = {
            "inr_usd":"INR/USD Rate",
            "cpi_inflation":"CPI Inflation %",
            "gdp_growth":"GDP Growth %",
            "fiscal_deficit_gdp":"Fiscal Deficit % GDP",
            "fdi_bn_usd":"FDI $Bn",
        }
        ind = st.selectbox("Indicator",list(ind_map2.keys()),
            format_func=lambda x:ind_map2[x])
        df_all  = pd.DataFrame(
            [{"Year":yr,**v} for yr,v in ECONOMY_DATA.items()])
        df_plot = df_all[df_all[ind].notna()]
        fig = px.line(df_plot, x="Year", y=ind,
            title=f"India — {ind_map2[ind]} (1947–2024)",
            color_discrete_sequence=["#22c55e"])
        colors = [
            "rgba(59,130,246,0.07)","rgba(249,115,22,0.07)",
            "rgba(168,85,247,0.07)","rgba(34,197,94,0.07)",
            "rgba(239,68,68,0.07)",
        ]
        for i,(k,v) in enumerate(PRIME_MINISTERS.items()):
            fig.add_vrect(
                x0=v["start_year"],x1=min(v["end_year"],2024),
                fillcolor=colors[i%len(colors)],opacity=1,
                layer="below",line_width=0,
                annotation_text=v["name"].split()[-1],
                annotation_position="top left",
                annotation_font=dict(size=9,color="#888"))
        fig.update_layout(yaxis_tickformat=',', plot_bgcolor="#0e1117",
            paper_bgcolor="#0e1117",font_color="white")
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Shaded bands = PM tenures. Hover to see exact values.")
    st.markdown(
        "📎 Sources: [World Bank](https://data.worldbank.org/indicator/NY.GDP.MKTP.KD.ZG?locations=IN) | "
        "[FRED (1950–2010)](https://fred.stlouisfed.org/series/FXRATEINA618NUPN) | "
        "[FRED INR/USD (2010–present)](https://fred.stlouisfed.org/series/AEXINUS) | "
        "[RBI](https://rbi.org.in)",
        unsafe_allow_html=True)


render_footer()

