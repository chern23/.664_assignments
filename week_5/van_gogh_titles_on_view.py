# in the `week_5` folder create a python script named `van_gogh_titles_on_view.py`
# mimic the bavior of the previous script, search for all the van gogh related objects that are on view and have images
# for each of these objects, use the api to get more details of the object
# create a list of all the object titles for these objects
# print the list

# https://collectionapi.metmuseum.org/public/collection/v1/search?isOnView=true&q=sunflower


import requests
import json

# API endpoint URLs
search_api_url = "https://collectionapi.metmuseum.org/public/collection/v1/search"
object_api_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects"

# Parameters for the search query
search_params = {
    "q": "van gogh",
    "isOnView": True,
    "hasImages": True
}

# Make a GET request to the MET's search API
search_response = requests.get(search_api_url, params=search_params)

# Check if the search request was successful
if search_response.status_code == 200:
    # Parse the JSON response
    search_data = search_response.json()
    object_ids = search_data.get("objectIDs", [])

    # List to store object titles
    object_titles = []
    
    # Iterate over each object ID and fetch object details
    for object_id in object_ids:
        object_response_url = f"{object_api_url}/{object_id}"
        object_response = requests.get(object_response_url)
        
        # Check if the object request was successful
        if object_response.status_code == 200:
            # Parse the JSON response for object details
            object_data = object_response.json()
            title = object_data.get("title", "Title not available")
            object_titles.append(title)
        else:
            object_titles.append("Title not available")
    
    # for title in object_titles:
    #     print(title)

else:
    print(f"Error: Unable to fetch data from API. Status code: {search_response.status_code}")

print(object_titles)
