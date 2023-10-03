#import csv

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

#PULL NATIONALITY BE
# country_count = {}
# with open('Artworks.csv') as file:
#     csv_file = csv.DictReader(file)
#     for line in csv_file:
#         nationalities = line['Nationality']
#         for nat in nationalities.split(' '):
#             country_count[nat] = country_count.setdefault(nat,0) + 1

# print(country_count['(Belgian)'])


# nat_count = {}

# # setdefault is a special method that prevents the system from crashing by returning the default value
# with open('Artworks.csv') as artworks_file:
#     artworks_csv_file = csv.DictReader(artworks_file)
#     for artwork in artworks_csv_file:
#         nat_list_for_artwork = artwork["Nationality"].split(" ")
#         for nat in nat_list_for_artwork:
#             nat_count[nat] = nat_count.setdefault(nat, 0) + 1

# print(nat_count)


# remember to close all files at the end 

import csv

# nationality_count = {}

# with open('Artworks.csv') as file:
#   processed_csv = csv.DictReader(file)
#   for row in processed_csv:
#     nationalities_str = row['Nationality']
#     nationalities = nationalities_str.split(' ')
#     for nat in nationalities:
#       nationality_count[nat] = nationality_count.setdefault(nat,0) + 1

# print(nationality_count)


# INSTRUCTIONS: create a file for each nationality with all of the artworks for those people in one file
    

nat_list = {}

# WRONG
# with open('Artworks.csv') as art_file:
#     with open('Nationalities.csv', 'w') as nat_file:
#         processed_csv = csv.DictReader(art_file)
#         csv_nat = csv.DictWriter(nat_file, fieldnames=processed_csv.fieldnames)
#         print(processed_csv.fieldnames)
#         csv_nat.writeheader()
#         for nat in processed_csv:
#             print(nat)
#             if nat['Artwork'] == 'Nationality':
#                 csv_nat.writerow(nat)

# ALSO WRONG
     # Artworks = []
        # for row in processed_csv:
        #     record = {}
        #     for i, value  in enumerate(row):
        #         record[processed_csv[i]] = value
        #     Artworks.append(record)

with open('Artworks.csv') as art_file:
        processed_csv = csv.DictReader(art_file)
        for artwork in processed_csv:
            nationalities_str = artwork['Nationality']
            nationalities_list = nationalities_str.split(' ')
            for nat in nationalities_list:
                 # create a new file for nationality if that file does not exist yet
                 # write my artwork to the file
               if nat_list.get(nat) is None:
                # file does not exist yet
                nat_file = open(f'art_nationalities_files/{nat}.csv', 'w')
                # need to create a dicrtionary writer
                nat_dict_writer = csv.DictWriter(nat_file, processed_csv.fieldnames)
                # nat_files[nat] = {'file': nat_file, 'nat_dict_writer': nat_dict_writer}
                nat_dict_writer.writeheader()
                nat_dict_writer.writerow(artwork)
                nat_list[nat] = True
               else: 
                # file exists   
                nat_file = open(f'art_nationalities_files/{nat}.csv', 'a')
                nat_dict_writer = csv.DictWriter(nat_file, processed_csv.fieldnames)
                nat_dict_writer.writerow(artwork)
            
            

                