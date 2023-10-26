# Write a script that will mimic the behavior of the complex csv example
# split out the art pieces into separate json files. One for each nationality e.g. `Belgian.json`
# All those files should be in a sub folder called ‘res’ (make sure you create the folder manually before running your script
# Try to give the json files an indentation of 2
# Ensure you do not commit all the files you generate to git either


import json

art_pieces_by_nationality = {}

with open('Artworks.json', 'r') as art_file:
    artwork_data = json.load(art_file)
    for art_piece in artwork_data:
        nationalities = art_piece.get('Nationality', ['Unknown'])
        for nationality in nationalities:
            if nationality not in art_pieces_by_nationality:
                art_pieces_by_nationality[nationality] = []
            art_pieces_by_nationality[nationality].append(art_piece)

    for nationality, pieces in art_pieces_by_nationality.items():
        filename = f'res/{nationality}.json'
        with open(filename, 'w') as outfile:
            json.dump(pieces, outfile, indent=2)




#DID NOT WORK

# import json


# art_pieces_by_nationality = {}

# with open('Artworks.json', 'r') as art_file:
    # artwork_data = json.load(art_file)
    # for art_piece in artwork_data:
    #     Nationality = art_piece.get('Nationality', ['Unknown'])
    #     if Nationality not in art_pieces_by_nationality:
    #         art_pieces_by_nationality[Nationality] == []
    #     art_pieces_by_nationality[Nationality].append(art_piece)

    # for Nationality, pieces in art_pieces_by_nationality.items():
    #     filename = f'week_5/res/{Nationality}.json'
    # with open(filename, 'w') as outfile:
    #     json.dump(pieces, outfile, indent=2)

# print("JSON files created successfully in the 'res' folder.")