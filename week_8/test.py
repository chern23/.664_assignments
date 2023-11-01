import requests
from bs4 import BeautifulSoup
import time

# URL of the Phillips Collection with the specified filters
url = "https://www.phillipscollection.org/collection?filters%5Bon_view%5D=1&filters%5Bperiod%5D=Nineteenth-century&filters%5Bhas_image%5D=1"

# Send a request to the website and get the content
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find all the artworks displayed on the page
artworks = soup.find_all("p", class_="artwork")
print(artworks)

# # Extract artist names and artwork titles and store them in an array
# artwork_names = []
# for artwork in artworks:
#     artist = artwork.find("p", class_="artist").text.strip()
#     title = artwork.find("p", class_="title").text.strip()
#     artwork_names.append(f"{title} ({artist})")

# # Print the array of artwork names
# print(artwork_names)

# # Add a small delay before exiting to avoid being blocked
# time.sleep(0.25)