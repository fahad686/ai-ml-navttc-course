import pandas as pd
import numpy as np

df=pd.read_csv('water_potability.csv')
print(df.head())
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())
# print(df['Potability'].value_counts())

##getting null values with true 
df.isna().sum()
print(df['Potability'].value_counts())

#update null value with average value
df_water=df.fillna(df.mean())
print(f'check update with null data: {df_water}')