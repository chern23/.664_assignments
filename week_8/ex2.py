import requests
from bs4 import BeautifulSoup
import time

result_art = []
i = 0  # image

while i <= 2:
    time.sleep(0.25)
    url = f"https://www.phillipscollection.org/collection?on_view=1&has_image=1&field_period_target_id[86]=86&page={i}"
    soup = BeautifulSoup(requests.get(url).content, "html.parser")

    artworks = soup.find_all("div", {"class": "grid__content"})

    for artwork in artworks:
        artwork_url = "https://www.phillipscollection.org" + artwork.find("a")["href"]
        artwork_soup = BeautifulSoup(requests.get(artwork_url).content, "html.parser")
        subtitles = artwork_soup.find_all("p", class_="collection-header__subtitle")
        artist = subtitles[0].find("a").text.strip()
        meta_values = artwork_soup.find_all("span", class_="collection-meta__value")
        material = meta_values[2].text.strip()
        dimensions = meta_values[4].text.strip()
        art_dict = {
        "artist": artist,
        "material": material,
        "dimensions": dimensions,
        }
        result_art.append(art_dict)

    i += 1  

print(result_art)