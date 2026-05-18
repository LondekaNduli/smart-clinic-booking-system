#Import libraries
import pandas as pd
import plotly.express as px
import numpy as np

#Read file
df = pd.read_csv("salesforcasting.csv", sep=";")
print(df.head())
print(df.shape)