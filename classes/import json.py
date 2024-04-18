import json




# Read JSON file

def open_and_format_json(file_path):
    with open(file_path, 'rb') as f:
        data = json.load(f)

    for entry in data:
        entry['response'] = json.loads(entry["response"])
    
    with open('modified_data.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)
    
    return data

open_and_format_json('reviews.json')
