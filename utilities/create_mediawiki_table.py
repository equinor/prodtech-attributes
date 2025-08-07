import yaml
import os

VALID_YAML = os.path.join("attributes", "well_attributes.yaml")


def yaml_to_mediawiki_table(yaml_file):
    def handle_null(value):
        return value if value is not None else ""

    with open(VALID_YAML, "r") as file:
        data = yaml.safe_load(file)
        attributes_data = data["attribute"]

    # Start the mediawiki table with headers
    mediawiki_table = (
        '{| class="wikitable" style="text-align:left;"\n'
        "! Identifier\n"
        "! Identifier (norwegian)\n"
        "! Alias\n"
        "! Description\n"
        "! Color\n"
        "! PI AF Category\n"
        "! PI AF Cat\n"
    )

    # Fill the table with rows of data
    for _, attribute_details in attributes_data.items():
        identifier_no = ""
        if (
            "identifier_translations" in attribute_details
            and attribute_details["identifier_translations"]
        ):
            identifier_no = attribute_details["identifier_translations"].get("no", "")

        color_value = handle_null(attribute_details["color"])
        if color_value:
            color_cell = f'| style="background-color:{color_value};" | {color_value}\n'
        else:
            color_cell = f"| {color_value}\n"

        row = (
            f"|-\n"
            f'| <b>{handle_null(attribute_details["identifier"])}</b>\n'
            f"| {handle_null(identifier_no)}\n"
            f'| {handle_null(attribute_details["alias"])}\n'
            f'| {handle_null(attribute_details["description"])}\n'
            f"{color_cell}"
            f'| {handle_null(attribute_details["af_category"])}\n'
            f'| {handle_null(attribute_details["af_category_2"])}\n'
        )
        mediawiki_table += row

    mediawiki_table += "|}"
    return mediawiki_table


if __name__ == "__main__":
    mediawiki_table = yaml_to_mediawiki_table(VALID_YAML)
    with open("utilities//well_attributes_mediawiki.txt", "w") as mw_file:
        mw_file.write(mediawiki_table)
