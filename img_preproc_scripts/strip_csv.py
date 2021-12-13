import pandas as pd

filename = 'C:\\Users\\jackk\\Desktop\\IOT Final Project\\toCSV\\fingers_data_colab.csv'
filename_out = 'C:\\Users\\jackk\\Desktop\\IOT Final Project\\toCSV\\fingers_data_colab_5orNothing.csv'

df = pd.read_csv(filename)
print(df.iloc[df.index,2])


df_out = df[(df.iloc[df.index,2] == '0L') | (df.iloc[df.index,2] == '0R') | (df.iloc[df.index,2] == '5L') | (df.iloc[df.index,2] == '5R')]
# print(df_out.iloc[df_out.index,2])
print(df_out)
print('done')

df_out.to_csv(filename_out, index=False)

#[1799 rows x 11 columns]