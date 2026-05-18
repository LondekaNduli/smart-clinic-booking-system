import pandas as pd
import matplotlib.pyplot as plt
#you can import straight from other file instead of copy and paste of data
# e.g import file name, then choose exactly by filename.whatyouwant e.g quantity= project.quantity_list
df = pd.read_excel("data.xlsx")
print(df.head())

dq = pd.read_excel("data.xlsx",
                   usecols = ["Price"]
)
print(dq)


#line graph
plt.figure(figsize=(8, 5))
plt.plot(df["Fruits"], df["Price"])
plt.title("Fruits by Prices")
plt.xlabel("Fruits")
plt.ylabel("Prices")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



plt.figure(figsize=(8, 5))
plt.bar(df["Fruits"], df["Price"])
plt.title("Fruits by Prices")
plt.xlabel("Fruits")
plt.ylabel("Prices")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 5))
plt.pie(df["Quantity"], labels=df["Fruits"], autopct='%1.1f%%')
plt.title("Fruits Quantity")
plt.legend(df["Fruits"], title="Fruits", loc="center left", bbox_to_anchor=(1, 0.5))
plt.show()

plt.fill_between(df["Fruits"], df["Quantity"])
plt.title("Fruit Quantity Area Chart")
plt.show()


plt.scatter(df["Price"], df["Quantity"])
plt.title("Prices vs Quantity")
plt.xlabel("Prices")
plt.ylabel("Quantities")
plt.show()
