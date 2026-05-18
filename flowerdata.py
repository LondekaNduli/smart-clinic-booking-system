#import pandas
import pandas as pd

#read data
xcel_file = 'Flowers_Data.xlsx'
df = pd.read_excel(xcel_file)

#print(df.head(12))
#print(df.describe())
#print(df.shape)
print(df.dtypes)