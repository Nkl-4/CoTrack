import pandas as pd
import matplotlib.pyplot as plt
from datetime import date
import datascrap as ds
import os.path

if not(os.path.isfile('data.csv')):
    ds.scrap()

df = pd.read_csv('data.csv')

with open('total.txt', 'r') as f:
    s = f.readline()

dat = (s[41:].split())
df.sort_values(["Total Confirmed cases"], axis=0, ascending=[True],inplace=True)

df.plot(kind='barh',x='Name of State / UT', y='Total Confirmed cases',figsize=(18,8))
plt.title(f"{s[:40]} - {dat[0]}     Cured - {dat[1]}     Death - {dat[2]}")
plt.suptitle(f"COVID-19 India  {date.today()}")
plt.savefig('affected.png')

df.sort_values(["Death"], axis=0, ascending=[True],inplace=True)


df.plot(kind='barh',x='Name of State / UT', y='Death',figsize=(18,8))
plt.title(f"{s[:40]} - {dat[0]}     Cured - {dat[1]}      Death - {dat[2]}")
plt.suptitle(f"COVID-19 India  {date.today()}")
plt.savefig('death.png')
