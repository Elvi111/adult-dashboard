import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("adult (1).csv")
df = df.dropna()

st.title("📊 Adult Dataset Dashboard")

# Filter
age_range = st.slider("Select Age Range",
                      int(df.age.min()),
                      int(df.age.max()),
                      (20, 50))

filtered_df = df[(df.age >= age_range[0]) & (df.age <= age_range[1])]

# Histogram
fig1 = px.histogram(filtered_df, x='age', nbins=30, title='Age Distribution')
st.plotly_chart(fig1)

# Bar chart
fig2 = px.histogram(filtered_df, x="education", color="income", barmode="group",
title="Income by Education")
st.plotly_chart(fig2)

# Scatter
fig3 = px.scatter(filtered_df, x='age', y='hours.per.week',
color='income', title='Age vs Working Hours')
st.plotly_chart(fig3)

# Pie
fig4 = px.pie(filtered_df, names='income', title='Income Distribution')
st.plotly_chart(fig4)
