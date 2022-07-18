# Output
#{'Apricot': 1,
# 'Blackcurrant': 1,
# 'Cantaloupe': 1,
# 'Feijoa': 1,
# 'Grapefruit': 1,
# 'Juniper berry': 1,
# 'Salal berry': 1,
# 'Soursop': 1}

from pprint import pprint

fruits = [
    "Soursop", 
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
#        fruit_count = {fruit: 1}
        fruit_count[fruit] = fruit_count.get(fruit,0) + 1
    else:
        fruit_count[fruit] += 1
        

pprint(fruit_count)