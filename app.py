import streamlit as st 
st.title("⚡Energy Dashboard")
st.subheader("Interactive dashboard for energy demand analysis")

import pandas as pd 
df=pd.read_csv("electricity_demand.csv")
df.columns=df.columns.str.strip()

st.subheader("📊Dataset Preview")
st.write(df.head())
st.subheader("📈Energy Demand Over Time")
df['utc_timestamp']=pd.to_datetime(df['utc_timestamp'])

df['year']=df['utc_timestamp'].dt.year

year=st.slider(
    "Select Year",
    int(df["utc_timestamp"].dt.year.min()),
    int(df['utc_timestamp'].dt.year.max()))

filtered_df=df[df['year']==year]
filtered_df=filtered_df.sort_values("utc_timestamp")
st.write(f"Showing data for year: {year}")
st.line_chart(
    filtered_df.set_index('utc_timestamp')['AT_load_actual_entsoe_transparency'],
    use_container_width=True
)
st.subheader("📊Actual load vs Forecasted Load")
comparison_df=filtered_df[[
    "utc_timestamp",
    "AT_load_actual_entsoe_transparency",
    "AT_load_forecast_entsoe_transparency"
]].dropna()

comparison_df=comparison_df.sort_values("utc_timestamp")
comparison_df=comparison_df.set_index("utc_timestamp")

st.line_chart(
    comparison_df[[
        "AT_load_actual_entsoe_transparency",
        "AT_load_forecast_entsoe_transparency"
    ]],
    use_container_width=True
)