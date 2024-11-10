"""
============================
5.9 pivot vs melt
============================
"""
import time
import pandas as pd

print(time.asctime())
print(pd.__version__)

# %%

url = "https://danepubliczne.imgw.pl/data/dane_pomiarowo_obserwacyjne/dane_hydrologiczne/dobowe/2020/codz_2020_01.zip"

df = pd.read_csv(
    url, compression='zip', encoding="ISO-8859-1",  engine='python', 
    on_bad_lines="skip",
    names=['stn_id', 'year', 'day', 'q_cms', 'month'],
    usecols=[0, 3, 5, 7, 9]
    )

df.index = pd.to_datetime(pd.DataFrame({
    'year': df.pop('year'),
    'month': df.pop('month'),
    'day': df.pop('day'),
}))

df

# %%

print(df.shape)

# %%
len(df['stn_id'].unique())

# %%

pivoted_table = df.pivot_table(index=df.index, columns="stn_id", values="q_cms")

pivoted_table

# %%

pivoted_table.shape

# %%

pivoted_table.columns

# %%

len(pivoted_table.columns)

# %%
# Melt
# ====

melted_table = df.melt(id_vars=["stn_id"], value_vars=["q_cms"])

melted_table
