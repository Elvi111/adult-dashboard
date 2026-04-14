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

# Sidebar
st.sidebar.header("Filters")

education = st.sidebar.multiselect(
"Education",
df["education"].unique(),
default=df["education"].unique()
)

income = st.sidebar.multiselect(
"Income",
df["income"].unique(),
default=df["income"].unique()
)

# Filter data
filtered_df = df[
(df["education"].isin(education)) &
(df["income"].isin(income))
]

# Show data
st.subheader("Data")
st.dataframe(filtered_df)

# Charts
st.subheader("Age Distribution")
fig1 = px.histogram(filtered_df, x="age")
st.plotly_chart(fig1)

st.subheader("Income Distribution")
fig2 = px.pie(filtered_df, names="income")
st.plotly_chart(fig2)

st.subheader("Education Distribution")
fig3 = px.bar(filtered_df, x="education")
st.plotly_chart(fig3)

st.subheader("Age vs Hours")
fig4 = px.scatter(filtered_df, x="age", y="hours.per.week", color="income")
st.plotly_chart(fig4)
