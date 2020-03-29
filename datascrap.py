from bs4 import BeautifulSoup
import requests as re   

url="https://www.mohfw.gov.in/"

#GET req to fetch data 
html_content = re.get(url).text

#parsing html content 
soup = BeautifulSoup(html_content, "lxml")

data = []
table_div = soup.find('div', {'id':'cases'})
table = table_div.find('table')


print(table)    