import yaml
import os

VALID_YAML = os.path.join("attributes", "well_attributes.yaml")


def yaml_to_markdown_table(yaml_file):
    def handle_null(value):
        return value if value is not None else ""

    with open(VALID_YAML, "r") as file:
        data = yaml.safe_load(file)
        attributes_data = data["attribute"]

    # Start the markdown table with headers
    markdown_table = (
        "| attribute_identifier | attribute_alias "
        "|attribute_description | attribute_color "
        "| af_category | af_category_2 |\n"
    )
    markdown_table += (
        "|----------------------|-----------------"
        "|----------------------|-----------------"
        "|-------------|---------------|\n"
    )

    # Fill the table with rows of data
    for _, attribute_details in attributes_data.items():
        # Handle None values by calling the helper function
        row = (
            f"| {handle_null(attribute_details['identifier'])} | "
            f"{handle_null(attribute_details['alias'])} | "
            f"{handle_null(attribute_details['description'])} | "
            f"{handle_null(attribute_details['color'])} | "
            f"{handle_null(attribute_details['af_category'])} | "
            f"{handle_null(attribute_details['af_category_2'])} |\n"
        )
        markdown_table += row

    return markdown_table


if __name__ == "__main__":
    markdown_table = yaml_to_markdown_table(VALID_YAML)
    with open("utilities//well_attributes.md", "w") as md_file:
        md_file.write(markdown_table)
