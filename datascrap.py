from bs4 import BeautifulSoup
import requests as re 
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

url="https://www.mohfw.gov.in/"
total = []

def scrap():
    #GET req to fetch data 
    html_content = re.get(url).text

    data = []
    headers = []
    sname = []
    Tc = []
    cured = []
    death = []

    #parsing html content 
    soup = BeautifulSoup(html_content, "lxml")


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
    global total
    total = data[-1]
    data = data[:-1]
    #print(headers)
    #rint(total)

    for d in data:
        sname.append(d[1])
        Tc.append(int(d[2]))
        cured.append(int(d[3]))
        death.append(int(d[4]))


    pdata = { 
        'Name of State / UT':sname, 
        'Total Confirmed cases':Tc, 
        'Cured/Discharged/Migrated':cured, 
        'Death':death
    }
    df = pd.DataFrame(pdata,columns=['Name of State / UT','Total Confirmed cases','Cured/Discharged/Migrated', 'Death'])

    df.to_csv('data.csv', encoding='utf-8', index=False)

    s = ""

    for  ele in total:
    	s+=ele
    	s+=" "

    with open('total.txt', 'w') as f:
    	f.write(s)

    
scrap()
