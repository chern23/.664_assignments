# Reading and writing files

# with open("my_file.txt", 'w') as my_file:
#     # lines = ["hello \n", "world \n", "I know how to write a file \n"]
#     # my_file.writelines(lines) -- same result as following set
#     my_file.write("hello\n")
#     my_file.writelines("hello\n")
#     my_file.write("all of these are on their own line because of the \\n \n") 
#     # # extra \ allows '\n' to be part of text if needed

# cool_file = open("my_file.txt", 'w')
# my_file.write("hello")

# with open("my_file.txt", 'r') as my_file:
#   for line in my_file:
#     print(line)


# CSV Lists - python has a built in module, 3rd party module is called pandas
#f2 lets you highlight a variable and rename them all together
# # NOTES 
# `w` : write => it fully overwrites the file every time you “open” the file with “w” 
# `a`  : Append 
# `r`   : Read 


# import csv
# with open('pets.csv') as file:
#    processed_csv = csv.reader(file)
#    for row in processed_csv:
#       print(row)

import csv

#READER
# with open("week_4/pets.csv", 'r') as my_file:
#    csv_interpreted = csv.reader(my_file)
#    first_line = next(csv_interpreted)
# #    print(first_line)
#    for line in csv_interpreted:
#       print(line[0])

# Reading CSV using reader and DictReader


#DICTREADER
# with open("week_4/pets.csv", 'r') as my_file:
#    csv_interpreted = csv.DictReader(my_file)
#    for line in csv_interpreted:
#       if line['Type'] == 'cat':
#          print(line['Name']['Type'])


# #DICTREADER
# with open("week_4/pets.csv", 'r') as my_file:
#    processed_csv = csv.DictReader(my_file)
#    first_line = next(processed_csv)
#    for row in processed_csv:
#       print(row)


all_summed_cat_ages = 0
with open("week_4/pets.csv", 'r') as pets_csv_file:
   csv_interpreted = csv.reader(pets_csv_file)
   for line in csv_interpreted:
      if line['Type'] == 'cat':
         all_summed_cat_ages =+ int(line['Age'])
print(all_summed_cat_ages['Age'])