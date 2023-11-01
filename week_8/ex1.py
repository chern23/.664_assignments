import requests
import cloudscraper
from bs4 import BeautifulSoup
import csv
import time

links = [] # move the dict to the top of the list
i = 1 #image

while i <= 1: 
    #to slow down cloudscraper
    time.sleep(0.25)
    page_url = f"https://collection.artbma.org/objects/images?page={i}&perpage=10" f"https://www.phillipscollection.org/collection"
    # https://www.phillipscollection.org/collection?on_view=1&has_image=1&field_period_target_id[86]=86
    i+=1 #adding increment
    print(page_url)
    #same as request.get
    scraper = cloudscraper.create_scraper() 
    page = scraper.get(page_url)
    page = requests.get(page_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    primary_media_elements = soup.find_all("span")
    for div_elem in primary_media_elements:
        link_elem = div_elem.find('a')
        link = link_elem.attrs['href']
        links.append(link)

# print(len(links)) #links is a list, we will loop through it

result_art = []
# print(links)

for link in links:
    print(link)
    time.sleep(0.25)
    art_url = f"https://collection.artbma.org{link}"
    print(art_url)
    page = requests.get(art_url)
    soup = BeautifulSoup(page.text, 'html.parser')

    #to pull all the code from the page
    # print(soup.prettify()) 

    title = soup.find('h1').text
    artist_area = soup.find('div', {'class': 'detailField peopleField'})
    artist_name = artist_area.find('span', {'itemprop': 'name'}).text.strip() 
    date = soup.find('span', {'itemprop': 'dateCreated'}).text.strip() 
    medium = soup.find('span', {'itemprop': 'artMedium'}).text.strip() 
    #strip removes trailing white space

    art_dict = {
        'title': title,
        'artist': artist_name,
        'date': date,
        'medium': medium
    }
    print(art_dict)
    result_art.append(art_dict)
print(result_art)

with open('bma_art_in_class.csv', 'w') as file:
    csv_file = csv.DictWriter(file, fieldnames=result_art[0].keys())
    csv_file.writeheader()
    csv_file.writerows(result_art) 

print(soup.prettify()) 