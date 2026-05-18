import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Finance Dashboard", layout="wide")

st.title("💰 Personal Finance Dashboard")

# -----------------------------
# 📊 GENERATE DATA (your logic)
# -----------------------------
np.random.seed(42)
n = 1000

dates = pd.date_range(start="2025-01-01", periods=n, freq="D")
categories = ["Food", "Transport", "Rent", "Entertainment", "Utilities", "Shopping"]

data = {
    "date": np.random.choice(dates, n),
    "category": np.random.choice(categories, n),
    "amount": np.random.randint(20, 2000, n),
    "description": np.random.choice(
        ["Groceries", "Taxi", "Electricity", "Clothes", "Movie", "Dinner"], n
    )
}

df = pd.DataFrame(data)

df["income"] = np.random.randint(1000, 5000, len(df))

# Sort + balance (IMPORTANT FIX)
df = df.sort_values("date")
df["balance"] = (df["income"] - df["amount"]).cumsum()

df["month"] = df["date"].dt.to_period("M").astype(str)

# -----------------------------
# 📈 AGGREGATIONS
# -----------------------------
monthly = df.groupby("month").agg({
    "income": "sum",
    "amount": "sum"
})

monthly["savings"] = monthly["income"] - monthly["amount"]
monthly["savings_rate"] = (monthly["savings"] / monthly["income"]) * 100

category_summary = df.groupby("category")["amount"].sum().sort_values()

category_trend = df.pivot_table(
    values="amount",
    index="month",
    columns="category",
    aggfunc="sum"
)

# -----------------------------
# 📌 KPIs
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Income", f"{monthly['income'].sum():,.0f}")
col2.metric("Total Spending", f"{monthly['amount'].sum():,.0f}")
col3.metric("Net Savings", f"{monthly['savings'].sum():,.0f}")
col4.metric("Current Balance", f"{df['balance'].iloc[-1]:,.0f}")

st.divider()

# -----------------------------
# 📊 CATEGORY SPENDING
# -----------------------------
st.subheader("📊 Spending by Category")

st.bar_chart(category_summary)

st.write("🔺 Most spent on:", category_summary.idxmax())
st.write("🔻 Least spent on:", category_summary.idxmin())

# -----------------------------
# 📈 INCOME VS SPENDING
# -----------------------------
st.subheader("📈 Income vs Spending")

fig1, ax1 = plt.subplots(figsize=(5,3))
ax1.plot(monthly.index, monthly["income"], label="Income")
ax1.plot(monthly.index, monthly["amount"], label="Spending")

ax1.set_title("Income vs Spending Over Time")
ax1.legend(loc="upper left",
           fontsize=8,
           borderpad=0.3
)
ax1.tick_params(axis='both', labelsize=5)

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig1, use_container_width=False)

# -----------------------------
# 💰 BALANCE TREND
# -----------------------------
st.subheader("💰 Balance Over Time")

st.line_chart(df.set_index("date")["balance"])

# -----------------------------
# 📉 MONTHLY TREND + FORECAST
# -----------------------------
st.subheader("📉 Spending Trend (with Moving Average)")

fig2, ax2 = plt.subplots(figsize=(5,3))

ax2.plot(monthly.index, monthly["amount"], label="Actual Spending")
ax2.plot(
    monthly.index,
    monthly["amount"].rolling(3).mean(),
    label="3-Month Avg"
)
ax2.set_title("Spending Trend")
ax2.legend(loc="upper left",
           fontsize=8,
           borderpad=0.3
)
ax2.tick_params(axis='both', labelsize=5)

plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig2, use_container_width=False)

# -----------------------------
# 🔝 TOP 3 CATEGORY TRENDS
# -----------------------------
st.subheader("🔥 Top 3 Category Trends")

top_categories = category_summary.nlargest(3).index
st.line_chart(category_trend[top_categories])

# -----------------------------
# 🧠 INSIGHTS
# -----------------------------
st.subheader("🧠 Insights")

# Financial status
if df["balance"].iloc[-1] > df["balance"].mean():
    st.success("📈 Your financial position is improving")
else:
    st.warning("⚠️ Your financial position is declining")

# Overspending
if monthly["savings"].mean() < 0:
    st.error("⚠️ You are consistently overspending")
else:
    st.success("✅ You are saving on average")

# Daily average
st.write(f"📊 Average daily spending: {df['amount'].mean():,.2f}")

# Highest expense
highest_day = df.loc[df["amount"].idxmax()]
st.write("💸 Highest spending transaction:")
st.write(highest_day)

# Volatility
st.write(f"📉 Spending volatility: {df['amount'].std():,.2f}")

# Correlation
st.write("🔗 Income vs Spending Correlation:")
st.write(df[["income", "amount"]].corr())

# Recurring expenses
st.subheader("🔁 Recurring Expenses")
recurring = df["description"].value_counts()
recurring = recurring[recurring > 5]
st.write(recurring)