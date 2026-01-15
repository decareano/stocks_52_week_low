# app.py
import streamlit as st
import pandas as pd
from datetime import datetime
from .data_generator import generate_stock_universe
from .visualizations import (
    create_heatmap_chart,
    create_scatter_chart,
    create_sector_charts,
)

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title="52-Week Low Scanner",
    page_icon="📉",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ========== DEMO BANNER ==========
st.markdown(
    """
<div style="background: linear-gradient(90deg, #1E3A8A, #3B82F6); 
            padding: 1.5rem; 
            border-radius: 12px; 
            color: white;
            margin-bottom: 2rem;
            box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);">
    <div style="display: flex; align-items: center; justify-content: space-between;">
        <div>
            <h2 style="margin: 0; color: white;">📊 52-Week Low Stock Scanner</h2>
            <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">
                Scan 500+ stocks for potential buying opportunities at 52-week lows
            </p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 0.5rem 1rem; border-radius: 8px;">
            <strong>DEMO MODE</strong><br>
            <small>Sample Data • Architecture Demo</small>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ========== LOAD DATA ==========
with st.spinner("📊 Loading stock universe..."):
    df = generate_stock_universe()

# ========== SIDEBAR FILTERS ==========
with st.sidebar:
    st.header("🔍 Scanner Filters")

    threshold = st.slider(
        "Maximum % from 52-week low:",
        min_value=0.0,
        max_value=15.0,
        value=5.0,
        step=0.5,
    )

    sectors = sorted(df["Sector"].unique())
    selected_sectors = st.multiselect(
        "Filter by sector:", options=sectors, default=sectors
    )

    min_cap, max_cap = st.slider(
        "Market Cap Range (Billions):",
        min_value=0.0,
        max_value=500.0,
        value=(10.0, 200.0),
        step=10.0,
    )

    min_volume = st.number_input(
        "Minimum Daily Volume (Millions):", min_value=0.0, value=5.0, step=5.0
    )

    scan_clicked = st.button(
        "🚀 Run 52-Week Low Scan", type="primary", use_container_width=True
    )

    st.divider()

    # Stats
    st.metric("Total Stocks", f"{len(df):,}")
    st.metric("Sectors", len(sectors))
    st.metric(
        "Price Range",
        f"${df['Current Price'].min():.0f}-${df['Current Price'].max():.0f}",
    )

# ========== MAIN APP LOGIC ==========
if not scan_clicked:
    # Welcome screen
    col1, col2 = st.columns([2, 1])

    with col1:
        st.info("👈 **Configure your scan in the sidebar and click 'Run Scan'**")

        st.markdown(
            """
            ### 🎯 What This Scanner Does:
            
            This tool scans **500+ real stocks** across all major sectors to find:
            
            - ✅ **Stocks trading near 52-week lows** - potential buying opportunities
            - ✅ **Sector-level trends** - which industries are under pressure
            - ✅ **Filtered results** - by market cap, volume, and sectors
            - ✅ **Visual insights** - heatmaps and distributions
            
            **Perfect for:** Value investors, contrarian strategies, market analysis
            """
        )

    with col2:
        st.subheader("📊 Sample Findings")

        # Show a few near-low stocks as example
        sample_near_low = df.nsmallest(5, "% From Low")

        for _, row in sample_near_low.iterrows():
            st.markdown(
                f"""
            <div style="background: #FEF2F2; padding: 0.75rem; border-radius: 8px; margin-bottom: 0.5rem;">
                <strong>{row['Symbol']}</strong> • {row['Sector']}<br>
                <span style="color: #EF4444; font-weight: bold;">{row['% From Low']}% from low</span><br>
                <small>${row['Current Price']} • ${row['Market Cap (B)']}B cap</small>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.divider()

    # Show universe overview
    st.subheader("🌎 Stock Universe Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Stocks", f"{len(df):,}")

    with col2:
        avg_from_low = df["% From Low"].mean()
        st.metric("Avg % From Low", f"{avg_from_low:.1f}%")

    with col3:
        stocks_below_5pct = len(df[df["% From Low"] <= 5])
        st.metric("Within 5% of Low", stocks_below_5pct)

    with col4:
        sector_count = len(df["Sector"].unique())
        st.metric("Sectors", sector_count)

else:
    # ========== RUN SCAN ==========
    with st.spinner(f"🔍 Scanning {len(df):,} stocks..."):
        filtered_df = df[
            (df["Sector"].isin(selected_sectors))
            & (df["Market Cap (B)"] >= min_cap)
            & (df["Market Cap (B)"] <= max_cap)
            & (df["Volume (M)"] >= min_volume)
        ].copy()

        filtered_df["Near Low"] = filtered_df["% From Low"] <= threshold
        near_low_df = filtered_df[filtered_df["Near Low"]].sort_values("% From Low")

    # ========== DISPLAY RESULTS ==========
    st.success(
        f"✅ Scan complete! Found **{len(near_low_df)} stocks** within {threshold}% of 52-week lows"
    )

    # Summary metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Stocks Scanned", f"{len(filtered_df):,}")

    with col2:
        st.metric("Near 52-Week Lows", len(near_low_df))

    with col3:
        if len(near_low_df) > 0:
            closest_pct = near_low_df["% From Low"].min()
            st.metric("Closest to Low", f"{closest_pct:.1f}%")
        else:
            st.metric("Closest to Low", "N/A")

    with col4:
        avg_from_low = filtered_df["% From Low"].mean()
        st.metric("Market Avg", f"{avg_from_low:.1f}%")

    # ========== DISPLAY STOCK RESULTS ==========
    if len(near_low_df) > 0:
        st.subheader(f"🎯 Top {min(20, len(near_low_df))} Stocks Near 52-Week Lows")

        # Display top stocks
        top_stocks = near_low_df.head(20)

        for idx, row in top_stocks.iterrows():
            col1, col2, col3, col4 = st.columns([1, 2, 2, 1])

            with col1:
                st.markdown(f"**{row['Symbol']}**")
                # COMPANY NAME SHOWS HERE
                st.caption(f"{row['Name']}")
                st.caption(row["Sector"])

            with col2:
                progress = row["% From Low"] / threshold * 100
                st.progress(
                    min(100, progress) / 100, text=f"{row['% From Low']:.1f}% from low"
                )

            with col3:
                st.markdown(f"**${row['Current Price']:.2f}**")
                st.caption(f"Range: ${row['52W Low']:.2f}-${row['52W High']:.2f}")

            with col4:
                st.metric("Cap", f"${row['Market Cap (B)']:.0f}B")

            st.divider()

        # ========== VISUALIZATION 1: HEATMAP ==========
        st.subheader("📊 Sector Heatmap")
        heatmap_fig = create_heatmap_chart(filtered_df)
        st.plotly_chart(heatmap_fig, use_container_width=True)

        # ========== VISUALIZATION 2: SCATTER PLOT ==========
        st.subheader("📈 Market Cap vs % From Low")
        scatter_fig = create_scatter_chart(filtered_df, threshold)
        st.plotly_chart(scatter_fig, use_container_width=True)

        # ========== VISUALIZATION 3: SECTOR BREAKDOWN ==========
        st.subheader("🏭 Sector Breakdown")
        bar_fig, pie_fig = create_sector_charts(near_low_df)
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(bar_fig, use_container_width=True)
        with col2:
            st.plotly_chart(pie_fig, use_container_width=True)

        # ========== DATA TABLE ==========
        with st.expander("📋 View All Near-Low Stocks", expanded=False):
            display_df = near_low_df.copy()
            display_df["Current Price"] = display_df["Current Price"].apply(
                lambda x: f"${x:.2f}"
            )
            display_df["52W Low"] = display_df["52W Low"].apply(lambda x: f"${x:.2f}")
            display_df["52W High"] = display_df["52W High"].apply(lambda x: f"${x:.2f}")
            display_df["Market Cap (B)"] = display_df["Market Cap (B)"].apply(
                lambda x: f"${x:.0f}B"
            )

            # COMPANY NAME INCLUDED IN TABLE
            st.dataframe(
                display_df[
                    [
                        "Symbol",
                        "Name",
                        "Sector",
                        "Current Price",
                        "% From Low",
                        "52W Low",
                        "52W High",
                        "Market Cap (B)",
                        "Volume (M)",
                    ]
                ],
                use_container_width=True,
                height=400,
            )

            # Download button
            csv = near_low_df.to_csv(index=False)
            st.download_button(
                label="📥 Download Results as CSV",
                data=csv,
                file_name=f"52_week_low_stocks_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv",
            )

        # ========== INSIGHTS ==========
        with st.expander("🤖 AI-Powered Insights", expanded=True):
            if len(near_low_df) > 10:
                st.markdown(
                    f"""
                **📊 Market Analysis:**
                - Found **{len(near_low_df)} stocks** ({len(near_low_df)/len(filtered_df)*100:.1f}% of scanned) near 52-week lows
                - Average distance from low: **{near_low_df['% From Low'].mean():.1f}%**
                
                **🎯 Investment Considerations:**
                1. **Sector Concentration:** Review sector distribution above
                2. **Market Cap Range:** Near-low stocks average ${near_low_df['Market Cap (B)'].mean():.0f}B cap
                3. **Volume Check:** Ensure adequate liquidity (filtered for >{min_volume}M volume)
                
                **⚠️ Next Steps:**
                - Research why specific sectors are underperforming
                - Check company fundamentals for near-low stocks
                - Consider dollar-cost averaging into quality names
                - Monitor for potential sector rotation
                """
                )
            else:
                st.info(
                    f"Only {len(near_low_df)} stocks found near lows. Market may be in an uptrend or consider adjusting your threshold."
                )

    else:
        st.warning(
            f"❌ No stocks found within {threshold}% of 52-week lows with current filters."
        )

        # Suggest adjustments
        st.info(
            """
        **💡 Try adjusting your filters:**
        - Increase the threshold percentage
        - Include more sectors
        - Adjust market cap range
        - Lower volume requirements
        """
        )

        # Show closest candidates
        closest_candidates = filtered_df.nsmallest(10, "% From Low")
        if len(closest_candidates) > 0:
            st.subheader("📊 Closest Candidates")
            st.dataframe(
                closest_candidates[
                    [
                        "Symbol",
                        "Name",
                        "Sector",
                        "Current Price",
                        "% From Low",
                        "Market Cap (B)",
                    ]
                ],
                use_container_width=True,
            )

# ========== FOOTER ==========
st.divider()
st.markdown(
    """
<div style="text-align: center; color: #6B7280; padding: 1rem;">
    <p>
        <strong>📊 Stock Universe:</strong> 500+ sample stocks across 6 sectors • 
        <strong>📅 Data:</strong> December 2024 sample data •
        <strong>🎯 Purpose:</strong> Architecture demonstration
    </p>
    <p style="font-size: 0.9rem; margin-top: 0.5rem;">
        <strong>⚠️ DISCLAIMER:</strong> This is a demo application showing scanning architecture. 
        Not financial advice. In production, would connect to real-time market data APIs.
    </p>
</div>
""",
    unsafe_allow_html=True,
)
