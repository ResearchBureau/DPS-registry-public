# Data Processing Specification 'Internal 4' (internal with original dates)

## Deidentification domain
_The context in which this DPS is meant to prevent the attribution of data original subjects. 
This can include the organizational elements expected to handle the data as well as the
types of data that will be processed._

### Users
Data processed under this DPS can **only** be used **internally**. This means all users 
of this data are RadboudUMC employees or have signed data processing agreement with 
RadboudUMC.

### Data types
The data processed under this DPS is all DICOM image data handled by the Research 
Bureau at the department of medical imaging of the Radboud University Medical Center 
(RadboudUMC).


## Purpose of processing
_Why is personal data being used/processed? What is it used for?_
* Scientific image research.

## Protective measures
_What is being done to meet data protection requirements? This can include organizational
measures such as contracts and data access restriction, as well as technical measures
such as pseudonymization, encryption and authentication_

### Researchers are informed
Department researchers are informed that they should only use this data within the 
department and can not publish it.

### Data processing agreement
For parties outside the RadboudUMC, a signed data processing agreement is required.

### Deidentification
Deidentification using protocol `Internal_4/Internal4.json`. This protocol is based
on the DICOM standard deidentification profile and options ([DICOM PS3.15E.1](https://dicom.nema.org/medical/dicom/current/output/chtml/part15/chapter_E.html#sect_E.1))
In addition to conforming to the standard, non-standard DICOM is rejected, and several
filters and operations have been added based on years of experience with RadboudUMC
data. All additions make the deidentification stricter than the standard.