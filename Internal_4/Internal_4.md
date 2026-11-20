# Deidentification Protocol
## Tags
What is done to each DICOM tag? The official DICOM key for an 'image type' is the SOPClass.
The DICOM standard has different answers according to which SOPClass you are processing. Therefore,
the answer to 'what is done to each tag?' is split according to SOPClass. The designations
can include an asterisk (`*`) wildcard to indicate any SOPClass matching the pattern.


### SOPClass "* (*)"

| Tag | Name | Action | Comment |
| --- | ---- | ------ | ------- |
| (0000,1000) | AffectedSOPInstanceUID | REMOVE | Read from CTP |
| (0000,1001) | RequestedSOPInstanceUID | UID | Read from CTP |
| (0002,0003) | MediaStorageSOPInstanceUID | UID | Read from CTP |
| (0004,1511) | ReferencedSOPInstanceUIDInFile | UID | Read from CTP |
| (0008,0012) | InstanceCreationDate | DUMMY | Read from CTP |
| (0008,0014) | InstanceCreatorUID | UID | Read from CTP |
| (0008,0015) | InstanceCoercionDateTime | KEEP | Read from CTP |
| (0008,0015) | InstanceCoercionDateTime | KEEP | Read from CTP |
| (0008,0016) | SOPClassUID | KEEP | Read from CTP |
| (0008,0016) | SOPClassUID | KEEP | Read from CTP |
| (0008,0018) | SOPInstanceUID | UID | Read from CTP |
| (0008,0020) | StudyDate | KEEP | Read from CTP |
| (0008,0021) | SeriesDate | KEEP | Read from CTP |
| (0008,0022) | AcquisitionDate | KEEP | Read from CTP |
| (0008,0023) | ContentDate | KEEP | Read from CTP |
| (0008,0024) | OverlayDate | KEEP | Read from CTP |
| (0008,0025) | CurveDate | KEEP | Read from CTP |
| (0008,002A) | AcquisitionDateTime | KEEP | Read from CTP |
| (0008,0050) | AccessionNumber | DUMMY | Read from CTP |
| (0008,0058) | FailedSOPInstanceUIDList | UID | Read from CTP |
| (0008,0070) | Manufacturer | KEEP | Read from CTP |
| (0008,0080) | InstitutionName | REMOVE | Read from CTP |
| (0008,0081) | InstitutionAddress | REMOVE | Read from CTP |
| (0008,0082) | InstitutionCodeSequence | REMOVE | Read from CTP |
| (0008,0090) | ReferringPhysicianName | EMPTY | Read from CTP |
| (0008,0092) | ReferringPhysicianAddress | REMOVE | Read from CTP |
| (0008,0094) | ReferringPhysicianTelephoneNumbers | REMOVE | Read from CTP |
| (0008,0096) | ReferringPhysicianIdentificationSequence | REMOVE | Read from CTP |
| (0008,010D) | ContextGroupExtensionCreatorUID | UID | Read from CTP |
| (0008,1010) | StationName | KEEP | Read from CTP |
| (0008,1030) | StudyDescription | KEEP | Read from CTP |
| (0008,103E) | SeriesDescription | DUMMY | Read from CTP |
| (0008,1040) | InstitutionalDepartmentName | REMOVE | Read from CTP |
| (0008,1048) | PhysiciansOfRecord | REMOVE | Read from CTP |
| (0008,1049) | PhysiciansOfRecordIdentificationSequence | REMOVE | Read from CTP |
| (0008,1050) | PerformingPhysicianName | REMOVE | Read from CTP |
| (0008,1052) | PerformingPhysicianIdentificationSequence | REMOVE | Read from CTP |
| (0008,1060) | NameOfPhysiciansReadingStudy | REMOVE | Read from CTP |
| (0008,1062) | PhysiciansReadingStudyIdentificationSequence | REMOVE | Read from CTP |
| (0008,1070) | OperatorsName | REMOVE | Read from CTP |
| (0008,1072) | OperatorIdentificationSequence | REMOVE | Read from CTP |
| (0008,1080) | AdmittingDiagnosesDescription | KEEP | Read from CTP |
| (0008,1090) | ManufacturerModelName | KEEP | Read from CTP |
| (0008,1120) | ReferencedPatientSequence | REMOVE | Read from CTP |
| (0008,1150) | ReferencedSOPClassUID | KEEP | Read from CTP |
| (0008,1155) | ReferencedSOPInstanceUID | UID | Read from CTP |
| (0008,1195) | TransactionUID | UID | Read from CTP |
| (0008,2111) | DerivationDescription | KEEP | Read from CTP |
| (0008,2112) | SourceImageSequence | REMOVE | Read from CTP |
| (0008,3010) | IrradiationEventUID | UID | Read from CTP |
| (0008,4000) | IdentifyingComments | REMOVE | Read from CTP |
| (0008,9123) | CreatorVersionUID | UID | Read from CTP |
| (0010,0010) | PatientName | KEEP | Read from CTP |
| (0010,0010) | PatientName | KEEP | Read from CTP |
| (0010,0010) | PatientName | DUMMY | Read from CTP |
| (0010,0020) | PatientID | KEEP | Read from CTP |
| (0010,0020) | PatientID | KEEP | Read from CTP |
| (0010,0020) | PatientID | DUMMY | Read from CTP |
| (0010,0021) | IssuerOfPatientID | REMOVE | Read from CTP |
| (0010,0030) | PatientBirthDate | EMPTY | Read from CTP |
| (0010,0032) | PatientBirthTime | REMOVE | Read from CTP |
| (0010,0040) | PatientSex | KEEP | Read from CTP |
| (0010,0050) | PatientInsurancePlanCodeSequence | REMOVE | Read from CTP |
| (0010,0101) | PatientPrimaryLanguageCodeSequence | REMOVE | Read from CTP |
| (0010,0102) | PatientPrimaryLanguageModifierCodeSequence | REMOVE | Read from CTP |
| (0010,1000) | OtherPatientIDs | REMOVE | Read from CTP |
| (0010,1001) | OtherPatientNames | REMOVE | Read from CTP |
| (0010,1002) | OtherPatientIDsSequence | REMOVE | Read from CTP |
| (0010,1005) | PatientBirthName | REMOVE | Read from CTP |
| (0010,1010) | PatientAge | KEEP | Read from CTP |
| (0010,1020) | PatientSize | KEEP | Read from CTP |
| (0010,1030) | PatientWeight | KEEP | Read from CTP |
| (0010,1040) | PatientAddress | REMOVE | Read from CTP |
| (0010,1050) | InsurancePlanIdentification | REMOVE | Read from CTP |
| (0010,1060) | PatientMotherBirthName | REMOVE | Read from CTP |
| (0010,1080) | MilitaryRank | REMOVE | Read from CTP |
| (0010,1081) | BranchOfService | REMOVE | Read from CTP |
| (0010,1090) | MedicalRecordLocator | REMOVE | Read from CTP |
| (0010,2000) | MedicalAlerts | KEEP | Read from CTP |
| (0010,2110) | Allergies | KEEP | Read from CTP |
| (0010,2150) | CountryOfResidence | REMOVE | Read from CTP |
| (0010,2152) | RegionOfResidence | REMOVE | Read from CTP |
| (0010,2154) | PatientTelephoneNumbers | REMOVE | Read from CTP |
| (0010,2160) | EthnicGroup | KEEP | Read from CTP |
| (0010,2180) | Occupation | KEEP | Read from CTP |
| (0010,21A0) | SmokingStatus | KEEP | Read from CTP |
| (0010,21B0) | AdditionalPatientHistory | EMPTY | Read from CTP |
| (0010,21C0) | PregnancyStatus | KEEP | Read from CTP |
| (0010,21F0) | PatientReligiousPreference | REMOVE | Read from CTP |
| (0010,2203) | PatientSexNeutered | KEEP | Read from CTP |
| (0010,2297) | ResponsiblePerson | REMOVE | Read from CTP |
| (0010,2299) | ResponsibleOrganization | REMOVE | Read from CTP |
| (0010,4000) | PatientComments | REMOVE | Read from CTP |
| (0012,0062) | PatientIdentityRemoved | DUMMY | Read from CTP |
| (0012,0063) | DeidentificationMethod | DUMMY | Read from CTP |
| (0012,0064) | DeidentificationMethodCodeSequence | DUMMY | Read from CTP |
| (0018,0010) | ContrastBolusAgent | KEEP | Read from CTP |
| (0018,0015) | BodyPartExamined | KEEP | Read from CTP |
| (0018,1000) | DeviceSerialNumber | KEEP | Read from CTP |
| (0018,1002) | DeviceUID | UID | Read from CTP |
| (0018,1004) | PlateID | KEEP | Read from CTP |
| (0018,1005) | GeneratorID | KEEP | Read from CTP |
| (0018,1007) | CassetteID | KEEP | Read from CTP |
| (0018,1008) | GantryID | KEEP | Read from CTP |
| (0018,1012) | DateOfSecondaryCapture | DUMMY | Read from CTP |
| (0018,1020) | SoftwareVersions | KEEP | Read from CTP |
| (0018,1030) | ProtocolName | KEEP | Read from CTP |
| (0018,1070) | RadiopharmaceuticalRoute | KEEP | Read from CTP |
| (0018,1071) | RadiopharmaceuticalVolume | KEEP | Read from CTP |
| (0018,1072) | RadiopharmaceuticalStartTime | KEEP | Read from CTP |
| (0018,1072) | RadiopharmaceuticalStartTime | KEEP | Read from CTP |
| (0018,1074) | RadionuclideTotalDose | KEEP | Read from CTP |
| (0018,1075) | RadionuclideHalfLife | KEEP | Read from CTP |
| (0018,1076) | RadionuclidePositronFraction | KEEP | Read from CTP |
| (0018,1077) | RadiopharmaceuticalSpecificActivity | KEEP | Read from CTP |
| (0018,1078) | RadiopharmaceuticalStartDateTime | KEEP | Read from CTP |
| (0018,1079) | RadiopharmaceuticalStopDateTime | KEEP | Read from CTP |
| (0018,1200) | DateOfLastCalibration | KEEP | Read from CTP |
| (0018,1400) | AcquisitionDeviceProcessingDescription | KEEP | Read from CTP |
| (0018,4000) | AcquisitionComments | REMOVE | Read from CTP |
| (0018,700A) | DetectorID | KEEP | Read from CTP |
| (0018,700C) | DateOfLastDetectorCalibration | DUMMY | Read from CTP |
| (0018,9424) | AcquisitionProtocolDescription | KEEP | Read from CTP |
| (0018,A003) | ContributionDescription | KEEP | Read from CTP |
| (0020,000D) | StudyInstanceUID | UID | Read from CTP |
| (0020,000E) | SeriesInstanceUID | UID | Read from CTP |
| (0020,0010) | StudyID | EMPTY | Read from CTP |
| (0020,0052) | FrameOfReferenceUID | UID | Read from CTP |
| (0020,0200) | SynchronizationFrameOfReferenceUID | UID | Read from CTP |
| (0020,3401) | ModifyingDeviceID | REMOVE | Read from CTP |
| (0020,3404) | ModifyingDeviceManufacturer | REMOVE | Read from CTP |
| (0020,3406) | ModifiedImageDescription | REMOVE | Read from CTP |
| (0020,4000) | ImageComments | REMOVE | Read from CTP |
| (0020,9158) | FrameComments | REMOVE | Read from CTP |
| (0020,9161) | ConcatenationUID | UID | Read from CTP |
| (0020,9164) | DimensionOrganizationUID | UID | Read from CTP |
| (0028,0301) | BurnedInAnnotation | KEEP | Read from CTP |
| (0028,0303) | LongitudinalTemporalInformationModified | KEEP | Read from CTP |
| (0028,1199) | PaletteColorLookupTableUID | UID | Read from CTP |
| (0028,1214) | LargePaletteColorLookupTableUID | UID | Read from CTP |
| (0028,4000) | ImagePresentationComments | REMOVE | Read from CTP |
| (0032,0012) | StudyIDIssuer | REMOVE | Read from CTP |
| (0032,1000) | ScheduledStudyStartDate | DUMMY | Read from CTP |
| (0032,1020) | ScheduledStudyLocation | KEEP | Read from CTP |
| (0032,1021) | ScheduledStudyLocationAETitle | KEEP | Read from CTP |
| (0032,1030) | ReasonForStudy | KEEP | Read from CTP |
| (0032,1032) | RequestingPhysician | REMOVE | Read from CTP |
| (0032,1033) | RequestingService | REMOVE | Read from CTP |
| (0032,1040) | StudyArrivalDate | DUMMY | Read from CTP |
| (0032,1050) | StudyCompletionDate | DUMMY | Read from CTP |
| (0032,1060) | RequestedProcedureDescription | KEEP | Read from CTP |
| (0032,1070) | RequestedContrastAgent | KEEP | Read from CTP |
| (0032,4000) | StudyComments | REMOVE | Read from CTP |
| (0038,0004) | ReferencedPatientAliasSequence | REMOVE | Read from CTP |
| (0038,0010) | AdmissionID | REMOVE | Read from CTP |
| (0038,0011) | IssuerOfAdmissionID | REMOVE | Read from CTP |
| (0038,001E) | ScheduledPatientInstitutionResidence | REMOVE | Read from CTP |
| (0038,0040) | DischargeDiagnosisDescription | KEEP | Read from CTP |
| (0038,0050) | SpecialNeeds | KEEP | Read from CTP |
| (0038,0060) | ServiceEpisodeID | REMOVE | Read from CTP |
| (0038,0061) | IssuerOfServiceEpisodeID | REMOVE | Read from CTP |
| (0038,0062) | ServiceEpisodeDescription | KEEP | Read from CTP |
| (0038,0300) | CurrentPatientLocation | REMOVE | Read from CTP |
| (0038,0400) | PatientInstitutionResidence | REMOVE | Read from CTP |
| (0038,0500) | PatientState | REMOVE | Read from CTP |
| (0038,4000) | VisitComments | REMOVE | Read from CTP |
| (0040,0001) | ScheduledStationAETitle | KEEP | Read from CTP |
| (0040,0006) | ScheduledPerformingPhysicianName | REMOVE | Read from CTP |
| (0040,0007) | ScheduledProcedureStepDescription | KEEP | Read from CTP |
| (0040,0009) | ScheduledProcedureStepID | REMOVE | Read from CTP |
| (0040,000B) | ScheduledPerformingPhysicianIdentificationSequence | REMOVE | Read from CTP |
| (0040,0010) | ScheduledStationName | KEEP | Read from CTP |
| (0040,0011) | ScheduledProcedureStepLocation | KEEP | Read from CTP |
| (0040,0012) | PreMedication | KEEP | Read from CTP |
| (0040,0241) | PerformedStationAETitle | KEEP | Read from CTP |
| (0040,0242) | PerformedStationName | KEEP | Read from CTP |
| (0040,0243) | PerformedLocation | REMOVE | Read from CTP |
| (0040,0250) | PerformedProcedureStepEndDate | REMOVE | Read from CTP |
| (0040,0253) | PerformedProcedureStepID | REMOVE | Read from CTP |
| (0040,0254) | PerformedProcedureStepDescription | KEEP | Read from CTP |
| (0040,0280) | CommentsOnThePerformedProcedureStep | REMOVE | Read from CTP |
| (0040,0555) | AcquisitionContextSequence | REMOVE | Read from CTP |
| (0040,1001) | RequestedProcedureID | REMOVE | Read from CTP |
| (0040,1004) | PatientTransportArrangements | REMOVE | Read from CTP |
| (0040,1005) | RequestedProcedureLocation | REMOVE | Read from CTP |
| (0040,1010) | NamesOfIntendedRecipientsOfResults | REMOVE | Read from CTP |
| (0040,1011) | IntendedRecipientsOfResultsIdentificationSequence | REMOVE | Read from CTP |
| (0040,1101) | PersonIdentificationCodeSequence | REMOVE | Read from CTP |
| (0040,1102) | PersonAddress | REMOVE | Read from CTP |
| (0040,1103) | PersonTelephoneNumbers | REMOVE | Read from CTP |
| (0040,1400) | RequestedProcedureComments | REMOVE | Read from CTP |
| (0040,2001) | ReasonForTheImagingServiceRequest | KEEP | Read from CTP |
| (0040,2008) | OrderEnteredBy | REMOVE | Read from CTP |
| (0040,2009) | OrderEntererLocation | REMOVE | Read from CTP |
| (0040,2010) | OrderCallbackPhoneNumber | REMOVE | Read from CTP |
| (0040,2016) | PlacerOrderNumberImagingServiceRequest | EMPTY | Read from CTP |
| (0040,2017) | FillerOrderNumberImagingServiceRequest | EMPTY | Read from CTP |
| (0040,2400) | ImagingServiceRequestComments | REMOVE | Read from CTP |
| (0040,3001) | ConfidentialityConstraintOnPatientDataDescription | REMOVE | Read from CTP |
| (0040,4023) | ReferencedGeneralPurposeScheduledProcedureStepTransactionUID | UID | Read from CTP |
| (0040,4034) | ScheduledHumanPerformersSequence | REMOVE | Read from CTP |
| (0040,4035) | ActualHumanPerformersSequence | REMOVE | Read from CTP |
| (0040,4036) | HumanPerformerOrganization | REMOVE | Read from CTP |
| (0040,4037) | HumanPerformerName | REMOVE | Read from CTP |
| (0040,A027) | VerifyingOrganization | REMOVE | Read from CTP |
| (0040,A043) | ConceptNameCodeSequence | REMOVE | Read from CTP |
| (0040,A073) | VerifyingObserverSequence | REMOVE | Read from CTP |
| (0040,A075) | VerifyingObserverName | EMPTY | Read from CTP |
| (0040,A078) | AuthorObserverSequence | REMOVE | Read from CTP |
| (0040,A07A) | ParticipantSequence | REMOVE | Read from CTP |
| (0040,A07C) | CustodialOrganizationSequence | REMOVE | Read from CTP |
| (0040,A088) | VerifyingObserverIdentificationCodeSequence | REMOVE | Read from CTP |
| (0040,A123) | PersonName | EMPTY | Read from CTP |
| (0040,A124) | UID | UID | Read from CTP |
| (0040,A160) | TextValue | EMPTY | Read from CTP |
| (0040,A168) | ConceptCodeSequence | REMOVE | Read from CTP |
| (0040,A504) | ContentTemplateSequence | REMOVE | Read from CTP |
| (0040,A730) | ContentSequence | REMOVE | Read from CTP |
| (0040,DB0C) | TemplateExtensionOrganizationUID | UID | Read from CTP |
| (0040,DB0D) | TemplateExtensionCreatorUID | UID | Read from CTP |
| (0054,1321) | DecayFactor | KEEP | Read from CTP |
| (0054,1322) | DoseCalibrationFactor | KEEP | Read from CTP |
| (0054,1323) | ScatterFractionFactor | KEEP | Read from CTP |
| (0070,0001) | GraphicAnnotationSequence | REMOVE | Read from CTP |
| (0070,0008) | TextObjectSequence | REMOVE | Read from CTP |
| (0070,0009) | GraphicObjectSequence | REMOVE | Read from CTP |
| (0070,005A) | DisplayedAreaSelectionSequence | REMOVE | Read from CTP |
| (0070,0060) | GraphicLayerSequence | REMOVE | Read from CTP |
| (0070,0080) | ContentLabel | DUMMY | Read from CTP |
| (0070,0084) | ContentCreatorName | EMPTY | Read from CTP |
| (0070,0086) | ContentCreatorIdentificationCodeSequence | REMOVE | Read from CTP |
| (0070,031A) | FiducialUID | UID | Read from CTP |
| (0088,0140) | StorageMediaFileSetUID | UID | Read from CTP |
| (0088,0200) | IconImageSequence | REMOVE | Read from CTP |
| (0088,0904) | TopicTitle | REMOVE | Read from CTP |
| (0088,0906) | TopicSubject | REMOVE | Read from CTP |
| (0088,0910) | TopicAuthor | REMOVE | Read from CTP |
| (0088,0912) | TopicKeywords | REMOVE | Read from CTP |
| (0400,0100) | DigitalSignatureUID | REMOVE | Read from CTP |
| (0400,0402) | ReferencedDigitalSignatureSequence | REMOVE | Read from CTP |
| (0400,0403) | ReferencedSOPInstanceMACSequence | REMOVE | Read from CTP |
| (0400,0404) | MAC | REMOVE | Read from CTP |
| (0400,0550) | ModifiedAttributesSequence | REMOVE | Read from CTP |
| (0400,0561) | OriginalAttributesSequence | REMOVE | Read from CTP |
| (2030,0020) | TextString | REMOVE | Read from CTP |
| (3006,0008) | StructureSetDate | DUMMY | Read from CTP |
| (3006,0024) | ReferencedFrameOfReferenceUID | UID | Read from CTP |
| (3006,00C2) | RelatedFrameOfReferenceUID | UID | Read from CTP |
| (300A,0013) | DoseReferenceUID | UID | Read from CTP |
| (300E,0008) | ReviewerName | REMOVE | Read from CTP |
| (4000,0010) | Arbitrary | REMOVE | Read from CTP |
| (4000,4000) | TextComments | REMOVE | Read from CTP |
| (4008,0042) | ResultsIDIssuer | REMOVE | Read from CTP |
| (4008,0102) | InterpretationRecorder | REMOVE | Read from CTP |
| (4008,010A) | InterpretationTranscriber | REMOVE | Read from CTP |
| (4008,010B) | InterpretationText | KEEP | Read from CTP |
| (4008,010C) | InterpretationAuthor | REMOVE | Read from CTP |
| (4008,0111) | InterpretationApproverSequence | REMOVE | Read from CTP |
| (4008,0114) | PhysicianApprovingInterpretation | REMOVE | Read from CTP |
| (4008,0115) | InterpretationDiagnosisDescription | KEEP | Read from CTP |
| (4008,0118) | ResultsDistributionListSequence | REMOVE | Read from CTP |
| (4008,0119) | DistributionName | REMOVE | Read from CTP |
| (4008,011A) | DistributionAddress | REMOVE | Read from CTP |
| (4008,0202) | InterpretationIDIssuer | REMOVE | Read from CTP |
| (4008,0300) | Impressions | KEEP | Read from CTP |
| (4008,4000) | ResultsComments | REMOVE | Read from CTP |
| (FFFA,FFFA) | DigitalSignaturesSequence | REMOVE | Read from CTP |
| (FFFC,FFFC) | DataSetTrailingPadding | REMOVE | Read from CTP |



## Private


### Private group
Private DICOM elements used for guiding the de-identification process

| tag | description | VR | VM |
| --- | ---- | ------ | ------- |
| 0075,[RADBOUDUMCANONYMIZER]00 | AnonymizedPatientName | PN | 1 |
| 0075,[RADBOUDUMCANONYMIZER]01 | AnonymizedPatientID | LO | 1 |
| 0075,[RADBOUDUMCANONYMIZER]02 | AnonymizedPatientNamePrefix | PN | 1 |
| 0075,[RADBOUDUMCANONYMIZER]03 | AnonymizedPatientIdPrefix | LO | 1 |
| 0075,[RADBOUDUMCANONYMIZER]04 | InternalPatientNameChanged | PN | 1 |
| 0075,[RADBOUDUMCANONYMIZER]05 | InternalPatientIdChanged | LO | 1 |
| 0075,[RADBOUDUMCANONYMIZER]06 | InternalStudyAndSeriesIdChanged | LO | 1 |
| 0075,[RADBOUDUMCANONYMIZER]10 | AnonymizedAccessionNumber | SH | 1 |
| 0075,[RADBOUDUMCANONYMIZER]11 | AnonymizedStudyId | SH | 1 |
| 0075,[RADBOUDUMCANONYMIZER]21 | ProjectName | LO | 1 |
| 0075,[RADBOUDUMCANONYMIZER]22 | SiteName | LO | 1 |
| 0075,[RADBOUDUMCANONYMIZER]23 | SiteID | LO | 1 |
| 0075,[RADBOUDUMCANONYMIZER]24 | TrialName | LO | 1 |
| 0075,[RADBOUDUMCANONYMIZER]25 | Subject | LO | 1 |
| 0075,[RADBOUDUMCANONYMIZER]26 | UIDRoot | UI | 1 |
| 0075,[RADBOUDUMCANONYMIZER]27 | JobID | LO | 1 |
| 0075,[RADBOUDUMCANONYMIZER]28 | SourceInstanceID | LO | 1 |
| 0075,[RADBOUDUMCANONYMIZER]70 | BasicConfidentiallyProfile | CS | 1 |
| 0075,[RADBOUDUMCANONYMIZER]71 | CleanPixelDataOption | CS | 1 |
| 0075,[RADBOUDUMCANONYMIZER]72 | CleanRecognizableVisualFeaturesOption | CS | 1 |
| 0075,[RADBOUDUMCANONYMIZER]73 | CleanGraphicsOption | CS | 1 |
| 0075,[RADBOUDUMCANONYMIZER]74 | CleanStructuredContentOption | CS | 1 |
| 0075,[RADBOUDUMCANONYMIZER]75 | CleanDescriptorsOption | CS | 1 |
| 0075,[RADBOUDUMCANONYMIZER]76 | RetainLongitudinalTemporalInformationWithFullDatesOptions | CS | 1 |
| 0075,[RADBOUDUMCANONYMIZER]77 | RetainPatientCharacteristicsOption | CS | 1 |
| 0075,[RADBOUDUMCANONYMIZER]78 | RetainDeviceIdentityOption | CS | 1 |
| 0075,[RADBOUDUMCANONYMIZER]79 | RetainUIDsOption | CS | 1 |
| 0075,[RADBOUDUMCANONYMIZER]80 | RetainSafePrivateOption | CS | 1 |
| 0075,[RADBOUDUMCANONYMIZER]81 | RetainLongitudinalTemporalInformationWithModifiedDatesOptions | CS | 1 |
| 0075,[RADBOUDUMCANONYMIZER]82 | InternalDatesChanged | CS | 1 |
| 0075,[RADBOUDUMCANONYMIZER]90 | CallingAET | AE | 1 |
| 0075,[RADBOUDUMCANONYMIZER]91 | CallingIP | LO | 1 |
| 0075,[RADBOUDUMCANONYMIZER]92 | CalledAET | AE | 1 |

### Private group
From Siemens DICOM Conformance statement MAMMOMAT Inspiration WH AWS VB41

| tag | description | VR | VM |
| --- | ---- | ------ | ------- |
| 0019,[SIEMENS MED SP DXMG WH AWS 1]01 | AECCoordinates | UL | 1-n |
| 0019,[SIEMENS MED SP DXMG WH AWS 1]02 | AECCoordinates Size | US | 1-n |
| 0019,[SIEMENS MED SP DXMG WH AWS 1]05 | UNKNOWN_(LO:Always0) | US | 1 |
| 0019,[SIEMENS MED SP DXMG WH AWS 1]06 | UNKNOWN_(LO:Always0) | US | 1 |
| 0019,[SIEMENS MED SP DXMG WH AWS 1]10 | DerivationDescription | ST | 1 |
| 0041,[SIEMENS MED SP DXMG WH AWS 1]02 | ReasonForTheRequestedProcedure | LO | 1 |
| 0051,[SIEMENS MED SP DXMG WH AWS 1]10 | UNKNOWN_(LO:Some(Recon)Parameters) | ST | 1 |
| 0051,[SIEMENS MED SP DXMG WH AWS 1]20 | UNKNOWN_(LO:HistogramStatistics) | ST | 1 |
| 0051,[SIEMENS MED SP DXMG WH AWS 1]21 | UNKNOWN_(LO:SIEMENS_TOMO) | LO | 1 |
| 0051,[SIEMENS MED SP DXMG WH AWS 1]32 | ImagePosition(Tomo) | DS | 3 |
| 0051,[SIEMENS MED SP DXMG WH AWS 1]37 | ImageOrientation(Tomo) | DS | 6 |
| 0051,[SIEMENS MED SP DXMG WH AWS 1]50 | ProjectionSeriesInstanceUID | UI | 1 |
| 0051,[SIEMENS MED SP DXMG WH AWS 1]60 | PrimaryPositionerScanArc | DS | 1 |
| 0051,[SIEMENS MED SP DXMG WH AWS 1]61 | SecondaryPositionerScanArc | DS | 1 |
| 0051,[SIEMENS MED SP DXMG WH AWS 1]62 | PrimaryPositionerScanStartAngle | DS | 1 |
| 0051,[SIEMENS MED SP DXMG WH AWS 1]63 | SecondaryPositionerScanStartAngle | DS | 1 |
| 0051,[SIEMENS MED SP DXMG WH AWS 1]64 | PrimaryPositionerIncrement | DS | 1 |
| 0051,[SIEMENS MED SP DXMG WH AWS 1]65 | SecondaryPositionerIncrement | DS | 1 |
| 0055,[SIEMENS MED SP DXMG WH AWS 1]01 | ProjectionViewDisplayString | LO | 1 |

### Private group
From Siemens DICOM Conformance statement Biograph mCT VG60A

| tag | description | VR | VM |
| --- | ---- | ------ | ------- |
| 0071,[SIEMENS MED PT]21 | RegistrationMatrixUID | UI | 1 |
| 0071,[SIEMENS MED PT]22 | DecayCorrectionDateTime | DT | 1 |
| 0071,[SIEMENS MED PT]23 | RegistrationMatrix | FD | 1-n |
| 0071,[SIEMENS MED PT]24 | TableMotion | CS | 1 |

### Private group
Based on CTP script

| tag | description | VR | VM |
| --- | ---- | ------ | ------- |
| 0071,[SIEMENS MED PT MU MAP]01 | SOPClassOfSource | UI | 1 |
| 0071,[SIEMENS MED PT MU MAP]02 | RelatedMuMapSeries | UI | 1 |

### Private group
Based on CTP script

| tag | description | VR | VM |
| --- | ---- | ------ | ------- |
| 0019,[SIEMENS MR HEADER]0a | NumberOfImagesInMosaic | US | 1 |
| 0019,[SIEMENS MR HEADER]0b | SliceMeasurementDuration | DS | 1 |
| 0019,[SIEMENS MR HEADER]0c | B_value | IS | 1 |
| 0019,[SIEMENS MR HEADER]0d | DiffusionDirectionality | CS | 1 |
| 0019,[SIEMENS MR HEADER]0e | DiffusionGradientDirection | FD | 3 |
| 0019,[SIEMENS MR HEADER]0f | GradientMode | SH | 1 |
| 0019,[SIEMENS MR HEADER]27 | B_matrix | FD | 6 |
| 0019,[SIEMENS MR HEADER]28 | BandwidthPerPixelPhaseEncode | FD | 1 |

### Private group
Based on CTP script

| tag | description | VR | VM |
| --- | ---- | ------ | ------- |
| 7005,[TOSHIBA_MEC_CT3]0b | Filter | SH | 2 |
| 7005,[TOSHIBA_MEC_CT3]1b | ConvolutionKernel | SH | 1 |
| 7005,[TOSHIBA_MEC_CT3]23 | PitchFactor | DS | 1 |
| 7005,[TOSHIBA_MEC_CT3]41 | RawSliceInformation | SH | 1 |
| 7005,[TOSHIBA_MEC_CT3]92 | ReconProcess | SH | 1 |
| 7005,[TOSHIBA_MEC_CT3]93 | AcquisitionMode | SH | 1 |

### Private group
Based on CTP script

| tag | description | VR | VM |
| --- | ---- | ------ | ------- |
| 0029,[SIEMENS CSA HEADER]08 | CSAImageHeaderType | CS | 1 |
| 0029,[SIEMENS CSA HEADER]09 | CSAImageHeaderVersion | LO | 1 |
| 0029,[SIEMENS CSA HEADER]10 | CSAImageHeaderInfo | OB | 1 |
| 0029,[SIEMENS CSA HEADER]18 | CSASeriesHeaderType | CS | 1 |
| 0029,[SIEMENS CSA HEADER]19 | CSASeriesHeaderVersion | LO | 1 |
| 0029,[SIEMENS CSA HEADER]20 | CSASeriesHeaderInfo | OB | 3 |

### Private group
Based on CTP script

| tag | description | VR | VM |
| --- | ---- | ------ | ------- |
| 0021,[SIEMENS Ultrasound S2000]00 |  NipplePositionMarker | US | 1-n |
| 0021,[SIEMENS Ultrasound S2000]01 |  ABVSClipDerivedFromVolume  | US | 1-n |

### Private group
Based on CTP script

| tag | description | VR | VM |
| --- | ---- | ------ | ------- |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]00 | ReviewMode | US | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]01 | AnatomicalBackgroundPercent | US | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]02 | NumberofPhases | US | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]03 | ApplyAnatomicalBackground | US | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]04 | PixelShiftArray | SS | 4-4n |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]05 | Brightness | US | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]06 | Contrast | US | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]07 | EnabledShutters | US | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]08 | NativeEdgeEnh.PercentGain | US | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]09 | NativeEdgeEnh.LUTIndex | SS | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]0a | NativeEdgeEnh.KernelSize | SS | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]0b | Subtr.EdgeEnh.PercentGain | US | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]0c | Subtr.EdgeEnh.LUTIndex | SS | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]0d | Subtr.EdgeEnh.KernelSize | SS | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]0e | FadePercent | US | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]0f | FlippedbeforeLateralityApplied | US | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]10 | ApplyFade | US | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]12 | Zoom | US | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]13 | PanX | SS | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]14 | PanY | SS | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]15 | NativeEdgeEnh.AdvPercentGain | SS | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]16 | Subtr.EdgeEnh.AdvPercentGain | SS | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]17 | InvertFlag | US | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]1b | AcquisitionSize | US | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]1c | AutoWindowCenter | DS | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]1d | AutoWindowWidth | DS | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]1e | AutoWindowCorrectValue | IS | 2 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]1f | SigmoidWindowParameter | DS | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]20 | RoadmapCatheterContrast | DS | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]21 | RoadmapVesselContrast | DS | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]23 | ICStentROIOrigin | US | 2 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]24 | ICStentROISize | US | 2 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]25 | VFRInfo | US | 2-2n |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]30 | Frame#Roadmap-MinAmplification | US | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]31 | Frame#Roadmap-VesselMap | US | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]41 | PixelShiftValues | FL | 6-6n |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]42 | PixelShiftIndicator | US | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]43 | AppliedPixelShiftValues | FL | 6-6n |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]44 | PixelShiftValidity | US | 2-2n |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]51 | UIPnatProcessingMode | US | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]52 | UIPnatDDOKernelSize | US | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]53 | UIPnatDDOGain | US | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]54 | UIPnatConstrast | US | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]55 | UIPnatDynamic | US | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]56 | UIPnatAdaptiveFlavor | US | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]57 | UIPnatPeakReduction | US | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]58 | UIPnatBrightnessControl | US | 1 |
| 0019,[SIEMENS SMS-AX  VIEW 1.0]59 | UIPnatBrightnessValue | US | 1 |

### Private group
Based on CTP script

| tag | description | VR | VM |
| --- | ---- | ------ | ------- |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]00 | AcquisitionType | US | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]01 | AcquisitionMode | US | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]02 | FootswitchIndex | US | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]03 | AcquisitionRoom | US | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]04 | CurrentTimeProduct | SL | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]05 | Dose | SL | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]08 | SkinDoseRate | SL | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]0a | CopperFilter | UL | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]0b | MeasuringField | US | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]0e | TotalSteps | SS | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]0f | DynaX-RayInfo | SL | 4-4n |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]10 | ModalityLUTInputGamma | US | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]11 | ModalityLUTOutputGamma | US | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]12 | SH_STPAR | OB | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]14 | DynaAngulationStep | SS | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]15 | DDOValue | US | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]16 | DRSingleFlag | US | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]17 | SourcetoIsocenter | SL | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]19 | ECGIndexArray | SL | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]1b | SH_ZOOM | OB | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]1c | SH_COLPAR | OB | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]1d | K-Factor | US | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]1e | EVE | US | 8 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]1f | TotalSceneTime | SL | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]20 | RestoreFlag | US | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]21 | StandMovementFlag | US | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]22 | FDRows | US | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]23 | FDColumns | US | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]24 | TableMovementFlag | US | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]28 | GammaLUTSequence | SQ | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]29 | SceneTimeins | DS | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]2a | 3DCardiacPhaseCenter | IS | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]2b | 3DCardiacPhaseWidth | IS | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]30 | OrganProgramInfo | OB | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]31 | SourceImageDistance | SS | 1-n |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]32 | OriginalPixelSpacing | DS | 2 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]3b | mAsModulation | IS | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]3c | 3DR-PeakReferenceTime | DT | 1-n |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]3d | ECGFrameTimeVector | SL | 1-n |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]3e | ECGStartTimeofRun | SL | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]40 | GammaLUTDescriptor | US | 3 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]41 | GammaLUTType | LO | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]42 | GammaLUTData | US | 1-n |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]43 | GlobalGain | US | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]44 | GlobalOffset | US | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]45 | DippMode | US | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]46 | ArtisSystemType | US | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]47 | ArtisTableType | US | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]48 | ArtisTableTopType | US | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]49 | WaterValue | SS | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]4a | CNRFlag | US | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]4b | CNRDemandedValue | FL | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]4b | CNRAchievedValue | FL | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]50 | X-rayTubeType | LO | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]51 | 3DPositionerPrimaryStartAngle | DS | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]52 | 3DPositionerSecondaryStartAngle | DS | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]53 | StandPosition | SS | 3 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]54 | RotationAngle | SS | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]55 | ImageRotation | US | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]56 | TableCoordinates | SS | 3 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]57 | IsocenterTablePosition | SS | 3 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]58 | TableObjectDistance | DS | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]59 | C-ArmCoordinateSystem | FL | 1-n |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]5a | RobotAxes | FL | 1-n |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]5b | TableCoordinateSystem | FL | 12 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]5c | PatientCoordinateSystem | FL | 12 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]5d | Angulation | SL | 1-n |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]5e | Orbital | SL | 1-n |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]61 | LargeVolumeOverlap | SS | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]62 | ReconstructionPreset | US | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]63 | 3DStartAngle | SS | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]64 | 3DPlannedAngle | SL | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]65 | 3DRotationPlaneAlpha | SL | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]66 | 3DRotationPlaneBeta | SL | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]67 | 3DFirstImageAngle | SL | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]68 | 3DTriggerAngle | SS | 1-n |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]71 | DetectorRotation | DS | 1-n |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]72 | PhysicalDetectorRotation | SL | 1-n |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]81 | TableHeadTilt | SS | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]82 | TableRotation | SS | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]83 | TableCradleTilt | SS | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]84 | ArtisSystemFamily | LO | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]a3 | 3DCardiacTriggerSequence | SQ | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]a4 | 3DFrameReferenceDateTime | DT | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]a5 | 3DCardiacTriggerDelayTime | FD | 1 |
| 0021,[SIEMENS SMS-AX  ACQ 1.0]a6 | 3DR-RIntervalTimeMeasured | FD | 1 |

### Private group
Based on CTP script

| tag | description | VR | VM |
| --- | ---- | ------ | ------- |
| 0023,[SIEMENS SMS-AX  QUANT 1.0]08 | CalibrationTODValue | IS | 1 |

### Private group
Based on CTP script

| tag | description | VR | VM |
| --- | ---- | ------ | ------- |
| 0025,[SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0]00 | ViewNative | US | 1 |
| 0025,[SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0]01 | OriginalSeriesNumber | US | 1 |
| 0025,[SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0]02 | OriginalImageNumber | US | 1 |
| 0025,[SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0]03 | WinCenter | US | 1 |
| 0025,[SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0]04 | WinWidth | US | 1 |
| 0025,[SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0]05 | WinBrightness | US | 1 |
| 0025,[SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0]06 | WinContrast | US | 1 |
| 0025,[SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0]07 | OriginalFrameNumber | US | 1 |
| 0025,[SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0]08 | OriginalMaskFrameNumber | US | 1 |
| 0025,[SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0]09 | Opac | US | 1 |
| 0025,[SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0]0a | OriginalNumberofFrames | US | 1 |
| 0025,[SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0]0b | OriginalSceneDuration | DS | 1 |
| 0025,[SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0]0c | IdentifierLOID | LO | 1 |
| 0025,[SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0]0d | OriginalSceneVFRInfo | SS | 1-n |
| 0025,[SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0]0e | OriginalFrameECGPosition | SS | 1 |
| 0025,[SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0]10 | ZoomFlag | SS | 1 |
| 0025,[SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0]11 | FlexiblePixelShift | US | 1 |
| 0025,[SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0]12 | NumberofMaskFrames | US | 1 |
| 0025,[SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0]13 | NumberofFillFrames | US | 1 |
| 0025,[SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0]14 | SeriesNumber | IS | 1 |
| 0025,[SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0]15 | ImageNumber | IS | 1 |
| 0025,[SIEMENS SMS-AX  ORIGINAL IMAGE INFO 1.0]16 | ReadyProcessingStatus | IS | 1 |

### Private group
Based on CTP script

| tag | description | VR | VM |
| --- | ---- | ------ | ------- |
| 0029,[SIEMENS CSA NON-IMAGE]08 | CSADataType | CS | 1 |
| 0029,[SIEMENS CSA NON-IMAGE]09 | CSADataVersion | LO | 1 |
| 0029,[SIEMENS CSA NON-IMAGE]10 | CSADataInfo | OB | 1 |

### Private group
Based on CTP script

| tag | description | VR | VM |
| --- | ---- | ------ | ------- |
| 0029,[SIEMENS MEDCOM HEADER]08 | MedComHeaderType | CS | 1 |
| 0029,[SIEMENS MEDCOM HEADER]09 | MedComHeaderVersion | LO | 1 |
| 0029,[SIEMENS MEDCOM HEADER]10 | MedComHeaderInfo | OB | 1 |
| 0029,[SIEMENS MEDCOM HEADER]20 | MedComHistoryInformation | OB | 1 |
| 0029,[SIEMENS MEDCOM HEADER]31 | PMTFInformation1 | LO | 1 |
| 0029,[SIEMENS MEDCOM HEADER]32 | PMTFInformation2 | UL | 1 |
| 0029,[SIEMENS MEDCOM HEADER]33 | PMTFInformation3 | UL | 1 |
| 0029,[SIEMENS MEDCOM HEADER]34 | PMTFInformation4 | CS | 1 |
| 0029,[SIEMENS MEDCOM HEADER]35 | PMTFInformation5 | UL | 1 |
| 0029,[SIEMENS MEDCOM HEADER]40 | ApplicationHeaderSequence | SQ | 1 |
| 0029,[SIEMENS MEDCOM HEADER]41 | ApplicationHeaderType | CS | 1 |
| 0029,[SIEMENS MEDCOM HEADER]42 | ApplicationHeaderID | LO | 1 |
| 0029,[SIEMENS MEDCOM HEADER]43 | ApplicationHeaderVersion | LO | 1 |
| 0029,[SIEMENS MEDCOM HEADER]44 | ApplicationHeaderInfo | OB | 1 |
| 0029,[SIEMENS MEDCOM HEADER]50 | WorkflowControlFlags | LO | 8 |
| 0029,[SIEMENS MEDCOM HEADER]51 | Arch.ManagementFlagKeepOnline | CS | 1 |
| 0029,[SIEMENS MEDCOM HEADER]52 | Arch.MgmntFlagDoNotArchive | CS | 1 |
| 0029,[SIEMENS MEDCOM HEADER]53 | ImageLocationStatus | CS | 1 |
| 0029,[SIEMENS MEDCOM HEADER]54 | EstimatedRetrieveTime | DS | 1 |
| 0029,[SIEMENS MEDCOM HEADER]55 | DataSizeofRetrievedImages | DS | 1 |

### Private group
Based on CTP script

| tag | description | VR | VM |
| --- | ---- | ------ | ------- |
| 0029,[SIEMENS MEDCOM OOG]08 | MedComOOGType | CS | 1 |
| 0029,[SIEMENS MEDCOM OOG]09 | MedComOOGVersion | LO | 1 |
| 0029,[SIEMENS MEDCOM OOG]10 | MedComOOGInfo | OB | 1 |

### Private group
Based on CTP script

| tag | description | VR | VM |
| --- | ---- | ------ | ------- |
| 0029,[CARDIO-D.R. 1.0]00 | StandardEdgeEnhancementSequence | SQ | 1 |
| 0029,[CARDIO-D.R. 1.0]01 | ConvolutionKernelSize | US | 2 |
| 0029,[CARDIO-D.R. 1.0]02 | ConvolutionKernelCoefficients | US | 1-n |
| 0029,[CARDIO-D.R. 1.0]03 | EdgeEnhancementGain | FL | 1 |

### Private group
Based on CTP script

| tag | description | VR | VM |
| --- | ---- | ------ | ------- |
| 2121,[PMI Private Calibration Module Version 2.0]01 | CalibrationMethod | ST | 1 |
| 2121,[PMI Private Calibration Module Version 2.0]02 | CalibrationMethodInfo | ST | 1 |
| 2121,[PMI Private Calibration Module Version 2.0]03 | CalibrationObjectSize | FL | 1 |
| 2121,[PMI Private Calibration Module Version 2.0]04 | CalibrationObjectSDev | FL | 1 |
| 2121,[PMI Private Calibration Module Version 2.0]05 | CalibrationHorizontalPixelSpacing | FL | 1 |
| 2121,[PMI Private Calibration Module Version 2.0]06 | CalibrationVerticalPixelSpacing | FL | 1 |
| 2121,[PMI Private Calibration Module Version 2.0]08 | CalibrationFileName | ST | 1 |
| 2121,[PMI Private Calibration Module Version 2.0]09 | CalibrationFrameNumber | IS | 1 |
| 2121,[PMI Private Calibration Module Version 2.0]0a | CalibrationObjectUnit | SH | 1 |
| 2121,[PMI Private Calibration Module Version 2.0]0b | AveragedCalibrationsPerformed | SS | 1 |
| 2121,[PMI Private Calibration Module Version 2.0]0c | AutoMagnifyFactor | FL | 1 |
| 2121,[PMI Private Calibration Module Version 2.0]0d | HorizontalPixelSDev | FL | 1 |
| 2121,[PMI Private Calibration Module Version 2.0]0e | VerticalPixelSDev | FL | 1 |

### Private group
Based on CTP script

| tag | description | VR | VM |
| --- | ---- | ------ | ------- |
| 2121,[PMI Private 3D Reconstruction Attributes V]01 | rsion1.0Binary3DVesselData | OB | 1 |

### Private group
Based on CTP script

| tag | description | VR | VM |
| --- | ---- | ------ | ------- |
| 2121,[PMI Private 3D Reconstruction Attributes Version 1.0]02 | 3DControlDisplayedAreaSequence | SQ | 1 |
| 2121,[PMI Private 3D Reconstruction Attributes Version 1.0]03 | 3DControlDisplayedAreaTopLeftCorner | SL | 2 |
| 2121,[PMI Private 3D Reconstruction Attributes Version 1.0]04 | 3DControlDisplayedAreaBottomRightCorner | SL | 2 |

### Private group
Based on CTP script

| tag | description | VR | VM |
| --- | ---- | ------ | ------- |
| 0033,[SIEMENS MED NM]1038 | Pixel scale factor | FL | 1 |
| 0033,[SIEMENS MED NM]38 | Pixel scale factor | FL | 1 |


## Filters
To be implemented
## Pixel
To be implemented