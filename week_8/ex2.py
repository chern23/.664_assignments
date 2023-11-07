import requests
import cloudscraper
from bs4 import BeautifulSoup
import time

links = []
i = 0  # image

while i <= 2:
    # to slow down cloudscraper
    time.sleep(0.25)
    url = f"https://www.phillipscollection.org/collection?on_view=1&has_image=1&field_period_target_id[86]=86&page={i}"
    i += 1  # adding increment

    scraper = cloudscraper.create_scraper()
    page = scraper.get(url)

    soup = BeautifulSoup(page.text, "html.parser")
    artworks = soup.find_all("div", {"class": "grid__content"})

    for artwork in artworks:
        link = artwork.find("a")["href"]
        links.append(link)

result_art = []

for link in links:
    time.sleep(0.25)
    art_url = f"https://www.phillipscollection.org{link}"
    page = requests.get(art_url)
    soup = BeautifulSoup(page.text, "html.parser")

    title = soup.find("h1", {"class": "collection-header__title"}).text.strip()
    # artist = soup.find("span", {"class": "collection-meta__value"}).text.strip()

    # First attempt - got H
    material = soup.find("span", {"class": "collection-meta__value"}).text.strip()[2]
    dimensions = soup.find("span", {"class": "collection-meta__value"}).text.strip()[3]

    # # Got ALL values in ul 1
    # material = soup.find("ul", {"class": "collection-meta flex-layout__item"}).text.strip()
    # dimensions = soup.find("ul", {"class": "collection-meta flex-layout__item"}).text.strip()
    
    # ## Loooking within dictionaries - got H
    # content_area = soup.find("div", {"class": "flex-layout"})
    # material_area = content_area.find("ul", {"class": "collection-meta flex-layout__item"})
    # material = material_area.find("span", {"class": "collection-meta__value"}).text.strip()[2]
    # # dimensions = material_area.find("ul", {"class": "collection-meta flex-layout__item"}).text.strip()
    


    art_dict = {
        "title": title,
        "material": material,
        "dimensions": dimensions,
    }
    result_art.append(art_dict)

print(result_art)