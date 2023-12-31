schedule = {
	"monday" :   ['Human-Information Behavior','Information Professions','Research Mthds/Law Lit','Strategic Leadership','Conservation and Preservation','Info Services & Resources'],
	"tuesday":   ['Information Arch/Inter Design','Information Professions','Acad Libraries and Scholarly','Info Services & Resources'],
	"wednesday": ['Info Services & Resources','Usability Theory & Practice','Mgmt of Archives/Sp Collection','Government Info Sources','Library Media Centers','Mgmt of Archives/Sp Collection'],
	"thursday": ['Information Science Research','Information Professions','Information Professions'],
}


for day in schedule:
    print(day)
    for classes in schedule[day]:
        print(classes)



#loop through each day in schedule, print the name of the day, and then loop through all the class names and print them out

#output sample:

# ❯ python3 pratt_schedule2.py
# monday
# Human-Information Behavior
# Information Professions
# ...



# ATTEMPT 1 - prints days only
# day = "{'monday'} {'tuesday} {'wednesday} {'thursday'}"

# for day in schedule:
#           print(schedule)


# ATTEMPT 2 - prints schedule but not in right format
# for day in schedule:
#     print(day,
#           schedule[day])
    

# # ATTEMPT 3 - same result as ATTEMPT 4
# for day in schedule:
#     print(schedule[day])

