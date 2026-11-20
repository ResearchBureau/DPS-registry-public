# DPS-register

An example of a collection of Data Processing Specifications (DPS) 

A DPS specifies a context in which personal medical data is used, the reason it is used,
and the measures that are used to safeguard privacy and other GDPR provisions.

Once audited and approved, each DPS fully describes how to responsibly use medical data for
a specified purpose in a specified context.


## Creating a new DPS
* Add a new folder. The folder name will be the id of the new DPS
* Add a file `dps.md` to the new folder. Use the following template:

```
# Data Processing Specification <DPS id (same as folder name)>

## Deidentification domain
_The context in which this DPS is meant to prevent the attribution of data to
original subjects. This can include the organizational elements expected to
 handle the data as well as the types of data that will be processed._

## Purpose of processing
_Why is personal data being used/processed? What is it used for?_

## Protective measures
_What is being done to meet data protection requirements? This can include
 organizational measures such as contracts and data access restriction, as
 well as technical measures such as pseudonymization, encryption and 
 authentication_
```


## Deidentification protocol

Most DPS's will include a deidentification protocol as part of their protective measures.
Deidentification protocols are defined in the [MIDOM](https://midom.readthedocs.io/en/latest/components.html) syntax.
A MIDOM protocol is usually save as a .json file.

### Creating and updating Deidentification Protocol
* Clone this repo
* Create a .json file in the DPS folder
* Add this .json file in `/scripts/update_mds.py`
* Run `uv run scripts/update_mds.py` to write/update the .md file 