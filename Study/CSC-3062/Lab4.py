import pandas as pd
df = pd.read_csv("D:\\Projects\\Pythons\\Data\\CSC-3062\\games.csv")
df = df.dropna()
df = df.reset_index(drop=True)
new_df = df.iloc[:, 1:11]
new_df['Month_Average_Sales'] = new_df['Global_Sales'] / 12
for index, row in new_df.iterrows():
    new_df.at[index, 'EU_Sales_Percentage'] = row['EU_Sales'] / row['Global_Sales'] * 100.0
