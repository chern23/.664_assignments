# in the `week_5` folder create a python script named `van_gogh_search.py`
# Use the MET's search API to get the object id's of all they "van gogh" related objects that are currently on view and have an image
# print the resulting json, but ensure you print it "pretty" using the `indent=2`



import requests
import json

# API endpoint URL for MET's search API
api_url = "https://collectionapi.metmuseum.org/public/collection/v1/search"

# Parameters for the search query
search_params = {
    "q": "van gogh",
    "isOnView": "true",
    "hasImages": "true"
}

# Make a GET request to the API
response = requests.get(api_url, params=search_params)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response and pretty print it
    data = response.json()
    pretty_json = json.dumps(data, indent=2)
    print(pretty_json)
