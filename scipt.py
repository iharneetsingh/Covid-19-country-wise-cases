import requests
from bs4 import BeautifulSoup

data = {}
URL = 'https://www.worldometers.info/coronavirus/'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# Entire Table
dataTable = soup.find(id='main_table_countries_today')
tbody = dataTable.find('tbody')

trs = tbody.find_all('tr')
for tr in trs:
    countryDetail = tr.find_all('td')
    countryName = countryDetail[0].text.strip()
    totalDeath = countryDetail[3].text
    totalRecovered = countryDetail[5].text.strip()
    activeCases = countryDetail[6].text.strip()
    data[countryName] = [activeCases, totalRecovered, totalDeath]

'''
for key in data:
    print(key , "  ->  ", data[key][0], ", ", data[key][1], ", ", data[key][2])
'''
print('****************************')
print('******** COVID-19 **********')
print('****************************')
wantToQ = True
while(wantToQ):
    countryNameInput = input('Enter name of your country: ')
    print('---------------------------')
    print('🤒 Active Cases in '+ countryNameInput+ " : " +data[countryNameInput][0])
    print('😊 Recovered Cases in '+ countryNameInput+ " : " +data[countryNameInput][1])
    print('💀 Fatal Cases in '+ countryNameInput+ " : " + data[countryNameInput][2])
    ask = input('\nDo you want check cases in some other country ? ')
    if ask == 'N' or 'n' or 'no':
        wantToQ = False