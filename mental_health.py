import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("mental_health.csv")
print(df.head())

df.info()


plt.figure(figsize=(8, 5))
plt.scatter(df["academic_performance"], df["anxiety_level"])
plt.title("Academic perfomance vs anxiety")
plt.xlabel("academic level")
plt.ylabel("anxiety")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#Features and target 
X = df.drop("pass", axis=1)
y = df["pass"]

#train_test_split
#split model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) 

#train model
model = LogisticRegression()
model.fit(X_train, y_train)

#predict model
y_pred = model.predict(X_test)

#Evaluate
# print("Accuracy:", accuracy_score(y_test, y_pred))
# print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

print(y_test)