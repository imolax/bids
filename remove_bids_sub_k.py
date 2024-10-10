# In this script, you can modify the terms_to_remove list to include any values of k you want to remove (e.g., ['59', '60', '61']). 
# The script will then remove all occurrences of "bids::sub-k/" for each specified k in all JSON files in the "dwi" and "fmap" directories.

import json
import os

def remove_term(data, terms):
    if isinstance(data, dict):
        return {k: remove_term(v, terms) for k, v in data.items()}
    elif isinstance(data, list):
        return [remove_term(item, terms) for item in data]
    elif isinstance(data, str):
        for term in terms:
            data = data.replace(f"bids::sub-{term}/", "")
        return data
    return data

def process_json_file(file_path, terms):
    with open(file_path, 'r') as f:
        data = json.load(f)

    cleaned_data = remove_term(data, terms)

    with open(file_path, 'w') as f:
        json.dump(cleaned_data, f, indent=4)

def main():
    # Define the variable values for k
    terms_to_remove = ['59', '60', '61']  # Add more values as needed
    
    for k in terms_to_remove:
        directories = [f"/data/BILCOR/BIDS/sub-{k}/dwi", f"/data/BILCOR/BIDS/sub-{k}/fmap"]
        for directory in directories:
            if os.path.exists(directory):
                for filename in os.listdir(directory):
                    if filename.endswith('.json'):
                        file_path = os.path.join(directory, filename)
                        print(f'Processing {file_path}...')
                        process_json_file(file_path, terms_to_remove)
            else:
                print(f"Directory '{directory}' does not exist.")

if __name__ == "__main__":
    main()


