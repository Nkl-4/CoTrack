from bs4 import BeautifulSoup
import requests as re 
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

url="https://www.mohfw.gov.in/"

#GET req to fetch data 
html_content = re.get(url).text

#parsing html content 
soup = BeautifulSoup(html_content, "lxml")

data = []
headers = []
sname = []
Tcin = []
Tcfn = []
cured = []
death = []

table_div = soup.find('div', {'id':'cases'})
table = table_div.find('table')

head = table.find_all('th')
for h in head:
    headers.append(h.text.strip())

table_body = table.find("tbody")
rows  = table_body.find_all('tr')



#data.append(headers)

for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

#data[-1].insert(0,None)
total = data[-1]
data = data[:-1]
#print(headers)



for d in data:
    sname.append(d[1])
    Tcin.append(int(d[2]))
    Tcfn.append(int(d[3]))
    cured.append(int(d[4]))
    death.append(int(d[5]))


pdata = { 
    'Name of State / UT':sname, 
    'Total Confirmed cases (Indian National)':Tcin, 
    'Total Confirmed cases ( Foreign National )':Tcfn, 
    'Cured/Discharged/Migrated':cured, 
    'Death':death
}
df = pd.DataFrame(pdata,columns=['Name of State / UT','Total Confirmed cases (Indian National)','Total Confirmed cases ( Foreign National )','Cured/Discharged/Migrated', 'Death'])

df.to_csv('temp.csv', encoding='utf-8', index=False)

#plot graph
df.plot(kind='barh',x='Name of State / UT', y='Total Confirmed cases (Indian National)',figsize=(18,8))
plt.title(f"COVID-19 India  {date.today()}")
plt.savefig('affected.png')

df.plot(kind='barh',x='Name of State / UT', y='Death',figsize=(18,8))
plt.title(f"COVID-19 India  {date.today()}")
plt.savefig('death.png')
