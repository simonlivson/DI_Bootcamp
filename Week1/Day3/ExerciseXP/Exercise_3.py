# ===== Exercise_3.py =====
# Exercise 3: Zara
#
# What you learn here:
#   - Creating dictionaries
#   - Accessing and modifying dictionary elements
#   - Dictionary methods like .pop() and .update()
#
# Instructions:
#   Create and manipulate a dictionary that contains information about the
#   Zara brand.
#
# Brand Information:
#   name: Zara
#   creation_date: 1975
#   creator_name: Amancio Ortega Gaona
#   type_of_clothes: men, women, children, home
#   international_competitors: Gap, H&M, Benetton
#   number_stores: 7000
#   major_color:
#       France: blue,
#       Spain: red,
#       US: pink, green
#
#   1. Create a dictionary called brand with the provided data.
#   2. Modify and access the dictionary as follows:
#      - Change the value of number_stores to 2.
#      - Print a sentence describing Zara's clients using the type_of_clothes key.
#      - Add a new key country_creation with the value Spain.
#      - Check if international_competitors exists and, if so, add "Desigual"
#        to the list.
#      - Delete the creation_date key.
#      - Print the last item in international_competitors.
#      - Print the major colors in the US.
#      - Print the number of keys in the dictionary.
#      - Print all keys of the dictionary.
#
# Bonus:
#   Create another dictionary called more_on_zara with creation_date and
#   number_stores. Merge this dictionary with the original brand dictionary
#   and print the result.

brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': ['blue'],
        'Spain': ['red'],
        'US': ['pink', 'green']
    }
}

# Change number_stores to 2
brand['number_stores'] = 2

# Sentence about Zara's clients
clothes = brand['type_of_clothes']
print(f"Zara's clients are {clothes[0]}, {clothes[1]}, {clothes[2]} and {clothes[3]}.")

# Add country_creation
brand['country_creation'] = 'Spain'

# Add Desigual if international_competitors exists
if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')

# Delete creation_date
del brand['creation_date']

# Last international competitor
print(brand['international_competitors'][-1])

# Major colors in the US
print(brand['major_color']['US'])

# Number of keys
print(len(brand))

# All keys
print(brand.keys())

# Bonus: merge more_on_zara into brand
more_on_zara = {'creation_date': 1975, 'number_stores': 10000}
brand.update(more_on_zara)
print(brand)
