# creating a tuple
from random import random


new_tuple = tuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# print(new_tuple)

# packing and unpacking tuples
sample_tuple = ("John", 25, "Doe") # packing variables into a tuple

name, age, lastname = sample_tuple # unpacking variables from a tuple
# print(sample_tuple) 

# accesing items in a tuple 
string_tuple = ("p", "y", "t", "h", "o", "n")
# print(string_tuple[0]) # access items using the index

# slicing a tuple
# print(string_tuple[1:5])

# find items in a tuple
# print(string_tuple.index("t"))

# modyfying items in a tuple
# string_tuple[0] = "i"

# modyfying nested items in a tuple
example_tuple = ("p", "y", "t", "h", "o", "n", [1, 2, 3])
# print(example_tuple[-1][1])
# example_tuple[6][1] = 12
# print(example_tuple[6][1])


# converting tuple to a list
# tuple_to_list = list(example_tuple)
# print(tuple_to_list)

# converting list to tuple
# list_to_tuple = tuple(tuple_to_list)
# print(list_to_tuple)

# count occurences
# print(example_tuple.count("o"))

# inbuilt functions
print(sum(new_tuple))
print(min(new_tuple))
print(max(new_tuple))




