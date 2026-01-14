# visualizations.py
import plotly.express as px
import plotly.graph_objects as go


def create_heatmap_chart(filtered_df):
    """Create sector heatmap visualization"""
    heatmap_data = filtered_df.pivot_table(
        values="% From Low", index="Sector", aggfunc="mean"
    ).sort_values("% From Low")

    fig = px.imshow(
        [heatmap_data["% From Low"].values],
        x=heatmap_data.index,
        y=["Avg % From Low"],
        color_continuous_scale="RdYlGn_r",
        labels=dict(x="Sector", y="", color="% From Low"),
        aspect="auto",
    )
    fig.update_layout(height=200)
    return fig


def create_scatter_chart(filtered_df, threshold):
    """Create scatter plot visualization"""
    fig = px.scatter(
        filtered_df,
        x="Market Cap (B)",
        y="% From Low",
        color="Near Low",
        hover_name="Symbol",
        hover_data=["Sector", "Current Price", "52W Low"],
        color_discrete_map={True: "#EF4444", False: "#3B82F6"},
        size="Volume (M)",
        size_max=20,
        labels={
            "Market Cap (B)": "Market Cap (Billions)",
            "% From Low": "% From 52-Week Low",
            "Near Low": "Near 52W Low",
        },
    )

    fig.add_hline(
        y=threshold,
        line_dash="dash",
        line_color="red",
        annotation_text=f"Threshold: {threshold}%",
    )

    fig.update_layout(height=500)
    return fig


def create_sector_charts(near_low_df):
    """Create sector breakdown charts"""
    sector_analysis = near_low_df["Sector"].value_counts().reset_index()
    sector_analysis.columns = ["Sector", "Count"]

    # Bar chart
    fig_bar = px.bar(
        sector_analysis,
        x="Sector",
        y="Count",
        color="Count",
        color_continuous_scale="reds",
        title="Near-Low Stocks by Sector",
    )

    # Pie chart
    fig_pie = px.pie(
        sector_analysis, values="Count", names="Sector", title="Sector Distribution"
    )

    return fig_bar, fig_pie
