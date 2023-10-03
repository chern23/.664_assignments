"""
people = ['Rik','Mia','Luke']

p = 3.14159

for p in people:
  print(p)


print(p)


state_info = {
  'NY': 'New York',
  'NJ': 'New Jersey',
  'MN': 'Minnesota',
  'codes': ['NY','NJ','MN'],
  'pop': {
    'NY': 19.84,
    'NJ': 9.27,
    'MN': 5.71
  }
}


for el_key in state_info:
    # if isinstance(el, list):
    el = state_info[el_key]
    if type(el) == list:
        for state_code in el:
            print(state_code)

for c in "hello, this is my lengthy text":
    print(c)
    

letters = ['a','b','c','d','e','f','g','h']

try:
    print(letters[100])
except IndexError:
    print("sad trombone")

print("tada")

a_number = 12
a_string = "hello"

print(str(a_number) + a_string)
"""

"""
#methods
a_string = "Hello, World"
print(a_string.lower())

help(str) #shows all of the functoins that str can perform -- STRIP is very important
"""

"""#create your own functions

def my_function(text="tada"):
    print("hello world")

def my_function():
    return 6

a = my_function
print(a)

import os

files = os.listdir()
print(files)
"""


# #exercise 1
# animals = ['Kira','Milo','Sommer','Biscotti','Lulu']

# print(animals)

# #exercise 2
# pets = [
#     {'name': 'Kira', 'type':'dog', 'age': 7 },
#     {'name': 'Milo', 'type':'cat', 'age': 4 },
#     {'name': 'Sommer', 'type':'cat', 'age': 2 },
#     {'name': 'Biscuit', 'type':'cat', 'age': 5 },
#     {'name': 'Lulu', 'type':'dog', 'age': 11 }
# ]

# for name in pets:
#         if (name['type']) == 'dog':
#                 print(name['name'])





# #Exercise 3
# pets = {
#     'Kira' : { 'type':'dog', 'age': 7 },
#     'Milo' : { 'type':'cat', 'age': 4 },
#     'Sommer' : { 'type':'cat', 'age': 2 },
#     'Biscuit' : { 'type':'cat', 'age': 5 },
#     'Lulu' : { 'type':'dog', 'age': 11 }
# }

# #for name in pets:
#  #       if (name['type']['age'])
#   #          print(name['name', 'age'])

# #keys = name['type', 'age']

# for name in pets:
#        if pets[name]['type'] == 'dog':
#               print(name)


#exercise4
pets = {
 'Kira' : { 'type':'dog', 'age': 7 },
 'Milo' : { 'type':'cat', 'age': 4 },
 'Sommer' : { 'type':'cat', 'age': 2 },
 'Biscuit' : { 'type':'cat', 'age': 5 },
 'Lulu' : { 'type':'dog', 'age': 11 }
}

sum=0

for name in pets:
        if pets[name]['type'] == 'cat':
            sum+= pets[name]['age']

print(sum)
                