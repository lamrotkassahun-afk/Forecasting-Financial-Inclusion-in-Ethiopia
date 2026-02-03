import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. LOAD DATA
@st.cache_data
def load_data():
    df = pd.read_csv('data/processed/ethiopia_fi_unified_enriched.csv')
    matrix = pd.read_csv('data/processed/event_impact_matrix.csv', index_col=0)
    return df, matrix

df, matrix = load_data()

st.title("🇪🇹 ET Financial Inclusion Overview")

# 2. OVERVIEW PAGE (As seen in your screenshot)
col1, col2, col3 = st.columns(3)
col1.metric("Current Ownership (2024)", "49.0%", "+3.0%")
col2.metric("NFIS-II Target", "70.0%", "Target Year: 2025")
col3.metric("Digital Adoption", "34%", "Mobile Money")

# 3. INTERACTIVE FORECAST SECTION
st.divider()
st.header("🔮 2027 Inclusion Projections")
scenario = st.radio("Select Growth Scenario", ["Conservative", "Accelerated"], horizontal=True)

# Data for Plotting (Using your Task 4 Results)
years = [2024, 2025, 2026, 2027]
if scenario == "Accelerated":
    values = [49.0, 67.5, 70.5, 73.07] # Actual results from your Task 4
    color = "green"
else:
    values = [49.0, 55.8, 58.5, 61.32] # Actual results from your Task 4
    color = "red"

fig = go.Figure()
fig.add_trace(go.Scatter(x=years, y=values, mode='lines+markers', name=scenario, line=dict(color=color, width=4)))
# Add Target Line
fig.add_shape(type="line", x0=2024, y0=70, x1=2027, y1=70, line=dict(color="Blue", dash="dot"))
fig.add_annotation(x=2025.5, y=72, text="70% NFIS-II Target", showarrow=False, font=dict(color="blue"))

fig.update_layout(yaxis_title="Account Ownership (%)", xaxis_title="Year", template="plotly_dark")
st.plotly_chart(fig, use_container_width=True)

# 4. EVENT IMPACT ANALYSIS (Your Task 3 Matrix)
st.divider()
st.header("📊 Event Impact Analysis")
st.write("Quantified impact of market events on inclusion indicators:")
fig_heat = px.imshow(matrix, text_auto=True, color_continuous_scale='RdBu_r', aspect="auto")
st.plotly_chart(fig_heat, use_container_width=True)