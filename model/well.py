from pydantic import BaseModel, Field, ValidationError, field_validator
from typing import Dict, Optional, Literal
import yaml
import os

VALID_YAML_PATH = os.path.join("attributes", "well_attributes.yaml")

af_categories = Literal[
    "Calculated",
    "Control and Monitoring",
    "ESP",
    "Flow Meter",
    "Gas Lift",
    "ICV",
    "Info",
    "Sand",
    "Valves",
]


class Attribute(BaseModel):
    alias: str = Field(..., min_length=1)
    color: Optional[str] = None
    description: str = Field(..., min_length=1)
    identifier: str = Field(..., min_length=1)
    af_category: af_categories
    af_category_2: Optional[af_categories] = None

    @field_validator("identifier", "alias", "description", mode="before")
    @classmethod
    def check_not_empty(cls, value, field):
        if not value:
            raise ValueError(f"Error: {field} must not be empty")
        return value


class WellAttributes(BaseModel):
    attribute: Dict[str, Attribute]

    @field_validator("attribute", mode="before")
    @classmethod
    def validate_unique_identifiers(cls, value):
        seen_identifiers = set()
        seen_alias = set()

        for key, attr in value.items():
            identifier = attr["identifier"]
            alias = attr["alias"]

            if identifier in seen_identifiers:
                raise ValueError(f"Duplicate identifier found: {identifier}")
            if alias in seen_alias:
                raise ValueError(f"Duplicate alias found: {alias}")

            seen_identifiers.add(identifier)
            seen_alias.add(alias)
        return value


# Load YAML file and validate
def load_and_validate_yaml(file_path: str) -> WellAttributes:
    with open(file_path, "r") as file:
        yaml_data = yaml.safe_load(file)
    return WellAttributes(**yaml_data)


if __name__ == "__main__":
    try:
        validated_attributes = load_and_validate_yaml(VALID_YAML_PATH)
        print("Validation successful. Data is valid.")
    except ValidationError as e:
        print(f"Validation failed: {e}")
