import os
import pandas as pd

# Set the directory where the .xlsx files are located
directory = './src/'

# Initialize an empty list to store the data frames
df_list = []

# Iterate over all the files in the directory
for file in os.listdir(directory):
    # Only consider .xlsx files
    if file.endswith('.xlsx'):
        # Read the file into a data frame
        df = pd.read_excel(os.path.join(directory, file))
        df = df.loc[df['Язык'] == 'javascript']
        df = df.loc[df['Название проекта'].isin(['Игры разума', 'Brain Games'])]
        # Append the data frame to the list
        df_list.append(df)

# Concatenate all the data frames into a single data frame
result = pd.concat(df_list)

# Write the data frame to a new .xlsx file
result.to_excel('merged_result.xlsx', index=False)
