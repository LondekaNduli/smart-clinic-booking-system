import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
df["balance"] = df["income"] - df["amount"]


df.to_csv("expenses_large.csv", index=False)

print(df.head(100))

#grouping categories
category_summary = df.groupby("category")["amount"].sum().sort_values()


#Bargraph, spending by category
category_summary.plot(kind="bar")

plt.title("Spending by Category (Least to Most)")
plt.xlabel("Category")
plt.ylabel("Total Amount Spent")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

least_category = category_summary.idxmin()
most_category = category_summary.idxmax()

print("Least spent on:", least_category)
print("Most spent on:", most_category)



# Group by month
df["month"] = df["date"].dt.to_period("M")

monthly = df.groupby("month").agg({
    "income": "sum",
    "amount": "sum"
})

monthly.plot(kind="line", marker="o")
plt.title("Income vs Spending Over Time")
plt.xlabel("Month")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Area chart, financial strain
monthly.plot(kind="area", alpha=0.5)
plt.title("Income vs Spending (Area View)")
plt.show()

#monthly balance trend
df["month"] = df["date"].dt.to_period("M")
monthly_balance = df.groupby("month")["balance"].last()

monthly_balance.plot(kind="line", marker="o")
plt.title("Monthly Ending Balance")
plt.show()

#top 3 categories spending trends over time
df["month"] = df["date"].dt.to_period("M")

category_trend = df.pivot_table(
    values="amount",
    index="month",
    columns="category",
    aggfunc="sum"
)

top_categories = df.groupby("category")["amount"].sum().nlargest(3).index

filtered = category_trend[top_categories]

filtered.plot(figsize=(10,5))

plt.title("Top 3 Spending Categories Over Time")
plt.legend(loc='upper left')
plt.show()

category_trend.plot(subplots=True, figsize=(10,8), layout=(3,2), sharex=True)
plt.suptitle("Category Trends (Separate Views)")
plt.tight_layout()
plt.show()


if df["balance"].iloc[-1] > df["balance"].mean():
    print("📈 Your financial position is improving")
    
#Average spending per day   
daily_avg = df["amount"].mean()
print(daily_avg)

print("##################################################################################################")

#Highest spending day
highest_day = df.loc[df["amount"].idxmax()]
print(highest_day)

#Savings Rate
monthly["savings"] = monthly["income"] - monthly["amount"]
monthly["savings_rate"] = (monthly["savings"] / monthly["income"]) * 100

if monthly["savings"].mean() < 0:
    print("⚠️ You are consistently overspending")

if df.groupby("category")["amount"].sum().idxmax() == "Food":
    print("🍔 Most of your money goes to Food")

#budget vs actual
budget = {
    "Food": 2000,
    "Transport": 1000,
    "Entertainment": 800
}

df["budget"] = df["category"].map(budget)
df["over_budget"] = df["amount"] > df["budget"]
print(df)

#Recurring Expenses Detection
recurring = df["description"].value_counts()
recurring = recurring[recurring > 5]
print(recurring)

#Spending volatility: High = unpredictable spending, Low = stable spending
volatility = df["amount"].std()
print(volatility)

#Predict future spendings
plt.figure(figsize=(10,5))

# Actual spending
plt.plot(monthly.index.astype(str), monthly["amount"], label="Actual Spending")

# Rolling average (trend)
plt.plot(monthly.index.astype(str),
         monthly["amount"].rolling(3).mean(),
         label="3-Month Moving Average")

plt.title("Monthly Spending Trend")
plt.xlabel("Month")
plt.ylabel("Amount")

plt.xticks(rotation=45)

plt.legend()
plt.tight_layout()
plt.show()

correlation = df[["income", "amount"]].corr()
print(correlation)