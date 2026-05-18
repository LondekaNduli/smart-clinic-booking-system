#Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from xgboost import XGBRegressor
import plotly.express as px

#Read file
df = pd.read_csv("sales_data.csv")

#Data Exploration
print(df.head())
print(df.info())
print(df.describe())

# Check missing values
print(df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Convert date
df['Date'] = pd.to_datetime(df['Date'])

print(df.shape)

#Create time Features
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df['Weekday'] = df['Date'].dt.weekday
df['Quarter'] = df['Date'].dt.quarter
df['Weekend'] = df['Weekday'].apply(lambda x: 1 if x >= 5 else 0)
print(df)

#Line graph on Monthly sales
monthly_sales = df.groupby('Month')['Revenue'].sum()

plt.figure(figsize=(12,6))
plt.plot(monthly_sales.index, monthly_sales.values)

plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")

plt.show()

# Sort data first
df = df.sort_values(by='Date')

# Lag features
df['Lag_1'] = df['Revenue'].shift(1)
df['Lag_7'] = df['Revenue'].shift(7)
df['Lag_30'] = df['Revenue'].shift(30)

# Rolling averages
df['Rolling_Mean_7'] = df['Revenue'].rolling(window=7).mean()
df['Rolling_Mean_30'] = df['Revenue'].rolling(window=30).mean()

# Rolling standard deviation
df['Rolling_STD_7'] = df['Revenue'].rolling(window=7).std()

# Convert categorical columns
df = pd.get_dummies(df, columns=[
    'Store',
    'Product',
    'Category',
    'Promotion',
    'Holiday',
    'Region'
], drop_first=True)

#Drop missing values
df.dropna(inplace=True)

print(df.shape)

#Prepare Data for Forecasting, separate features and target.

X = df.drop(columns=['Date', 'Revenue'])

y = df['Revenue']

split_index = int(len(df) * 0.8)

X_train = X[:split_index]
X_test = X[split_index:]

y_train = y[:split_index]
y_test = y[split_index:]


#Train XGBoost Model
model = XGBRegressor(
    n_estimators=300,
    learning_rate=0.05,
    max_depth=8,
    random_state=42
)

model.fit(X_train, y_train)

#Make Predictions
predictions = model.predict(X_test)
print(predictions[:5])

#Evaluate Model
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

mae = mean_absolute_error(y_test, predictions)

rmse = mean_squared_error(
    y_test,
    predictions
) ** 0.5

r2 = r2_score(y_test, predictions)

print(f"MAE: {mae}")
print(f"RMSE: {rmse}")
print(f"R2 Score: {r2}")

#Actual vs Predicted Graph
plt.figure(figsize=(14,6))

actual = y_test.reset_index(drop=True)
predicted = pd.Series(predictions)

plt.plot(
    actual[:200],
    label='Actual Revenue',
    linewidth=3
)

plt.plot(
    predicted[:200],
    label='Predicted Revenue',
    linestyle='--'
)

plt.title("Actual vs Predicted Revenue")
plt.xlabel("Observations")
plt.ylabel("Revenue")

plt.legend()

plt.show()

#Create future data
future_dates = pd.date_range(
    start=df['Date'].max(),
    periods=31,
    freq='D'
)[1:]

future_df = pd.DataFrame({
    'Date': future_dates
})

#Create Future Time Features
future_df['Year'] = future_df['Date'].dt.year
future_df['Month'] = future_df['Date'].dt.month
future_df['Day'] = future_df['Date'].dt.day
future_df['Weekday'] = future_df['Date'].dt.weekday
future_df['Quarter'] = future_df['Date'].dt.quarter
future_df['Weekend'] = future_df['Weekday'].apply(
    lambda x: 1 if x >= 5 else 0
)

#Add Forecast Features
future_df['Lag_1'] = df['Revenue'].iloc[-1]
future_df['Lag_7'] = df['Revenue'].iloc[-7]
future_df['Lag_30'] = df['Revenue'].iloc[-30]

future_df['Rolling_Mean_7'] = df['Revenue'].rolling(7).mean().iloc[-1]
future_df['Rolling_Mean_30'] = df['Revenue'].rolling(30).mean().iloc[-1]

future_df['Rolling_STD_7'] = df['Revenue'].rolling(7).std().iloc[-1]

#match dummy columns
missing_cols = set(X_train.columns) - set(future_df.columns)

for col in missing_cols:
    future_df[col] = 0

future_df = future_df[X_train.columns]

#predict future revenue
future_predictions = model.predict(future_df)

print(future_predictions[:5])

#Plot future forecast
plt.figure(figsize=(14,6))

plt.plot(
    future_dates,
    future_predictions,
    marker='o'
)

plt.title("30-Day Revenue Forecast")
plt.xlabel("Date")
plt.ylabel("Predicted Revenue")

plt.xticks(rotation=45)

plt.show()


#Plot feature importance
importance = pd.DataFrame({
    'Feature': X_train.columns,
    'Importance': model.feature_importances_
})

importance = importance.sort_values(
    by='Importance',
    ascending=False
)

print(importance.head(10))

#visualize feature importance
top_features = importance.head(10)

plt.figure(figsize=(10,6))

plt.barh(
    top_features['Feature'],
    top_features['Importance']
)

plt.title("Top 10 Important Features")

plt.gca().invert_yaxis()

plt.show()

#Revenue Trend Interactive Chart
monthly_revenue = df.groupby('Month')['Revenue'].sum().reset_index()

fig = px.line(
    monthly_revenue,
    x='Month',
    y='Revenue',
    title='Interactive Monthly Revenue Trend',
    markers=True
)

fig.show()


#Forecast Interactive Chart
forecast_df = pd.DataFrame({
    'Date': future_dates,
    'Forecasted_Revenue': future_predictions
})

fig = px.line(
    forecast_df,
    x='Date',
    y='Forecasted_Revenue',
    title='30-Day Revenue Forecast',
    markers=True
)

fig.show()

#interactive category analysis
category_sales = df.groupby('Category_Accessories')['Revenue'].sum().reset_index()

fig = px.bar(
    category_sales,
    x='Category_Accessories',
    y='Revenue',
    title='Revenue by Category'
)

fig.show()
