import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("🏥 Patient Visit Dashboard")

# Load data
df = pd.read_csv("patient_visits.csv", sep=";")

# Show data
st.subheader("Raw Data")
st.dataframe(df)

# -------------------------
# 📊 Department Pie Chart
# -------------------------
st.subheader("Visits by Department")

dept_counts = df["Department"].value_counts()

fig1, ax1 = plt.subplots()
ax1.pie(dept_counts, labels=dept_counts.index, autopct='%1.1f%%')
st.pyplot(fig1)

# -------------------------
# 📊 Outcome Bar Chart
# -------------------------
st.subheader("Patient Outcomes")

outcome_counts = df["Outcome"].value_counts()

fig2, ax2 = plt.subplots()
ax2.barh(outcome_counts.index, outcome_counts.values)
st.pyplot(fig2)

# -------------------------
# 💰 Total Revenue
# -------------------------
st.subheader("Total Revenue")

total_revenue = df["Treatment_Cost"].sum()
st.metric("Total Revenue", f"R{total_revenue}")