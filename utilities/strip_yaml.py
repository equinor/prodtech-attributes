import yaml
import os

# Define a custom representer for quoting non-null strings while leaving null values unquoted
def custom_string_presenter(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:str', data, style="'")

# Define a representer for None that does not add quotes
def none_presenter(dumper, data):
    return dumper.represent_scalar('tag:yaml.org,2002:null', 'null')

# Register the custom representers
yaml.add_representer(str, custom_string_presenter)
yaml.add_representer(type(None), none_presenter)

# Path to your input YAML file
input_file_path = os.path.join('attributes', 'well_attributes.yaml')

# Load YAML content from the input file
with open(input_file_path, 'r', encoding='utf-8') as file:
    original_data = yaml.safe_load(file)

# Path for the output YAML file
output_file_path = 'quoted_attributes.yaml'

# Write the modified data to the output file, setting the default_flow_style to False
# for better readability and setting allow_unicode to True to handle any unicode characters
with open(output_file_path, 'w', encoding='utf-8') as file:
    yaml.safe_dump(original_data, file, default_flow_style=False, allow_unicode=True)

print(f"Data with quoted non-null string values written to {output_file_path}")