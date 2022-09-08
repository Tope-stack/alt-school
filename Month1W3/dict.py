# creating a dictionary
sample_dict = {'name': 'John', 'age': 30, 'city': 'Lagos' }
# print(sample_dict)

# accesing items in a dictionary
print(sample_dict['name'])
print(sample_dict['age'])
print(sample_dict['city'])

# adding items to a dictionary
sample_dict['phone'] = '232-222'

# removing items in a dictionary
del(sample_dict['age'])
print(sample_dict)

# sample_dict.pop('name')
print(sample_dict)

# length of a dictionary
print(len(sample_dict))

# dictionary keys
print(sample_dict.keys())

# dictionary values
print(sample_dict.values())

# dictionary items
print(sample_dict.items())

# check if key exists
print('age' in sample_dict)

# join dictionary / update dictionary
dict1 = {'Bill': 20, 'age': 23, 'city': 10}
dict2 = {'name': 54, 'toni': 33, 'ajax': 21}

dict1.update(dict2)
# print the updated dictionary
print(dict1)

# nested dictionary or dictionary within dictionary
simple_dict = {
    'name': 'John',
    'age': 34,
    'race': 'black',
    'department': {
        'name': 'IT',
        'location': 'new york'
    }
}

print(simple_dict['department']['location'])