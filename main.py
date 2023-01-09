import os
import pandas as pd

directory = './src/'

df_list = []

for file in os.listdir(directory):
    if file.endswith('.xlsx'):
        df = pd.read_excel(os.path.join(directory, file))
        df = df.loc[df['Язык'] == 'javascript']
        df = df.loc[df['Название проекта'].isin(['Игры разума', 'Brain Games'])]
        df_list.append(df)

result = pd.concat(df_list)

result.to_excel('merged_result.xlsx', index=False)
