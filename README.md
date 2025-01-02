<p align="center">
<img src="resources/images/logo.jpg" title="ProdTech Attributes" height="300"/>
</p>
<p align="center"><i>Logo created using OpenAI's DALL·E</i></p>

[![SCM Compliance](https://scm-compliance-api.radix.equinor.com/repos/equinor/4c903977-52bb-4275-b702-4da3efd24716/badge)](https://developer.equinor.com/governance/scm-policy/)

# Production Technology Attributes


## Purpose
> Standardize on naming practices for attributes of objects relevant in modeling production- and injection networks.

## Scope
The scope of this repository includes establishing a core set of attribute identifiers for the following objects:
* **Well**
* *Flowline (TBA)*
* *Separator (TBA)*
* *Pump (TBA)*

The core set of attribute identifiers aims to cover minimum functional Equinor internal requirements for these objects.

## Attributes
| Column Name     | Constraints      |  Usage Guideline |
|-----------------|------------------|------------------|
| `identifier`    | Required, Unique | The unique identifier for the object attribute |
| `alias`         | Required, Unique |An alias that can be used in backend systems when using the attribute identifier is not feasible |
| `description`   | Required         |A description of the intended representation of the attribute |
| `color`         | Optional         |A recommended color (HEX code) to represent the attribute when used in visualization tools |
| `af_category`   | Required         |A recommended primary asset framework category for the attribute |
| `af_category_2` | Optional         |A recommended secondary asset framework category for the attribute |

Defined attributes can be found in the project **Attributes** folder.

## Contributing
If you want to contribute to the project and make it better, your help
is very much welcome. Follow the instructions given in [CONTRIBUTING.md](CONTRIBUTING.md) before getting started.