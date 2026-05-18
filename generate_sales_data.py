import pandas as pd
import numpy as np

# Reproducibility
np.random.seed(42)

# Date range
dates = pd.date_range(start='2022-01-01', end='2025-12-31', freq='D')

# Categories
stores = ['Store_A', 'Store_B', 'Store_C', 'Store_D']
products = ['Laptop', 'Phone', 'TV', 'Tablet', 'Headphones', 'Keyboard']
categories = {
    'Laptop': 'Electronics',
    'Phone': 'Electronics',
    'TV': 'Electronics',
    'Tablet': 'Electronics',
    'Headphones': 'Accessories',
    'Keyboard': 'Accessories'
}

regions = ['KZN', 'Gauteng', 'Western Cape', 'Free State']

data = []

for date in dates:
    for store in stores:
        for product in products:

            # Base sales
            units = np.random.randint(10, 80)

            # Seasonal effect
            if date.month in [11, 12]:
                units += np.random.randint(20, 50)

            # Weekend effect
            if date.weekday() >= 5:
                units += np.random.randint(5, 15)

            # Promotion effect
            promotion = np.random.choice(['Yes', 'No'], p=[0.3, 0.7])

            if promotion == 'Yes':
                units += np.random.randint(10, 25)

            # Holiday effect
            holiday = np.random.choice(['Yes', 'No'], p=[0.05, 0.95])

            if holiday == 'Yes':
                units += np.random.randint(20, 40)

            # Prices
            prices = {
                'Laptop': 15000,
                'Phone': 12000,
                'TV': 9000,
                'Tablet': 7000,
                'Headphones': 800,
                'Keyboard': 600
            }

            unit_price = prices[product]

            revenue = units * unit_price

            temperature = np.random.randint(18, 36)

            data.append([
                date,
                store,
                product,
                categories[product],
                units,
                unit_price,
                revenue,
                promotion,
                holiday,
                temperature,
                np.random.choice(regions)
            ])

# Create dataframe
df = pd.DataFrame(data, columns=[
    'Date',
    'Store',
    'Product',
    'Category',
    'Units_Sold',
    'Unit_Price',
    'Revenue',
    'Promotion',
    'Holiday',
    'Temperature',
    'Region'
])

# Save CSV
df.to_csv('sales_data.csv', index=False)


print(df.head())
print(df.shape)