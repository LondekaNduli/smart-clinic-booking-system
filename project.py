import pandas as pd
import matplotlib.pyplot as plt

fruits_names= ['Apple', 'Orange', 'Grapes', 'Mango', 'Litchi'],
people_names = ['Londeka', 'Jane', 'Joshua', 'Jessica', 'Luke'],
prices = [2, 4, 6, 8, 10],
quantity = [10, 30, 40, 50, 90]

data = {
   "fruits_names": ['Apple', 'Orange', 'Grapes', 'Mango', 'Litchi'],
   "people_names": ['Londeka', 'Jane', 'Joshua', 'Jessica', 'Luke'],
   "prices": [2, 4, 6, 8, 10],
   "quantity": [10, 30, 40, 50, 90]
}

df = pd.DataFrame(data)
df["Total Cost"] = df["prices"] * df["quantity"]

#df.to_excel("project.xlsx", index=False)
print(df)


plt.figure(figsize=(8, 5))
plt.plot(df["Fruits"], df["Price"])
plt.title("Fruits by Prices")
plt.xlabel("Fruits")
plt.ylabel("Prices")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
