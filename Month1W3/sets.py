# creating a set
sample_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(sample_set)

list_of_numbers = [1, 2, 3, 4, 5, 6]
# print(len(list_of_numbers))

set_of_numbers = set(list_of_numbers)
# print(set_of_numbers)
# print(type(set_of_numbers))

# check if element is in set
# print(2 in set_of_numbers)

# length of a set
# print(len(set_of_numbers))

# add items to a set
# set_of_numbers.add(21)

# remove items from a set
# set_of_numbers.remove(2)
# set_of_numbers.discard(2)

# print(set_of_numbers)

# set operations

color_set = {'grey', 'red', 'white', 'pink'}
remaining_color = {'green', 'white', 'purple'}

# all_colors = color_set | remaining_color
# or 
# all_colors = color_set.union(remaining_color)
# print(all_colors)

# intersection = color_set & remaining_color
# print(intersection)

# difference = color_set - remaining_color
# print(difference)

symmetric_color = color_set ^ remaining_color
print(symmetric_color)