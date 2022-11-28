import csv
import numpy as np
import seaborn as sns
import pandas as pd

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


print()

houses.drop(["date"],axis=1,inplace = True)
print(houses.head())
