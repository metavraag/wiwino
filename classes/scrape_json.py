import json
import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()



# Read JSON file
with open('wine.json', 'rb') as f:
    data = json.load(f)

# Extract names of people

id = [region['id'] for region in data['regions']]
name = [region['name'] for region in data['regions']]
parent_id = [region['parent_id'] for region in data['regions']]
country_code = [region['country']['code'] for region in data['regions']]
country = [region['country']['name'] for region in data['regions']]


country_data = {
    'country_code': country_code,
    'country': country
}

# Construct a list of tuples from the input data
data_tuples = zip(*[country_data[key] for key in country_data])
# Insert multiple rows into the table
cursor.executemany('INSERT OR REPLACE INTO countries (country_code, country) VALUES (?, ?)', data_tuples)



region_data = {
    'region_id': id,
    'name': name,
    'parent_id': parent_id,
    'fk_country_code':country_code
}

# Construct a list of tuples from the input data
data_tuples = zip(*[region_data[key] for key in region_data])
# Insert multiple rows into the table
cursor.executemany('INSERT OR REPLACE INTO Regions (region_id, name, parent_id, fk_country_code) VALUES (?, ?, ?, ?)', data_tuples)

# Commit the transaction
conn.commit()



grape_id = []
grape_names = []
parent_grape_id = []
for region in data['regions']:
    for grape in region['country']['most_used_grapes']:
        grape_id.append(grape['id'])
        grape_names.append(grape['name'])
        parent_grape_id.append(grape['parent_grape_id'])

grape_data = {
    'grape_id': grape_id,
    'name': grape_names,
    'parent_grape_id': parent_grape_id
}
data_tuples = zip(*[grape_data[key] for key in grape_data])

cursor.executemany('INSERT OR REPLACE INTO grapes (grape_id, name, parent_grape_id) VALUES (?, ?, ?)', data_tuples)





