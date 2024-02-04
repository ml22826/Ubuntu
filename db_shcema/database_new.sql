CREATE TABLE Population (
    PopulationCode VARCHAR(50),
    PopulationName VARCHAR(255),
    PopulationDescription TEXT,
    SuperpopulationCode VARCHAR(50),
    SuperpopulationName VARCHAR(255),
    PRIMARY KEY (PopulationCode),
    FOREIGN KEY (PopulationCode) REFERENCES Sample(PopulationCode),
    FOREIGN KEY (PopulationCode) REFERENCES Allele_Frequency(PopulationCode)
);

CREATE TABLE Sample (
    SampleID VARCHAR(255),
    PopulationCode VARCHAR(50),
    PRIMARY KEY (PopulationCode)
);

CREATE TABLE Varient (
    Chorm INT(40),
    Position INT(100),
    SNP_ID VARCHAR(255),
    Reference_allele VARCHAR(255),
    Alternate_allele VARCHAR (255),
    PRIMARY KEY (SNP_ID),
    FOREIGN KEY (SNP_ID) REFERENCES Allele_Frequency(SNP_ID),
    FOREIGN KEY (SNP_ID) REFERENCES gwas_clinvar(SNP_ID)
);

CREATE TABLE Allele_Frequency (
    SNP_ID INT,
    PopulationCode INT,
    Allele_Frequencies FLOAT,
    PRIMARY KEY (SNP_ID)
);

CREATE TABLE gwas_clinvar (
    SNP_ID VARCHAR(255),
    DISEASE_TRAIT VARCHAR(255),
    CHR_ID DECIMAL(5, 1),
    CHR_POS DECIMAL(10, 1),
    MAPPED_GENE VARCHAR(255),
    STRONGEST_SNP_RISK_ALLELE VARCHAR(255),
    SNPS VARCHAR(255),
    MERGED DECIMAL(5, 1),
    SNP_ID_CURRENT DECIMAL(10, 1),
    CONTEXT VARCHAR(255),
    INTERGENIC DECIMAL(5, 1),
    RISK_ALLELE_FREQUENCY DECIMAL(10, 6),
    P_VALUE DECIMAL(20, 10),
    PVALUE_MLOG DECIMAL(20, 6),
    P_VALUE_TEXT VARCHAR(255),
    OR_OR_BETA VARCHAR(255),
    CI_95_TEXT VARCHAR(255),
    PLATFORM VARCHAR(255),
    SNPS_PASSING_QC DECIMAL(10, 0),
    CNV VARCHAR(1),
    PRIMARY KEY (SNP_ID)
);



