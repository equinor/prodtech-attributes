# Production Technology Attributes

## Purpose
Standardize attribute identifiers for objects relevant in modeling production- and injection networks.

## Scope
The scope of this repository includes establishing a core set of attribute names for the following objects:
* **Well**
* *Flowline (TBA)*
* *Separator (TBA)*
* *Pump (TBA)*

The core set of attribute names aims to cover minimum functional Equinor internal requirements for these objects.

## Attributes
| Column Name | Usage Guideline |
|-------------|-----------------|
| `identifier` | The unique identifier for the object attribute |
| `alias` | An alias that can be used in backend systems when using the attribute identifier is not feasible |
| `description` | A description of the intended representation of the attribute |
| `color` | A recommended color (HEX code) to represent the attribute when used in visualization tools |
| `af_category` | A recommended primary asset framework category for the attribute |
| `af_category_2` | A recommended secondary asset framework category for the attribute |

Defined attributes can be found in the project **Attributes** folder.

## Contributing
If you want to contribute to the project and make it better, your help
is very much welcome. Follow the instructions given in [CONTRIBUTING.md](CONTRIBUTING.md) before getting started.