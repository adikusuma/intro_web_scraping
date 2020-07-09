import requests
from bs4 import BeautifulSoup

url = 'https://www.jadwalsholat.org/adzan/monthly.php?id=47'
contents = requests.get(url)
soup = BeautifulSoup(contents.text, "html.parser")
data = soup.find_all('tr', 'table_highlight')
data[0]

sholat = {}
i = 0
for d in data[0]:
    if i == 1:
        sholat['Imsyak'] = d.get_text()
    if i ==2:
        sholat['shubuh'] = d.get_text()
    if i == 3:
        sholat['dzuhur'] = d.get_text()
    if i == 4:
        sholat['ashar'] = d.get_text()
    if i == 5:
        sholat['maghrib'] = d.get_text()
    if i == 6:
        sholat['isya'] = d.get_text()
    i += 1

for k, v in sholat.items():
    print(k ,' : ', v)