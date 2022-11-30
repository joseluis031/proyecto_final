import csv
import numpy as np
import seaborn as sns
import pandas as pd
print("ej 1")
houses = pd.read_csv("regression_data.csv")
print(houses.head())

fila = ["id","date","bedrooms","bathrooms","sqft_living","sqft_lot",
        "floors","waterfront","view","condition","grade","sqft_above",
        "sqft_basement","yr_built","yr_renovated","zipcode","lat","long",
        "sqft_living15","sqft_lot15","price"]
x = houses.columns
houses.columns = fila
houses.loc[0] = x
print(houses.head())


print("ej 2")

houses.drop(["date"],axis=1,inplace = True)
print(houses.head())

print("ej 3")

print(len(houses.axes[0]))

print("ej 4")

print(houses["bedrooms"].unique())
print(houses["bathrooms"].unique())
print(houses["floors"].unique())
print(houses["condition"].unique())
print(houses["grade"].unique())



print("ej 5")

a =houses.sort_values(houses["price"],ascending= False)
print(a.head())


print("ej 6")

print(houses["price"].mean())

