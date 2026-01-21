import pandas as pd

df = pd.read_csv("logs/biscayne_bay_water_quality.csv")

print(df.head()) # print the first 5 rows (unless specified)
print(df.tail()) # print the last 5 rows (unless specified)

print(df.columns)
print(df.shape)

print(df.dtypes)

print(df.isna().sum()) # check how many missing values per column

print(df["Temp C"])
print("Minimum value:", df["Temp C"].min())
print("Maximum value:", df["Temp C"].max())
print("Mean value:", df["Temp C"].mean())
print("Standard deviation value:", df["Temp C"].std())


# Descriptive Statistics

print(df.describe())

# Basic Filtering
## Boolean indexing

print(df[df["Temp C"] > 24.5])

print(df[["Latitude","Longitude","TWC"]]) # to plot bathymetry for example
print(df.describe().T[["min","max","mean"]])

# Do you see potential outliers?
# Check minimum and maximum values of all parameters? Anything unusual?
# What percentage of my data is questionable?
## Domain rule: values of salinity should be above 30


invalid_salinity = df[df["Salinity"] < 30]
print(len(invalid_salinity)/len(df)*100)

clean_df = df[df["Salinity"].between(30,45)]
print(clean_df.shape)

print(clean_df[["Latitude","Longitude","Salinity"]].describe())

print(clean_df.corr(numeric_only=True))