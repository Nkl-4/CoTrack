from bs4 import BeautifulSoup
import requests as re 
import pandas as pd
import matplotlib.pyplot as plt

url="https://www.mohfw.gov.in/"

#GET req to fetch data 
html_content = re.get(url).text

#parsing html content 
soup = BeautifulSoup(html_content, "lxml")

data = []
headers = []
table_div = soup.find('div', {'id':'cases'})
table = table_div.find('table')

head = table.find_all('th')
for h in head:
    headers.append(h.text.strip())

table_body = table.find("tbody")
rows  = table_body.find_all('tr')

data.append(headers)

for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

data[-1].insert(0,28)
df = pd.DataFrame(data)

#df.to_csv('temp.csv', encoding='utf-8', index=False)
print(df.iloc[1])