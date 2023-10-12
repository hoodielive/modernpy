import json
import toml

# Function to convert JSON to TOML
def json_to_toml(json_file_path, toml_file_path):
    # Load JSON data from the file
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)
    
    # Convert JSON to TOML
    toml_data = toml.dumps(json_data)
    
    # Write the TOML data to a file
    with open(toml_file_path, 'w') as toml_file:
        toml_file.write(toml_data)

# Specify the paths for the JSON and TOML files
json_file_path = './odus_data.json'  # Replace with your JSON file
toml_file_path = 'odus_data.toml'  # Replace with the desired TOML output file

# Convert JSON to TOML
json_to_toml(json_file_path, toml_file_path)

print(f"Conversion from JSON to TOML completed. Output saved to {toml_file_path}")

