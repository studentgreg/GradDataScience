import pandas as pd
import plotly.express as px

df2 = pd.read_csv("logs/starbucks_drinkMenu_expanded.csv")

print("******************** EDA  *********************")

print(df2)
print(df2.head()) # display the first 5 rows
print(df2.tail()) # display the last 5 rows
print(df2.columns)
print(df2.info())
print(df2.describe()) # descriptive statistics is one of the first things we do with a dataset
print(df2[["Beverage","Caffeine (mg)","Sodium (mg)"]]) # this is how we select multiple columns at once
print(df2.loc[0]) # accessing one specific row with ALL the columns
print(df2.loc[[20,45]]) # accessing multiple rows with ALL the columns
print(df2.loc[[20,45],["Beverage","Caffeine (mg)"]]) # accessing some rows with specific columns

print("******************** Missing Values  *********************")

# The usual way to find missing values:

print(df2.isna()) # returns a table with true of false where true is a missing value

print(df2.isna().sum()) # returns the number of missing values for each column

# Can you filter the table to display only beverages with calories below 100

print(df2[df2["Calories"]<100])

condition2 = ((df2["Calories"]) < 100 & (df2["Caffeine (mg)"] < 50))
print(df2[condition2])

category_calories_mean = df2.groupby("Beverage_category")["Calories"].mean()
print(category_calories_mean)
# %%
print(df2.columns)
# %%
df_filtered = df2[['Calories',
       'Total Fat (g)', 'Trans Fat (g)', 'Saturated Fat (g)', 'Sodium (mg)',
       'Total Carbohydrates (g)', 'Cholesterol (mg)', 'Dietary Fibre (g)',
       'Sugars (g)', 'Protein (g)', 'Vitamin A (% DV)', 'Vitamin C (% DV)',
       'Calcium (% DV)', 'Iron (% DV)', 'Caffeine (mg)']]
print(df_filtered.head())
# %%
corr=df_filtered.corr()

fig = px.imshow(
    corr,
    text_auto=True,
    # color_continuous_scale="RdBu",
    zmin=-1,
    zmax=1,
    title="Correlation Matrix Heatmap"
)

fig.show()