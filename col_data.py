import requests
from bs4 import BeautifulSoup
import pickle

# grabbing the links to all of the cities. Stored in hrefs
r = requests.get("https://www.erieri.com/cost-of-living/canada/ontario")
print(f"Status Code: {r.status_code}")
soup = BeautifulSoup(r.text, 'html.parser')
h2_tags = soup.find_all('h2')
hrefs = []
for tag in h2_tags:
    if tag.text == 'A':
        a_tag = tag.find_next('a')
        run = True
        while run:
            href = a_tag.get('href')
            hrefs.append(href)
            a_tag = a_tag.find_next('a')
            if "acton" in str(a_tag).lower():  # <a class="green" href="/cost-of-living/canada/ontario/acton">Acton</a>
                run = False
                break
        break


# usuing hrefs links to grab the city name and col percentage difference from avg canadian city. Fills col_data
col_data = {}
for href in hrefs:
    r = requests.get(f"https://www.erieri.com{href}")
    soup = BeautifulSoup(r.text, 'html.parser')
    city = href.split("/")[-1].strip()
    percentages = soup.find_all('div', {'class': 'dsp-tbl-cel comparison-data-label fnt-wt-bld'})
    percentage_txt = percentages[0].text
    percentage = percentage_txt.split(" ")[1].strip()
    col_data[city] = percentage

# saving col_data to file so we don't have to run this again
with open('col_data.pickle', 'wb') as handle:
    pickle.dump(col_data, handle, protocol=pickle.HIGHEST_PROTOCOL)
