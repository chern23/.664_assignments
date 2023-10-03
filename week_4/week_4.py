import csv

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

with open('week_4/Artworks.csv') as art_file:
        processed_csv = csv.DictReader(art_file)
        for artwork in processed_csv:
            nationalities_str = artwork['Nationality']
            nationalities_list = nationalities_str.split(' ')
            for nat in nationalities_list:
                 # create a new file for nationality if that file does not exist yet
                 # write my artwork to the file
               if nat_list.get(nat) is None:
                # file does not exist yet
                nat_file = open(f'week_4/res/{nat}.csv', 'w')
                # need to create a dicrtionary writer
                nat_dict_writer = csv.DictWriter(nat_file, processed_csv.fieldnames)
                # nat_files[nat] = {'file': nat_file, 'nat_dict_writer': nat_dict_writer}
                nat_dict_writer.writeheader()
                nat_dict_writer.writerow(artwork)
                nat_list[nat] = True
               else: 
                # file exists   
                nat_file = open(f'week_4/res/{nat}.csv', 'a')
                nat_dict_writer = csv.DictWriter(nat_file, processed_csv.fieldnames)
                nat_dict_writer.writerow(artwork)