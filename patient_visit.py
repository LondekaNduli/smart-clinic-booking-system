import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("patient_visits.csv", sep = ";")

# Total revenue
print("Total Revenue:", df["Treatment_Cost"].sum())

# Visits per department
dept_counts = df["Department"].value_counts()
print(df["Department"].value_counts())

# Average cost
print(df["Treatment_Cost"].mean())

#number of visits per department, pie chart
plt.figure(figsize=(8, 6))
plt.pie(dept_counts, labels=dept_counts.index, autopct='%1.1f%%')
plt.title("Patient Visits by Department")

plt.show()

outcome_counts = df["Outcome"].value_counts()
print()

#bar graphs patients outcomes 
plt.figure(figsize=(8, 5))
plt.bar(outcome_counts.index, outcome_counts.values)
plt.title("Patient Outcomes Distribution")
plt.xlabel("Outcome")
plt.ylabel("Number of Patients")

plt.show()

outcome_dept = pd.crosstab(df["Department"], df["Outcome"])
outcome_dept.plot(kind="bar")
plt.title("Outcomes by Department")
plt.xlabel("Department")
plt.ylabel("Number of Patients")

plt.show()