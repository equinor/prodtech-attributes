# Contributing

If you want to contribute to the project and make it better, your help 
is very welcome. By using the proposed attribute naming across companies, we can better validate and improve upon it together.

## Types of Contributions

### Report Bugs

Report improvement or change to existing code at https://github.com/equinor/prodtech-attributes/issues by registering an issue with the label `bug`.

* Explain in detail why there is a need for change
* Keep the scope as narrow as possible, to make it easier to implement.

### Propose New Features
The best way to propose new attributes is to open an issue at
https://github.com/equinor/pysand/issues with the label `enhancement`.
If you are proposing new attributes or a feature:

* Explain in detail how it should work.
* Try to adhere to guideline below
* Keep the scope as narrow as possible, to make it easier to implement.


#### Guideline for Establishing New Attributes
To assist defining asset specific attributes not yet covered, below are some guidelines to be taken into consideration

* Strive for short names, 15 characters or less
* Avoid obvious terms (e.g gauge, valve, position, travel)
* Use established abbreviations (see section below)

The compilation order of the attribute name shold be: `System` < `Placement` < `Equipment` < `Measurement` < `Suffix`

Here you see a few examples to clarify the use of the compilation order:

| Attribute name | System | Placement | Equipment | Measurement | Suffix |
|----------------|--------|-----------|-----------|-------------|--------|
| DH Press       |        | DH        |           | Press       |        |
| WH Ann A Temp  |        | WH Ann A  |           | Temp        |        |
| GL Rate        | GL     |           |           | Rate        |        |
| Sand Raw 2     | Sand   |           |           | Raw         | 2      |
| Master Lower   |        |           | Master    |             | Lower  |
| DSC Press A    |        | DSC       |           | Press       | A      |
| DH SI WH Press | DH SI  | WH        |           | Press       |        |

In order to shorten the attribute names, the standard uses well established abbreviations. These should also be used when creating names not covered by the standard list.

**DH** = Downhole  
**WH** = Wellhead  
**USC** = Upstream Choke  
**DSC** = Downstream Choke  
**Ann** = Annulus  
**GL** = Gas Lift  
**Press** = Pressure  
**Temp** = Temperature  
**DHSV** = Downhole Safety Valve  
**ASV** = Annular Safety Valve  
**MPM** = Multi Phase Meter  
**FM** = Flow Meter  
**ASD** = Acoustic Sand Detector  
**ESP** = Electrical Submersible Pump  
**SI** = Scale Inhibitor  
**WaxI** = Wax Inhibitor  
**TS** = Topside  
**Tsep** = Test Separator  
**SS** = Short String (Completion string #2, dual completion)  


### Implement Features

Look through the Git issues for feature requests. Anything tagged with "enhancement" is open to whoever wants to
implement it.

## Getting Started to contribute

Ready to contribute?

1. Assign yourself to the issue in the issue list
2. Fork the `prodtech-attributes` repo
3. Clone your fork locally
4. Create a branch for local development
5. Make your changes locally
6. Commit your changes (with reference to the issue) and push 
your branch to GitHub
7. Submit a pull request through GitHub
