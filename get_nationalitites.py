import csv

# #count_line = 0
# with open('Artworks.csv') as file:
#     csv_file = csv.DictReader(file)
#     for line in csv_file:
#         #count_line = count_line + 1
#         print(line['Nationality'])  -- counts nationalities

# country_count = {}
# with open('Artworks.csv') as file:
#     csv_file = csv.DictReader(file)
#     for line in csv_file:
#         country_count[line['Nationality']] = 1

# print(country_count) -- WORKS


country_count = {}
with open('Artworks.csv') as file:
    csv_file = csv.DictReader(file)
    for line in csv_file:
        nationalities = line['Nationality']
        for nat in nationalities.split(' '):
            country_count[nat] = country_count.setdefault(nat,0) + 1

print(country_count['(Belgian)'])

