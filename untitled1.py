import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Adult Dashboard", layout="wide")

# Load data
df = pd.read_csv("adult (1).csv", sep=",", skipinitialspace=True)
df = df.dropna()
df.columns = df.columns.str.strip()

# Title
st.title("Adult Income Dashboard")
st.markdown("Interactive dashboard for exploring the Adult dataset")

# Sidebar filters
st.sidebar.header("Filters")

education_options = sorted(df["education"].dropna().unique())
income_options = sorted(df["income"].dropna().unique())

selected_education = st.sidebar.multiselect(
"Select Education",
education_options,
default=education_options
)

selected_income = st.sidebar.multiselect(
"Select Income",
income_options,
default=income_options
)

age_range = st.sidebar.slider(
"Select Age Range",
int(df["age"].min()),
int(df["age"].max()),
(int(df["age"].min()), int(df["age"].max()))
)

hours_range = st.sidebar.slider(
"Select Working Hours Range",
int(df["hours.per.week"].min()),
int(df["hours.per.week"].max()),
(int(df["hours.per.week"].min()), int(df["hours.per.week"].max()))
)

# Apply filters
filtered_df = df[
(df["education"].isin(selected_education)) &
(df["income"].isin(selected_income)) &
(df["age"].between(age_range[0], age_range[1])) &
(df["hours.per.week"].between(hours_range[0], hours_range[1]))
]

# Metrics
st.subheader("Summary")
col1, col2, col3 = st.columns(3)

col1.metric("Rows", len(filtered_df))
col2.metric("Average Age", round(filtered_df["age"].mean(), 1) if len(filtered_df) > 0 else 0)
col3.metric("Average Weekly Hours", round(filtered_df["hours.per.week"].mean(), 1) if len(filtered_df) > 0 else 0)

# Preview
st.subheader("Dataset Preview")
st.dataframe(filtered_df)

# Charts
col4, col5 = st.columns(2)

with col4:
st.subheader("Age Distribution")
fig1 = px.histogram(filtered_df, x="age", nbins=30)
st.plotly_chart(fig1, use_container_width=True)

with col5:
st.subheader("Income Distribution")
fig2 = px.pie(filtered_df, names="income")
st.plotly_chart(fig2, use_container_width=True)

col6, col7 = st.columns(2)

with col6:
st.subheader("Education Distribution")
education_counts = filtered_df["education"].value_counts().reset_index()
education_counts.columns = ["education", "count"]
fig3 = px.bar(education_counts, x="education", y="count")
st.plotly_chart(fig3, use_container_width=True)

with col7:
st.subheader("Age vs Working Hours")
fig4 = px.scatter(filtered_df, x="age", y="hours.per.week", color="income")
st.plotly_chart(fig4, use_container_width=True)
