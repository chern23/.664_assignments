# WRITING CSV FILES

import csv

# with open('pets.csv') as file:
#  with open('cats.csv', 'w') as write_file:
#    processed_csv = csv.reader(file)
#    write_csv = csv.writer(write_file)
#    header = next(processed_csv,None)
#    write_csv.writerow(header)
#    for row in processed_csv:
#      if row[1] == 'cat':
#        write_csv.writerow(row)
#        print(row)

# with open('pets.csv') as pets_file:
#     with open('dogs.csv', 'w') as dogs_file:
#         csv_pets = csv.reader(pets_file)
#         csv_dogs = csv.writer(dogs_file)
#         header_row = next(csv_pets)
#         print(header_row)
#         for pet in csv_pets:
#             if pet[1] == 'dog':
#                 print(pet)
#                 csv_dogs.writerow(pet)


# writing CSV files in dictionary

with open('week_4/pets.csv') as pets_file:
    with open('dogs.csv', 'w') as dogs_file:
        csv_pets = csv.DictReader(pets_file)
        csv_dogs = csv.DictWriter(dogs_file, fieldnames=csv_pets.fieldnames)
        print(csv_pets.fieldnames)
        csv_dogs.writeheader()
        for pet in csv_pets:
            print(pet)
            if pet['Type'] == 'dog':
                csv_dogs.writerow(pet)