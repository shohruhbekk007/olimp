import pandas as pd

# Ma'lumotlarni yaratamiz
data = {'Ism': ['John', 'Alice', 'Bob', 'Charlie'],
        'Yosh': [25, 28, 22, 35],
        'Mamlakat': ['AQSH', 'Kanada', 'Angliya', 'Avstraliya']}

# DataFrame yaratamiz
df = pd.DataFrame(data)

# DataFrame ni Excel fayliga yozamiz
df.to_excel('malumotlar.xlsx', index=False)

# Excel faylni o'qiyapmiz
# df_read = pd.read_excel('malumotlar.xlsx')

# # Natijani chop etamiz
# print(df_read)
