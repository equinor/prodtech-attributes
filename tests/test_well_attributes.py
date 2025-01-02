import os
from model.well import WellAttributes
import pytest
from pydantic import ValidationError
import yaml

VALID_YAML_PATH = os.path.join("attributes", "well_attributes.yaml")

# Dummy data for testing
duplicate_identifier_yaml = """
attribute:
  ASD 2 Alarm:
    alias: attribute_alias
    color: null
    description: 'Attribute description'
    identifier: 'DUPLICATE'
    af_category: null
    af_category_2: null
  ASD 2 Alarm Level:
    alias: attribute_alias_2
    color: null
    description: 'Attribute description 2'
    identifier: 'DUPLICATE'
    af_category: null
    af_category_2: null
"""

duplicate_alias_yaml = """
attribute:
  ASD 2 Alarm:
    alias: DUPLICATE
    color: null
    description: 'Attribute description'
    identifier: 'attribute identifier'
    af_category: null
    af_category_2: null
  ASD 2 Alarm Level:
    alias: DUPLICATE
    color: null
    description: 'Attribute description 2'
    identifier: 'Attribute identifier 2'
    af_category: null
    af_category_2: null
"""


# Helper function to load YAML data
def load_yaml_data(yaml_data: str):
    return yaml.safe_load(yaml_data)


# Test valid WellAttributes
def test_valid_well_attributes():
    with open(VALID_YAML_PATH, "r") as file:
        yaml_data = yaml.safe_load(file)

    try:
        WellAttributes(**yaml_data)
    except ValidationError as e:
        pytest.fail(f"Validation failed: {e}")


# Test duplicate identifiers
def test_duplicate_identifier():
    data = load_yaml_data(duplicate_identifier_yaml)
    with pytest.raises(ValidationError) as e:
        WellAttributes(**data)
    assert "Duplicate identifier found" in str(e.value)


# Test duplicate alias
def test_duplicate_alias():
    data = load_yaml_data(duplicate_alias_yaml)
    with pytest.raises(ValidationError) as e:
        WellAttributes(**data)
    assert "Duplicate alias found" in str(e.value)