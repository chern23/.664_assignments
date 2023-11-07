import requests
import cloudscraper
from bs4 import BeautifulSoup
import time


artist_names = []
i = 0 #image

while i <= 2: 
    #to slow down cloudscraper
    time.sleep(0.25)
    url = f"https://www.phillipscollection.org/collection?on_view=1&has_image=1&field_period_target_id[86]=86&page={i}" 
    i+=1 #adding increment

    scraper = cloudscraper.create_scraper() 
    page = scraper.get(url)

    # response = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    artworks = soup.find_all("div", {"class" : "grid__content"})

# Extract artist names and artwork titles and store them in an array
    for artwork in artworks:
        artist = artwork.find('p')
        title = artist.find('a').text.strip()

        artist_names.append(title)

print(artist_names)